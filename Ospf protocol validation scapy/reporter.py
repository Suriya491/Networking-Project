import csv

def write_report(results):
    with open('ospf_report.csv','w',newline='') as f:
        w=csv.writer(f)
        w.writerow(['Device','Status'])
        w.writerows(results)
