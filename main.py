import csv

data=[]
with open('final.csv','r') as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append(row)

headers=data[0]
star_data=data[1:]

dist_star_data=[]
for data in star_data:
    cd=float(data[4])
    if(cd<=100):
        dist_star_data.append(data)

grav_star_data=[]
for data in dist_star_data:
    cd=float(data[8])
    if(cd>150 and cd<350):
        grav_star_data.append(data)

with open('real_final.csv','a+') as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(grav_star_data)