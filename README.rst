========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor|
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/ML-Utils/badge/?style=flat
    :target: https://readthedocs.org/projects/ML-Utils
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/awaemmanuel/ML-Utils.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/awaemmanuel/ML-Utils

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/awaemmanuel/ML-Utils?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/awaemmanuel/ML-Utils

.. |version| image:: https://img.shields.io/pypi/v/ml-utils.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/ml-utils

.. |wheel| image:: https://img.shields.io/pypi/wheel/ml-utils.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/ml-utils

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/ml-utils.svg
    :alt: Supported versions
    :target: https://pypi.org/project/ml-utils

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/ml-utils.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/ml-utils

.. |commits-since| image:: https://img.shields.io/github/commits-since/awaemmanuel/ML-Utils/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/awaemmanuel/ML-Utils/compare/v0.0.0...master



.. end-badges

A collection of ML and AI utils

* Free software: MIT license

Installation
============

::

    pip install ml-utils

You can also install the in-development version with::

    pip install https://github.com/awaemmanuel/ML-Utils/archive/master.zip


Documentation
=============


https://ML-Utils.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
