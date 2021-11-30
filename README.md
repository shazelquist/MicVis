# MicVis
A small python application for visualizing microphone input

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)




## Why does this project exist?
  - The voice actor Kyle McCarley asked for something like this and I couldn't find anything suitable.
  Source: [tweet-1](https://twitter.com/KyleMcCarley/status/1452832666357698561?s=20), [tweet-2](https://twitter.com/KyleMcCarley/status/1452834856639950848?s=20)
  
  
## Goals:
  - Simple & customizable visualization for microphones
  - Frozen executables for non-coding folk
  - Integrate with OBS scripting
  
## How to contribute:

  1) Check the listed [issues](https://github.com/shazelquist/MicVis/issues)
  2) Set up a github account, fork the project and clone your version of the project. Create a branch with a descriptive name for the issue you've chosen.
  3) Install a package manager on your device, recomended [miniconda](https://docs.conda.io/en/latest/miniconda.html)
  4) Set up your package manager and install the project dependancies

    conda create -c conda-forge -n MV_dev python=3.6
    conda activate MV_dev
    conda install PyAudio
    pip install -r requirements.txt

  5) Code up your [PEP-8](https://www.python.org/dev/peps/pep-0008/) complient solution, aditional linting with `black youreditedfile.py` and push your solution to your fork.
  6) Open a pull request.
