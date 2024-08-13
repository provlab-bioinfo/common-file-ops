# common-file-ops
 [![Lifecycle: WIP](https://img.shields.io/badge/lifecycle-WIP-yellow.svg)](https://lifecycle.r-lib.org/articles/stages.html#experimental) [![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/provlab-bioinfo/sequencing-run-ops/issues) [![License: GPL3](https://img.shields.io/badge/license-GPL3-lightgrey.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html) [![minimal Python version: 3.10](https://img.shields.io/badge/Python-3.10-6666ff.svg)](https://www.python.org/) [![Package Version = 0.0.1](https://img.shields.io/badge/Package%20version-0.0.1-orange.svg?style=flat-square)](https://github.com/provlab-bioinfo/sequencing-run-ops/blob/main/NEWS) [![Last-changedate](https://img.shields.io/badge/last%20change-2024--07--12-yellowgreen.svg)](https://github.com/provlab-bioinfo/sequencing-run-ops/blob/main/NEWS)

## Introduction

Python package for sequencer-agnostic file retrieval and manipulation

## Table of Contents

- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Installation](#installation)

## Dependencies

See [environments.yml](environments.yml) for package dependancies.

## Installation

### Remote

Install with pip:

```
$ pip install git+https://github.com/provlab-bioinfo/common-file-ops
```

### Local

[Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) is required to build an environment with required workflow dependencies:

```bash
conda env create -f ./environments/environment.yml
conda activate common-file-ops
```
### Access in python:
```python
>>> import common_file_ops as cfo
```
