def my_function(dirname, search):
    files = os.listdir(dirname)
    for file in files:
        path = dirname + '\\' + file
        if os.path.isdir(path):
            print(path)
            my_function(path, search)
        elif path.endswith('.py'):
            if seach in file.lower():
                print('FOUND: ' + path)

try:
    root_path = os.curdir
    search = input('Filename? ').lower()
    if os.path.isdir(root_path):
        my_function(root_path, search)
except OSError as err:
    print(err)
    print("Stopping, can't access files.")