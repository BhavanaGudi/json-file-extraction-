import json
json_data=open('sonar-qube.json').read()
data = json.loads(json_data)
print 'component.id='+data['component']['id']
print 'component.key='+data['component']['key']
print 'component.name='+data['component']['name']
print 'component.qualifier='+data['component']['qualifier']
i = 0
while len(data['component']['measures'][i]['metric']) != 0:
    print data['component']['measures'][i]['metric']+'='+data['component']['measures'][i]['value']
    i = i+1

