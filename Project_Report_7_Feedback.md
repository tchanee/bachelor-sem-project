regarding lost tail/whisker in statistics: it's lost since my top 25% are pretty much at the max range

in the long run maybe consider a distance measure that considers the variance (so not just the ratio -> it doesn't use the full information that you have)









for next week:

- maybe change distance metric
- maybe try to caricaturize zuckerberg
  - 2 options
    - PyChubby
    - triangulation + transform method;
      - tobias proposes for ex if i want to change mouth, 
        - either just transform mouth and leave the rest untouched
          - calculate mouth landmark triangulations and do something with them
        - or 
- Maybe consider Areas instead of distance
  - openCV function that lets you find convex hull of points
    - then maybe find a function that calculates area of that convex hul
  - BIG ISSUE is that need more facial landmarks







NOTES:

```
# wont use triangulation, these are affine transforms with a scale
# because when i used delaunay i had a goal of going from T1 to T2, but here no T2
# so i just used affine transform to a reference space where i do my shit
```