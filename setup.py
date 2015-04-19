import os
from setuptools import find_packages, setup

execfile(os.path.join(os.path.dirname(__file__),
                      "sound_evolution", "release.py"))

setup(
    name="sound_evolution",
    packages=find_packages(),
    version=version,
    description=description,
    author=author,
    download_url=download_url,
    install_requires=[
        'nose',
        ],
    zip_safe=True,
    keywords=[
        ],
    classifiers=[
        ],
    )
