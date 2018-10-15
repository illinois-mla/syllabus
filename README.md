---
layout: default
permalink: /
---

# <b><span style="color:blue">Data Analysis and Machine Learning Applications</span></b>
![](assets/pynstein.jpg)
<!-- {: style="width: 550px; float: center; margin: 30px 0 30px 0; border: 10px"} -->

* **Course:** [PHYS 398MLA](https://physics.illinois.edu/academics/courses/profile/PHYS398MLA-120188)
* **Instructor:** Prof. Mark Neubauer, [msn@illinois.edu](mailto:msn@illinois.edu)
* **TA:** Dewen Zhong, [dzhong6@illinois.edu](mailto:dzhong6@illinois.edu)
* **Lectures:** Mondays from 3-4:50 pm in 222 Loomis Laboratory of Physics
* **Need help?**
    * [![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/illinois-mla/)
        * It sends message digests to people who aren't active in the room, so feel free to ask a question even if no one's around.
    * Look through and create [issues](https://github.com/illinois-mla/syllabus/issues)
    * Office Hours
        * Dewen Zhong: Thursdays from 2-3 pm in 420 Loomis
        * Prof. Neubauer: Thursdays from 3-4 pm in 411 Loomis
   * [Email](mailto:msn@illinois.edu) for 1-on-1 help, or to set up a time to meet

## <span style="color:Red">Course Description</span>

Welcome you to the Data Analysis and Machine Learning Application (for physicists) course!

In this course, you will learn fundamentals of how to analyze and interpret scientific data and apply modern machine learning tools and techniques to problems common in physics research such as classification and regression. This course offering is very timely given the explosion of interest and rapid development of data science and artificial intelligence. Every day there are new applications of machine learning to the physical sciences in ways that are advancing our knowledge of nature.

This course is designed to be interactive and collaborative, employing Active Learning methods, at the same time developing your own skills and knowledge (and course grade :). I initiated this course out of my view that we live in an increasingly data-centric world, with both people and machines learning from vast amounts of data. There has never been a time where early-career physicists were more in need of a solid understanding in the basics of scientific data analysis, data-driven inference and machine learning, and a working knowledge of the most important tools and techniques from modern data science than today.

This is a new course and unlike any that is being taught in our Department. As such, I ask for your feedback on any aspect of the course so that I can work to improve the curriculum.

## <span style="color:Red">Prerequisites</span>

### Courses
* Credit or Concurrent Registration: [MATH 285](https://netmath.illinois.edu/college/math-285)
* Credit for [PHYS 225](https://physics.illinois.edu/academics/courses/profile/PHYS225) and [PHYS 325](https://physics.illinois.edu/academics/courses/profile/PHYS325)

### Hardware
* You need a laptop for this course. It is assumed that you have a laptop running MacOS, Linux or Windows for use both inside and outside of the class.

### Software
* Some knowledge of python preferred but not required. You do need to have a working knowledge of the basics of computer programming.

### Setting up your environment
* There is some setup required to ensure a consistent and functioning software environment on your computer to use the Jupyter notebooks in this course. This setup is detailed [here](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/Setup.ipynb) and is best started before the first lecture to work out any wrinkles so that we can get started on the physics and data science content of the course.

## <span style="color:Red">Course Overview</span>

Topics covered include:

* *Notebooks and numerical python*
* *Handling and Visualizing Data*
* *Finding structure in data*
* *Measuring and reducing dimensionality*
* *Adapting linear methods to nonlinear problems*
* *Estimating probability density*
* *Probability theory*
* *Statistical methods*
* *Bayesian statistics*
* *Markov-chain Monte Carlo in practice*
* *Stochastic processes and Markov-chain theory*
* *Variational inference*
* *Optimization*
* *Computational graphs and probabilistic programming*
* *Bayesian model selection*
* *Learning in a probabilistic context*
* *Supervised learning in Scikit-Learn*
* *Cross validation*
* *Neural networks*
* *Deep learning*

Topics will be demonstrated in-class through live-code examples/slides in Juypter notebooks, available at [syllabus/notebooks](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks).

## <span style="color:Red">Class Participation</span>

The lectures will include physics and data science pedagogy, demonstrated through live examples in Jupyter notebooks that you will work through in class. You are required to attend each lecture with your laptop and working environment. Attendance will be taken.

## <span style="color:Red">Homework</span>

Homework is an important part of the course where you will have an opportunity to apply the techniques you are learning to problems relevant to the analysis of scientific data. All assignments are listed within the [Course Outline](#course-outline). You will submit your homework via your private Github repository.

## <span style="color:Red">Projects</span>

Approximately halfway through the course, you will have the opportunity to choose from a set of projects that use open scientific data. You will be asked to answer certain questions about the data, supported by your analysis and written up in a Jupyter notebook which you will submit. Your notebook will also include background information about how the data is generated, its scientific relevance and your methodology.

## <span style="color:Red">Grading</span>

* *Class Participation*: **~30%**
* *Homework*: **~50%**
* *Research project*: **~20%**

## <span style="color:Red">Course Outline</span>

<!--################### Lecture 01 ######################-->

### <span style="color:blue">[Aug 27]</span> **Lec 01**: <span style="color:red">*Introduction*</span>

#### *Goals*
* Getting overview of the course, including reading list and homework assignments
* Setting up your environment

#### *Lecture notebooks*
* [Reading list](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/References.ipynb)
* [Course introduction](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/Intro.ipynb)
* [Setup your environment](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/Setup.ipynb)
* [Homework assignments](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/Homework.ipynb)

#### *Homework*
* Complete setting up your environment so that you can launch and execute notebooks

#### *Required reading*
* *A Whirlwind Tour of Python*, Jake VanderPlas: [free PDF](http://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf), notebooks [online](http://nbviewer.jupyter.org/github/jakevdp/WhirlwindTourOfPython/blob/master/Index.ipynb).

#### *Supplemental reading*
* None

<!--################### NO Lecture ######################-->

### <span style="color:blue">[Sep 03]</span> **NO LECTURE** (Labor Day)

<!--################### Lecture 02 ######################-->

### <span style="color:blue">[Sep 10]</span> **Lec 02**: <span style="color:red">Data Science</span>

#### Goals
* Gain familiarity with Jupyter Notebooks and Numerical python
* Learn about handling and describing data

#### Lecture notebook(s)
* [Notebooks and numerical python](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/JupyterNumpy.ipynb)
* [Handle data](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/Pandas.ipynb)

#### Homework
* [Homework 1](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/homework/Homework1.ipynb): Numerical python and data handling
  * Released on Monday, Sep 10
  * Due by __3:00 pm CDT__ on __Monday, Sept 17__

#### Supplemental reading
* [IPython: Beyond Normal Python](https://jakevdp.github.io/PythonDataScienceHandbook/01.00-ipython-beyond-normal-python.html)
* [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/index.html)
* [Introduction to NumPy](https://jakevdp.github.io/PythonDataScienceHandbook/02.00-introduction-to-numpy.html)
* [Data Manipulation with Pandas](https://jakevdp.github.io/PythonDataScienceHandbook/03.00-introduction-to-pandas.html)

<!--################### Lecture 03 ######################-->

### <span style="color:blue">[Sep 17]</span> **Lec 03**: <span style="color:red">Visualizing & Finding Structure in Data</span>

#### Goals
* Learn about visualizing data
* Learn about the importance of clustering data in physics
* Learn how to find structure in data (clustering)
   * KMeans, Spectral Clustering, DBSCAN

#### Lecture notebook(s)
* [Visualize data](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/Visualization.ipynb)
* [Find structure in data](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/Clustering.ipynb)

#### Homework
* None

#### Supplemental reading
* [Scikit-learn](http://scikit-learn.org)
* [Whitening transformation](https://en.wikipedia.org/wiki/Whitening_transformation)

<!--################### Lecture 04 ######################-->

### <span style="color:blue">[Sep 24]</span> **Lec 04**: <span style="color:red">Dimensionality & Linearity</span>

#### Goals
* Measure and reduce dimensionality
* Adapt linear models to nonlinear problems

#### Lecture notebook(s)
* [Measure and reduce dimensionality](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/Dimensionality.ipynb)
* [Adapt linear methods to nonlinear problems](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/Nonlinear.ipynb)

#### Homework
* [Homework 2](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/homework/Homework2.ipynb): Visualization, Covariance and Correlation
  * Released on Monday, Sep 24
  * Due by __3:00 pm CDT__ on __Monday, Oct 1__

#### Supplemental reading
* [Principle Component Analysis](https://en.wikipedia.org/wiki/Principal_component_analysis)
* [Blind Signal Separation](https://en.wikipedia.org/wiki/Blind_signal_separation)

<!--################### Lecture 05 ######################-->

### <span style="color:blue">[Oct 01]</span> **Lec 05**: <span style="color:red">Kernel Functions and Probability Theory</span>

#### Goals
* Learn about Kernel functions
* Learn about Probability Theory

#### Lecture notebook(s)
* [Kernel Functions](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/Nonlinear.ipynb)
* [Probability theory](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/Probability.ipynb)

#### Homework
* [Homework 3](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/homework/Homework3.ipynb):  Expectation-Maximization Algorithm, K-Means, Principle Component Analysis
  * Released on Monday, Oct 1
  * Due by __3:00 pm CDT__ on __Monday, Oct 8__

#### Supplemental reading
  * [Kernel Method](https://en.wikipedia.org/wiki/Kernel_method)
  * [Mercer's Theorem](https://en.wikipedia.org/wiki/Mercer%27s_theorem)
  * [Similarity Measure](https://en.wikipedia.org/wiki/Similarity_measure)
  * [Nonlinear Dimensionality Reduction by Locally Linear Embedding](http://science.sciencemag.org/content/290/5500/2323)

<!--################### Lecture 06 ######################-->

### <span style="color:blue">[Oct 08]</span> **Lec 06**: <span style="color:red">Probability Density Estimation and Statistics</span>

#### Goals
* Estimate probability density
* Learn about Statistical Methods

#### Lecture notebook(s)
* [Estimate probability density from Data](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/Density.ipynb)
* [Statistical methods](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/Statistics.ipynb)

#### Homework
* [Homework 4](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/homework/Homework4.ipynb): Probability
  * Released on Monday, Oct 8
  * Due by __3:00 pm CDT__ on __Monday, Oct 15__

#### Supplemental reading
* [Positive Definite Matrix definition](https://en.wikipedia.org/wiki/Positive-definite_matrix)
* [AstroML: Machine Learning and Data Mining for Astronomy](http://www.astroml.org)
* [Freedman-Diaconis Rule for choice of binning](https://en.wikipedia.org/wiki/Freedman–Diaconis_rule)
* [Kernel Density Estimation](https://en.wikipedia.org/wiki/Kernel_density_estimation)
* [Algorithms for calculating variance](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance)
* [Probability Mass Function](https://en.wikipedia.org/wiki/Probability_mass_function)

<!--################### Lecture 07 ######################-->

### <span style="color:blue">[Oct 15]</span> **Lec 07**: <span style="color:red">Bayesian Statistics and Markov-chain Monte Carlo</span>

#### Goals
* Learn about Bayesian Statistics
* Markov-chain Monte Carlo put into practice

#### Lecture notebook(s)
* [Bayesian statistics](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/Bayes.ipynb)
* [Markov-chain Monte Carlo in practice](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/MCMC.ipynb)

#### Homework
* [Homework 5](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/homework/Homework5.ipynb): Probability
  * Released on Monday, Oct 15
  * Due by __3:00 pm CDT__ on __Monday, Oct 22__

#### Supplemental reading
* [Beta Distribution](https://en.wikipedia.org/wiki/Beta_distribution)
* [Gamma Function](https://en.wikipedia.org/wiki/Gamma_function)
* [Uninformative Priors](https://en.wikipedia.org/wiki/Prior_probability#Uninformative_priors)
* [Conjugate Priors](https://en.wikipedia.org/wiki/Conjugate_prior)
* [Importance Sampling](https://en.wikipedia.org/wiki/Importance_sampling#Application_to_probabilistic_inference)
* [C. Maes, <i>An introduction to the theory of Markov processes mostly for physics students</i>](https://fys.kuleuven.be/itf/staff/christ/files/pdf/pub/markovlectures2015.pdf)
* [Foreman-Mackey, Hogg, Lang, Goodman, </i>emcee: The MCMC Hammer](https://arxiv.org/abs/1202.3665)

<!--################### Lecture 08 ######################-->

### <span style="color:blue">[Oct 22]</span> **Lec 08**: <span style="color:red">Stochastic Processes, Markov Chains & Variational Inference</span>


#### Goals
* Learn about Stochastic processes
* Learn about Markov-chain Theory
* Learn about Variational Inference

#### Lecture notebook(s)
* [Stochastic processes and Markov-chain theory](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/Markov.ipynb)
* [Variational inference](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/Variational.ipynb)

#### Homework
* None

#### Supplemental reading

<!--################### Lecture 09 ######################-->

### <span style="color:blue">[Oct 29]</span> **Lec 09**: <span style="color:red">Optimization & Comput. Graphs, Prob. Prog.</span>

#### Goals
* Learn about Optimization and Stochastic Gradient Descent
* Learn about Frameworks for Computational Graphs
* Learn about Probabilistic Programming methods

#### Lecture notebook(s)
* [Optimization](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/Optimization.ipynb)
* [Frameworks for computational graphs and probabilistic programming](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/Frameworks.ipynb)

#### Homework
* None

#### Supplemental reading

<!--################### Lecture 10 ######################-->

### <span style="color:blue">[Nov 5]</span> **Lec 10**: <span style="color:red">Bayesian Models & Probabilistic Learning & Supervised Learning </span>

#### Goals

#### Lecture notebook(s)
* [Bayesian model selection](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/ModelSelection.ipynb)
* [Learning in a probabilistic context](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/Learning.ipynb)

#### Homework
* None

#### Supplemental reading

<!--################### Lecture 11 ######################-->

### <span style="color:blue">[Nov 12]</span> **Lec 11**: <span style="color:red">Cross Validation</span>


#### Goals
* Learn about Cross Validation

#### Lecture notebook(s)
* [Supervised learning in Scikit Learn](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/Supervised.ipynb)
* [Cross validation](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/CrossValidation.ipynb)

#### Homework
* None

#### Supplemental reading

<!--################### NO Lecture ######################-->

### <span style="color:blue">[Nov 19]</span> **NO LECTURE** (Fall Break)


<!--################### Lecture 12 ######################-->

### <span style="color:blue">[Nov 26]</span> **Lec 12**: <span style="color:red">Artificial Neural Networks</span>

#### Goals
* Learning in a Neural Networks

#### Lecture notebook(s)
* [Neural networks](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/NeuralNetworks.ipynb)

#### Homework
* None

#### Supplemental reading


<!--################### Lecture 13 ######################-->

### <span style="color:blue">[Dec 03]</span> **Lec 13**: <span style="color:red">Deep Learning I</span>

#### Goals
* Learn about Deep Learning

#### Lecture notebook(s)
* [Deep learning](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/DeepLearning.ipynb)"

#### Homework
* None

#### Supplemental reading

<!--################### Lecture 14 ######################-->

### <span style="color:blue">[Dec 10]</span> **Lec 14**: <span style="color:red">Deep Learning II</span>

#### Goals

#### Lecture notebook(s)

#### Homework
* None

#### Supplemental reading

## _________________________________________

## <span style="color:Red">Resources</span>

### References

* You can find the references list, including required and recommended reading, at [Reading list](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/References.ipynb)

* Some quick reference guides
    * [Linux Bash Shell](https://learncodethehardway.org/unix/bash_cheat_sheet.pdf)
    * [Github](https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf)
    * [Conda](https://conda.io/docs/_downloads/conda-cheatsheet.pdf)
    * [Python](http://ehmatthes.github.io/pcc/cheatsheets/README.html)
    * [Markdown](http://packetlife.net/media/library/16/Markdown.pdf)
    * Jupyter Notebooks: [Interface](http://datacamp-community.s3.amazonaws.com/48093c40-5303-45f4-bbf9-0c96c0133c40), [Keyboard shortcuts](https://www.cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/pdf_bw)

### Tools

* Sharing code snippets: [gist.github.com](https://gist.github.com/)
* Asking questions of broader development community: [Stack Overflow](http://stackoverflow.com/)

#### *Git* and *GitHub*

* [Official GitHub Help](https://help.github.com/)
* [Recommended resources](http://hackerhours.org/resources.html#github)

#### *Anaconda* and *Conda*
* [Official site](https://www.anaconda.com)
* [Conda](https://conda.io/docs)

#### *Project Jupyter*
* [Official site](http://jupyter.org)
* [nbviewer](https://nbviewer.jupyter.org)

#### *Atom*
I found the Atom editor to be the best option. It has full Github integration which avoids having to type git commands every time
* [Official Site](https://atom.io)

With a plug-in, it also does latex syntax highlighting. Install it with:

``apm install latex``

``apm install language-latex``

## <span style="color:Red">Acknowledgements</span>

I would like to acknowledge [David Kirby](https://github.com/dkirkby) at the University of California at Irvine for the materials and setup for which this course is based and the helpful discussions we have had. I would like to thank [Matthew Feickert](https://github.com/matthewfeickert) for his guidance and contributions to the course. I also acknowledge the course at <a href="https://github.com/advanced-js">github.com/advanced-js</a> for which the syllabus template was utilized.

## _________________________________________

Material for a [University of Illinois](http://illinois.edu) course offered by the [Physics Department](https://physics.illinois.edu).

Content is maintained on [github](https://github.com/illinois-mla) and distributed under a [BSD3 license](https://opensource.org/licenses/BSD-3-Clause).

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause) [![nbviewer](https://img.shields.io/badge/view%20on-nbviewer-brightgreen.svg)](http://nbviewer.jupyter.org/github/illinois-mla/syllabus/blob/master/notebooks/Contents.ipynb)
