# bachelor-sem-project
EPFL-BA5 Bachelor Semester Project @ IDIAP



#### Title:
Learning of non-photorealistic renderings for a caricaturist robot 

#### Description:
This project aims to review, categorize and test existing approaches in deep learning to map an image to a set of trajectories that a robot can then draw on a canvas, by taking the example of portrait caricatures as an example of generative non-photorealistic rendering (NPR) problem (see CariGAN or WarpGAN as starting examples). Several data processing pipelines can be considered, with parts that can be specified manually, and others that can be learned from examples. It also includes the potential consideration of intermediary steps, such as detecting the location of facial features (e.g., by using Google's MediaPipe Face Mesh), image-to-image processing applying pencil/brush sketch rendering effects, or applying a distortion mask for a warping transformation defined explicitly. The project also aims at studying metrics or methods to compare these different approaches. The selected approach(es) will take into account the amount of data that these methods require, the availability of these data and of pretrained models, and the possibility of employing the selected method(s) on smartphones or CPUs (instead of GPUs).
