"""Setup for MTG-Pack-Generator."""
import setuptools

setuptools.setup(
    name="MTG-Pack-Generator",
    version="0.0",
    url="https://github.com/DanielPDWalker/MTG-Pack-Generator",

    author="DaniePDWalker",

    description="Python script to generate MTG booster packs.",

    packages=setuptools.find_packages(exclude=["*.tests",
                                               "*.tests.*",
                                               "tests.*",
                                               "test*"]),

    license='MIT',

    install_requires=[
            'requests',
            'mtgsdk'],

    classifiers=[
        'Programming Language :: Python :: 3.6'
    ],
)
