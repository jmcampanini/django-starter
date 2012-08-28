import os

def string_to_bool(s, default=False):
	"""
	Turns a string into a bool, giving a default value preference.
	"""
	if len(str(s).strip()) == 0: return default

	if default:
		if s[0].upper() == "F": return False
		else: return True
	else:
		if s[0].upper() == "T": return True
		else: return False


def load_the_environment(env=None, verbose=False):
	"""
	Loads the environment files into the environment variables.
	"""
	if env is None: env = "dev"

	if env == "prod": env_file = ".env"
	else: env_file = ".env.%s" % env

	if os.path.exists(env_file):
		if verbose: print "Loading ENV File: `%s`" % env_file

		with open(env_file, "r+") as f:
			for curline in f:
				clean_line = str(curline).strip()
				if len(clean_line) > 0 and clean_line[0] != "#":
					eqloc = curline.index("=")
					var = str(curline[:eqloc]).strip()
					val = str(curline[eqloc + 1:]).strip()

					if verbose: print "....Adding `%s` with value `%s`" % (var, val)
					os.environ[var] = val

	else:
		if verbose: print "Not Found - ENV File: `%s`" % env_file