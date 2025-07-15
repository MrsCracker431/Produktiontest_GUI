<<<<<<< HEAD
# Production Test GUI

Simple pass/fail test interface for production line operators.

## Quick Start

1. **Install Python** (3.8 or newer)

2. **Download project and install dependencies:**
   ```bash
   cd GUI Produktionstest
   pip install -r requirements.txt
   ```

3. **Run the GUI:**
   ```bash
   python src/main.py
   ```
   Or double-click `start_test_gui.pyw` on Windows

## How It Works

- **START TEST** - Begins hardware test sequence
- **Green Screen** = PASS ✓
- **Red Screen** = FAIL ✗ (shows what failed)
- Click button again to retry after failure



## Adding Your Own Tests

Replace the mock test in `tests/hardware_tests.py` with your actual hardware test:

```python
def test_production():
    # Your hardware test code here
    assert voltage == 3.3, "Voltage out of range"
```

## Configuration

Edit `pytest.ini` to change test behavior:
- Timeout settings
- Output verbosity
- Test discovery paths

## Troubleshooting

- **"Module not found"** → Run: `pip install -r requirements.txt`
- **Test won't stop** → Click STOP button or close window
- **Can't see test output** → Check console window where you started the GUI

## For Production Operators

1. Click the big **START TEST** button
2. Wait for test to complete
3. **Green = Good**, **Red = Bad**
=======
# Production Test GUI

Simple pass/fail test interface for production line operators.

## Quick Start

1. **Install Python** (3.8 or newer)

2. **Download project and install dependencies:**
   ```bash
   cd GUI Produktionstest
   pip install -r requirements.txt
   ```

3. **Run the GUI:**
   ```bash
   python src/main.py
   ```
   Or double-click `start_test_gui.pyw` on Windows

## How It Works

- **START TEST** - Begins hardware test sequence
- **Green Screen** = PASS ✓
- **Red Screen** = FAIL ✗ (shows what failed)
- Click button again to retry after failure



## Adding Your Own Tests

Replace the mock test in `tests/hardware_tests.py` with your actual hardware test:

```python
def test_production():
    # Your hardware test code here
    assert voltage == 3.3, "Voltage out of range"
```

## Configuration

Edit `pytest.ini` to change test behavior:
- Timeout settings
- Output verbosity
- Test discovery paths

## Troubleshooting

- **"Module not found"** → Run: `pip install -r requirements.txt`
- **Test won't stop** → Click STOP button or close window
- **Can't see test output** → Check console window where you started the GUI

## For Production Operators

1. Click the big **START TEST** button
2. Wait for test to complete
3. **Green = Good**, **Red = Bad**
>>>>>>> 7219fbe912656346efc7d1ff426f83e2809bddf7
4. If red, check which test failed and click button to retry