import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'online-cook=book'
app.config["MONGO_URI"] = 'mongodb://admin:admin1@ds119160.mlab.com:19160/online-cook-book'

mongo = PyMongo(app)

@app.route('/')
def homepage():
    return render_template("homepage.html", sections=mongo.db.sections.find())
@app.route('/getrecipes')
def getrecipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find(), sections=mongo.db.sections.find())

@app.route('/addrecipe')
def addrecipe():
    sections = []
    add_sections = []
    db_sections=mongo.db.sections.find()
    for section in db_sections:
        sections.append(section)
        add_sections.append(section)
    return render_template('addrecipe.html',
                           sections=sections,
                           add_sections=add_sections)

@app.route('/insertrecipe', methods=['POST'])
def insertrecipe():
    recipe = request.form.to_dict()
    recipe['allergens'] = 'allergens' in recipe
    print(recipe)
    mongo.db.recipes.insert_one(recipe)
    return redirect(url_for('getrecipes'))

@app.route('/editrecipe/<recipeid>')
def editrecipe(recipeid):
    sections = []
    add_sections = []
    therecipe = mongo.db.recipes.find_one({'_id': ObjectId(recipeid)})
    allsections = mongo.db.sections.find()
    for section in allsections:
        sections.append(section)
        add_sections.append(section)
    return render_template(
        'editrecipe.html', recipe=therecipe, sections=add_sections)


@app.route('/changerecipe/<recipeid>', methods=['POST'])
def changerecipe(recipeid):
    mongo.db.recipes.update(
        {'_id': ObjectId(recipeid)},
        {
            'recipename': request.form.get('recipename'),
            'sectionname': request.form.get('sectionname'),
            'recipeingredients': request.form.get('ingredients'),
            'imgurl': request.form.get('imgurl'),
            'cooking_time': request.form.get('cooking_time'),
        })
    return redirect(url_for('getrecipes'))


@app.route('/deleterecipe/<recipeid>', methods=['POST'])
def deleterecipe(recipeid):
    mongo.db.recipes.remove({'_id': ObjectId(recipeid)})
    return redirect(url_for('getrecipes'))


@app.route('/getsections')
def getsections():
    return render_template('sections.html',
                           sections=mongo.db.sections.find())


@app.route('/editsection/<sectionid>')
def editsection(sectionid):
    thesection = mongo.db.categories.find_one(
        {'_id': ObjectId(sectionid)})
    return render_template('editsection.html', section=thesection, sections=mongo.db.sections.find())


@app.route('/changesection/<sectionid>', methods=['POST'])
def changesection(sectionid):
    mongo.db.sections.update(
        {'_id': ObjectId(sectionid)},
        {'sectionname': request.form.get('sectionname')})
    return redirect(url_for('getsections'))


@app.route('/deletesection/<sectionid>', methods=['POST'])
def deletesection(sectionid):
    mongo.db.sections.remove({'_id': ObjectId(sectionid)})
    return redirect(url_for('getsections'))


@app.route('/insertsection', methods=['POST'])
def insertsection():
    sectionname_doc = {'sectionname': request.form.get('sectionname')}
    mongo.db.sections.insert_one(sectionname_doc)
    return redirect(url_for('getsections'))


@app.route('/addsection')
def addsection():
    return render_template('addsection.html', sections=mongo.db.sections.find())

@app.route('/search/<sectionname>')
def search(sectionname):
    return render_template("recipes.html", sections=mongo.db.sections.find(), recipes=mongo.db.recipes.find({"sectionname": sectionname}), sectionname=sectionname)

@app.route('/searchresults/<recipeingredients>', methods=['POST'])
def searchresults(recipeingredients):
    recipeingredients=request.form.to_dict()
    return render_template("results.html", ingredients=mongo.db.sections.find(), recipes=mongo.db.recipes.find({"recipeingredients": recipeingredients}),recipeingredients=recipeingredients)    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)