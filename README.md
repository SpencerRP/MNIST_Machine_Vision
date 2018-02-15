# Capstone
#### Goals
My overall, pretty obvious goal is to correctly predict which digit is represented by the 2-d image of a handwritten digit. My more near term goals are to implement effective & speedy image processing methods by hand (I need to learn more about noise removal and deskewing in particular), to actually be able to run models on the full dataset (currently not possible: They just take forever, even on a t2 Large.), and to fully understand how neural networks work: I feel that while I could explain the vague details of how they work (i.e. like neurons) I do not particularly firmly grasp the math. 

#### Metrics
My metric for my main goal is the accuracy of the prediction. Accuracy is more valuable than specificity et. al because getting a character wrong in either direction isn't a life or death thing, we only care about getting it wrong - we don't care about bias, we care about variance. I have not yet reached the point of focusing on that, solely because my models just are not fitting.

#### Findings
Thus, at present I do not have any findings.

#### Background/Blather that I'll shape into the opening for the high-level presentation.
The MNIST dataset is two sets of 28x28-sized images of digits handwritten by government officials and by high school students. These 28x28 images can be unfolded into vectors of length 784. Thus, each set is an array of n length and 784 width. The training set contains 60 thousand of these images in a 60k x 784 matrix and is accompanied by a 60k x 1 value set. The testing set contains 10k x 784 & 10k x 1. Needless to say, this is a lot of data. This is true even though the bits that represent the images are only on a 0-255 (256 total size) range.

My variables of interest are the 784 features which make up the 28 by 28 images in the MNIST dataset. Because images are more or less superficially recognizable by humans - i.e. based on the 28x28 image most anyone can figure out what digit it is - these features should be sufficient to accurately predict which digit it is. And indeed, even naive models trained on a mere sixth of the dataset perform with ~88% accuracy.

So, what steps need to be taken to make this score better? At least based on the work presented in Yann Lecun's 1998 paper reviewing progress that has been made in the field and the advantages of a then-relatively-new approach, neural networks, one can get the best scores through a) Pre-processing and then using a GridSearchCV for normal models, or c) simply shoving it all into a Neural Net, which outperforms nearly all of the normal methods. I.e., a "committee of 35 conv. net, 1-20-P-40-P-150-10 w/ elastic distortions" has a loss rate of 0.22%, while the next best non-neural model, "K-NN with non-linear deformation (P2DHMDM)", has a loss rate of 0.52% - more than double.

Because the images was pre-processed, I did not need to perform data imputation or remove outliers. I did, however, perform the following pre-processing methods: de-noising with an nl-means algorithm found on scikit-images; blurring with a box-blur method made myself; deskewing with a deskewing function found on https://fsix.github.io/; and finally a 1-pixel shift that expanded the data by 4 additional sets of images.

I have yet to see what the end result of my work is because, again, non of the models are actually finishing running.

Once I have finished this process I will need to select which of the models are best. Out of the non-neural-net models, I expect that KNeighborsClassifier will do the best. KNC is somewhat remarkably well-suited to this. Fundamentally, the differences between letters are distance-based. Where convolutional neural networks - and probably KNN w/ shiftable edges - perform better is their ability to segment significant aspects of the feature array - and thus areas in the image which differ significantly between digits.

### What I Could Have Done Better
What I can improve:
-Actually get the GridSearchCV models to work.
-Improve the speed of my pre-processing functions.
-Actually implement the NeuralNet (focused too much on creating the pre-processing functions).
-Take aspirin when I have a headache.

### Questions For Mike & Paul
Why might my models not be able to run? While it's an issue of memory for GridSearchCV, my basic Linear Regression model is only taking up half of the available memory and yet hasn't finished fitting in more than 20 minutes. So I really don't get it. A single Linear Regression model?? Really??

How can I speed up my pre-processing methods? At the moment, each of them takes around 0.1 seconds, which adds up.

Beyond getting the models to actually work, what standards should I impose on myself in order to consider this capstone sufficiently well-developed?

From a high-level, abstract perspective, what is it about the fundamental nature of neural networks and the MNIST problem that makes them suited for each other?

What steps would be necessary to apply these models to less well-prepared images? Do neural networks need any pre-processing? (I'm assuming they do not, but it would be good to double-check.)

What other projects or canonical dataset build off of the skills I appear to have gained here?

