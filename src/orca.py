import subprocess, getopt, sys

def pullContainer(images = None, tag = "latest"):
    if images != None:
        for image in images:
            try:
                subprocess.call(["docker","pull",image + ":" + tag])
                
            except IOError:
                raise IOError
    else:
        print("Error: No image specified.")
                   
def instantiateDockerContainer(image = None, tag = "latest", count = 1, name = None, host_port = None, container_port = None, env_variables = None, daemonized = True):
    if image != None and daemonized == True:
        try:
            for x in range(1,count + 1):
                subprocess.call(["docker","run","-d", "--name", name + "" + str(x),
                                 "-p", str(host_port) + ":" + str(container_port),
                                 image + ":" + tag], shell = True)
                host_port = host_port + 1
                
        except IOError:
            raise IOError
    else:
        return 0
        
'''def monitorContainers(containers = None):
    running_containers = subprocess.check_output("docker ps", shell = True)
    
    print(str(running_containers))'''

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"i:t:h:c:n:d:hp:cp",["image=","tag=","count=","name=","host-port=","container-port=","daemonized="])
    except getopt.GetoptError:
        raise getopt.GetoptError
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == "-h":
            print("Yo")
            sys.exit()
        elif opt in ("-i","--image"):
            imagep = str(arg)
        elif opt in ("-t","--tag"):
            tagp = str(arg)
        elif opt in ("-c","--count"):
            countp = arg
        elif opt in ("-n","--name"):
            namep = str(arg)
        elif opt in ("-hp","--host-port"):
            host_portp = str(arg)
        elif opt in ("cp","--container-port"):
            container_portp = str(arg)
        elif opt in ("-d","--daemonized"):
            daemonizedp = True
        else:
            print("Did not input a valid argument.")
            sys.exit()
        
    instantiateDockerContainer(image = imagep, tag = tagp, count = countp, name = namep,
                               host_port = host_portp, container_port = container_portp,
                               daemonized = daemonizedp)
        
    
    

if __name__ == "__main__":
    main(sys.argv[1:])
        
                                       
                            
                    

# pullContainer(images = ["httpd"])
# instantiateDockerContainer(image = "httpd",count = 5, name = "website")
                                 
