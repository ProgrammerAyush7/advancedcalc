from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='advancedcalc',
  version='0.0.1',
  description='An Advanved Calculator with Trignometry and Other Functions',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/programmerayush7/advancedcalc',  
  author='Programmer Ayush',
  author_email='programmerayush777@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='calculator', 
  packages=find_packages(),
  install_requires=[''] 
)
