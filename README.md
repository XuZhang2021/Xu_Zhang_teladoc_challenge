# Xu_Zhang_teladoc_challenge
For teladoc coding challenge 

## Installation

This .py requires only one extra package to be installed manually. Other packages are default python packages. I just uploaded chromedriver.exe(ChromeDriver 95.0.4638.17) into my repository via second push.
Please download everything from the latest branch name Chromedriverupload. If the chromedriver.exe doesn't fit your local chrome version, please download a chrome driver that works for you from here https://chromedriver.chromium.org/downloads.

```bash
python -m pip install selenium
```

## Usage

```python
Two scripts are loaded here. One is automatically fill out all the metadata and upload a record to the website. After upload is complete, it will verify if the data is correct on the UI. The script name is UITest_AddUser.py. Another one is for deleting a record from the website automatically, as well as verifying if the data has been removed. Script name is UITest_DeleteUser.py.

1. UITest_AddUser.py
This script is able to fill out first name, last name, username, Customer, Role, email address and phone number via "add user" mini app. After the key in process is complete, it will automatically go back the UI and self test if all the metadata has been loaded into the system correctly. The output can specify which ones are loaded on the UI correctly and which ones are not.

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
