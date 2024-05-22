from setuptools import setup, find_packages
import version

setup(
    name='spicextract',
    version=version.__version__,
    packages=find_packages(include=['spicextract', 'spicextract.*']),
    include_package_data=True,
    package_data={
        '': ['../version.py'],
    },
    install_requires=[
        'requests',
        'urllib3',
    ],
    entry_points={
        'console_scripts': [
            'spicextract=spicextract.main:main',
        ],
    },
    author='lHumaNl',
    author_email='fisher_sam@mail.ru',
    description='Util for easy download SPICE file for Proxmox VMs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/lHumaNl/SpiceXtract',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Sound/Audio',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='spice proxmox vm downloader',
)
