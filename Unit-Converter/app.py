from flask import Flask, render_template, request

app = Flask(__name__)

#------------------Length------------------------
length_units = {
    "millimeter": 0.001,
    "centimeter": 0.01,
    "meter":1,
    "kilometer": 1000,
    "inch": 0.0254,
    "foot":0.3048,
    "yard":0.9144,
    "mile": 1609.34,
}

#-------------------Weight------------------------
weight_units = {
    "milligram": 0.001,
    "gram": 1,
    "kilogram": 1000,
    "ounce": 28.3495,
    "pound": 453.592,
}

# ---------------- TEMPERATURE ----------------
def convert_temperature(value, from_unit, to_unit):
    # Convert from any unit to Celsius first
    if from_unit == "Celsius":
        celsius = value
    elif from_unit == "Fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    else:
        return None
    
    # Convert from Celsius to target unit
    if to_unit == "Celsius":
        return celsius
    elif to_unit == "Fahrenheit":
        return (celsius * 9/5) + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15
    else:
        return None

# --------------------Routes---------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/length",methods=["GET","POST"])
def length():
    result = None
    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]

        meters = value * length_units[from_unit]     
        result = meters / length_units[to_unit]       
    return render_template("length.html", units=length_units.keys(), result=result)

@app.route("/weight", methods=["GET", "POST"])
def weight():
    result = None
    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]

        grams = value * weight_units[from_unit]      
        result = grams / weight_units[to_unit]       
    return render_template("weight.html", units=weight_units.keys(), result=result)

@app.route("/temperature", methods=["GET", "POST"])
def temperature():
    result = None
    if request.method == "POST":
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]

        result = convert_temperature(value, from_unit, to_unit)
    return render_template("temperature.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)