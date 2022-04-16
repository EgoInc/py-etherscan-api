import setuptools

setuptools.setup(
    name='py_etherscan_api',
    version='0.9.1',
    packages=['examples', 'examples.stats', 'examples.tokens',
              'examples.accounts', 'examples.blocks', 'examples.transactions',  'etherscan'],
    url='https://github.com/EgoInc/py-etherscan-api',
    license='MIT',
    author='coreypetty',
    author_email='sex.btc@gmail.com',
    description='Python Bindings to Etherscan.io API',
    install_requires=[
        'requests>=2.20.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)
