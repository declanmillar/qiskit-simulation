# Qiskit Simulation

![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-informational)
[![Python](https://img.shields.io/badge/Python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-informational)](https://www.python.org/)
[![Qiskit](https://img.shields.io/badge/Qiskit-%E2%89%A5%201.0.0-6133BD)](https://github.com/Qiskit/qiskit)

<!-- [![Tests](https://github.com/qiskit-community/qiskit-simulation/actions/workflows/test.yml/badge.svg)](https://github.com/qiskit-community/qiskit-simulation/actions/workflows/test.yml) -->
<!-- [![Coverage](https://coveralls.io/repos/github/qiskit-community/qiskit-simulation/badge.svg?branch=main)](https://coveralls.io/github/qiskit-community/qiskit-simulation?branch=main) -->
<!-- [![Release](https://img.shields.io/github/release/qiskit-community/qiskit-simulation.svg?include_prereleases&label=Release)](https://github.com/qiskit-community/qiskit-simulation/releases) -->
<!-- [![DOI](https://img.shields.io/badge/DOI-zz.nnnn/zenodo.ddddddd-informational)](https://zenodo.org/) -->
<!-- [![License](https://img.shields.io/github/license/qiskit-community/qiskit-simulation?label=License)](LICENSE.txt) -->

> [!WARNING]  
> **Qiskit Simulations is a recent partial successor of Qiskit Algorithms**.  
> Like any other Apache 2 licensed code, you are free to use it or/and extend it, but please be
> aware that it is under your own risk.

## Table of contents

1. [About this Project](#about-this-project)
2. [Installation](#installation)
3. [Documentation](#documentation)
4. [Deprecation Policy](#deprecation-policy)
5. [Contributing](#contributing)
6. [Authors and Citation](#authors-and-citation)
7. [Acknowledgements](#acknowledgements)
8. [License](#license)

## About this Project

A library of quantum simulation algorithms for Qiskit.

## Installation

We encourage installing Qiskit Simulation via the pip tool (a python package manager) **when there
is a PyPI release!**

```bash
pip install qiskit-simulation
```

**pip** will handle all dependencies automatically and you will always install the latest (and
well-tested) version.

If you want to work on the very latest work-in-progress versions, either to try features ahead of
their official release or if you want to contribute to Qiskit Simulation, then you can install from
source.

This package can be installed from source, alongside all required and optional dependencies, via
`pip`:

```sh
pip install -e ".[dev,test,lint,docs,notebook]"
```

For more detailed information and alternative installation options see the [installation
guide](INSTALL.md).

## Documentation

- Complete documentation can be found in the code docstrings.
- Check out the [file map](FILEMAP.md) for more information on the structure of this repository.

## Deprecation Policy

This software is meant to evolve rapidly and, as such, does not follow [Qiskit's deprecation
policy](https://github.com/Qiskit/qiskit/blob/main/DEPRECATION.md).

## Contributing

- The easiest way to contribute is by [giving feedback](CONTRIBUTING.md#giving-feedback).
- If you wish to contribute to the development of the software, you must read and follow our
  [contribution guidelines](CONTRIBUTING.md).
- By participating, you are expected to uphold our [code of conduct](CODE_OF_CONDUCT.md).

## Authors and Citation

Qiskit Simulation was inspired, authored and brought about by the collective work of a team of
researchers. Qiskit Simulation continues to grow with the help and work of [many
people](https://github.com/qiskit-community/qiskit-simulation/graphs/contributors), who contribute
to the project at different levels.

If you use Qiskit Simulations, please cite as per the included [BibTeX file](CITATION.bib).

If you use Qiskit, please cite as per the provided
[BibTeX file](https://github.com/Qiskit/qiskit/blob/main/CITATION.bib).

## Acknowledgements

Qiskit Simulation is a fork of Qiskit Algorithms intended to maintain the quantum simulation
methods.

## License

[Apache License 2.0](LICENSE.txt)
