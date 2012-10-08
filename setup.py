import os
from setuptools import setup, find_packages
from setuptools.dist import Distribution
import pkg_resources
import taggit_live

add_django_dependency = True
# See issues #50, #57 and #58 for why this is necessary
try:
    pkg_resources.get_distribution('Django')
    add_django_dependency = False
except pkg_resources.DistributionNotFound:
    try:
        import django
        if django.VERSION[0] >= 1 and django.VERSION[1] >= 2 and django.VERSION[2] >= 0:
            add_django_dependency = False
    except ImportError:
        pass

Distribution({
    "setup_requires": add_django_dependency and  ['Django >=1.4.0'] or []
})

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
        'Django >=1.4.0',
        'django-taggit'
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    package_data = {
        '': ['*.css', '*.js', '*.gif', '*.png',],
    },
)


