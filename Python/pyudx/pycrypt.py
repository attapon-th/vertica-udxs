# -*- coding: utf-8 -*-
import vertica_sdk  # type: ignore
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from base64 import urlsafe_b64encode, urlsafe_b64decode


def compile_key(key: bytes | str) -> bytes:
    if isinstance(key, str):
        key = key.encode("utf-8", errors="replace")
    return SHA256.new(key).digest()


def encrypt(plaintext: str, secret_key: str, header_str: str = "none_set") -> str:
    data: bytes = plaintext.encode("utf-8")
    header: bytes = header_str.encode("utf-8")
    key: bytes = compile_key(secret_key)
    cipher = AES.new(key, AES.MODE_OCB)

    cipher.update(header)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return ".".join([urlsafe_b64encode(x).decode("ascii") for x in (cipher.nonce, header, ciphertext, tag)])


def decrypt(ciphertext: str, secret_key: str) -> str:
    s: str = ""
    try:
        key: bytes = compile_key(secret_key)
        jv = [urlsafe_b64decode(x.encode("ascii")) for x in ciphertext.split(".")]
        if len(jv) != 4:
            raise ValueError
        cipher = AES.new(key, AES.MODE_OCB, nonce=jv[0])
        cipher.update(jv[1])
        plaintext: bytes = cipher.decrypt_and_verify(jv[2], jv[3])
        s = plaintext.decode("utf-8", errors="replace")
    except (ValueError, KeyError):
        print("Incorrect decryption")
    return s


class pyencrypt(vertica_sdk.ScalarFunction):
    """
    Scalar function which performs check thai cid mod11
    (CHAR, VARCHAR, or LONG VARCHAR) input.
    """

    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            if arg_reader.isNull(0):
                res_writer.setNull()
            else:
                message: str = arg_reader.getString(0)
                key: str = arg_reader.getString(1)
                res_writer.setString(encrypt(message, key, ""))
            res_writer.next()
            if not arg_reader.next():
                break


class pyencrypt_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        arg_types.addVarchar()
        return_type.addVarchar()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addVarchar(6500)

    def createScalarFunction(self, srv):
        return pyencrypt()


class pydecrypt(vertica_sdk.ScalarFunction):
    """
    Scalar function which performs check thai cid mod11
    (CHAR, VARCHAR, or LONG VARCHAR) input.
    """

    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            if arg_reader.isNull(0):
                res_writer.setNull()
            else:
                message: str = arg_reader.getString(0)
                key: str = arg_reader.getString(1)

                res_writer.setString(decrypt(message, key))

            res_writer.next()
            if not arg_reader.next():
                break


class pydecrypt_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        arg_types.addVarchar()
        return_type.addVarchar()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addVarchar(6500)

    def createScalarFunction(self, srv):
        return pydecrypt()
