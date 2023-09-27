import requests 
import time 
import datetime 

hostname = "https://google.com"

def ping(_hostname):
  try: 
    x = requests.get(_hostname)
  except: 
    return False

  if x.status_code == 200: 
    return True 

  return False 


#Start the main loop 
then = 0 
while(True): 
  now = time.time() * 1000 

  if(now <= then + 1000):
    continue 

  then = now 
  #At this point 1 second has passed 
  date = datetime.datetime.now() 
  hasInternet = ping(hostname)
  str_status = "Success" if hasInternet else "Failed"
  
  output = f"[{date}] Http request to {hostname}: {str_status}\n"
  print(output)
  
  output_file = open("./logs.txt", "a")
  output_file.write(output)
  output_file.close() 
  
  
print("End of program")
