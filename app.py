from flask import Flask, render_template, request
import pickle
import os
app = Flask(__name__)
model=pickle.load(open('model','rb'))
clusters=pickle.load(open('clusters','rb'))
users=pickle.load(open('users','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/text', methods=['POST'])
def index(): 
    l=request.form.getlist('mycheckbox')

    g=l[0]
    l1=[]
    for i in l[1:]:
        l1.append(int(i))

    pred=model.predict([l1])
    pred=clusters[pred[0]]
    f=users[pred]
    pred=[i for i in f if i[-2]!=g]
    output=[]
    for i in pred:
        output.append(i[-1])
    # output=' '.join(output)

        # return 'Done'
    # return render_template('Index.html', prediction_text='The recommended users for you are: {}'.format(output))
    final="The recommended users for you are:\n"
    # final=final+os.linesep
    for i in output:
        final=final+i+"\n"

    return final


if __name__ == "__main__":
    app.run(debug=True)