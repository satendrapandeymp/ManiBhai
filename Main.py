import os, aiml, time

kernel = aiml.Kernel()
filename = "aiml/brain/100005540460570.brn"

def train(filename):
        kernel.bootstrap(learnFiles = os.path.abspath("aiml/XMLS/100005540460570.xml"), commands = "load aiml b")
        kernel.saveBrain(filename)

train(filename)

if os.path.isfile(filename):
	kernel.bootstrap(brainFile = filename)

while(True):
	message = raw_input("Type your query : ")
	time1 = time.time()
    	message = kernel.respond(message)
	print "time taken is " , time.time() - time1
	if message == "":
		message = "I'm just the basic version, Go to FAQ for more help"
	print message
