from setuptools import setup, find_namespace_packages


setup(
	name="weatherapp.sinoptik",
	version="0.1.0",
	author="Marina Popryzhuk",
	description="SinoptikWeather provider",
	packages=find_namespace_packages(),
	entry_points={
	    '': '',
	},
	install_requires=[
	   'requests',
	   'bs4',
	]
)
