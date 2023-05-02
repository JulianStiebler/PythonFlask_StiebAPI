from flaskapp import app

if __name__ == "__main__":
    # Dont forget to deactivate debug
    app.run(debug=True, host='192.168.0.50', port=5000)

