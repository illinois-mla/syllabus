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
* It is assumed that you have a Mac or Windows laptop for use both inside and outside of the class.

### Software
* Some knowledge of python preferred but not required. You do need to have knowledge of the basics of computer programming.

### Setup of your environment
* There is some setup required to ensure a consistent and functioning software environment to use the Jupyter notebooks in this course. This setup is detailed [here](notebooks/Setup.ipynb) and is best started before the first lecture to work out any wrinkles so that we can get started on the physics and data science content of the course .

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

Topics will be demonstrated through live-code examples/slides in Juypter notebooks, available at [advanced-js.github.io/deck](http://advanced-js.github.io/deck/).  Additional exercises will completed in-class.

## Homework/Projects

All assignments are listed within the [Course Outline](#course-outline).

### Workflow

If you're using GitHub Desktop, these general instructions will help:

* <https://guides.github.com/activities/forking/>
* <https://help.github.com/desktop/guides/contributing/>

Enabling `Edit`->`Automatically Sync after Committing` is recommended. Here are the steps:

1. Fork the repository for the exercise/project (found under [github.com/advanced-js](https://github.com/advanced-js)).
1. Clone the repository to your computer.
1. Open the `index.html` file in a browser and open the Developer Tools.
1. Modify the files to complete your solution.
1. Refresh the `index.html` page to see the results, and repeat.
1. Make sure all of your code is committed.
1. Push/sync up to GitHub.
1. [Create a pull request](https://help.github.com/articles/creating-a-pull-request/) on the original repository. All assignments are due at the start of the following class, unless otherwise specified.
1. You can continue to push fixes and improvements until the close date (listed in Classes) – just add a comment in the pull request to let me know it's been updated.

When the pull request is created, you should see a message saying that "the Travis CI build is in progress" – this means that your solution is being automatically checked for syntax errors.  If this "build" ends up failing (which will show a red "X"), click through the "details" link and scroll to the bottom to see what the errors were.  Per the [requirements](#requirements) below, please fix the issues and push up the changes.

Feedback will be given in the pull request, so please respond with your thoughts and questions!  You are welcome to open the pull request early as a work-in-progress if you are stuck and want to ask a question.  Note that your solution will also be live at `http://USERNAME.github.io/EXERCISE`.

#### Versions

For exercises with multiple Versions (`V1`, `V2`, etc.) listed in the README: these are intended as guidelines for how to complete the assignments in the smallest/simplest possible increments.  You are expected to reach the highest Version for each assignment by the due date. See also: [extra credit](#extra-credit).

### Requirements

These apply to real life, as well.

* [Travis CI](https://docs.travis-ci.com/) build should pass, which includes:
    * All HTML files should pass [W3C Markup Validation](http://validator.w3.org).
    * All written JS should pass [JSHint](http://jshint.com).
* Must apply "good programming style" learned in class
    * Functions should be "short" (see [Sandi Metz's rules for developers](https://robots.thoughtbot.com/sandi-metz-rules-for-developers)).
    * Optimize for readability.
        * ["Programs must be written for people to read, and only incidentally for machines to execute." -Harold Abelson](https://www.goodreads.com/quotes/9168-programs-must-be-written-for-people-to-read-and-only)
    * Avoid using anonymous callbacks within other functions, especially if the callback is more than one or two lines.
    * For projects, use Object-Oriented Programming.
* Any borrowed code must be properly [annotated](#instructor).

#### Extra Credit

Bonus points for:

* Automated tests
* Creativity (as long as requirements are fulfilled)
* Anything listed under `BONUS` in the README of the exercise.

## Course Outline

<!--################### Lecture 01 ######################-->

### <span style="color:blue">[Aug 27]</span> Lecture 01: <span style="color:red">Introduction</span>

#### Goals
* Getting overview of the course, including reading list and homework assignments
* Setting up your environment

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 02 ######################-->

### <span style="color:blue">[Sep 03]</span> Lecture 02: <span style="color:red">Data Science</span>

#### Goals
* Gain familiarity with Jupyter Notebooks and Numerical python
* Learn about handling and visualizing scientific data

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 03 ######################-->

### <span style="color:blue">[Sep 10]</span> Lecture 03: <span style="color:red">Dimensionality & Linearity</span>

#### Goals
* Find structure in data
* Measure and reduce dimensionality
* Adapt linear models to nonlinear problems

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 04 ######################-->

### <span style="color:blue">[Sep 17]</span> Lecture 04: <span style="color:red">Probability</span>

#### Goals
* Estimate probability density
* Learn about Probability Theory

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 05 ######################-->

### <span style="color:blue">[Sep 24]</span> Lecture 05: <span style="color:red">Statistics</span>

#### Goals
* Learn about Statistical Methods
* Learn about Bayesian Statistics

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 06 ######################-->

### <span style="color:blue">[Oct 01]</span> Lecture 06: <span style="color:red">Stochastic processes & Markov chains</span>

#### Goals
* Learn about Stochastic processes
* Learn about Markov-chain Theory
* Markov-chain Monte Carlo put in practice

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

#### Supplemental reading
* [C. Maes, <i>An introduction to the theory of Markov processes mostly for physics students</i>](https://fys.kuleuven.be/itf/staff/christ/files/pdf/pub/markovlectures2015.pdf)

<!--################### Lecture 07 ######################-->

### <span style="color:blue">[Oct 08]</span> Lecture 07: <span style="color:red">Variational Inference</span>

#### Goals
* Learn about Variational Inference

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 08 ######################-->

### <span style="color:blue">[Oct 15]</span> Lecture 08: <span style="color:red">Optimization</span>

#### Goals
* Learn about Optimization

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 09 ######################-->

### <span style="color:blue">[Oct 22]</span> Lecture 09: <span style="color:red">Comput. Graphs & Probabilistic Programming</span>

#### Goals
* Learn about Frameworks for Computational Graphs
* Learn about Probabilistic Programming methods

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 10 ######################-->

### <span style="color:blue">[Oct 29]</span> Lecture 10: <span style="color:red">Bayesian Models</span>

#### Goals
* Learn about Bayesian model selection

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 11 ######################-->

### <span style="color:blue">[Nov 05]</span> Lecture 11: <span style="color:red">Probabilistic Learning</span>

#### Goals
* Learning in a probabilistic context

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 12 ######################-->

### <span style="color:blue">[Nov 12]</span> Lecture 12: <span style="color:red">Supervised Learning</span>

#### Goals
* Supervised learning in scikit-learn

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 13 ######################-->

### <span style="color:blue">[Nov 26]</span> Lecture 13: <span style="color:red">Cross Validation</span>

#### Goals
* Learn about Cross Validation

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 14 ######################-->

### <span style="color:blue">[Dec 03]</span> Lecture 14: <span style="color:red">Neural Networks</span>

#### Goals
* Learn about Neural Networks

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 15 ######################-->

### <span style="color:blue">[Dec 10]</span> Lecture 15: <span style="color:red">Deep Learning</span>

#### Goals
* Learn about Deep Learning

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

## Resources

### Required Reading

* Stuff

### Recommended Reading

* Stuff

#### Specific Topics

* Stuff

#### Other Lists

* Stuff

### Tools

* sharing code snippets: [gist.github.com](https://gist.github.com/)
* asking questions: [Stack Overflow](http://stackoverflow.com/)

#### GitHub

* Git and GitHub
    * [Official GitHub Help](https://help.github.com/)
    * [Recommended resources](http://hackerhours.org/resources.html#github)
* GitHub Pages
    * [Official site](https://pages.github.com/)
    * [Thinkful guide](http://www.thinkful.com/learn/a-guide-to-using-github-pages/)

### Reference

* [w3schools](http://www.w3schools.com/jsref/default.asp)

## Grading

* Class Participation – 30%
* Homework – 70%

## Bottom

Material for a [University of Illinois](http://illinois.edu) course offered by the [Physics Department](https://physics.illinois.edu).

Content is maintained on [github](https://github.com/illinois-mla) and distributed under a [BSD3 license](https://opensource.org/licenses/BSD-3-Clause).

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause) [![nbviewer](https://img.shields.io/badge/view%20on-nbviewer-brightgreen.svg)](http://nbviewer.jupyter.org/github/dkirkby/MachineLearningStatistics/tree/master/notebooks/Contents.ipynb)
