# Unit Converter Web App

A simple Flask-based web application to convert between different units of measurement.

## Features
- Convert Length units (millimeter, centimeter, meter, kilometer, inch, foot, yard, mile)
- Convert Weight units (milligram, gram, kilogram, ounce, pound)
- Convert Temperature units (Celsius, Fahrenheit, Kelvin)

## Project Structure
```
unit_converter/
├── app.py
├── templates/
│   ├── index.html
│   ├── length.html
│   ├── weight.html
│   └── temperature.html
```

## Installation and Running

1. Clone this repository or download the project folder.

2. Navigate to the project folder:
   ```bash
   cd unit_converter
   ```

3. (Optional but recommended) Create a virtual environment:
   ```bash
   python -m venv venv
   ```
   Activate it:
   - On Windows: `venv\Scripts\activate`
   - On Mac/Linux: `source venv/bin/activate`

4. Install Flask:
   ```bash
   pip install flask
   ```

5. Run the app:
   ```bash
   python app.py
   ```

6. Open your browser and go to:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Usage
- Visit the homepage and select the type of conversion (Length, Weight, Temperature).
- Enter a value, choose the source and target units, and press **Convert**.
- The converted result will be displayed on the same page.

## Requirements
- Python 3.x
- Flask

