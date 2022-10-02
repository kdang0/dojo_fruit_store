from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = "MAKE IT MAKE SENSE" 

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    print(f'Charging {request.form["first_name"]} for {int(request.form["strawberry"]) + int(request.form["apple"]) + int(request.form["raspberry"])}')
    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    session["student_id"] = request.form["student_id"]
    session["apple"] = request.form["apple"]
    session["raspberry"] = request.form["raspberry"]
    session["strawberry"] = request.form["strawberry"]
    return redirect("/show")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")


@app.route('/show')
def show_form():
    print("Showing this form")
    print(request.form)
    return render_template("checkout.html", first_name = session["first_name"],
    last_name = session["last_name"], student_id = session["student_id"], apple =session["apple"], raspberry =session["raspberry"], strawberry=session["strawberry"])

if __name__=="__main__":   
    app.run(debug=True)    