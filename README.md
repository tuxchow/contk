# Conversational Toolkits

[![CodeFactor](https://www.codefactor.io/repository/github/thu-coai/contk/badge)](https://www.codefactor.io/repository/github/thu-coai/contk)
[![Coverage Status](https://coveralls.io/repos/github/thu-coai/contk/badge.svg?branch=master)](https://coveralls.io/github/thu-coai/contk?branch=master)
[![Build Status](https://travis-ci.com/thu-coai/contk.svg?branch=master)](https://travis-ci.com/thu-coai/contk)

## Environment

* **python 3**
* numpy >= 1.13
* nltk >= 3.2

## Document

Please refer to [document](https://thu-coai.github.io/contk_docs/)

## To Developer

### Contk Package

`./contk` is the package folder.

* All your code must followed a coding standard specified by **Pylint**. You can simply install Pylint via pip:

  ```
  pip install pylint
  ```
  In this project, you should follow the default pylint configuration that we provide and check `contk` after you update it:

  ```
  pylint contk
  ```

* Class and function docstring are always required.  

#### Some suggestions for docstring

You can have a look at docstring in other files. Or you may want to go to learn how docstring is written in other projects:

* [https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
* [http://www.sphinx-doc.org/en/1.5/ext/example_google.html](http://www.sphinx-doc.org/en/1.5/ext/example_google.html)
* [https://github.com/pytorch/pytorch](https://github.com/pytorch/pytorch)
* [https://pytorch.org/docs/stable/torch.html](https://pytorch.org/docs/stable/torch.html) (click '[source]' after functions, you can see the original docstrings)

Here are some references of docstring (it is a part of reStructuredText, like markdown).

* [http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html](http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)

### Models

You can implement your model in './models'.

* Before you run a model, you have to install `contk` by  run `pip install -e .` in project root directory.
* When you run a model, your CWD(current working directory) should be model's folder (eg: Using `python run.py` in `./model/seq2seq-pytorch`).
* Code style is not so strict in your model implementation.
* But you have to explain how to use your model.
* You should provide a pretrained model file for your implementation. (But don't commit it to git repo.)

## The Team

`Contk` is maintained and developed by THU-coai group from Tsinghua University.

This project is welcome for community contribution.

## License

MIT License
