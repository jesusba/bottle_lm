from bottle import Bottle,route,run,request,template
from lxml import etree
import requests

@route('/')
def principal():
	return template('index.html')

@route('/ciudad', method='POST')
def ciudad():
	ciudad = request.forms.get('ciudad')
	url_base="http://api.openweathermap.org/data/2.5/"
	dic={"q":ciudad,"mode":"xml","units":"metric"}

	r=requests.get(url_base+"weather",params=dic)
	doc=etree.fromstring(r.text.encode("utf-8"))
	temp=doc.find("temperature").attrib["value"]
	return template("template_tiempo.tpl",ciudad=ciudad,temp=temp)

run(host='0.0.0.0', port=8080)