from pathlib import Path
from setuptools import setup


readme = (Path(__file__).parent / 'README.rst').read_text()


setup(
    name='etap2pcap',
    version='0.0.1',
    description='Tibbo Ethernet Tap pcap logger',
    long_description=readme,
    long_description_content_type='text/x-rst',
    url='https://github.com/bnozokopic/etap2pcap',
    packages=['etap2pcap'],
    license='GPLv3',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
    entry_points={'console_scripts': ['etap2pcap = etap2pcap.main:main']})
