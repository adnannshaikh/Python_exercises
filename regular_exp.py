import re
a = re.compile('is')
sent = 'This is really annoying'

print(a.search(sent))