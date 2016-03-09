from flask import Flask, render_template, request, redirect
from flask_restful import Resource, Api
#This is a init commit from yutong
app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run()
