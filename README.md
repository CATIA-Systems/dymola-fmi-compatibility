<img src="resources/3DS.svg" width="400"/>

# Dymola FMI Compatibility Information

This repository provides example FMUs exported from [Dymola](https://www.3ds.com/products/catia/dymola).

## Example FMUs

Format: `<Dymola_version>/<model_name>_<fmi_version>_<solver>.fmu`

Binaries: x86_64 binaries for Linux and Windows

### Models

- `CoupledClutches`: a simple dynamic model based on `Modelica.Mechanics.Rotational.Examples.CoupledClutches` with inputs and outputs

### Solvers

| Solver                |         CS         |         ME         |       Source       |
|-----------------------|:------------------:|:------------------:|:------------------:|
| Dassl                 | :heavy_check_mark: |                    |                    |
| Ida                   | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Cvode                 | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Inline Explicit Euler | :heavy_check_mark: |                    | :heavy_check_mark: |

## License

Copyright 2024 Dassault Systemes.
All rights reserved.
The models and accompanying materials may only be used for testing and validation of FMI implementations.
