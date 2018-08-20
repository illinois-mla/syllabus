---
layout: default
permalink: /
---

# <b><span style="color:blue">Data Analysis and Machine Learning Applications</span></b>
![](assets/pynstein.jpg)
<!-- {: style="width: 550px; float: center; margin: 30px 0 30px 0; border: 10px"} -->

* **Course:** [PHYS 398MLA](https://physics.illinois.edu/academics/courses/profile/PHYS398MLA-120188)
* **Instructor:** Mark Neubauer, [msn@illinois.edu](mailto:msn@illinois.edu)
* **TA:** Dewen Zhong, [dzhong6@illinois.edu](mailto:dzhong6@illinois.edu)
* **Lectures:** Mondays from 3-4:50 pm in 222 Loomis Laboratory of Physics
* **Need help?**
    * [![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/illinois-mla/)
        * It sends message digests to people who aren't active in the room, so feel free to ask a question even if no one's around.
    * Look through and create [issues](https://github.com/illinois-mla/syllabus/issues)
    * Office Hours : TBD
   * [Email](mailto:msn@illinois.edu) for 1-on-1 help, or to set up a time to meet

## Course Description

In this course, you will learn the fundamentals of how to analyze and interpret scientific data and apply modern machine learning tools and techniques to problems such as classification and regression.

## Prerequisites

### Courses
* Credit or Concurrent Registration: [MATH 285](https://netmath.illinois.edu/college/math-285)
* Credit for [PHYS 225](https://physics.illinois.edu/academics/courses/profile/PHYS225) and [PHYS 325](https://physics.illinois.edu/academics/courses/profile/PHYS325)

### Hardware
* You need a laptop for this course. It is assumed that you have a Mac or Windows laptop for use both inside and outside of the class.

### Software
* Some knowledge of python preferred but not required. You do need to have a working knowledge of the basics of computer programming.

### Setting up your environment
* There is some setup required to ensure a consistent and functioning software environment on your computer to use the Jupyter notebooks in this course. This setup is detailed [here](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/Setup.ipynb) and is best started before the first lecture to work out any wrinkles so that we can get started on the physics and data science content of the course.

## Course Overview

Topics covered include:

* Notebooks and numerical python
* Handling and Visualizing Data
* Finding structure in data
* Measuring and reducing dimensionality
* Adapting linear methods to nonlinear problems
* Estimating probability density
* Probability theory
* Statistical methods
* Bayesian statistics
* Markov-chain Monte Carlo in practice
* Stochastic processes and Markov-chain theory
* Variational inference
* Optimization
* Computational graphs and probabilistic programming
* Bayesian model selection
* Learning in a probabilistic context
* Supervised learning in Scikit-Learn
* Cross validation
* Neural networks
* Deep learning

Topics will be demonstrated in-class through live-code examples/slides in Juypter notebooks, available at [syllabus/notebooks](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks).

## Homework/Projects

All assignments are listed within the [Course Outline](#course-outline).

## Course Outline

<!--################### Lecture 01 ######################-->

### <span style="color:blue">[Aug 27]</span> Lecture 01: <span style="color:red">Introduction</span>

#### Goals
* Getting overview of the course, including reading list and homework assignments
* Setting up your environment

#### Lecture notebook(s)
* [Setup your environment](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/Setup.ipynb)
* [Reading list](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/References.ipynb)
* [Homework assignments](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/Homework.ipynb)
* [Course introduction](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/Intro.ipynb)

#### Homework
* None

#### Supplemental reading

<!--################### Lecture 02 ######################-->
<!--
### <span style="color:blue">[Sep 03]</span> Lecture 02: <span style="color:red">Data Science</span>

#### Goals
* Gain familiarity with Jupyter Notebooks and Numerical python
* Learn about handling and visualizing scientific data

#### Lecture notebook(s)
* [Notebooks and numerical python](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/JupyterNumpy.ipynb)
* [Handle data](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/Pandas.ipynb)
* [Visualize data](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/Visualization.ipynb)

#### Homework
* None

#### Supplemental reading

<!--################### Lecture 03 ######################-->
<!--
### <span style="color:blue">[Sep 10]</span> Lecture 03: <span style="color:red">Dimensionality & Linearity</span>

#### Goals
* Find structure in data
* Measure and reduce dimensionality
* Adapt linear models to nonlinear problems

#### Lecture notebook(s)
* [Find structure in data](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/Clustering.ipynb)
* [Measure and reduce dimensionality](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/Dimensionality.ipynb)
* [Adapt linear methods to nonlinear problems](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/Nonlinear.ipynb)

#### Homework
* None

#### Supplemental reading

<!--################### Lecture 04 ######################-->
<!--
### <span style="color:blue">[Sep 17]</span> Lecture 04: <span style="color:red">Probability</span>

#### Goals
* Estimate probability density
* Learn about Probability Theory

#### Lecture notebook(s)
* [Estimate probability density](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/Density.ipynb)
* [Probability theory](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/Probability.ipynb)

#### Homework
* None

#### Supplemental reading

<!--################### Lecture 05 ######################-->
<!--
### <span style="color:blue">[Sep 24]</span> Lecture 05: <span style="color:red">Statistics</span>

#### Goals
* Learn about Statistical Methods
* Learn about Bayesian Statistics

#### Lecture notebook(s)
* [Statistical methods](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/Statistics.ipynb)
* [Bayesian statistics](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/Bayes.ipynb)

#### Homework
* None

#### Supplemental reading

<!--################### Lecture 06 ######################-->
<!--
### <span style="color:blue">[Oct 01]</span> Lecture 06: <span style="color:red">Stochastic processes & Markov chains</span>

#### Goals
* Learn about Stochastic processes
* Learn about Markov-chain Theory
* Markov-chain Monte Carlo put in practice

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)
* [Markov-chain Monte Carlo in practice](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/MCMC.ipynb)
* [Stochastic processes and Markov-chain theory](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/Markov.ipynb)

#### Homework
* None

#### Supplemental reading
* [C. Maes, <i>An introduction to the theory of Markov processes mostly for physics students</i>](https://fys.kuleuven.be/itf/staff/christ/files/pdf/pub/markovlectures2015.pdf)

<!--################### Lecture 07 ######################-->
<!--
### <span style="color:blue">[Oct 08]</span> Lecture 07: <span style="color:red">Variational Inference</span>

#### Goals
* Learn about Variational Inference

#### Lecture notebook(s)
* [Variational inference](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/Variational.ipynb)

#### Homework
* None

#### Supplemental reading

<!--################### Lecture 08 ######################-->
<!--
### <span style="color:blue">[Oct 15]</span> Lecture 08: <span style="color:red">Optimization</span>

#### Goals
* Learn about Optimization

#### Lecture notebook(s)
* [Optimization](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/Optimization.ipynb)

#### Homework
* None

#### Supplemental reading

<!--################### Lecture 09 ######################-->
<!--
### <span style="color:blue">[Oct 22]</span> Lecture 09: <span style="color:red">Comput. Graphs & Probabilistic Programming</span>

#### Goals
* Learn about Frameworks for Computational Graphs
* Learn about Probabilistic Programming methods

#### Lecture notebook(s)
* [Frameworks for computational graphs and probabilistic programming](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/Frameworks.ipynb)

#### Homework
* None

#### Supplemental reading

<!--################### Lecture 10 ######################-->
<!--
### <span style="color:blue">[Oct 29]</span> Lecture 10: <span style="color:red">Bayesian Models</span>

#### Goals
* Learn about Bayesian model selection

#### Lecture notebook(s)
* [Bayesian model selection](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/ModelSelection.ipynb)

#### Homework
* None

#### Supplemental reading

<!--################### Lecture 11 ######################-->
<!--
### <span style="color:blue">[Nov 05]</span> Lecture 11: <span style="color:red">Probabilistic Learning</span>

#### Goals
* Learning in a probabilistic context

#### Lecture notebook(s)
* [Learning in a probabilistic context](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/Learning.ipynb)

#### Homework
* None

#### Supplemental reading

<!--################### Lecture 12 ######################-->
<!--
### <span style="color:blue">[Nov 12]</span> Lecture 12: <span style="color:red">Supervised Learning</span>

#### Goals
* Supervised learning in scikit-learn

#### Lecture notebook(s)
* [Supervised learning in Scikit Learn](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/Supervised.ipynb)

#### Homework
* None

#### Supplemental reading

<!--################### Lecture 13 ######################-->
<!--
### <span style="color:blue">[Nov 26]</span> Lecture 13: <span style="color:red">Cross Validation</span>

#### Goals
* Learn about Cross Validation

#### Lecture notebook(s)
* [Cross validation](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/CrossValidation.ipynb)

#### Homework
* None

#### Supplemental reading

<!--################### Lecture 14 ######################-->
<!--
### <span style="color:blue">[Dec 03]</span> Lecture 14: <span style="color:red">Neural Networks</span>

#### Goals
* Learn about Neural Networks

#### Lecture notebook(s)
* [Neural networks](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/NeuralNetworks.ipynb)

#### Homework
* None

#### Supplemental reading

<!--################### Lecture 15 ######################-->
<!--
### <span style="color:blue">[Dec 10]</span> Lecture 15: <span style="color:red">Deep Learning</span>

#### Goals
* Learn about Deep Learning

#### Lecture notebook(s)
* [Deep learning](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/DeepLearning.ipynb)"

#### Homework
* None

#### Supplemental reading
-->
## Resources

### References

* You can find the references list, including required and recommended reading, at [Reading list](https://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/References.ipynb)

### Tools

* Sharing code snippets: [gist.github.com](https://gist.github.com/)
* Asking questions: [Stack Overflow](http://stackoverflow.com/)

#### GitHub

* Git and GitHub
    * [Official GitHub Help](https://help.github.com/)
    * [Recommended resources](http://hackerhours.org/resources.html#github)
* GitHub Pages
    * [Official site](https://pages.github.com/)
    * [Thinkful guide](http://www.thinkful.com/learn/a-guide-to-using-github-pages/)

## Grading

* TBD

<!--
* Class Participation: 30%
* Homework: 70%
* Research project: XX%
-->

## Acknowledgements

I would like to acknowledge David Kirby at the University of California at Irvine for the materials and setup for which this course is based and the helpful discussions we have had. I also acknowledge the course at href="https://github.com/advanced-js">github.com/advanced-js</a> for which the syllabus template was utilized.

## _________________________________________

Material for a [University of Illinois](http://illinois.edu) course offered by the [Physics Department](https://physics.illinois.edu).

Content is maintained on [github](https://github.com/illinois-mla) and distributed under a [BSD3 license](https://opensource.org/licenses/BSD-3-Clause).

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause) [![nbviewer](https://img.shields.io/badge/view%20on-nbviewer-brightgreen.svg)](http://nbviewer.jupyter.org/github/illinois-mla/syllabus/tree/master/notebooks/Contents.ipynb)
