# XLIFF Google Translator
Uses Google Cloud Translate API to translate XLIFF files. This has been identified as helpful for translators as it reduces the amount of typing. Translation jobs become more like heavy proof-reading or copywriting tasks.
# License
As the license is no license please feel absolutely free to use this and change it as much as you like.
# Requirements
1. Pip, Python 3\* (modify the Pipfile for your version - also check the Google Translate API packages for their current requirements)
2. Pipenv (can also be adjusted for Venv)
3. Google Cloud Platform account
# Installation
More extensive instructions available soon and potentially a PyPi package made public.
1. Activate billing on your GCP project and get the JSON credentials file then add the path to that google-credentials.json to your environment
2. Install pipenv with pip then use pipenv install to install the required packages to virtual environment
3. Use cmd pipenv shell to activate the venv
# How to use
1. Place the XLF file you want to translate into the same folder as the program.
2. Activate the virtual environment
3. Run the following command:
```
$ ~ python xliff-google-translator.py <target> <filename.xlf>
```
# NOTE:
This tool is in early stage of development. Please see the Google Cloud Translate API docs for help using this script:
- List of supported languages: https://cloud.google.com/translate/docs/languages
- This tool uses the Python client library for Cloud Translate: https://cloud.google.com/translate/docs/reference/libraries/v2/python, https://googleapis.dev/python/translation/latest/client.html
# TODO
- Setup dotenv to create environment variable: GOOGLE_APPLICATION_CREDENTIALS to point to location of google-service-account.json file
- Update to token
