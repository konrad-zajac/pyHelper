def begApp(x):
    for f in listdir(os.path.dirname(os.path.abspath(__file__))):
        if not (f == 'pyHelper.py'):
            os.rename(f, append(f))
