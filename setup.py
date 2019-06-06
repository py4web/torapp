from setuptools import setup


setup(
    name="testtorapp",
    version="0.1.0",
    description="tornado example",
    long_description="tornado torapp example",
    author="huashengduncn",
    author_email="huashengduncn@gmail.com",
    url="https://github.com/py4web/torapp/",
    packages=['torapp'],
    license='MIT',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'tornado>=4.5.0',
    ],
)
