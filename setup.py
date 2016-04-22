from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

if __name__ == "__main__":
	setup(name='Progress bar',
		  version='0.1',
		  description='A python progress bar that writes to the same line on the console.',
		  long_description=readme(),
		  url='some github url (update this!)',
		  author="Sean D. O'Connor",
		  author_email='sdo51@uclive.ac.nz',
		  license='MIT',
		  packages=['progbar'],
		  install_requires=[],
		  dependency_links=[], 
		  zip_safe=False,
		  #packages=find_packages()
		  )