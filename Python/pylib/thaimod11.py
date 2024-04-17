# -*- coding: utf-8 -*-
import vertica_sdk  # type: ignore


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
                if len(cid) != 13 or not cid.isdigit():
                    res_writer.setInt(0)
                else:
                    cid12: str = cid[0:12]  # ตัวเลขหลักที่ 1 - 12 ของบัตรประชาชน
                    cid13: str = cid[12]  # ตัวเลขหลักที่ 13 ของบัตรประชาชน
                    if int(cid12[0]) == 0 or int(cid12[1]) == 0:
                        res_writer.setInt(0)
                    else:
                        sum_num: int = 0  # ผลรวม
                        for i, num in enumerate(cid12):  # วนลูปเช็คว่า pid มีตัวอักษรอยู่ในตำแหน่งไหน
                            sum_num += int(num) * (13 - i)  # นำตัวเลขที่เจอมาคูณกับ 13 - i

                        digit13: int = sum_num % 11  # หาเศษจากผลรวมที่ได้จากการคูณด้วย 11
                        digit13 = (11 - digit13) % 10

                        res_writer.setInt(int(cid13) == digit13 and 1 or 0)
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
