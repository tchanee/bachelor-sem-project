##### 14/10/2021

What we mostly care about is the warping of the face, not necessarily the processing.

the idea was to find the facial landmarks, and distort them using opencv functions or something

how to choose which facial landmarks to distort?

	- they were first looking at caricature style drawings, to get inspired

###### how they transform the picture currently: 

- ergodic control technique
- u sample the picture (it is a seen a probabilistic distribution)
- those are the starting positions for strokes ^
- the strokes are draw using the ergodic control technique



###### I was too focused on the face recognition techniques, a way to distort the image is more important 



#### Parts of the pipeline:

- face recognition first, then the robot tries to align your nose to the middle of the image
- then the image is recorded (currently the operator presses `space` or something)
- then its the part where we do the caricature style of the image (currently not being done), here there is some image processing also (filtering to get rid of background, unwanted features of the face)
- ergodic control technique to then draw the resulting caricature (it expects a gray-scale image)
  - it computes strokes in 2D in the image frame, which is then transformed into 3D points, which then runs through the algorithm *ILQR* which gives a joint angle trajectory

Ideally, what I should find is a way to caricaturize a portrait (check photo i took on my phone) to do it automatically (the photo is being done by hand) + it's implementation if possible

virtual spring damp system can be used to link 2 points in the face (?)

maybe try working on a system that takes an image as input and outputs it caricaturized/deformed in a certain way

	- maybe i could do parts of it one at a time, so a function that distorts the forehead, one the mouth etc etc, and potentially reassemble at the end.



the face detection is used to find the facial landmarks that will be distorted/caricaturized (i wont really be doing the face detection, i can use the one they implemented with dlib, but it's upto to choose what I want. focus on caricature technique)





general structure of the report should follow that of a technical report

- literature review, relevant state of the art
- describe in detail how my wethods works *my method needs to have maths involved, parameters aswell -> could be played around with them for different result!* 
- experiements, distorted faces that I made
- comparing them against relevant state of the art techniques
- some conclusions about htat

include images, diagrams,  etc in the report!



### Notes during meeting

- they stopped using mediapipe facemesh because it's in python. it was working fine though
- I should have access to the code in the gitlab projects, i currently don't as a
- the project has technically been submitted a week ago, now there will be a collaboration with another university (one in Constants and one in London) that will focus on the physical aspects (which pens, brushes, strokes, colors etc







START LOOKING INTO WARPING , NOT NECESSARILY FACES ONLY, JUST WARPING OF POINTS IN GENERAL (but keep the face in mind!!!) 

