from website import create_app

# call create app from folder website
app = create_app()

# run debug auto
if __name__ == '__main__':
    app.run(debug=True)

