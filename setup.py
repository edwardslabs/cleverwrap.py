from distutils.core import setup
ver = '0.2.3.5'
setup(
          name = 'cleverwrap',
          packages = ['cleverwrap'],
          license = 'MIT',
          install_requires = ['requests'],
          version = ver,
          description = 'A wrapper for the official cleverbot.com API',
          author = 'Andrew Edwards',
          author_email = 'andrewthomasedwards@gmail.com',
          url = 'https://github.com/edwardslabs/cleverwrap.py',
          download_url = 'https://github.com/edwardslabs/cleverwrap.py/tarball/{}'.format(ver),
          keywords = ['cleverbot', 'wrapper', 'clever'],
          classifiers =[
              'Programming Language :: Python :: 3 :: Only',
              'License :: OSI Approved :: MIT License',
              'Intended Audience :: Developers',
              'Natural Language :: English',
          ],
)
