import urllib2

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = urllib2.urlopen(word_site)
txt = response.read()

with open('./words.txt', 'w') as fh:
    fh.write(txt);

print open('./words.txt').read()
