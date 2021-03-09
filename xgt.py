from bs4 import BeautifulSoup
import bs4
import lxml
import os.path
import sys

def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    import six
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    #print(u"Text: {}".format(result["input"]))
    #print(u"Translation: {}".format(result["translatedText"]))
    #print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
    return result['translatedText']

def write_file(source_with_target_str, filename):
    xliff_output = open(filename, "w")
    xliff_output.write(source_with_target_str)
    xliff_output.close()

def main():
    TARGET = sys.argv[1]
    FILENAME = sys.argv[2]
    target_filename = TARGET + '_' + FILENAME

    try:
        with open(FILENAME) as f:
            source_file = f.read()
    except IOError:
        print('\nCommand should look like this: \n$ ~ python xliff-google-translator.py <target language eg. fr for French, zh for Chinese> <filename.xlf>')
        print(f'File {FILENAME} not found. Please put the file in the same directory as this script, check the name, include the extension, and try again')
        print('Exiting program...\n')
        exit()

    if os.path.isfile(target_filename):
        print ("Translation file exists. Opening...")
        with open(target_filename) as f:
            target_file = f.read()
    else:
        print ("Translation file does NOT exist. Creating...")
        target_file = translate_text(TARGET, source_file)
        write_file(target_file, target_filename)

    source_soup = BeautifulSoup(source_file, 'lxml')
    target_soup = BeautifulSoup(target_file, 'lxml')

    source_trans_units = source_soup.find_all('trans-unit')
    target_trans_units = target_soup.find_all('trans-unit')
    ttu_str = [trans_unit.source.contents for trans_unit in target_trans_units]

    target_gen = (target for target in target_trans_units)
    print('XLIFF file name', FILENAME)
    print(len(source_trans_units), 'source trans-units and', len(target_trans_units), 'targets')
    print('Word count:', len(target_soup.get_text().split()))

    for tu in source_trans_units:
        target_element = next(target_gen).source
        target_element.name = 'target'
        tu.source.insert_after(target_element)

    for file_tag in source_soup.find_all('file'):
        file_tag['target-language'] = TARGET

    for target_tag in source_soup.find_all('target'):
        if target_tag.string:
            target_tag.string = target_tag.string.strip()

    '''
    for g_tag in source_soup.find_all('g'):
        if g_tag.string:
            g_tag.string = g_tag.string.strip()
    '''

    write_file(str(source_soup), 'done_' + TARGET + '_' + FILENAME)


if __name__ == '__main__':
    main()

# TODO
# - package up
# - separate concerns and move code into main function
