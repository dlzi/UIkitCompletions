# Changelog

All notable changes to UIkitCompletions will be documented in this file.

## [2.2.0] - 14/08/2025

### Added
- 

### Changed
- Bumped package version to **2.2.0** to exceed version `2.0.1` of the abandoned UIkit Autocomplete package for compatibility and version resolution purposes.
- Updated the classes and attributes.

### Fixed
- 

## [1.2.0] - 14/05/2025

### Added
- Added autocomplete support for component snippets using their `tabTrigger` (e.g., `uikit-card`), restricted to `<body>` or `<html>` contexts.
- Added dynamic snippet loading to support custom paths and Package Control installations.
- Added Card component snippet.
- Added support for `.vue`, `.twig`, and `.php` file types via configurable `supported_scopes`.

### Changed
- Updated plugin to use Python 3.8 features (e.g., f-strings) for Sublime Text 4 compatibility.
- Refactored component snippets to use `.sublime-snippet` files for better maintainability.
- Improved documentation for snippet usage and customization.

### Fixed
- Fixed class and attribute completions to ensure they trigger correctly in their respective contexts.

## [1.1.0] - 25/03/2025

### Added
  - Added dynamic snippet loading for custom paths and Package Control.
  - Added Card component snippet.
  - Added support for `.vue`, `.twig`, and `.php` file types.

### Changed
- Refactored component snippets to use `.sublime-snippet` files.
- Improved documentation.

### Fixed
- N/A

## [1.0.0] - 10/03/2025

### Added
  - Class and attribute completions for HTML files.
  - Component snippets (Grid Layout, Navigation Bar, Modal Dialog, Slider).
  - Local file parsing for completions.
  - Settings integration.

### Changed
- N/A (initial release)

### Fixed
- N/A (initial release)