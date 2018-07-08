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

* Credit or Concurrent Registration: [MATH 285](https://netmath.illinois.edu/college/math-285)
* Credit for [PHYS 225](https://physics.illinois.edu/academics/courses/profile/PHYS225) and [PHYS 325](https://physics.illinois.edu/academics/courses/profile/PHYS325)
* Some knowledge of python preferred but not required

These won't be enforced by the instructor, but you will be pretty lost without understanding those concepts. If you need a refresher, take a look at the [Beginner Materials](#beginner-materials).

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

### <b><span style="color:blue">[Aug 27]</span></b> Lecture 01
<b><span style="color:red">Setting your environment, Reading list, Homework assignments, Course introduction</span></b>

#### Goals
* Learn stuff

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 02 ######################-->

### <b><span style="color:blue">[Sep 03]</span></b> Lecture 02
<b><span style="color:red">Notebooks and numerical python, Handling data, Visualize data</span></b>

#### Goals
* Learn stuff

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 03 ######################-->

### <b><span style="color:blue">[Sep 10]</span></b> Lecture 03
<b><span style="color:red">Find structure in data, Measure and reduce dimensionality, Adapt linear methods to nonlinear problems</span></b>

#### Goals
* Learn stuff

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 04 ######################-->

### <b><span style="color:blue">[Sep 17]</span></b> Lecture 04
<b><span style="color:red">Estimate probability density, Probability theory</span></b>

#### Goals
* Learn stuff

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 05 ######################-->

### <b><span style="color:blue">[Sep 24]</span></b> Lecture 05
<b><span style="color:red">Statistical methods, Bayesian statistics</span></b>

#### Goals
* Learn stuff

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 06 ######################-->

### <b><span style="color:blue">[Oct 01]</span></b> Lecture 06
<b><span style="color:red">Markov-chain Monte Carlo in practice, Stochastic processes and Markov-chain theory</span></b>

#### Goals
* Learn stuff

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 07 ######################-->

### <b><span style="color:blue">[Oct 08]</span></b> Lecture 07
<b><span style="color:red">Variational inference</span></b>

#### Goals
* Learn stuff

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 08 ######################-->

### <b><span style="color:blue">[Oct 15]</span></b> Lecture 08
<b><span style="color:red">Optimization</span></b>

#### Goals
* Learn stuff

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 09 ######################-->

### <b><span style="color:blue">[Oct 22]</span></b> Lecture 09
<b><span style="color:red">Frameworks for computational graphs and probabilistic programming</span></b>

#### Goals
* Learn stuff

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 10 ######################-->

### <b><span style="color:blue">[Oct 29]</span></b> Lecture 10
<b><span style="color:red">Bayesian model selection</span></b>

#### Goals
* Learn stuff

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 11 ######################-->

### <b><span style="color:blue">[Nov 05]</span></b> Lecture 11
<b><span style="color:red">Learning in a probabilistic context</span></b>

#### Goals
* Learn stuff

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 12 ######################-->

### <b><span style="color:blue">[Nov 12]</span></b> Lecture 12
<b><span style="color:red">Supervised learning in Scikit Learn</span></b>

#### Goals
* Learn stuff

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 13 ######################-->

### <b><span style="color:blue">[Nov 26]</span></b> Lecture 13
<b><span style="color:red">Cross validation</span></b>

#### Goals
* Learn stuff

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 14 ######################-->

### <b><span style="color:blue">[Dec 03]</span></b> Lecture 14
<b><span style="color:red">Neural networks</span></b>

#### Goals
* Learn stuff

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

<!--################### Lecture 15 ######################-->

### <b><span style="color:blue">[Dec 10]</span></b> Lecture 15
<b><span style="color:red">Deep learning</span></b>

#### Goals
* Learn stuff

#### Lecture notebook(s)
* [Intro.ipynb](DataAnalysisMachineLearningApplications/notebooks/Intro.ipynb)

#### Homework
* None

## Resources

### Required Reading

* [Google JavaScript Style Guide](http://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml)
* [JavaScript Garden](http://bonsaiden.github.com/JavaScript-Garden/)
* [Mozilla's Introduction to Object-Oriented Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Introduction_to_Object-Oriented_JavaScript)
* [What’s so great about JavaScript Promises?](http://blog.parse.com/learn/engineering/whats-so-great-about-javascript-promises/)

### Beginner Materials

This class assumes you are confident with this material, but in case you need a brush-up...

* Codecademy – [JavaScript](https://www.codecademy.com/learn/javascript) and [jQuery](https://www.codecademy.com/learn/jquery)
* [Eloquent JavaScript](http://eloquentjavascript.net/index.html) by Marijn Haverbeke, Chapters 1-5
* [Want to learn JavaScript in 2015?](https://medium.com/@_cmdv_/i-want-to-learn-javascript-in-2015-e96cd85ad225)
* [How jQuery Works](https://learn.jquery.com/about-jquery/how-jquery-works/)
* see also – [Other Lists](#other-lists)

### Recommended Reading

* [Functional JavaScript](http://shop.oreilly.com/product/0636920028857.do) by Michael Fogus
* [Front-end Job Interview Questions](https://github.com/h5bp/Front-end-Developer-Interview-Questions) by @darcyclarke (for testing yourself)
* [JavaScript Best Practices](http://www.thinkful.com/learn/javascript-best-practices-1/)
* [JavaScript Patterns](http://shichuan.github.io/javascript-patterns/) by @shichuan (thanks @iandrewfuchs)
* [JavaScript Patterns](http://www.amazon.com/JavaScript-Patterns-Stoyan-Stefanov/dp/0596806752) by Stoyan Stephanov
* [JavaScript Web Applications](http://www.amazon.com/JavaScript-Web-Applications-Alex-MacCaw/dp/144930351X/) by Alex MacCaw
* [JavaScript: The Good Parts](http://www.amazon.com/JavaScript-Good-Parts-Douglas-Crockford/dp/0596517742) by Douglas Crockford
* [Learning Advanced JavaScript slides](http://ejohn.org/apps/learn/) by John Resig
* [Static Web Apps](http://www.staticapps.org/)
* [Test-Driven JavaScript Development](http://www.amazon.com/Test-Driven-JavaScript-Development-Developers-Library/dp/0321683919) by Christian Johansen
* [The JavaScript Interpreter, Interpreted](http://www.slideshare.net/marthakelly/js-interpreter-interpreted) by Martha Girdler [(video)](https://www.youtube.com/watch?v=iSxNCYcPAFk)

#### Specific Topics

* [Classical Inheritance in JavaScript](http://www.crockford.com/javascript/inheritance.html) by Douglas Crockford
* [Partial Application in JavaScript](http://benalman.com/news/2012/09/partial-application-in-javascript/) by Ben Alman (thanks @michaelBenin)
* [HTML5 Rocks](http://www.html5rocks.com)
* [Learning JavaScript Design Patterns](http://addyosmani.com/resources/essentialjsdesignpatterns/book/) by Addy Osmani

#### Other Lists

* [JS: The Right Way](http://www.jstherightway.org/) (an overview of the JS landscape)
* [Code School](https://www.codeschool.com/paths/javascript)
* Thoughtbot's [Javascript Trail Map](https://upcase.com/javascript)
* [How To Learn JavaScript Properly](http://javascriptissexy.com/how-to-learn-javascript-properly/)
* [Superhero.js](http://superherojs.com)
* [Teach Yourself to Code](http://teachyourselftocode.com/javascript)

### Tools

* code validation: [JSLint](http://jslint.com) / [JSHint](http://jshint.com)
* debugging:
    * [Chrome Developer Tools](https://developer.chrome.com/devtools/index)
        * [Official debugging tutorial](https://developer.chrome.com/extensions/tut_debugging)
        * Tutorial: [JavaScript Diagnosis](http://www.macwright.org/2015/03/10/javascript-diagnosis.html)
    * [Firefox Developer Edition](https://www.mozilla.org/en-US/firefox/developer/)
* sharing code snippets: [gist.github.com](https://gist.github.com/)
* asking questions: [Stack Overflow](http://stackoverflow.com/)

#### GitHub

* Git and GitHub
    * [Official GitHub Help](https://help.github.com/)
    * [Recommended resources](http://hackerhours.org/resources.html#github)
* GitHub Pages
    * [Official site](https://pages.github.com/)
    * [Thinkful guide](http://www.thinkful.com/learn/a-guide-to-using-github-pages/)

#### HTML/CSS/JS Sandboxes

* [JS Bin](http://jsbin.com/) (recommended)
* [bl.ocks.org](http://bl.ocks.org/)
* [Cloud9](https://c9.io/)
* [CodePen](http://codepen.io/pen/)
* [JSFiddle](http://jsfiddle.net/)
* [Mozilla Thimble](https://thimble.mozilla.org)
* [Plunker](http://plnkr.co/)
* [rawgithub.com](http://rawgit.com/)

#### Frameworks

* Framework comparison: [TodoMVC](http://todomvc.com)
* [Testing](https://coderwall.com/p/ntbixw)

### Reference

* [Mozilla Developer Network](https://developer.mozilla.org/en/JavaScript) and [Learn JavaScript](https://developer.mozilla.org/en-US/learn/javascript)
* [w3schools](http://www.w3schools.com/jsref/default.asp)
* [JavaScript: The Definitive Guide](http://shop.oreilly.com/product/9780596000486.do) by David Flanagan
* [Simplified JavaScript Jargon](http://jargon.js.org/)

### More Examples

* [map/reduce](http://jsbin.com/ojapAsUR/2/edit?js) (in [Underscore](http://underscorejs.org/#map))

## Grading

* Class Participation – 30%
* Homework – 70%

## bottom

Material for a [University of Illinois](http://illinois.edu) course offered by the [Physics Department](https://physics.illinois.edu).

Content is maintained on [github](https://github.com/illinois-mla) and distributed under a [BSD3 license](https://opensource.org/licenses/BSD-3-Clause).

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause) [![nbviewer](https://img.shields.io/badge/view%20on-nbviewer-brightgreen.svg)](http://nbviewer.jupyter.org/github/dkirkby/MachineLearningStatistics/tree/master/notebooks/Contents.ipynb)
