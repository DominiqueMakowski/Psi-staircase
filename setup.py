from setuptools import setup, find_packages
import re

# ------------------
def find_version():
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format("__version__"), open('PsiStaircase/__init__.py').read())
    return result.group(1)
# ------------------

setup(
name = "PsiStaircase",
description = ("Psi adaptive staircase procedure for use in psychophysics."),
version = find_version(),
license = "Mozilla Public License Version 2.0",
author = "Nynke Niehof, James Cooke",
author_email = "",
maintainer = "Nynke Niehof, James Cooke",
maintainer_email = "",
packages = find_packages(),
package_data = {},
install_requires = [],
dependency_links=[],
long_description = open('README.md').read(),
keywords = "Psi-staircase",
url = "https://github.com/DominiqueMakowski/Psi-staircase/",
download_url = 'https://github.com/DominiqueMakowski/Psi-staircase/zipball/master',
test_suite='nose.collector',
tests_require=['nose'],
classifiers = [
	'Intended Audience :: Science/Research',
	'Intended Audience :: Developers',
	'Programming Language :: Python',
	'Topic :: Software Development',
	'Topic :: Scientific/Engineering',
	'Operating System :: Microsoft :: Windows',
	'Operating System :: Unix',
	'Operating System :: MacOS',
	'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.6']
)
