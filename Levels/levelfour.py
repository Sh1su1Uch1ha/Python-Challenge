import urllib2
nothing = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
url = nothing + "93781"
for i in range(1000):
    response = urllib2.urlopen(url)
    data = response.read()
    nums = [s for s in data.split() if s.isdigit()]
    url = nothing + nums[0]
    print data
