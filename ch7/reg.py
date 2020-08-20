#! usr/bin/python3

import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 650-391-7742')
print('Phone number found: ' + mo.group())


