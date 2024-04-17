import vertica_sdk
import base64


class vb64encode(vertica_sdk.ScalarFunction):
    """
    Scalar function which performs base64 encoding of a
    (CHAR, VARCHAR, LONG VARCHAR or VARBINARY) input.
    """

    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            if arg_reader.isNull(0):
                res_writer.setNull()
            else:
                x: bytes = arg_reader.getBinary(0)
                y: bytes = base64.b64encode(x)
                res_writer.setString(y.decode(encoding="ascii", errors="replace"))
            res_writer.next()
            if not arg_reader.next():
                break


class vb64encode_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addBinary()
        return_type.addVarchar()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addVarchar(65000)

    def createScalarFunction(self, srv):
        return vb64encode()


class vb64decode(vertica_sdk.ScalarFunction):
    """
    Scalar function which performs base64 decoding of a
    """

    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            if arg_reader.isNull(0):
                res_writer.setNull()
            else:
                x: str = arg_reader.getString(0)
                y: bytes = base64.b64decode(x.encode(encoding="ascii"))
                res_writer.setString(y.decode(encoding="utf-8", errors="replace"))
            res_writer.next()
            if not arg_reader.next():
                break


class vb64decode_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addVarchar()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addVarchar(65000)

    def createScalarFunction(self, srv):
        return vb64decode()
