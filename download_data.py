"""
FOR CERTIFICATION ERROR

MAC users needs to install Python certificates.
Search for these files in Finder:
Install Certificates.command
Update Shell Profile.command
and Run them

Source : https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org

"""



import urllib.request

# Read the classes
def read_classes():
  f = open ("classes", "r")
  classes = f.readlines()
  f.close()
  for i in range(0, len(classes)):
    classes[i] = classes[i].replace('\n', '').replace(' ', '_')
  return classes



# Define a function to download the data and store it in our local system.
def obtain_dataset(out_classes):
    base_url = "https://storage.googleapis.com/quickdraw_dataset/full/numpy_bitmap/"
    category = ''

    for i in range(0, len(out_classes)):
        ## Create URL
        category = out_classes[i].replace('_', '%20')
        url = base_url + category + ".npy"
        ## Fetch...
        print("downloading " + url + " ...")
        urllib.request.urlretrieve(url, "datasets/" + out_classes[i] + ".npy")
