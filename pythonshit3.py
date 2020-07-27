from urllib import request
#what we want to download
reliance_url='https://in.finance.yahoo.com/quote/RELIANCE.NS/history?p=RELIANCE.NS'
 
#function
def download_stock(csv_url):
	response=request.urlopen(csv_url)  #opening url
	csv=response.read()					#reading and saving data
	csv_string=str(csv)					#converting csv into stirng
	lines=csv_string.split("\\n")		#seprating lines of csv 
	destination=r'reliance_url.csv'			#destination in local pc to save the file involved
	fx=open(destination,'w')			#opening of file in write mode using openfunction
	for line in lines:					#changes in string file according to our comfart	
		fx.write(line+'\n')
	fx.close()							#closing of file


	download_stock(reliance_url)