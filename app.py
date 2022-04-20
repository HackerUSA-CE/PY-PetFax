from petfax import create_app
app = create_app()

# pets index route
@app.route('/pets')
def pets(): 
    return 'These are our pets available for adoption!'
