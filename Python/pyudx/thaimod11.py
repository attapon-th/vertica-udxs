# -*- coding: utf-8 -*-
import vertica_sdk  # type: ignore

# constants for Thai citizen ID
CID_NONE: int = 0
CID_LENGTH13: int = 1
CID_NUMBER: int = 2
CID_THAI: int = 9


def check_mod11(cid: str) -> bool:
    """
    Validate Thai citizen ID is Mod11

    เช็คเลขบัตรประชาชน 13 หลัก ตาม Mod11

    Args:
        cid (str): Thai citizen ID

    Returns:
        bool: True if valid else False
    """
    if cid is None and not isinstance(cid, str):
        return False
    if len(cid) != 13 or not cid.isnumeric():  # ถ้า pid ไม่ใช่ 13 ให้คืนค่า False
        return False
    if cid[0] == "0":  # ตัวเลขหลักที่ 0 ของบัตรประชาชน ไม่มีค่าเป็น 0
        return False
    if cid[1] == "0":  # ตัวเลขหลักที่ 1 ของบัตรประชาชน
        return False

    cid12: str = cid[0:12]  # ตัวเลขหลักที่ 1 - 12 ของบัตรประชาชน
    cid13: str = cid[12]  # ตัวเลขหลักที่ 13 ของบัตรประชาชน
    sum_num: int = 0  # ผลรวม
    for i, num in enumerate(cid12):  # วนลูปเช็คว่า pid มีตัวอักษรอยู่ในตำแหน่งไหน
        sum_num += int(num) * (13 - i)  # นำตัวเลขที่เจอมาคูณกับ 13 - i

    digit13: int = sum_num % 11  # หาเศษจากผลรวมที่ได้จากการคูณด้วย 11
    digit13 = (11 - digit13) % 10
    return int(cid13) == digit13


def verify_thaicid(cid: str) -> int:
    """
    Determines the type of Thai citizen ID based on the input string.

    Args:
        cid (str): The Thai citizen ID to be checked.

    Returns:
        int: The type of the Thai citizen ID. Possible return values are:

            - `CID_THAI`(9): If the ID is a valid Thai citizen ID.

            - `CID_NUMBER`(2): If the ID is a numeric string of length 13.

            - `CID_LENGTH13`(1): If the ID is a string of length 13.

            - `CID_NONE`(0): If the ID is not a valid Thai citizen ID.
    """
    if not isinstance(cid, str):
        cid = str(cid)

    if len(cid) == 13:
        if check_mod11(cid):
            return CID_THAI
        elif cid.isnumeric():
            return CID_NUMBER
        else:
            return CID_LENGTH13
    return CID_NONE


class thaimod11(vertica_sdk.ScalarFunction):
    """
    Scalar function which performs check thai cid mod11
    (CHAR, VARCHAR, or LONG VARCHAR) input.
    """

    def processBlock(self, server_interface, arg_reader, res_writer):
        while True:
            if arg_reader.isNull(0):
                res_writer.setNull()
            else:
                cid: str = arg_reader.getString(0)
                res_writer.setInt(verify_thaicid(cid))
            res_writer.next()
            if not arg_reader.next():
                break


class thaimod11_factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addInt()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addInt()

    def createScalarFunction(self, srv):
        return thaimod11()
