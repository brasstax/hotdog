# -*- coding: utf8 -*-

from setuptools import setup, find_packages
    
setup(
    # Basic info
    name='hotdog',
    version=1.0,
    author='Brass Tax',
    author_email='brasstax@noreply.users.github.com',
    url='https://github.com/brasstax/hotdog',
    description='Hotdog.',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],

    install_requires=[
        'discord.py',
    ],
    entry_points={
        'console_scripts': [
            'discord-hotdog = hotdog.__main__:main'],
    },

    zip_safe=False,
    platforms='any',
    license='WTFPL',
    packages=['hotdog'],
    include_package_data=True
)

