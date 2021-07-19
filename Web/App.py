from flask import flask, render_template, request
from flask_bootstrap import bootstrap
from Logic.Person import Person
from Logic.Package import Package
from typing import List


App= flask(__name__)
Bootstrap= bootstrap(App)
package_list= list()


@app.route("/package")
def package():
    return render_template('package.html')


@app.route('/Send_Package',methods=['POST'])
def  Send_Package():
    name_sender= request.form["name_sender"]
    last_name_sender= request.form['last_name_sender']
    address_sender= request.form['address_sender']
    sender= Person(name= name_sender, last_name= last_name_sender, address= address_sender)

    name_receiver= request.form["name_receiver"]
    last_name_receiver= request.form['last_name_receiver']
    address_receiver= request.form['address_receiver']
    receiver = Person(name=name_receiver, last_name=last_name_receiver, address= address_receiver)

    weight= float(request.form["weight"])
    description= request.form["description"]

    p= package(sender= sender, receiver= receiver, weight=weight, description=description)

    return render_template('Send_Package.html',value= p.__str__())

if __name__=='__main__':
    App.run()




