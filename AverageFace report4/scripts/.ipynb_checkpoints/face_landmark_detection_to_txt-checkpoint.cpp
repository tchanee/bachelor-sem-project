
#include <dlib/image_processing/frontal_face_detector.h>
#include <dlib/image_processing/render_face_detections.h>
#include <dlib/image_processing.h>
#include <dlib/gui_widgets.h>
#include <dlib/image_io.h>
#include <iostream>
#include <dlib/opencv.h>

#if CV_MAJOR_VERSION < 3
#include <opencv2/highgui/highgui.hpp> // If you are using OpenCV 2
#else
#include <opencv2/imgproc.hpp> // If you are using OpenCV 3
#endif

#include "render_face.hpp" 

using namespace dlib;
using namespace std;


// ----------------------------------------------------------------------------------------

int main(int argc, char** argv)
{  
    try
    {
        // This example takes in a shape model file and then a list of images to
        // process.  We will take these filenames in as command line arguments.
        // Dlib comes with example images in the examples/faces folder so give
        // those as arguments to this program.
        if (argc == 1)
        {
            cout << "Call this program like this:" << endl;
            cout << "./face_landmark_detection_ex shape_predictor_68_face_landmarks.dat faces/*.jpg" << endl;
            cout << "\nYou can get the shape_predictor_68_face_landmarks.dat file from:\n";
            cout << "http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2" << endl;
            return 0;
        }

        // We need a face detector.  We will use this to get bounding boxes for
        // each face in an image.
        frontal_face_detector detector = get_frontal_face_detector();
        // And we also need a shape_predictor.  This is the tool that will predict face
        // landmark positions given an image and face bounding box.  Here we are just
        // loading the model from the shape_predictor_68_face_landmarks.dat file you gave
        // as a command line argument.
        shape_predictor sp;
        deserialize(argv[1]) >> sp;


        image_window win, win_faces;
        // Loop over all the images provided on the command line.
        for (int i = 2; i < argc; ++i)
        {
            std::string filename(argv[i]);
            cout << "processing image " << filename << endl;
            //array2d<rgb_pixel> img;
            //load_image(img, argv[i]);
            cv::Mat imgMat = cv::imread(argv[i]);
            cv_image<bgr_pixel> img(imgMat);
            
            // Now tell the face detector to give us a list of bounding boxes
            // around all the faces in the image.
            std::vector<rectangle> dets = detector(img);
            cout << "Number of faces detected: " << dets.size() << endl;

            // Now we will go ask the shape_predictor to tell us the pose of
            // each face we detected.
            
            size_t lastindex = filename.find_last_of(".");
            string basename = filename.substr(0, lastindex);
            
            std::vector<full_object_detection> shapes;
            for (unsigned long j = 0; j < dets.size(); ++j)
            {
                full_object_detection shape = sp(img, dets[j]);
                shapes.push_back(shape);
                
                std::stringstream points_filename;
                std::ofstream ofs;
                
                if ( j == 0 )
                {
                    points_filename << basename <<  ".txt";
                }else
                {
                    points_filename << basename <<  "_"  << j << ".txt";
                }
                
                ofs.open(points_filename.str().c_str());
                const full_object_detection& d = shapes[0];
                for (unsigned long k = 0; k < shape.num_parts(); ++k)
                {
                    ofs << shape.part(k).x() << " " << shape.part(k).y() << endl;
                    
                }
                ofs.close();
                render_face(imgMat, shape);
                
            }
            
            cv::imshow("image", imgMat);
            cv::waitKey(0);
            

            

        }
    }
    catch (exception& e)
    {
        cout << "\nexception thrown!" << endl;
        cout << e.what() << endl;
    }
}