> showing him what I've done a 

maybe i hardcode caricature custom actions and use those at the end, but is this a good idea?



pre-defining everything manually first is a first step



maybe explore it in a direction where i make learning by demonstrations

- user gives demonstrations of what the caricature should look like
  - NOT A GOOD IDEA
- depending on these demonstrations, transform the image

should like into a solution that requires more of an algorithmic structure instead of tweaking parameters, would be more interesting for both me and to write about



a potential ways

- 
- detect the naturally large features in the face, then enhancing them/warping them and decrease the rest (like what i suggested in the first week)
  - compute average face
  - find differences with new input
  - find largest/smallest features
  - distort them (maybe have a scaling user parameter that says how large the distortion would be)
    - no network trained here
    - rather look into statistical methods, like simple gaussian mixture algorithms, clustering algorithms
      - statistical learning (feel free to ask Tobias for his advice/opinion on this)

**for next week i will look into computing an average face** this next step is important, so far ive been exploring, i should try and present this in 2 weeks (take a face, see the difference with an average face)

##### suggestion

. start with (and maybe sufficient for now), look at all the face mesh landmarks and calculate its gaussian distribution (given whatever number of input faces I have).  (so for new inputs, i'd be comparing **THE LANDMARKS** through the gaussian distribution, and pixel-by-pixel) 

with gaussians it would also be very easy to plot



### Administrative

need to send timeslots in the week of the 15th november of when im available, since slyvain very busy rn.

