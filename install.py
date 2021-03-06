"""
install or update dotfiles

usage:
install.py [-g]
"""

from glob import iglob
import sys, os, shutil, platform

# cd to the directory that contains this script
# to make sure it works when not running from
# that directory
cur_folder = os.path.dirname(os.path.realpath(__file__))
os.chdir(cur_folder)

def uniglob(base_path=os.getcwd(), path=None, exclude=[".git", ".gitignore", ".gitmodules", "README.md", ".DS_Store", "install.py", "install_packages.py", "build.sh", "shorten.c"]):
	"glob every file recursively"

	if not path: path = base_path

	# glob all visible files
	for f in iglob(os.path.join(path, "*")):
		# filter out excluded paths
		if get_path(f, base_path) in exclude or os.path.basename(f) in exclude: continue

		if os.path.isfile(f):
			yield get_path(f, base_path)	# yield the file
		elif os.path.isdir(f):
			yield from uniglob(base_path, f)# uniglob the subfolder

	# glob all dotfiles
	for f in iglob(os.path.join(path, ".*")):
		# filter out excluded paths
		if get_path(f, base_path) in exclude or os.path.basename(f) in exclude: continue

		if os.path.isfile(f):
			yield get_path(f, base_path)	# yield the file
		elif os.path.isdir(f):
			yield from uniglob(base_path, f)# uniglob the subfolder

def get_path(p, base):
	"get the relative path"
	return p.replace(base, "").lstrip("/")

def install(grab):
	if not grab:
		# install the dotfiles to home
		# ./ => ~/

		exclude = ["bin/shortener/shorten"]

		for source_file in uniglob(os.getcwd()):
			dest_file = os.path.expanduser(os.path.join("~", source_file))
			f = os.path.join(os.getcwd(), source_file)
			# filter out excluded paths
			if source_file in exclude: continue

			# source_file = ./...
			# dest_file = ~/...

			# create the directory if it doesn't exist
			d = os.path.dirname(dest_file)
			if not os.path.isdir(d):
				os.makedirs(d, exist_ok=True)
			# copy the file
			print("copying", f)
			shutil.copy(source_file, dest_file)
			
	else:
		# grab the dotfiles from home
		# ~/ => ./

		exclude = ["bin/shorten"]

		for dest_file in uniglob(os.getcwd()):
			source_file = os.path.expanduser(os.path.join("~", dest_file))
			f = os.path.join(os.getcwd(), dest_file)

			# filter out excluded paths
			if dest_file in exclude: continue

			# source_file = ~/...
			# dest_file = ./...

			# if the file doesn't exist in home, skip it
			if not os.path.isfile(source_file):
				continue
			# copy the file
			print("copying", f)
			shutil.copy(source_file, dest_file)

if True:
	# the actual script

	# check for the grab flag
	# this will copy the stuff in home to the repo instead of
	# copying the stuff from the repo to home
	if "--grab" in sys.argv or "-g" in sys.argv:
		grab = True
	else:
		grab = False

	# confirmation
	while True:
		if not grab: print("Are you sure you want to INSTALL the dotfiles (yes/no) ", end="")
		else: print("Are you sure you want to UPDATE the repo with your dotfiles? (yes/no) ", end="")

		a = input().lower()
		if a == "no": exit(0)
		elif a == "yes": break

	if not grab:
		# compile and move the shortener
		shorten_dir = "home/bin/shortener"
		shorten_cmd = "./build.sh"
		shorten_path= "home/bin/shortener/shorten"
		shorten_dest= "home/bin/shorten"
		t = os.getcwd()

		print(">>> cd", shorten_dir)
		os.chdir(shorten_dir)

		print(">>>", shorten_cmd)
		os.system(shorten_cmd)

		os.chdir(t)

		shutil.copyfile(shorten_path, shorten_dest)


	# move the files now

	universal_home = "home"
	linux_home = "linux"
	macos_home = "macos"

	# install the universal dotfiles
	t = os.getcwd()
	os.chdir(universal_home)
	install(grab)
	os.chdir(t)

	if platform.system() == "Linux":
		# install the linux dotfiles
		t = os.getcwd()
		os.chdir(linux_home)
		install(grab)
		os.chdir(t)

	elif platform.system() == "Darwin":
		# install the macos dotfiles
		t = os.getcwd()
		os.chdir(macos_home)
		install(grab)
		os.chdir(t)