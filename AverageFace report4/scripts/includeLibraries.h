//This file is used to import dlib and opencv libraries to cpp code

#pragma cling add_library_path("/usr/local/lib")
#pragma cling add_include_path("/usr/local/include")
// #pragma cling add_include_path("/usr/local/include/opencv4")
#pragma cling load("/usr/local/lib/libdlib.so")