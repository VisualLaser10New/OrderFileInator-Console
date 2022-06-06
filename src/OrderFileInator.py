import argparse
import shutil
import os, sys

class ContentType:
	__Name=''
	__FolderPath=''
	__GroupsExtension = []

	def __init__(self, name, folderPath, ext):
		self.__Name = name
		self.__FolderPath = folderPath
		self.__GroupsExtension = ext

	def getName(self):
		return self.__Name
	
	def getFolderPath(self):
		return self.__FolderPath
	
	def getExt(self):
		return self.__GroupsExtension
	
Files = {
	'Documents': ContentType('Documents', '.\\Documents', ext=
	{
		'Word': ['.doc', '.docx', '.odt', '.rtf'],
		'Excel': ['.xls', '.xlsx', '.ods'],
		'PowerPoint': ['.ppt', '.pptx', '.odp'],
		'Calendar': ['.ics'],
		'PDF': ['.pdf'],
		'Text': ['.txt'],
		'Log': ['.log'],
		'Config': ['.cfg', '.ini', '.conf', '.cnf'],
		'Certificate': ['.cer', '.crt', '.pem', '.der', '.p12', '.pfx'],
	}),
	'Executable': ContentType('Executable', '.\\Executable', ext=
	{
		'Windows': ['.exe', '.msi', '.msu', '.appx', '.appxbundle', '.msix', '.msixbundle'],
		'Mac': ['.app'],
		'Android':['.apk'],
		'iOS':['.ipa'],
	}),
	'Archives': ContentType('Archives', '.\\Archives', ext=
	{
		'All': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.lz', 
		'.lzo', '.lz4', '.lzop', '.lzma', '.lz4', '.lzop', '.xz', 
		'.zst', '.zpaq', '.cab', '.arj', '.cram', '.iso', '.dmg', '.udf', 
		'.wim', '.swm', '.lzh', '.lha', '.lzx']
	}),
	'Video': ContentType('Video', '.\\Video', ext=
	{
		'All': ['.mp4',' .mkv', '.avi', '.mpg', '.mpeg', '.wmv', '.flv', '.3gp',
		'.mov', '.m4v', '.m2ts', '.ts', '.mts', '.m2t', '.m2v', '.m4v', '.m4a',
		'.m4b', '.m4p', '.m4r', '.m4v', '.mov', '.qt', '.mxf', '.rm', '.rmvb',
		'.asf', '.ram', '.mp4', '.m4p', '.m4b', '.m4v', '.m4a', '.m4r', '.m4v', '.m4',]
	}),
	'Audio': ContentType('Audio', '.\\Audio', ext=
	{
		'All': ['.mp3', '.wav', '.wma', '.aac', '.flac', '.ogg', '.oga', '.mid', '.amr']
	}),
	'Pictures': ContentType('Pictures', '.\\Pictures', ext=
	{
		'Vectorial':['.svg','.eps','.svgz'],
		'Bitmap':['.bmp','.jpg','.jpeg','.png','.gif','.tiff','.tif','.raw','.webp', '.jfif', '.ico'],
	}),
	'SoftwareProjects': ContentType('SoftwareProjects', '.\\SoftwareProjects', ext=
	{
		'PhotoShop': ['.psd'],
		'Illustrator': ['.ai'],
		'InDesign': ['.indd'],
		'Pixelmator': ['.pxm'],
		'PixelFormer': ['.pxf'],
		'MultiSim': ['.msim', '.msm'],
		'Musescore': ['.mscz'],
		'Stylish': ['.dms'],
	}),
	'Programming': ContentType('Programming', '.\\Programming', ext=
	{		
		'Markup':['html', 'htm', 'xhtml', 'xml', 'xsl', 'xsd', 'xslx', 'xltx', 'xlsm'],

		'Markdown':['.md'],

		'C':['.c','.h'],
		'C++':['.cpp','.hpp'],
		'C#':['.cs'],
		'Java':['.java'],
		'JavaScript':['.js'],
		'Python':['.pya', '.pyb', '.pyc', '.pyd', '.pye', '.pyf', '.pyg', '.pyh', '.pyi',
		'.pyk', '.pyl', '.pym', '.pyn', '.pyo', '.pyq', '.pyr', '.pys', '.js', '.pyt',
		'.py', '.pyu', '.pyv', '.pyw'],
		'PHP':['.php'],
		'Ruby':['.rb'],
		'Perl':['.pl'],
		'Lua':['.lua'],
		'Go':['.go'],
		'Rust':['.rs'],
		'Scala':['.scala'],
		'Swift':['.swift'],
		'D':['.d'],
		'B':['.b'],
		'Objective-C':['.m'],
		'Assembly':['.asm'],
		'CMake':['.cmake'],
		'Makefile':['.mk', '.mak', '.make'],
		'Batch':['.bat', '.cmd'],
		'Shell':['.sh', '.bash', '.ksh', '.zsh'],
		'PowerShell':['.ps1', '.ps2', '.ps3', '.ps4', '.ps5', '.ps6', '.ps7', '.ps8', '.ps9',
		'.ps1xml', '.ps1n', '.ps1nxml', '.ps'],
		'Pascal':['.pas'],
		'Visual Basic':['.vb', '.vba', '.bas', '.frm', '.cls', '.ctl', '.dob', '.dfm', '.vbs', '.vbx'],
		'Php': ['.php', '.php3', '.php4', '.php5', '.phtml', '.phps'],
		'Git': ['.gitignore', '.gitattributes', '.gitmodules', '.gitconfig', '.gitkeep'],

		'Windows': ['.reg', '.regf', '.vbs', '.inf', '.ini', '.url', '.urls', '.urls', '.urls'],
		'VisualStudio': ['.vsprog', '.vsix'],
		'Other':['.css','.json'],
	}),
	'Other': ContentType('Other', '.\\Other', ext=
	{
		'All': ['All'],
	}),
}

