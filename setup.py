from setuptools import setup

setup(
    name="ennui",
    version="0.1",
    author="Robert Grant",
    author_email="rgrant@enthought.com",
    description="An alternate command-line UI for enstaller (enpkg).",
    license="BSD",
    keywords="enpkg",
    url="https://github.com/bgrant/ennui",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
    py_modules=["ennui"],
    entry_points=dict(
        console_scripts=[
            "ennui = ennui:main"
        ]
    ),
    install_requires=[
        'enstaller >= 4.5.6',
        'sh >= 1.07',
        'docopt >= 0.5.0'
    ]
)
