from flask import Flask, request, render_template, make_response
import json


app = Flask(__name__)

with open('data/school.json') as fp:
       data = json.load(fp)

@app.route("/")
def homepage():
    student_instance = []
    for i in data:
        if i["student_id"]:
            student_instance.append(i['name'])
            student_instance.append(i["student_id"])
            student_instance.append(i['term'])

    if len(student_instance) == 0:
        make_response(401)



    return make_response(render_template('./home.html', name= student_instance[0], student_id= student_instance[1], term = student_instance[2], name1= student_instance[3], student_id1 = student_instance[4], term1 = student_instance[5], name2= student_instance[6], student_id2 = student_instance[7], term2 = student_instance[8]), 200)



@app.route("/students", methods=["GET"])
def students():


    return render_template('./home.html', info= data)


@app.route("/student", methods=["POST"])
def add_student():
    data = request.json


@app.route("/student/<string:student_id>", methods=["GET"])
def get_student(student_id):
    student_instance = []
    for i in data:
        if i["student_id"] == student_id:
            student_instance.append(i['name'])
            student_instance.append(i["student_id"])
            student_instance.append(i['term'])
            break


    return render_template('./home.html', name= student_instance[0], student_id= student_instance[1], term = student_instance[2])     


@app.route("/student/<string:student_id>", methods=["PUT"])
def update_student(student_id):
    student_instance = []
    for i in data:
        if i["student_id"] == student_id:
            student_instance.append(i['name'])
            student_instance.append(i["student_id"])
            student_instance.append(i['term'])
            break
    return render_template('./home.html', name= student_instance[0], student_id= student_instance[1], term = student_instance[2])


@app.route("/help", methods=["DELETE"])
def delete_student(student_id):
    student_instance = []
    for i in data:
        if i["student_id"] == student_id:
            student_instance.append(i['name'])
            student_instance.append(i["student_id"])
            student_instance.append(i['term'])
            break
    return render_template('./home.html')





if __name__ == "__main__":
    app.run(debug=True)


#with open('data/school.json') as fp:
#        data = json.load(fp)

#    return data