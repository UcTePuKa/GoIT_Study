from setuptools import setup, find_namespace_packages

setup(
    name='sort',
    version='0.1',
    description='Sorter of trash from folder',
    url='',
    author='UcTePuKa',
    author_email='Vitalij.Ovechkin@gmail.com',
    license='™Forest®',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean_folder = clean_folder.main:start_scan']}
)