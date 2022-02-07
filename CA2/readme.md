# Color Space Transformations and Analysis - Computer Vision Assignment 2

## Instructions for execution
1. Open the Colab notebook CV_Assignment_2.ipynb with colab for jupyter notebook
2. Run all the cells sequentially and see the output
## Task:
Find, tabulate and discuss the average hue, saturation and intensity differences in the 10 color
images between:
1. The original given image 𝑰(𝑥, 𝑦) = [𝑅(𝑥, 𝑦), 𝐺(𝑥, 𝑦), 𝐵(𝑥, 𝑦)] and 𝑰 ′ (𝑥, 𝑦) = 𝑰(𝑥, 𝑦) × 𝑝, 0 < 𝑝 <1 .Ignore all pixels of 𝑰(𝑥, 𝑦) where 𝑅(𝑥, 𝑦) = 𝐺(𝑥, 𝑦) = 𝐵(𝑥, 𝑦).
2. The original given image 𝑰(𝑥, 𝑦) = [𝑅(𝑥, 𝑦), 𝐺(𝑥, 𝑦), 𝐵(𝑥, 𝑦)] and 𝑰 ′ (𝑥, 𝑦) = 𝑰(𝑥, 𝑦) + [𝐺(𝑥, 𝑦) −
𝑅(𝑥, 𝑦), 𝐵(𝑥, 𝑦) − 𝐺(𝑥, 𝑦), 𝑅(𝑥, 𝑦) − 𝐵(𝑥, 𝑦)]. Again, ignore all pixels of 𝑰(𝑥, 𝑦) where 𝑅(𝑥, 𝑦) =
𝐺(𝑥, 𝑦) = 𝐵(𝑥, 𝑦).
3. The original given image 𝑰(𝑥, 𝑦) = [𝑅(𝑥, 𝑦), 𝐺(𝑥, 𝑦), 𝐵(𝑥, 𝑦)] and
𝑰 ′ (𝑥, 𝑦) = [𝑅′(𝑥, 𝑦), 𝐺′(𝑥, 𝑦), 𝐵′(𝑥, 𝑦)] obtained by applying the given AWB. While doing analysis of
the hue change, ignore all pixels of 𝑰(𝑥, 𝑦) where 𝑅(𝑥, 𝑦) = 𝐺(𝑥, 𝑦) = 𝐵(𝑥, 𝑦) and 𝑅 ′ (𝑥, 𝑦) =
𝐺 ′ (𝑥, 𝑦) = 𝐵 ′ (𝑥, 𝑦).
Caution: Hue difference is angle difference!

## Deliverables (in a single .zip file):
1. A document containing all the findings asked under the task given along with discussion
using not more than 300 words in each part.
2. Codes used to generate the findings, tabulated values along with a command sequence
to generate all the values.