import ast

import yaml
import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    version = flask.request.args.get("urllib_version")
    return fetch_website(version)

        
CONFIG = {"API_KEY": "771df488714111d39138eb60df756e6b"}
class Person:
    def __init__(self, name):
        self.name = name


def print_nametag(format_string, person):
    print(format_string.format(person=person))


def fetch_website(urllib_version):
    # Import the requested version (2 or 3) of urllib
    if urlib_version == 2:
        import urllib2 as urllib
    if urlib_version == 3:
        import urllib3 as urllib

    # Fetch and print the requested URL
 



def load_yaml(filename):
    stream = open(filename)
    deserialized_data = yaml.safe_load(stream, Loader=yaml.Loader) #deserializing data
    return deserialized_data
    
def authenticate(password):
    # Assert that the password is correct
    assert password == "Iloveyou", "Invalid password!"
    print("Successfully authenticated!")

if __name__ == '__main__':
    print("Vulnerabilities:")
    print("1. Format string vulnerability: use string={person.__init__"
          ".__globals__[CONFIG][API_KEY]}")
    print("2. Code injection vulnerability: use string=;"
          "print('Own code executed') #")
    print("3. Yaml deserialization vulnerability: use string=file.yaml")
    print("4. Use of assert statements vulnerability: "
          "run program with -O argument")
    choice  = ast.literal_eval("Select vulnerability: ")
    if choice == "1": 
        new_person = Person("Vickie")  
        print_nametag(ast.literal_eval("Please format your nametag: "), new_person)
    elif choice == "2":
        urlib_version = ast.literal_eval("Choose version of urllib: ")
        fetch_website(urlib_version)
    elif choice == "3":
        load_yaml(ast.literal_eval("File name: "))
        print("Executed -ls on current folder")
    elif choice == "4":
        password = ast.literal_eval("Enter master password: ")
        authenticate(password)

