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
		'Excel': ['.xls', '.xlsx', '.ods', '.csv'],
		'PowerPoint': ['.ppt', '.pptx', '.odp', '.pptm'],
		'Calendar': ['.ics'],
		'PDF': ['.pdf'],
		'Ebook': ['.epub', '.pub'],
		'Text': ['.txt'],
		'Font': ['.ttf'],
		'Log': ['.log'],
		'Maps': ['.fit', '.gpx'],
		'Config': ['.cfg', '.ini', '.conf', '.cnf'],
		'Certificate': ['.cer', '.crt', '.pem', '.der', '.p12', '.pfx'],
	}),
	'Executable': ContentType('Executable', '.\\Executable', ext=
	{
		'Windows': ['.exe', '.msi', '.msu', '.appx', '.appxbundle', '.msix', '.msixbundle', '.dll'],
		'Mac': ['.app'],
		'Android':['.apk','.apks'],
		'iOS': ['.ipa'],
		'Java': ['.jar'],
		'Commodore': ['.d64', '.prg', '.wr3'],
	}),
	'Archives': ContentType('Archives', '.\\Archives', ext=
	{
		'Installable': ['.dmg', '.deb', '.cab'],
		'Image': ['.iso', '.img', '.aschdsk'],
		'Other': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.lz', 
		'.lzo', '.lz4', '.lzop', '.lzma', '.lz4', '.lzop', '.xz', 
		'.zst', '.zpaq', '.arj', '.cram', '.udf', 
		'.wim', '.swm', '.lzh', '.lha', '.lzx', '.tgz']
	}),
	'Video': ContentType('Video', '.\\Video', ext=
	{
		'All': ['.mp4',' .mkv', '.avi', '.mpg', '.mpeg', '.wmv', '.flv', '.3gp',
		'.mov', '.m4v', '.m2ts', '.ts', '.mts', '.m2t', '.m2v', '.m4v', '.m4a',
		'.m4b', '.m4p', '.m4r', '.m4v', '.mov', '.qt', '.mxf', '.rm', '.rmvb',
		'.asf', '.ram', '.mp4', '.m4p', '.m4b', '.m4v', '.m4a', '.m4r', '.m4v', '.m4', 
		'.m3u8', ]
	}),
	'Audio': ContentType('Audio', '.\\Audio', ext=
	{
		'All': ['.mp3', '.wav', '.wma', '.aac', '.flac', '.ogg', '.oga', '.mid']
	}),
	'Pictures': ContentType('Pictures', '.\\Pictures', ext=
	{
		'Vectorial':['.svg','.eps','.svgz'],
		'Bitmap':['.bmp','.jpg','.jpeg','.png','.gif','.tiff','.tif','.raw','.webp',
		'.ico', '.emf', '.wmf'],
	}),
	'SoftwareProjects': ContentType('SoftwareProjects', '.\\SoftwareProjects', ext=
	{
		'PhotoShop': ['.psd'],
		'Illustrator': ['.ai'],
		'InDesign': ['.indd'],
		'Pixelmator': ['.pxm'],
		'PixelFormer': ['.pxf'],
		'MultiSim': ['.msim', '.msm'],
		'MuseScore':['.mscz', '.qlm'],
		'AppInventor': ['.aia', '.aix'],
		'GeoGebra': ['.ggb'],
		'Aspire': ['.crv3d'],
		'PacketTracer': ['.pkt'],
		'VirtualBox': ['.ova'],

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
		'Manifest': ['.appxmanifest', '.manifest'],

		'Windows': ['.reg', '.regf', '.vbs', '.inf', '.ini', '.url', '.urls', '.urls', '.urls'],
		'VisualStudio': ['.vsproj', '.vsix', '.sln', '.csproj', ],
		'Other':['.css','.json'],
	}),
	'Other': ContentType('Other', '.\\Other', ext=
	{
		'All': ['All'],
	}),
}
