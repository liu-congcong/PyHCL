# PyHCL

Generate colors from the HCL color space.

## Installation

```shell
pip3 install https://github.com/liu-congcong/PyHCL/releases/download/v1.0.0/pyhcl-1.0.0-py3-none-any.whl
```

## Usage

```python3
from pyhcl.hcl import HCL
hcl = HCL()
for color in hcl.main(colors = 3):
    print(color)
```

\#F8766D #00BA38 #619CFF

```shell
pyhcl 3
```

\#F8766D #00BA38 #619CFF

```shell
pyhcl -t dec 3
```

(248, 118, 109) (0, 186, 56) (97, 156, 255)
