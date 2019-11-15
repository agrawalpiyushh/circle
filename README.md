circle
==============================
[//]: # (Badges)
[![Travis Build Status](https://travis-ci.org/bcalden/circle.svg?branch=master)](https://travis-ci.org/bcalden/circle)
[![codecov](https://codecov.io/gh/bcalden/circle/branch/master/graph/badge.svg)](https://codecov.io/gh/bcalden/circle/branch/master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6643c203caaf492cb137e69c7d93826d)](https://www.codacy.com/manual/bcalden/circle?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=bcalden/circle&amp;utm_campaign=Badge_Grade)

A demo project for APS Hack Day 2019

### Intro
GitHub is an excellent resource that provides hosting and version control for your software project. The most successful projects are generally the ones that leverge the most of GitHubs features. This includes not only the built-in features of versioning, commits, branching, etc., but also the add-ons. Continuous integration tools allow for checks to be run on every commit ensuring your package doesn't break when you update your codebase. Coverage checks ensure that the majority of your codebase (its hard to get 100%) is being tested against control data in some fashion. Automated code reviews scan your code for unused code (it happens), security issues, potential bugs, etc., and assigns a letter grade. B or better is generally a sign of well maintained and developed code. 

Very good resources for all of these fetures and many more are available at [MolSSI Best Practices](https://github.com/MolSSI-Education/python-package-best-practices). 

### CookieCutter
Use [CookieCutter](https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter) to create the basic directory structure and template files for your project. This includes Travis-CI & codecov.io integration.

With CookieCutter installed, run `cookiecutter gh:molssi/cookiecutter-cms` to create your template. Enter the project name, the repository (repo) name, the first module filename, your or your group name, email, and a basic description. You will be prompted to select a license. Many astro python projects use the BSD-3-Clause license. If you don't know the dependancy management tools your using, conda-forge is fine. If you don't need windows continuous integration, indicate as such. 

### Create your Repo
Go to GitHub and create your repository (after creating an account). You will upload the cookiecutter files to this repo so don't worry about creating a description or readme.md. Once you get the repo url, go to your local repository directory in the terminal and type `git remote add origin https://{yourrepourl}`. You can then commit everything by typing `git commit .`, entering a commit message, and quiting `vi` (type `i` to input text, when done, type `Esc` followed by `:wq` then press `Enter`).

Once committed, you can push these files to your repo by typing `git push -u origin master`.  

### Continuous Integration
Update the file, `.travis.yml` in the root directory to the appropriate build test systems desired. Create an account at [Travis-CI](http://travis-ci.org). Connect to your GitHub account and allow access in your GitHub settings (GitHub.com->Settings-Applications). I recommend only allowing access to specified repos. 

### Code Coverage
Create an account at [Codecov.io](http://www.codecov.io) with your GitHub account to allow for automated code coverage checking. This checks how much of your code is tested. 

### Codacy
Create an account at [Codacy.com](http://www.codacy.com) and connect it to your GitHub Repo. Codacy checks your code against best practicies for style, security, and usage among other things. As your code gets more complex, you can begin to maintain code that never gets called or is potentially insecure. 

### Integrated Development Environments
VS Code
PyCharm
SublimeText
vim
Never emacs

### Copyright

Copyright (c) 2019, Brian Alden


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.1.
