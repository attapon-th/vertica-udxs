

// #include "Vertica.h"
// #include <stdio.h>

// using namespace Vertica;

// static const std::string base64_chars =
//     "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
//     "abcdefghijklmnopqrstuvwxyz"
//     "0123456789+/";

// class Base64Encode : public ScalarFunction
// {
// public:
//     virtual void processBlock(ServerInterface &srvInterface,
//                               BlockReader &arg_reader,
//                               BlockWriter &res_writer)
//     {

//         // Basic error checking
//         if (arg_reader.getNumCols() != 2) // fixme: accept key as a parm
//             vt_report_error(0, "Function accepts exactly 2 arguments, but %zu provided",
//                             arg_reader.getNumCols());

//         // While we have inputs to process
//         do
//         {
//             char *t;
//             unsigned int l;
//             int r = 0;
//             std::string inStr = arg_reader.getStringRef(0).str();
//             std::string kStr = arg_reader.getStringRef(1).str();

//             l = inStr.capacity(); // warning, this might be a hack
//             l = inStr.length();   // warning, this might be a hack

//             t = (char *)malloc(l + 1); // add one for the null.
//             memset(t, 0, l + 1);

//             r = my_aes_decrypt(inStr.c_str(), l, t, kStr.c_str(), kStr.length());

//             if (r < 0)
//             {
//                 srvInterface.log("Base64Encode: Error encode: %d", r);
//                 return;
//             }
//             // We try to preserve the input string in it's entirety before encrypting it, this includes
//             // nulls. So the decrypted string should already be null terminated. But you never know. So we tack
//             // one on the end anyway.
//             t[r + 1] = 0;
//             res_writer.getStringRef().copy(t, r);
//             free(t);
//             res_writer.next();

//         } while (arg_reader.next());
//     }
// };

// class Base64EncodeFactory : public ScalarFunctionFactory
// {
//     // return an instance of RemoveSpace to perform the actual addition.
//     virtual ScalarFunction *createScalarFunction(ServerInterface &interface)
//     {
//         return vt_createFuncObj(interface.allocator, Base64Encode);
//     }

//     virtual void getPrototype(ServerInterface &interface,
//                               ColumnTypes &argTypes,
//                               ColumnTypes &returnType)
//     {
//         argTypes.addVarchar();
//         argTypes.addVarchar();
//         returnType.addVarchar();
//     }

//     virtual void getReturnType(ServerInterface &srvInterface,
//                                const SizedColumnTypes &argTypes,
//                                SizedColumnTypes &returnType)
//     {
//         const VerticaType &t = argTypes.getColumnType(0);
//         returnType.addVarchar(t.getStringLength());
//     }
// };

// RegisterFactory(Base64EncodeFactory);
