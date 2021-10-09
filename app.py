#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def abc():
    return render_template('f:h1.html')
@app.route('/info',methods=['GET','POST'])
def xyz():
    if(request.method=='POST'):
        Num1=int(request.form['a'])
        Num2=int(request.form['b'])
        total=Num1+Num2
        print(total)
        return render_template('h1.html',answer=total)
if __name__=='__main__':
    app.run()


# In[ ]:



