from flaskapp import app

if __name__ == "__main__":
    # Debug in dev-environment only!
    # app.run(debug=True, host='192.168.0.50', port=5000)
    
    app.run(debug=False, host='192.168.0.50', port=5000)

