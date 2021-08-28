# AdvancedCalc
An Advanced Calculator to Calculate Advanced Methods like Average, Trignometry, HCF, LCM easily

## Installation
AdvancedCalc requires an installation of python 3.6 or greater, as well as pip. Pip is typically bundled with python installations, and you can find options for how to install python at https://python.org.

To Install from pypi with pip:
```bash
pip install advancedcalc
```
Sometime, the pypi release becomes slightly outdated. To install from the source with pip:
```bash
pip install git+https://github.com/programmerayush7/advancedcalc/
```

## Quick Start

#### Adding Numbers
```python
import AdvancedCalc
calculator = AdvancedCalc.Calculator

# returns 10
sum = calculator.add(5, 5)
print(sum)
```

#### Subtracting Numbers
```python
import AdvancedCalc
calculator = AdvancedCalc.Calculator

# returns 5
answer = calculator.add(10, 5)
print(answer)
```

#### Using `auto_arrange` Parameter
The `auto_arrange` parameter is usually used to pretend to get negative answers (eg. -1, -6, etc.). 

- Without `auto_arrange`
```python
import AdvancedCalc
calculator = AdvancedCalc.Calculator

# returns -1
answer = calculator.subtract(4, 5)
print(answer)
```
- With `auto_arrange`
```python
import AdvancedCalc
calculator = AdvancedCalc.Calculator

# returns 1
answer = calculator.add(4, 5, auto_arrange = True)
print(answer)
```

#### Multiplying Numbers
Multiply 2 Numbers using this Function
```python
import AdvancedCalc
calculator = AdvancedCalc.Calculator

# returns 25
product = calculator.add(5, 5)
print(product)
```

#### Dividing Numbers
Divide 2 Numbers using this Function

```python
import AdvancedCalc
calculator = AdvancedCalc.Calculator

# returns 2
quotient = calculator.add(10, 5)
print(quotient)
```

#### Finding Remainders
Find the Remainder from the Division of 2 Numbers using this function

```python
import AdvancedCalc
calculator = AdvancedCalc.Calculator

# returns 2
remainder = calculator.remainder(10, 4)
print(remainder)
```

## Advanced Functions

#### Average Of Numbers
Find the Average of Numbers in a List

```python
from AdvancedCalc import Advanced

numbers = [1, 2, 3, 4, 5]

# Returns 3
average = Advanced.average(numbers)

print(average)
```

#### Cube
Find the Cube of a Number using this function
```python
from AdvancedCalc import Advanced

# returns 8
cube = Advanced.cube(2)

print(cube)
```

#### Percentage
lets try finding 10 percent of 200
- Note: This Function returns a float, so if you want a number, you can convert it into an int.

```python
from AdvancedCalc import Advanced

# returns 20.0
percent = Advanced.percent(10, 200)

print(percent)
```

#### Factors
Find all Factors of a Specific Numbers using this function

```python
from AdvancedCalc import Advanced

# returns a list of factors
factors = Advanced.factors(10)

print(factors)
```

#### HFC
Find the Highest Common Factor of 2 Numbers

```python
from AdvancedCalc import Advanced

# returns 10
hcf = Advanced.hfc(10, 20)

print(hfc)
```

#### LCM
Find the LCM of 2 Numbers using this Function.

```python
from AdvancedCalc import Advanced

# returns 11
lcm = Advanced.lcm(5, 6)

print(lcm)
```

# Changelog

#### 0.0.3
- Added Advanced Functions
- Modified Simple Functions
- Modified README.md
- Fixed Installing with PIP Error
