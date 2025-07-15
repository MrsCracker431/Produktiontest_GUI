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

Replace the mock test in `tests/hardware_tests.py` with your actual hardware test or change the testpath and python_file to your test location in the `pytest.ini` file:

```python
def test_production():
    # Your hardware test code here
    assert voltage == 3.3, "Voltage out of range"
```
### Test structure
Be desciptive in the assertion message within the test. This is what shows up in if test fails.
Example:
#### ❌ BAD - Generic message
assert voltage == 3.3, "Voltage error"

#### ✅ GOOD - Descriptive message for production team
assert voltage == 3.3, f"Power supply voltage {voltage}V is out of range (expected 3.3V) - Check J1 connector"



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
4. If red, check which test failed and click button to retry