from sync_app import app

def main():
    app.run(debug=False, host='0.0.0.0', port=1000)
    
    return


if __name__ == '__main__':
    main()