from setuptools import setup

setup(name='govai',
      version='0.0.0',
      description='ML Library',
      url='http://github.com/INF800/govai',
      author='Asapanna Rakesh',
      author_email='rakeshark22@gmail.com',
      license='Apache v2',
      packages=['govai'],
      zip_safe=False,
      install_requires=['omegaconf>=2.1.1',
                        'scikit-learn==1.0.1',
                        'pandas==1.3.4'])