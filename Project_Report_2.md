## Project Report 2 - Johnny Borkhoche

This week's goal is to look into ways of warping/distorting an image, ideally a face, to achieve caricaturization resembling that of a real-life caricaturist. I will be focusing on this dimension since the facial recognition part of the pipeline isn't the most important at the current stage of things (from what I've been told in meetings).   

I am looking for any tool, technique or program that does image warping. It doesn't necessarily have to be face-warping, but the goal is to get inspired and see if I could either implement a new way of doing it or to integrate an existing program into the pipeline.



### What I've Found

- **[PyChubby](https://github.com/jankrepl/pychubby)**
  - Package for automated face warping. It allows the user to programaticaly change facial expressions and shapes of any person in an image.
  - It's logic can be summarized into 3 blocks:
    - Landmark Detection: Given a photo, a pre-trained landmark detection model predicts 68 landmarks on each face
    - Reference space mapping: the landmarks are mapped into a so-called reference space. This mapping corrects for possible rotations, translations and scaling in the input image.
    - Manual Action Definition: either use some of the pre-built actions (with parameters) such as `StretchNostrils, Chubbify` which yield consistent warpings accross different faces or build your own custom actions.
- [GridDistort](https://github.com/snorpey/distort-grid)
  - Has a [website](https://snorpey.github.io/distort-grid/) to test things out manually. 
  - Based on grids, a bit similar to the GUI made with OpenGL and dlib that was shown to me, except that there's a limit to the distortion done through a singular point, and allows distortion of the entire image (not just face) by moving intersections in a gride.
- Paper [Morphing techniques for
  manipulating face images](https://link.springer.com/content/pdf/10.3758/BF03207733.pdf) -> from 1999 :/
  - Field Morphing:
    - user provides the algorithm with a set of control line segments. they serve to align the features of images A and B. the more line segments, the better the control.
    - Both Single & Multiple Control Line.s Segment techniques are discussed and the math explained
  - Mesh Warping
    - The user aligns a rectangular grid of points to key feature locations of images. For warping, the coordinates of the source and destination grids (calculated with coordinates that are weighted averages of the corresponding coordinates of the source grid) are fitted with piecewise continuous mapping functions. The warping phase then proceeds in two passes. In the first pass, an intermediate destination image is generated in which every row of the image is warped independently of the other rows. Then, in the second pass, the final destination image
      is created by warping every column of the intermediate image.
  - **INTERESTING** How to create face caricatures paragraph in here
- Paper [Facial Animation System Based on Image Warping 
  Algorithm](http://staff.ustc.edu.cn/~lfdong/research/SAPI50.pdf) -> mainly for making facial expressions
  - Mainly about technologies in facial animation application
  - Technologies used in face image warping are divided into two categories
    - Warping based on scattered point interpolation (*algorithm based on radial basis function RBF*), can produce realistic warped images. But usually the RBF functions selected are very complex, so the results are slow, and doesn't guarantee stability at the borders of the warped image
    - Warping based on fragments; mainly either algorithms based on *triangulation* or on *grid distortion* algorithms:
      - Triangulation is good for local warping in faces, but pre-processing of images divided into triangular pieces is quite complex. Overall *less convenient*
  - Mentions names of some algorithms and proposes a new architecture, but not very useful since it targets  animation of the face
- Paper [Facial Expression Morphing and Animation with Local Warping Methods](http://ivizlab.sfu.ca/arya/Papers/IEEE/Proceedings/I%20A%20P%20-%2098/Facial%20Expression%20Morphing.pdf)  -> also from 1999 :/
  - Again, mainly for facial expression morphing
  - To get a good approximation of facial expressions with computers, they used the FACS scheme which describes the set of all possible basic actions (Action Units) performed on a human face. (other models are briefly discussed too)
  - They regard the input 2D facial image as a 2D object, use spatial transformations on the image plane to obtain the facial expressions results
- Photo warping with [WebGL](https://testdrive-archive.azurewebsites.net/Graphics/Warp/Default.html)
  - To render a warped photo, a mesh of 400 triangle coordinates, a photo, a vertex & fragment shader program and uniform points are uploaded to the GPU using WebGL.
- Paper [Silhouette-Aware Warping for Image-Based Rendering](https://igl.ethz.ch/projects/IBR/warpibr_paper.pdf)
  - Has nothing to do with face caricature or even warping in general
  - More about reconstruction and improvement of image quality, centering etc
- Paper [Caricature Generator: The Dynamic Exaggeration of Faces by Computer](http://cutting.psych.cornell.edu/pubs/brennan.pdf)
  - The theory of computation  underlying the Caricature Generator is to exaggerate the metric differences between a graphic representation of a subject face and some other  similarly  structured face,  ideal  or norm.
  - His implementation is on page 6, interesting but quite old



### Idea(s) 

- Maybe we could use pre-existing tools like Photoshop or Adobe After Effects to automatically distort/warp the faces, will need to check for feasibility of automation however.
  - update: doesn't seem to be feasible

I will try to experiment with PyChubby, see if it's own facial recognition is good enough, and if we can actually achieve caricature-level distortion. 

I am also wondering whether or not I might end up having to design my own deep network, for things such as averaging faces (if I end up doing that) or training distortion, potentially. I am unsure regarding the training capabilities of my own computer so might end up needing a server?

