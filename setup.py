from distutils.core import setup

setup(
    name="bitfinex-api-py",
    version="3.0.7",
    description="Official Bitfinex Python API",
    long_description=(
        "A Python reference implementation of the Bitfinex API "
        "for both REST and websocket interaction."
    ),
    long_description_content_type="text/markdown",
    url="https://github.com/xLydianSoftware/bitfinex-api-py",
    author="Yuriy Arabsky",
    author_email="yuriy.arabsky@xlydian.com",
    license="Apache-2.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    keywords="bitfinex,api,trading",
    project_urls={},
    packages=[
        "bfxapi",
        "bfxapi._utils",
        "bfxapi.types",
        "bfxapi.websocket",
        "bfxapi.websocket._client",
        "bfxapi.websocket._handlers",
        "bfxapi.websocket._event_emitter",
        "bfxapi.rest",
        "bfxapi.rest._interface",
        "bfxapi.rest._interfaces",
    ],
    install_requires=[
        "pyee~=11.1.0",
        "websockets>=13.0",
        "requests>=2.32.3",
    ],
    extras_require={
        "typing": [
            "types-requests~=2.32.0.20241016",
        ]
    },
    python_requires=">=3.8",
    package_data={"bfxapi": ["py.typed"]},
)
