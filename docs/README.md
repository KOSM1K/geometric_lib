[![Test](https://github.com/KOSM1K/geometric_lib/actions/workflows/test.yml/badge.svg?branch=new_features_465031)](https://github.com/KOSM1K/geometric_lib/actions/workflows/test.yml)

# Geometric Lib
> Geometric Lib is a lib, that provides functions for calculations of area and perimeter of geometric figures

## Resent changes
- added documentation inside code
  commit hash: `cb5983787a1d1288c0177b68de07bda44b6aef2d`

- bug fix in rectangle->perimeter
  added functions for triangle
  commit hash: `77c3bffb659fbb93014a05dfb305add6a922bff9`

- added functions for rectangle 
  commit hash: `dbf80d6af4b85d8b5af61ecb61c5f0128d7983cc` 

## Functionality
### Circle
- area - returns area of circle
  parameters:
  - radius - radius of circle

  run:
  ```
  In [3]: area(5)
  Out[3]: 78.53981633974483
  ```
- perimeter - returns perimeter of circle
  parameters:
  - radius - radius of circle
  
  run:
  ```
  In [5]: perimeter(5)
  Out[5]: 31.41592653589793
  ```
  
### Rectangle
- area - returns area of rectangle
  parameters:
  - a - size of first side
  - b - size of second side

  run:
  ```
  In [3]: area(2, 3)
  Out[3]: 6
  ```
- perimeter - returns perimeter of rectangle
  parameters:
  - a - size of first side
  - b - size of second side
  
  run:
  ```
  In [5]: perimeter(2, 3)
  Out[5]: 10
  ```

### Square
- area - returns area of square
  parameters:
  - a - sizeof side

  run:
  ```
  In [3]: area(5)
  Out[3]: 25
  ```
- perimeter - returns perimeter of square
  parameters:
  - a - size of side
  
  run:
  ```
  In [5]: perimeter(5)
  Out[5]: 20
  ```


### Triangle
- area - returns area of triangle
  parameters:
  - a - size of side
  - h - size of height on that side

  run:
  ```
  In [3]: area(2,3)
  Out[3]: 3.0
  ```
- perimeter - returns perimeter of triangle
  parameters:
  - a - size of first side
  - b - size of second side
  - c - size of third side
  
  run:
  ```
  In [5]: perimeter(1,2,3)
  Out[5]: 6
  ```


# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a