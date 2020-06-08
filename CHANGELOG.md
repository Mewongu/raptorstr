# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
## [0.2.0] - 2020-06-08
### Added
- Checks for valid characters to begin with in tokenization
### Fixed
- License classifier was not consistent with file tokens
- Long description in setup.py


## [0.1.0] - 2020-05-29
### Added
- [Readme](./README.md)
- [LICENSE](./LICENSE)
- [noxfile.py](./noxfile.py) for ease of development
- [setup.cfg](./setup.cfg) for ease of development
- This changelog
- Tests for tokenization
- Tests for conversion and checking if strings conform to `snake_case`, `camelCase`, `PascalCase` and `kebab-case`
- Conversion functions to `snake_case`, `camelCase`, `PascalCase` and `kebab-case`
- Validation functions for checking if a string is `snake_case`, `camelCase`, `PascalCase` or `kebab-case`
- [pre-commit-config.yaml](./.pre-commit-config.yaml) for further ease of development
