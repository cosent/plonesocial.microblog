from setuptools import setup, find_packages

version = '0.7.0.dev'

long_description = (
    open('README.rst').read()
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(
    name='plonesocial.microblog',
    version=version,
    description="Simple microblogging in Plone",
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Plone :: 4.2',
        'Framework :: Plone :: 4.3',
        'Framework :: Plone',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='plone socbiz social microblog',
    author='Guido Stevens',
    author_email='guido.stevens@cosent.net',
    url='http://github.com/cosent/plonesocial.microblog',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plonesocial'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Acquisition',
        'plone.app.layout',
        'plone.app.portlets',
        'plone.app.uuid',
        'plone.behavior',
        'plone.portlets',
        'plone.uuid',
        'plone.api',
        'plonesocial.activitystream',
        'plonesocial.core',
        'Products.CMFCore',
        'Products.CMFPlone >=4.2',
        'Products.GenericSetup',
        'requests',
        'setuptools',
        'zope.component',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.schema',
    ],
    extras_require={
        'test': [
            'ExtensionClass',
            'plone.app.testing',
            'plone.browserlayer',
            'unittest2',
        ],
    },
    entry_points="""
      # -*- Entry points: -*-
          [z3c.autoinclude.plugin]
          target = plone
      """,)
