#cmake_minimum_required(VERSION 3.20)
#project(scripts)
#
#set(CMAKE_CXX_STANDARD 14)
#
#include_directories(.)
#
#add_executable(scripts
#        face_landmark_detection_to_txt.cpp
#        render_face.hpp)
#
#
#find_package(
#        dlib REQUIRED
#        opencv2 REQUIRED
#        OpenCV REQUIRED
#)
#target_link_libraries(
#        dlib::dlib
#        ${OpenCV_LIBS}
#)


cmake_minimum_required(VERSION 3.20)
project(scripts)

# Find OpenCV, you may need to set OpenCV_DIR variable
# to the absolute path to the directory containing OpenCVConfig.cmake file
# via the command line or GUI
find_package(
        dlib REQUIRED
        OpenCV REQUIRED PATHS /usr/include/opencv2
#        opencv2 REQUIRED
)
# If the package has been found, several variables will
# be set, you can find the full list with descriptions
# in the OpenCVConfig.cmake file.
# Print some message showing some of them
message(STATUS "OpenCV library status:")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")

#if(CMAKE_VERSION VERSION_LESS "2.8.11")
    # Add OpenCV headers location to your include paths
include_directories(${OpenCV_INCLUDE_DIRS} ${DLIB_INCLUDE_DIRECTORY})
#endif()

# Declare the executable target built from your sources
add_executable(
        scripts
        face_landmark_detection_to_txt.cpp
        render_face.hpp
)

# Link your application with OpenCV libraries
target_link_libraries(scripts ${OpenCV_LIBS} lapack cblas dlib)
