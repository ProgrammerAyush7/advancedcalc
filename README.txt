# AdvancedCalc
An Advanced Calculator to Calculate Advanced Methods like Average, Trignometry, HCF, LCM easily

## Installation
advancedCalc requires an installation of python 3.6 or greater, as well as pip. Pip is typically bundled with python installations, and you can find options for how to install python at https://python.org.

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
import advancedcalc
calculator = advancedcalc.Calculator()

# returns 10
sum = calculator.add(5, 5)
print(sum)
```

#### Subtracting Numbers
```python
import advancedcalc
calculator = advancedcalc.Calculator()

# returns 5
answer = calculator.add(10, 5)
print(answer)
```

#### Using `auto_arrange` Parameter
The `auto_arrange` parameter is usually used to pretend to get negative answers (eg. -1, -6, etc.). 

1. Without `auto_arrange`
```python
import advancedcalc
calculator = advancedcalc.Calculator()

# returns -1
answer = calculator.subtract(4, 5)
print(answer)
```
2. With `auto_arrange`
```python
import advancedcalc
calculator = advancedcalc.Calculator()

# returns 1
answer = calculator.add(4, 5, auto_arrange = True)
print(answer)
```

#### Multiplying Numbers
Multiply 2 Numbers using this Function
```python
import advancedcalc
calculator = advancedcalc.Calculator()

# returns 25
product = calculator.add(5, 5)
print(product)
```

#### Dividing Numbers
Divide 2 Numbers using this Function

```python
import advancedcalc
calculator = advancedcalc.Calculator()

# returns 2
quotient = calculator.add(10, 5)
print(quotient)
```

#### Finding Remainders
Find the Remainder from the Division of 2 Numbers using this function

```python
import advancedcalc
calculator = advancedcalc.Calculator()

# returns 2
remainder = calculator.remainder(10, 4)
print(remainder)
```