- What I had done:
  - made sure to TForm Zucc into 600x600, and align his eye so that results are coherent
  - found his biggest distance from average face, but that seemed "little" so I also used his second biggest distance
    - Note that I checked if it was smaller or bigger than average
  - Regarding the results... Idk how to feel. I feel like processing the image won't give a real "caricature", just a funny deformation. For a real caricature, i feel like one would need to "redraw" the entire image 





Realistic process might not matter, the final output is for me after all, it will be further abstracted by the robot drawing (sharp edges might go away)

 - its more important that the brightness and contrasts etc are preserved
 - might get access to a python implementation of the drawing
   	- could use it draw my results, and see what's up (if i should make edges bigger or stuff)

maybe try to stretch zuckerberg's face (bottom to top)





openCV pencil sketch transform





### For next week

- ill try with a different face
- see how far I can take the deformations
- try the pencil sketch maybe
- maybe add in the average boxplots how far the face-to-caricature is  
- regarding the distribution (distance), maybe try and see a measure of how different I am
  - maybe a measure of how different the face is from the average one
  - then determine the measure/scale of the deformation as a function of the previous measure
- be clear of how many images I used to make the average
  - maybe note a difference between male/female (their natural shape/sizes are diff)
  - then maybe generate some examples