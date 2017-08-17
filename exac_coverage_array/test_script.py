import sys, requests
from multiprocessing import Queue

def exac_coverage_array(chrom, coord):
    server = "http://exac.hms.harvard.edu/"
    headers = {"Content-Type" : "application/json"}
    coord_plus = int(coord) + 1
    ext = "rest/region/coverage_array/" + chrom + "-" + coord + "-" + str(coord_plus)
    print(server + ext)
    r = requests.get(server + ext, headers=headers)
    r_json = r.json()
    for item in r_json:
        if str(item['pos']) == (coord):
            x = int(float(item['20'])*121412)/2
            print(x)
            return str(x)
        else:
            pass
            
x = exac_coverage_array(sys.argv[1], sys.argv[2])


