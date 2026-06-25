import csv

def write_report(summary):
 f=open('reports/tcp_report.csv','w',newline='');w=csv.writer(f);w.writerow(['Metric','Value']);[w.writerow([k,v]) for k,v in summary.items()];f.close()
