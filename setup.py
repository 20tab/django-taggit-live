import os
from setuptools import setup, find_packages
from setuptools.dist import Distribution
import pkg_resources
import taggit_live

setup(name='django-taggit-live',
      version=taggit_live.__version__,
      description="It's an autocomplete widget for django-taggit TagField",
      author='20tab srl: Raffaele Colace',
      author_email='info@20tab.com',
      url='https://github.com/20tab/django-taggit-live',
      license='Mit License',
      platforms=['OS Independent'],
      classifiers=[
          #'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          #'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries :: Application Frameworks',
      ],
      install_requires=[
          'Django >=1.6',
          'django-taggit'
      ],
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      package_data={
          '': ['*.css', '*.js', '*.gif', '*.png', ],
      },
)


