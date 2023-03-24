from flask import render_template, request, abort, redirect, url_for, make_response
from dash_package.dashboard import app
from dash_package.functions import saveQuestion, getDatas, startPool,stopPool, findQuestion, optionselected, remove


@app.server.route('/dashApp')
def dashboard():
    return app.index()

@app.server.route('/treatment', methods =['POST'])
def treatment():
    p = saveQuestion(request.values.lists())
    return redirect(url_for('pools'))

@app.server.route('/pools_filter', methods =['GET'])
def poolFilter():
    listes = getDatas()
    startDate = request.args.get('start_date')
    endDate = request.args.get('end_date')
    
    if endDate == '' and startDate == '':
        return render_template('pool.html', listes = listes)
    else:
        results=[]
        for item in listes:   
            if endDate !='' and startDate !='':       
                if item[0]<=endDate:
                    if item[0]>=startDate:
                        results.append(item)

            if startDate !='' and endDate == '':
                if item[0]>=startDate:
                    results.append(item)

            if startDate =='' and endDate != '':
                if(item[0]<=endDate):
                    results.push(item)
        return render_template('pool.html', listes = results)

@app.server.route('/pools', methods =['GET'])
def pools():
    listes = getDatas()
    return render_template('pool.html', listes = listes)

@app.server.route('/')
def startPage():
    return render_template('index.html')

@app.server.route('/answer/<question_id>',  methods=['GET'])
def answer(question_id):
    ques = findQuestion(question_id)
    question = ques[2]
    type = ques[1]
    filtered  = ques[3].split('|')
    global possibilities
    possibilities = list(filter(lambda x: x != '', filtered ))
    return render_template('selection.html', id = question_id, question = question, type = type, possibilities = possibilities)

@app.server.route('/start/<question_id>', methods =['PUT'])
def start(question_id):
    b = startPool(question_id)
    if b == True:
        resp = make_response('True')
        resp.status_code = 201
    else:
        resp = make_response('False')
        resp.status_code = 501
    return resp

@app.server.route('/stop/<question_id>', methods =['PUT'])
def stop(question_id):
    b = stopPool(question_id)
    if b == True:
        resp = make_response('True')
        resp.status_code = 201
    else:
        resp = make_response('False')
        resp.status_code = 501
    return resp

@app.server.route('/voting', methods =['POST'])
def voting():
    length = len(request.values.lists())
    if  length >=2:
        id = request.values.lists()[0][1][0]
        for x in range(1, length):
            option = request.values.lists()[x][1][0]
            index = list.index(possibilities, option)
            index +=2
            change = optionselected(id, index)

        if change == True:    
            return render_template('thankpage.html')
        else:
            return render_template('poolstopped.html')
    else:
        return render_template('error.html')

@app.server.route('/remove_question/<question_id>', methods =['DELETE'])
def delete(question_id):
    remove(question_id)
    resp = make_response('True')
    resp.status_code = 201
    return resp