# AirBnB Clone [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/NamasakaLennox/AirBnB_clone/blob/master/LICENSE) [![Build Status](https://travis-ci.org/luischaparroc/AirBnB_clone.svg?branch=master)](https://github.com/NamasakaLennox/AirBnB_clone)

![HBnB Logo](./images/hbnblogo.png)

### Contents

- [Description](#Description)
- [Environment](#Environment)
- [Further Information](#Furtherinformation)
- [Requirements](#Requirements)
- [Repo Contents](#FileContents)
- [Installation](#Installation)
- [Usage](#Usage)
- [Built with](#Built-with)
- [Acknowledgements](#Acknowledgements)



## Description :page_facing_up:
This is the first of four phases of an attempt to make a copy of the AirBnB web app. To control the objects of the entire project in this initial phase, a simple console was built using the Cmd Python module, allowing the implementation of the methods create, show, update, all, and destroy to the existing classes and subclasses.

## Environment :computer:
The console was developed in Ubuntu 20.04LTS using python3 (version 3.8.5).

### Further information :bookmark_tabs:
For further information on python version, and documentation visit [python.org](https://www.python.org/).


## Requirements :memo:
- Knowledge in python3
- How to use a command line interpreter
- A computer with Ubuntu 20.04
- Python3 and pep8 style corrector.

## Repo Contents :clipboard:
This repository constains the following files:
|   **File**   |   **Description**   |
| -------------- | --------------------- |
|[AUTHORS](./AUTHORS) | Contains info about authors of the project |
|[base_model.py](./models/base_model.py) | Defines BaseModel class (parent class), and methods |
|[user.py](./models/user.py) | Defines subclass User |
|[amenity.py](./models/amenity.py) | Defines subclass Amenity |
|[city.py](./models/city.py)| Defines subclass City |
|[place.py](./models/place.py)| Defines subclass Place |
|[review.py](./models/review.py) | Defines subclass Review |
|[state.py](./models/state.py) | Defines subclass State |
|[file_storage.py](./models/engine/file_storage.py) | Creates new instance of class, serializes and deserializes data |
|[console.py](./console.py) | creates object, retrieves object from file, does operations on objects, updates attributes of object and destroys object |
|[test_base_model.py](./tests/test_models/test_base_model.py) | unittests for base_model |
|[test_user.py](./tests/test_models/test_user.py) | unittests for user |
|[test_amenity.py](./tests/test_models/test_amenity.py) | unittests for amenity |
|[test_city.py](./tests/test_models/test_city.py) | unittests for city |
|[test_place.py](./tests/test_models/test_place.py) | unittests for place |
|[test_review.py](./tests/test_models/test_review.py) | unittests for review |
|[test_state.py](./tests/test_models/test_state.py) | unittests for state |
|[test_file_storage.py](./tests/test_models/test_engine/test_file_storage.py) | unittests for file_storage |
|[test_console.py](./tests/test_console.py) | unittests for console |


## Installation :hammer_and_wrench:
Clone the repository and run the console.py
```
$ git clone https://github.com/codewithdani/AirBnB_clone
```

## Usage :wrench:

|   **Method**   |   **Description**   |
| -------------- | --------------------- |
|[create](./console.py) | Creates object of given class |
|[show](./console.py) | Prints the string representation of an instance based on the class name and id |
|[all](./console.py) | Prints all string representation of all instances based or not on the class name |
|[update](./console.py) | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) |
|[destroy](./console.py)| Deletes an instance based on the class name and id (save the change into the JSON file) |
|[count](./console.py)| Retrieve the number of instances of a class |
|[help](./console.py)| Prints information about specific command |
|[quit/ EOF](./console.py)| Exit the program |

###### Example No.1

```
(hbnb) create User
4bfe50ff-747c-4062-8c98-2da9405b84c1
(hbnb) show User 4bfe50ff-747c-4062-8c98-2da9405b84c1
[User] (4bfe50ff-747c-4062-8c98-2da9405b84c1) {'id': '4bfe50ff-747c-4062-8c98-2da9405b84c1', 'created_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 99815), 'updated_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 101018)}
(hbnb) all User
["[User] (597beedb-5d39-4546-a4d5-f3ddf2ae7d82) {'id': '597beedb-5d39-4546-a4d5-f3ddf2ae7d82', 'created_at': datetime.datetime(2023, 7, 16, 11, 10, 55, 757687), 'updated_at': datetime.datetime(2023, 7, 16, 11, 10, 55, 759466), 'first_name': 'John', 'age': '69'}", "[User] (4bfe50ff-747c-4062-8c98-2da9405b84c1) {'id': '4bfe50ff-747c-4062-8c98-2da9405b84c1', 'created_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 99815), 'updated_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 101018)}"]
(hbnb) update User update 4bfe50ff-747c-4062-8c98-2da9405b84c1 name Betty
** no instance found **
(hbnb) update User update 4bfe50ff-747c-4062-8c98-2da9405b84c1 name Betty
** no instance found **
(hbnb) update User 4bfe50ff-747c-4062-8c98-2da9405b84c1 name Betty
(hbnb) all User
["[User] (597beedb-5d39-4546-a4d5-f3ddf2ae7d82) {'id': '597beedb-5d39-4546-a4d5-f3ddf2ae7d82', 'created_at': datetime.datetime(2023, 7, 16, 11, 10, 55, 757687), 'updated_at': datetime.datetime(2023, 7, 16, 11, 10, 55, 759466), 'first_name': 'John', 'age': '69'}", "[User] (4bfe50ff-747c-4062-8c98-2da9405b84c1) {'id': '4bfe50ff-747c-4062-8c98-2da9405b84c1', 'created_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 99815), 'updated_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 101018), 'name': 'Betty'}"]
(hbnb) destroy User 597beedb-5d39-4546-a4d5-f3ddf2ae7d82
(hbnb) all
["[User] (4bfe50ff-747c-4062-8c98-2da9405b84c1) {'id': '4bfe50ff-747c-4062-8c98-2da9405b84c1', 'created_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 99815), 'updated_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 101018), 'name': 'Betty'}"]
(hbnb) show User 597beedb-5d39-4546-a4d5-f3ddf2ae7d82
** no instance found **
```

###### Example No.2

```
(hbnb)
(hbnb) User.create()
a7bb7ba5-711f-4490-a6df-972516441237
(hbnb) User.create
*** Unknown syntax: User.create
(hbnb) User.show()
** instance id missing **
(hbnb) User.update()
** instance id missing **
(hbnb) User.show(a7bb7ba5-711f-4490-a6df-972516441237)
[User] (a7bb7ba5-711f-4490-a6df-972516441237) {'id': 'a7bb7ba5-711f-4490-a6df-972516441237', 'created_at': datetime.datetime(2023, 7, 16, 16, 54, 57, 176780), 'updated_at': datetime.datetime(2023, 7, 16, 16, 54, 57, 177214)}
(hbnb) User.all()
["[User] (4bfe50ff-747c-4062-8c98-2da9405b84c1) {'id': '4bfe50ff-747c-4062-8c98-2da9405b84c1', 'created_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 99815), 'updated_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 101018), 'name': 'Betty'}", "[User] (a7bb7ba5-711f-4490-a6df-972516441237) {'id': 'a7bb7ba5-711f-4490-a6df-972516441237', 'created_at': datetime.datetime(2023, 7, 16, 16, 54, 57, 176780), 'updated_at': datetime.datetime(2023, 7, 16, 16, 54, 57, 177214)}"]
(hbnb) User.destroy(a7bb7ba5-711f-4490-a6df-972516441237)
(hbnb) User.all()
["[User] (4bfe50ff-747c-4062-8c98-2da9405b84c1) {'id': '4bfe50ff-747c-4062-8c98-2da9405b84c1', 'created_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 99815), 'updated_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 101018), 'name': 'Betty'}"]
(hbnb) quit
```


## Built with :gear:
python3 (3.8.5)

### Version :pushpin:
HBnB - version 5.5

### Acknowledgements :raised_hands:
To all the peers that contribuited with their knowledge

### Authors :fountain_pen:
* [Daniel Giday](https://github.com/codewithdani/)
* [Emmanuel Obinna](https://github.com/Emmaobi7)
