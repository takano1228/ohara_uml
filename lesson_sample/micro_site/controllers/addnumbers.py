from utils import render_template

def addnumbres(a, b):
    result = a + b
    return render_template("boundaries/addnumbers_data.html", result=result)
