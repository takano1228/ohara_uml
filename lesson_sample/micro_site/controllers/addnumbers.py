from utils import render_template

def addnumbres(a: int, b: int):
    result = a + b
    return render_template("boundaries/addmumbers_data.html", result=result)