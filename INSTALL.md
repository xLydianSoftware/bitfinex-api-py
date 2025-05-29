# Installation Guide

This project now uses `pyproject.toml` for configuration instead of the legacy `setup.py`.

## Development Setup

### Installing Dependencies

For regular dependencies:

```bash
pip install -e .
```

For development dependencies (includes linting, formatting, and type checking tools):

```bash
pip install -e ".[dev]"
```

For type checking support:

```bash
pip install -e ".[typing]"
```

### Building the Package

To build the package:

```bash
python -m build
```

This will create both wheel and source distributions in the `dist/` directory.

### Development Tools

The project includes several development tools configured in `pyproject.toml`:

- **Black**: Code formatting
- **isort**: Import sorting  
- **Flake8**: Linting
- **mypy**: Type checking
- **pre-commit**: Git hooks

Run these tools individually:

```bash
black .
isort .
flake8 .
mypy bfxapi
```

### Publishing

To publish to PyPI:

```bash
python -m build
twine upload dist/*
```

## Migration Notes

The following files have been removed as they are no longer needed:

- `setup.py` - Replaced by `pyproject.toml`
- `requirements.txt` - Dependencies now in `pyproject.toml`
- `dev-requirements.txt` - Development dependencies now in `pyproject.toml`

All package metadata, dependencies, and build configuration is now centralized in `pyproject.toml`.
