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

def write_file(source_with_target_str, file_name):
    xliff_output = open(file_name, "w")
    xliff_output.write(source_with_target_str)
    xliff_output.close()

from bs4 import BeautifulSoup
import bs4
import os.path

FILENAME = 'en-zh-06'
TARGET = 'zh'
EXT = '.xlf'

target_filename = TARGET + '_' + FILENAME + EXT

with open(FILENAME + EXT) as f:
    source_file = f.read()

if os.path.isfile(target_filename):
    print ("Translation file exists...Opening")
    with open(target_filename) as f:
        target_file = f.read()
else:
    print ("Translation file does not exist...Creating")
    target_file = translate_text(TARGET, source_file)
    write_file(target_file, target_filename)

source_soup = BeautifulSoup(source_file, 'xml')
target_soup = BeautifulSoup(target_file, 'xml')

stu = source_soup.find_all('trans-unit')
ttu = target_soup.find_all('trans-unit')
ttu_str = [tu.source.contents for tu in ttu]

target_gen = (target for target in ttu)
print('XLIFF file name', FILENAME)
print(len(stu), 'source trans-units and', len(ttu), 'targets')
print('Word count:', len(target_soup.get_text().split()))
#print(target_soup.get_text().split())

for tu in stu:
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

write_file(str(source_soup), 'done_' + TARGET + '_' + FILENAME + EXT)

# TODO
#  - strip the strings inside nested <g> tags
#  - add target-language="fr" attribute to <file> tags
#  - fix HTML encoded angle bracket problem
'''
for tu in stu:
    target_element = source_soup.new_tag("target")
    e = next(target_gen)
    target_element.string = str(e)
    tu.source.insert_after(target_element)

for tu in stu:
    target_element = source_soup.new_tag("target")
    target_content = ''
    print(next(target_gen).source)
    for child in next(target_gen).source.children:
        if child:
            target_content = target_content + str(child)
    target_element.string = target_content.strip()
    tu.source.insert_after(target_element)

'''
