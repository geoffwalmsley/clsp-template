## Installation

```sh
git clone https://github.com/geoffwalmsley/clsp-template.git ~/your/proj/path
```

Switch into the directory where the cloned repo is. Create and activate virtual env:

```sh
python3 -m venv venv
source venv/bin/activate
```

Install the requirements:
```sh
pip install -r requirements.txt
```

Run the tests:
```
pytest tests/
```

## Basic Usage
- The idea is to have a more structured, semi-test-driven approach to chialisp
- Write chialisp code in files inside `src/clsp/`
- Test the chialisp inside the test suite, not in the driver
- Use `utils/sim.py` for testing the driver code
