# LamRand

LamRand is a Python library for generating truly random numbers using advanced mathematical algorithms. This library is designed to be used in various applications where random numbers are needed, such as simulations, games, and cryptographic applications.

## Purpose

The purpose of LamRand is to provide a reliable and truly random number generator that can be used across different platforms and applications.

## Authors

- **calpimm** - *Full* - [Your GitHub](https://github.com/calpimm)

## Installation


You can install LamRand using pip:

```bash
pip install LamRand
```

## Dependencies

LamRand requires the following packages:

	•	openpyxl
	•	scipy

These dependencies will be installed automatically when you install LamRand using pip.


## Usage

Here are some usage examples:

- Importing LamRand

```python
from lamrand import LamRand, LamRandSecure

randomizer = LamRand()
secure_randomizer = LamRandSecure()
```

- Generating a random integer

```python
print(randomizer.next())
```

- Generating a random float

```python
print(randomizer.next_float())
```

- Generating a random integer between two values

```python
print(randomizer.next_int(1, 10))
```

- Generating a random boolean

```python
print(randomizer.next_bool())
```

- Shuffling a list

```python
data = [1,2,3,4,5]
print(randomizer.shuffle(data))
```

- Generating a random string of a given length

```python
print(randomizer.next_string(10))
```
- Running Tests

```bash
python -m unittest discover
```

### Generating a Gaussian random number with Box-Muller transform

```python
print(randomizer.next_gaussian_box_muller())
```

## Generating a Poisson random number

```python
print(randomizer.next_poisson(3.5))
```

## Saving and loading state

```python
state = randomizer.save_state()
randomizer.load_state(state)
```
## Using the secure randomizer

```python
print(secure_randomizer.next_int(1, 10))
print(secure_randomizer.next_float())
print(secure_randomizer.next_bool())
print(secure_randomizer.next_string(10))
```

## Feedback and New Features

We welcome feedback and suggestions for new features in LamRand. If you have any ideas or encounter any issues while using the library, please feel free to reach out to us.

### Providing Feedback
To provide feedback, you can:
- Open an issue on our [GitHub repository](https://github.com/calpimm/LamRand/issues).
- Contact the author directly via email or through their GitHub profile.

When providing feedback, please include as much detail as possible, including steps to reproduce the issue or a clear description of the new feature you would like to see.

### Requesting New Features
If you have a specific feature in mind that you would like to see added to LamRand, please follow these steps:
1. Check the existing issues and pull requests on our [GitHub repository](https://github.com/calpimm/LamRand) to see if the feature has already been requested or is being worked on.
2. If the feature hasn't been requested yet, open a new issue and clearly describe the feature you would like to see added. Provide any relevant details or examples that can help us understand your request better.
3. Our team will review your feature request and provide feedback or discuss the feasibility of implementing it.

We appreciate your feedback and contributions to make LamRand even better!


## License

This project is licensed under the MIT License - see the LICENSE file for details.