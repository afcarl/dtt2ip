#!/usr/bin/python

import commands, re

def getFrontEnds():
	# Initialize frontEnd dictionary 
	frontEndDict = {}

	# Make sure that resources.log file is clean
	fLog = open('logs/resources.log', 'w')

	# List the available adapters
	cmd = 'ls -l /dev/dvb/'
	fLog.write('Info: about to do find all available adapters\n')
	outtext = commands.getoutput(cmd)
	(exitstatus, outtext) = commands.getstatusoutput(cmd)
	if not exitstatus:
		linesArray = outtext.split('\n')
		for line in linesArray:
			matchAdapter = re.search(r'adapter([\w]+)', line)
			if matchAdapter:
				adapter = 'adapter' + matchAdapter.group(1)
				frontEndDict[adapter] = {}
				frontEndDict[adapter]['owner'] = '0.0.0.0'
				frontEndDict[adapter]['freq'] = ''
		fLog.write('Info: Available ' + adapter + ' detected\n')
	else:
		fLog.write('Info: NO AVAILABLE adapters detected\n')
	fLog.close()
	return frontEndDict
	
if __name__ == '__main__':
	getFrontEnds()