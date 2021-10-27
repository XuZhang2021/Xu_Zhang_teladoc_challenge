# Xu_Zhang_teladoc_challenge
For teladoc coding challenge 

## Installation

This .py only require one package needs to be installed. Other packages are default python packages.

```bash
python -m pip install selenium
```

## Usage

```python
Two scripts are loaded here. One is for UI auto fill all the metadata for uploading a record on the website, name UITest_AddUser.py. Another one is for delete a delete a record from the website automatically, name UITest_DeleteUser.py.

1. UITest_AddUser.py
This script is able to fill out first name, last name, username, Customer, Role, email address and phone number in add user mini app. After the key in process is complete, it will automatically go back the UI and self test if all the metadata has been loaded into the system correctly. The output can specify which ones are loaded on the UI correctly and which ones are not.

Here's a output from the script:
Please find the difference between UI and the expected output.
Metadata Name       |Website value       |Expected value
Company                                   Company BBB

As we can see that company value was not loaded into the system even though I have selected a value during the upload process, which is a bug from my point of view.

2. UITest_DeleteUser.py
Running this script can delete Mark Novak from the UI. After delete it, it will run another argument to verify if Novak has been removed from the list. It will print 'Target deleted' on the console if the record has been removed and will return 'Target not deleted' if not.
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
