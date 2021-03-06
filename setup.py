import ast
from typing import Optional
from setuptools import setup, find_packages


def get_version(file_name: str, version_name: str = "__version__") -> Optional[str]:
    with open(file_name) as f:
        tree = ast.parse(f.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                if node.targets[0].id == version_name:
                    return node.value.s
    raise ValueError(f"Couldn't find assignment to variable {version_name} in file {file_name}")


class About(object):
    NAME = "unicode-write"
    VERSION = get_version("unicode_write/__init__.py")
    AUTHOR = "blester125"
    EMAIL = f"{AUTHOR}@gmail.com"
    URL = f"https://github.com/{AUTHOR}/{NAME}"
    DL_URL = f"{URL}/archive/{VERSION}.tar.gz"
    LICENSE = "MIT"
    DESCRIPTION = "Unicode Write"


ext_modules = []


setup(
    name=About.NAME,
    version=About.VERSION,
    description=About.DESCRIPTION,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author=About.AUTHOR,
    author_email=About.EMAIL,
    url=About.URL,
    download_url=About.DL_URL,
    license=About.LICENSE,
    python_requires=">=3.6",
    packages=find_packages(),
    package_data={"unicode_write": ["unicode_write/data/emoji.json"],},
    include_package_data=True,
    install_requires=["prompt_toolkit", "file_or_name", "pyperclip", "string_distance", "inverted-index"],
    extras_require={"test": ["pytest"], "remote": ["flask", "requests"]},
    keywords=[],
    ext_modules=ext_modules,
    entry_points={
        "console_scripts": ["unicode-lookup = unicode_write.driver:main", "ucl = unicode_write.driver:main", "unicode-lookup-remote = unicode_write.client:main"],
    },
    classifiers={
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering",
    },
)
