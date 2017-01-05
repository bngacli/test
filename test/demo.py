1
2
import urllib

import urllib2

values={}
values['username'] = "defenyong@hotmail.com"
values['password'] = "123"
data = urllib.urlencode(values)
url = "https://www.zhihu.com/?next=%2Finbox#signin"
geturl = url +"?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
print geturl




