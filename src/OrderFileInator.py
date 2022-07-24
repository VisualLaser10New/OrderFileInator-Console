import argparse
import shutil
import os, sys
import re
from ContentType import ContentType as ContentType
from ContentType import Files as Files

Settings = {
	'Recursive': False,
	'DeleteAfterCopy': False,
	'CreateFolders': True,
	'FolderName': '',
	'BypassBigs': 0,
	'Substitute': False,
	'Exclude': '',
	'ExcludedList': [],
	'Log':'',
}

def handleArgs():

	parser = argparse.ArgumentParser(description='Order files by type')
	parser.add_argument('-r', '--recursive', action='store_true', help='Copy files recursively.')
	parser.add_argument('-d', '--delete', action='store_true', help='Delete files after copying.')
	parser.add_argument('-c', '--create', action='store_true', help='Create destination folders.')
	parser.add_argument('-s', '--substitute', action='store_true', help='Replace older files.')
	parser.add_argument('-l', '--log', metavar="PATH", help='Log all output to a file.')
	parser.add_argument('-e', '--exclude', metavar="PATH", help='Path of the file that contains a list of excluded extensions.')
	parser.add_argument('-f', '--folder', metavar="PATH", help='Folder to get files from.')
	parser.add_argument('-b',  '--bypassbigs', type=int, metavar="NUMBER", help='Bypass files bigger than (NUMBER).')
	args = parser.parse_args()
	
	if args.recursive:
		Settings['Recursive'] = True
	else:
		Settings['Recursive'] = False
	
	if args.delete:
		Settings['DeleteAfterCopy'] = True
	else:
		Settings['DeleteAfterCopy'] = False

	if args.create:
		Settings['CreateFolders'] = True
	else:
		Settings['CreateFolders'] = False

	if args.folder:
		Settings['FolderName'] = args.folder

	if args.bypassbigs:
		Settings['BypassBigs'] = int(args.bypassbigs)
	else:
		Settings['BypassBigs'] = 0
	
	if args.substitute:
		Settings['Substitute'] = True
	else:
		Settings['Substitute'] = False

	if args.exclude:
		Settings['Exclude'] = args.exclude
	else:
		Settings['Exclude'] = ''

	if args.log:
		Settings['Log'] = args.log
	else:
		Settings['Log'] = ''

def makeFolders():
	if Settings['CreateFolders']:
		for key in Files:
			if os.path.exists(Files[key].getFolderPath()):
				shutil.rmtree(Files[key].getFolderPath())
			os.mkdir(Files[key].getName())

def isExt(line):
	if(re.match('^\\.[^.]+$',line)):
		return True
	else:
		return False

def getExcludedList():
	epath = Settings['Exclude']
	if(os.path.exists(epath)):
		try:
			with open(epath, 'r') as f:
				Lines = f.readlines()

				#check if file is formatted correctly (each line contains an extension)
				for line in Lines:
					if(not isExt(line)):
						print("Excluded list not properly formatted")
						return False
				
				Settings['ExcludedList']=Lines
		except:
			print("Exclude file is not valid")
			return False
	else:
		print("Exclude file is not valid")
		return False
	return True
	
def copyFiles(folderName):
	totalfiles, copyedfiles, deletedfiles, bigfiles, errorfiles = 0, 0, 0, 0, 0
	#get all files and folders in folder
	try:
		dirs = os.listdir(folderName)
	except:
		print('Error: Folder \'%s\' does not exist.' % folderName)
		return
	
	#if recursive enter in folders
	if Settings['Recursive']:
		for folder in dirs:
			if os.path.isdir(folderName + '\\' + folder):
				copyFiles(folderName + '\\' + folder)

	#iterate all files in folder
	for fileName in dirs:
		totalfiles += 1
		#iterate all types
		if(Settings['BypassBigs'] > 0 and os.path.getsize(folderName + "\\" + fileName) > Settings['BypassBigs']):
			bigfiles += 1
			print('%s is a big file and was skipped.' % fileName)
			continue
		

		#check if the extension is excluded
		passthisfile = False
		for excl in Settings['ExcludedList']:
			if (fileName.endswith(excl)):
				passthisfile = True
		
		if passthisfile:
			continue

		
		for key in Files:
			breakall = False
			#key -> documents
			ct = Files[key].getExt()
			#ct -> all extensions and all types in documents
			for cf in ct:
				#cf -> word[]
				for ext in ct[cf]:
					#ext -> .docx

					#check if file matches extension
					if (fileName.lower().endswith(ext) and os.path.isfile(folderName + "\\" + fileName)) or (ext == 'All' and os.path.isfile(folderName + "\\" + fileName)):
						breakall = True
						#copy file to folder
						try:
							print("Copying %s to %s" % (fileName, Files[key].getName()))

							if(Settings['Substitute']):#replace older file
								if(os.path.exists(Files[key].getFolderPath() + "\\" + cf + "\\" + ext + "\\" + fileName)):
									os.remove(Files[key].getFolderPath() + "\\" + cf + "\\" + ext + "\\" + fileName)
							
							if(not os.path.exists(Files[key].getFolderPath() + "\\" + cf + "\\")): #create cf folder if not exists
								os.mkdir(Files[key].getFolderPath()+"\\"+ cf + "\\")

							if(not os.path.exists(Files[key].getFolderPath() + "\\" + cf + "\\" + ext + "\\")): #create ext folder if not exists
								os.mkdir(Files[key].getFolderPath()+"\\"+ cf + "\\" + ext + "\\")
							
							#copy file
							shutil.copyfile(folderName+ '\\' + fileName, Files[key].getFolderPath() + "\\" + cf + "\\" + ext + "\\" + fileName)
						except:
							errorfiles += 1
							print('Error: Could not copy file \'%s\'.' % fileName)
							break
						copyedfiles += 1
						#delete file if deleteAfterCopy is true
						if (Settings['DeleteAfterCopy']):
							try:
								os.remove(folderName + '\\' + fileName)
							except:
								print('Error: Could not delete file \'%s\'.' % fileName)
							deletedfiles += 1
						break
				if (breakall):
					break
			if(breakall):
				break
			
	print('%d Total files, %d files copied, %d files deleted, %d error, %d big files' % (totalfiles, copyedfiles, deletedfiles, errorfiles, bigfiles))
	return

def closeall(code):
	sys.stdout.close()
	exit(code)

def setlog():
	if(len(Settings['Log']) != 0):
		sys.stdout = open(Settings['Log'], 'w')

handleArgs()
setlog()
#get excluded list if is not empty
if(len(Settings['Exclude']) != 0):
	if(not getExcludedList(Settings['Exclude'])):
		closeall(1)

makeFolders()
copyFiles(Settings['FolderName'])


'''
#TODO: add option that if a recursive folder contains more than one file, which different extension copy the enteire folder
not each single file
'''