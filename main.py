from distutils.log import debug
from website import init_app

application = init_app()

if __name__ == '__main__': 
    application.run(debug=True)