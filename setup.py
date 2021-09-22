from setuptools import setup
setup(
    name='social',
    packages=['social'],
    version='0.1',
    description='gidimo oauth2 Package',
    url='https://github.com/jemikalajah123/gidimo-Oauth2-Python-Package',
    download_url='https://github.com/jemikalajah123/gidimo-Oauth2-Python-Package/archive/v_01.tar.gz',
    author='philip jemikalajah',
    author_email='okeoghene.philip5@gmail.com',
    license='MIT',
    install_requires=[
        'urllib.parse',
        'social_core.backends.oauth',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    zip_safe=False
)