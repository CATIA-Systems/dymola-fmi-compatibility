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

## FMU Import

With Dymola 2025x.

### Altair Activate 2020

#### FMI 2.0

| Model              |         CS         |         ME         |
|--------------------|:------------------:|:------------------:|
| ActivateRC         | :white_check_mark: | :white_check_mark: |
| Arenstorf          | :white_check_mark: | :white_check_mark: |
| Boocwen            |        :x:         | :white_check_mark: |
| CVloop             |        :x:         | :white_check_mark: |
| DiscreteController |        :x:         | :white_check_mark: |
| Pendulum           | :white_check_mark: | :white_check_mark: |

#### FMI 3.0

| Model                        |         CS         |         ME         |
|------------------------------|:------------------:|:------------------:|
| periodic_clock               |        :x:         | :white_check_mark: |
| sinewave_array               | :white_check_mark: | :white_check_mark: |
| triggered_and_periodic_clock |        :x:         | :white_check_mark: |

### FMI Toolbox 2.15

#### FMI 2.0

| Model             |         CS         |         ME         |
|-------------------|:------------------:|:------------------:|
| Continuous        | :white_check_mark: | :white_check_mark: |
| Discontinuities   | :white_check_mark: | :white_check_mark: |
| EmbeddedCode      | :white_check_mark: | :white_check_mark: |
| IntegrateSignal   | :white_check_mark: | :white_check_mark: |
| Signal_Attributes | :white_check_mark: | :white_check_mark: |

#### FMI 3.0

| Model             |         CS         |
|-------------------|:------------------:|
| Continuous        | :white_check_mark: |
| Discontinuities   | :white_check_mark: |
| EmbeddedCode      | :white_check_mark: |
| IntegrateSignal   | :white_check_mark: |
| Signal_Attributes | :white_check_mark: |

### MapleSim 2024

#### FMI 2.0

| Model                 |         CS         |         ME         |
|-----------------------|:------------------:|:------------------:|
| ControlledTemperature | :white_check_mark: | :white_check_mark: |
| CoupledClutches       | :white_check_mark: | :white_check_mark: |
| Rectifier             | :white_check_mark: | :white_check_mark: |

#### FMI 3.0

| Model                 |         CS         |         ME         |
|-----------------------|:------------------:|:------------------:|
| ControlledTemperature |        :x:         |        :x:         |
| CoupledClutches       |        :x:         |        :x:         |
| SlidingCrank          | :white_check_mark: | :white_check_mark: |

### Reference FMUs 0.0.36

#### FMI 1.0

| Model        |         CS         |         ME         |
|--------------|:------------------:|:------------------:|
| BouncingBall | :white_check_mark: | :white_check_mark: |
| Dahlquist    | :white_check_mark: | :white_check_mark: |
| Resource     | :white_check_mark: |                    |
| Stair        | :white_check_mark: | :white_check_mark: |
| VanDerPol    | :white_check_mark: | :white_check_mark: |

#### FMI 2.0

| Model        |         CS         |         ME         |
|--------------|:------------------:|:------------------:|
| BouncingBall | :white_check_mark: | :white_check_mark: |
| Dahlquist    | :white_check_mark: | :white_check_mark: |
| Resource     | :white_check_mark: | :white_check_mark: |
| Stair        | :white_check_mark: | :white_check_mark: |
| VanDerPol    | :white_check_mark: | :white_check_mark: |

#### FMI 3.0

| Model        |         CS         |         ME         |
|--------------|:------------------:|:------------------:|
| BouncingBall | :white_check_mark: |        :x:         |
| Dahlquist    | :white_check_mark: | :white_check_mark: |
| Resource     | :white_check_mark: | :white_check_mark: |
| Stair        | :white_check_mark: | :white_check_mark: |
| StateSpace   | :white_check_mark: | :white_check_mark: |
| VanDerPol    | :white_check_mark: | :white_check_mark: |

### MWorks Sysplorer 2024a

#### FMI 2.0

| Model           |         CS         |         ME         |
|-----------------|:------------------:|:------------------:|
| BouncingBall    | :white_check_mark: | :white_check_mark: |
| CoupledClutches | :white_check_mark: | :white_check_mark: |
| DFFREG          | :white_check_mark: | :white_check_mark: |


#### FMI 3.0

| Model           |         CS         |         ME         |
|-----------------|:------------------:|:------------------:|
| BouncingBall    | :white_check_mark: |        :x:         |
| CoupledClutches | :white_check_mark: |        :x:         |
| DFFREG          | :white_check_mark: | :white_check_mark: |

## License

Copyright 2024 Dassault Systemes.
All rights reserved.
The models and accompanying materials may only be used for testing and validation of FMI implementations.
