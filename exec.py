from PIL import Image
import sys

import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))

print("\n----------------------------\n")

jpn_txt = tool.image_to_string(
 Image.open('wiki-top-jpn.png'),
 lang='jpn',
 builder=pyocr.builders.TextBuilder()
)
eng_txt = tool.image_to_string(
 Image.open('wiki-top-eng.png'),
 lang='eng',
 builder=pyocr.builders.TextBuilder()
)

print(jpn_txt)
print("\n----------------------------\n")
print(eng_txt)
