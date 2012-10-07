import os
from setuptools import setup, find_packages
from setuptools.dist import Distribution
import pkg_resources
import taggit_live

def install_data_recursive(relative_dirname,result_list = {}):
    for infile in os.listdir(relative_dirname):
        if  os.path.isdir('%s/%s' % (relative_dirname, infile)):
            install_data_recursive(u'%s/%s' % (relative_dirname, infile),result_list)
        else:
            if relative_dirname in result_list:
                result_list[relative_dirname].append('%s/%s' % (relative_dirname, infile))
            else:
                result_list[relative_dirname] = ['%s/%s' % (relative_dirname, infile)]

def install_data(relative_dirname_list,data = {}):
    for relative_dirname in relative_dirname_list:
        install_data_recursive(relative_dirname,data)
    res = []
    for k,v in data.items():
        res.append((k,v))
    return res


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
    license='mit',
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
    data_files= install_data(['taggit_live/static_taggit_live',],
                             {}),
)


