from setuptools import setup

setup(
    name='lib_Partage_BSS',
    version='0.3.1',
    packages=['doc', 'venv.lib.python3.5.distutils', 'venv.lib.python3.5.encodings', 'venv.lib.python3.5.importlib',
              'venv.lib.python3.5.collections', 'venv.lib.python3.5.site-packages.py',
              'venv.lib.python3.5.site-packages.py._io', 'venv.lib.python3.5.site-packages.py._log',
              'venv.lib.python3.5.site-packages.py._code', 'venv.lib.python3.5.site-packages.py._path',
              'venv.lib.python3.5.site-packages.py._process', 'venv.lib.python3.5.site-packages.py._vendored_packages',
              'venv.lib.python3.5.site-packages.pip', 'venv.lib.python3.5.site-packages.pip.req',
              'venv.lib.python3.5.site-packages.pip.vcs', 'venv.lib.python3.5.site-packages.pip.utils',
              'venv.lib.python3.5.site-packages.pip.compat', 'venv.lib.python3.5.site-packages.pip.models',
              'venv.lib.python3.5.site-packages.pip._vendor', 'venv.lib.python3.5.site-packages.pip._vendor.distlib',
              'venv.lib.python3.5.site-packages.pip._vendor.distlib._backport',
              'venv.lib.python3.5.site-packages.pip._vendor.colorama',
              'venv.lib.python3.5.site-packages.pip._vendor.html5lib',
              'venv.lib.python3.5.site-packages.pip._vendor.html5lib._trie',
              'venv.lib.python3.5.site-packages.pip._vendor.html5lib.filters',
              'venv.lib.python3.5.site-packages.pip._vendor.html5lib.treewalkers',
              'venv.lib.python3.5.site-packages.pip._vendor.html5lib.treeadapters',
              'venv.lib.python3.5.site-packages.pip._vendor.html5lib.treebuilders',
              'venv.lib.python3.5.site-packages.pip._vendor.lockfile',
              'venv.lib.python3.5.site-packages.pip._vendor.progress',
              'venv.lib.python3.5.site-packages.pip._vendor.requests',
              'venv.lib.python3.5.site-packages.pip._vendor.requests.packages',
              'venv.lib.python3.5.site-packages.pip._vendor.requests.packages.chardet',
              'venv.lib.python3.5.site-packages.pip._vendor.requests.packages.urllib3',
              'venv.lib.python3.5.site-packages.pip._vendor.requests.packages.urllib3.util',
              'venv.lib.python3.5.site-packages.pip._vendor.requests.packages.urllib3.contrib',
              'venv.lib.python3.5.site-packages.pip._vendor.requests.packages.urllib3.packages',
              'venv.lib.python3.5.site-packages.pip._vendor.requests.packages.urllib3.packages.ssl_match_hostname',
              'venv.lib.python3.5.site-packages.pip._vendor.packaging',
              'venv.lib.python3.5.site-packages.pip._vendor.cachecontrol',
              'venv.lib.python3.5.site-packages.pip._vendor.cachecontrol.caches',
              'venv.lib.python3.5.site-packages.pip._vendor.webencodings',
              'venv.lib.python3.5.site-packages.pip._vendor.pkg_resources',
              'venv.lib.python3.5.site-packages.pip.commands', 'venv.lib.python3.5.site-packages.pip.operations',
              'venv.lib.python3.5.site-packages.attr', 'venv.lib.python3.5.site-packages.idna',
              'venv.lib.python3.5.site-packages.wheel', 'venv.lib.python3.5.site-packages.wheel.tool',
              'venv.lib.python3.5.site-packages.wheel.signatures', 'venv.lib.python3.5.site-packages.pluggy',
              'venv.lib.python3.5.site-packages._pytest', 'venv.lib.python3.5.site-packages._pytest._code',
              'venv.lib.python3.5.site-packages._pytest.assertion', 'venv.lib.python3.5.site-packages.certifi',
              'venv.lib.python3.5.site-packages.chardet', 'venv.lib.python3.5.site-packages.chardet.cli',
              'venv.lib.python3.5.site-packages.urllib3', 'venv.lib.python3.5.site-packages.urllib3.util',
              'venv.lib.python3.5.site-packages.urllib3.contrib',
              'venv.lib.python3.5.site-packages.urllib3.contrib._securetransport',
              'venv.lib.python3.5.site-packages.urllib3.packages',
              'venv.lib.python3.5.site-packages.urllib3.packages.backports',
              'venv.lib.python3.5.site-packages.urllib3.packages.ssl_match_hostname',
              'venv.lib.python3.5.site-packages.xmljson', 'venv.lib.python3.5.site-packages.requests',
              'venv.lib.python3.5.site-packages.setuptools', 'venv.lib.python3.5.site-packages.setuptools.extern',
              'venv.lib.python3.5.site-packages.setuptools.command', 'venv.lib.python3.5.site-packages.pkg_resources',
              'venv.lib.python3.5.site-packages.pkg_resources.extern',
              'venv.lib.python3.5.site-packages.pkg_resources._vendor',
              'venv.lib.python3.5.site-packages.pkg_resources._vendor.packaging', 'test_unitaire',
              'test_unitaire.lib_Partage_BSS', 'test_unitaire.lib_Partage_BSS.utils', 'lib_Partage_BSS',
              'lib_Partage_BSS.utils', 'lib_Partage_BSS.exceptions', 'test_integration',
              'test_integration.lib_Partage_BSS', 'test_integration.lib_Partage_BSS.utils'],
    url='https://gitlab.univ-rennes1.fr/57NUM/libPythonBssApi',
    license='',
    author='rpeillet',
    author_email='',
    description='Bibliothèque permettant l\'intégoration de l\'API BSS PAratage de RENATER',
    install_requires=['xmljson', 'requests']
)