Settings = {
	'Recursive': False,
	'DeleteAfterCopy': False,
	'CreateFolders': True,
	'FolderName': '',
	'BypassBigs': 0,
	'Substitute': False,
}

def handleArgs():
	parser = argparse.ArgumentParser(description='Order files by type')
	parser.add_argument('-r', '--recursive', action='store_true', help='Copy files recursively.')
	parser.add_argument('-d', '--delete', action='store_true', help='Delete files after copying.')
	parser.add_argument('-c', '--create', action='store_true', help='Create destination folders.')
	parser.add_argument('-s', '--substitute', action='store_true', help='Replace older files.')
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

def makeFolders():
	if Settings['CreateFolders']:
		for key in Files:
			if os.path.exists(Files[key].getFolderPath()):
				shutil.rmtree(Files[key].getFolderPath())
			os.mkdir(Files[key].getName())

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

							if(not os.path.exists(Files[key].getFolderPath() + "\\" + cf + "\\")): #create cf folder if not exists
								os.mkdir(Files[key].getFolderPath()+"\\"+ cf + "\\")

							if(not os.path.exists(Files[key].getFolderPath() + "\\" + cf + "\\" + ext + "\\")): #create ext folder if not exists
								os.mkdir(Files[key].getFolderPath()+"\\"+ cf + "\\" + ext + "\\")
							
							if(Settings['Substitute']):#replace older file
								if(os.path.exists(Files[key].getFolderPath() + "\\" + cf + "\\" + ext + "\\" + fileName)):
									os.remove(Files[key].getFolderPath() + "\\" + cf + "\\" + ext + "\\" + fileName)
							
								#copy file
								shutil.copyfile(folderName+ '\\' + fileName, Files[key].getFolderPath() + "\\" + cf + "\\" + ext + "\\" + fileName)
							else:
								#if not sobstitute file
								if(os.path.exists(Files[key].getFolderPath() + "\\" + cf + "\\" + ext + "\\" + fileName)):
									print("File %s already exists, so it will not be copied" % (fileName))
									errorfiles += 1
									break
								else:
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
								break
							deletedfiles += 1
						break
				if (breakall):
					break
			if(breakall):
				break
			
	print('%d Total files, %d files copied, %d files deleted, %d error, %d big files' % (totalfiles, copyedfiles, deletedfiles, errorfiles, bigfiles))
	return

handleArgs()
makeFolders()
copyFiles(Settings['FolderName'])
