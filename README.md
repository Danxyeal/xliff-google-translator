# XLIFF Google Translator
Uses Google Cloud Translate API to translate XLIFF files. This has been identified as helpful for translators as it reduces the amount of typing. Translation jobs become more like heavy proof-reading or copywriting tasks.
## About
The script takes 2 arguments on the command line, a target language and a path to any XLIFF type file (without target tags) as input. Google Cloud Translate API will detect the source language in your file but ignore the XML. It returns the file translated into your target language. This is where my script comes it. It should successfully combine the original file with all the source tags and additional target tags from the machine translated file.
There are a few further tag attributes that the script adds to the output. It then writes the file to disk with "done\_" prepended to the name. You can then import the done file into your app or service to have a translated version of your content. Alternatively, pass the done\_ file onto your translation team - they may use a XLIFF editor applications to proof-read the new translation prior to importing. I recommend Poedit for that purpose: https://poedit.net/download
## License
As the license is no license please feel absolutely free to use the algorithm and change it as much as you like.
## Requirements
1. Pip, Python 3\* (modify the Pipfile for your version - also check the Google Translate API packages for their current requirements)
2. Pipenv - you may also wish to ignore the venv instructions and just install the required packages:
    - google-cloud-translate
    - bs4
3. Google Cloud Platform account
## Installation
More extensive instructions available soon and potentially a PyPi package made public.
1. Activate billing on your GCP project and get the JSON credentials file then add the path to that google-credentials.json to your environment (https://cloud.google.com/docs/authentication/getting-started)
2. Install pipenv with pip `pip install pipenv --user`
3. Use pipenv install to install the required packages to virtual environment
4. Use cmd pipenv shell to activate the environment
## How to use
1. Place the XLIFF/XLF file you want to translate into the same folder as the program
2. Activate the virtual environment - usually indicated by the directory name in paretheses at the start of the prompt
3. Run the following command (don't include the angle brackets):
```
(xliff-google-translator) $ ~ python xgt.py <target language> <path/filename.xlf>
// For example, this will translate for English to French:
(xliff-google-translator) $ ~ python xgt.py fr english-output-chapter-01.xlf
```
## NOTE:
This tool is in early stages of development. Please see the Google Cloud Translate API docs for help using this script:
- List of supported languages: https://cloud.google.com/translate/docs/languages
- This tool uses the Python client library for Cloud Translate: https://cloud.google.com/translate/docs/reference/libraries/v2/python, https://googleapis.dev/python/translation/latest/client.html
## Feature Requests
Add batch processing functionality
## TODO (Dev notes)
- Setup dotenv to create environment variable: GOOGLE\_APPLICATION\_CREDENTIALS to point to location of google-service-account.json file
- Separate concerns in the code
