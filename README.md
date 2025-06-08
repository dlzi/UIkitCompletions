# UIkit Completions for Sublime Text

A lightweight auto-completion plugin for the UIkit CSS framework in Sublime Text 4, providing context-aware class, attribute, and component snippet suggestions. This plugin is a fork of the original uikit/uikit-sublime by YOOtheme GmbH.

## Features

- **Context-Aware Completions**: Suggests UIkit classes inside `class` attributes, `uk-` attributes in HTML tags, and component snippets via autocomplete within `<body>` or `<template>` contexts.
- **Component Snippets**: Insert common UIkit components (e.g., Grid Layout, Navigation Bar, Modal Dialog, Slider, Card) via `.sublime-snippet` files with tab-stops and placeholders, triggerable via autocomplete (inside `<body>` or `<template>`) or the Command Palette.
- **Dynamic Snippet Loading**: Automatically loads snippets from the `snippets/` directory, supporting both development and Package Control installations.
- **Multi-File Support**: Completions and snippets work in HTML, Vue, Twig, and PHP files.

## Installation

### Package Control (Recommended)
1. Install [Package Control](https://packagecontrol.io/installation) if not already installed.
2. Open the **Command Palette** (`Ctrl+Shift+P` or `Cmd+Shift+P`) and select **Package Control: Install Package**.
3. Search for `UIkitCompletions` and install it.
4. Generate the completions database (see **Setup** below).

*Note*: The plugin requires Sublime Text 4 (Python 3.8).

### Manual Installation
1. Download or clone this repository to a folder named `UIkitCompletions`.
2. Place the `UIkitCompletions` folder in your Sublime Text `Packages` directory:
   - Linux: `~/.config/sublime-text/Packages/`
   - macOS: `~/Library/Application Support/Sublime Text/Packages/`
   - Windows: `%APPDATA%\Sublime Text\Packages\`
   - Custom: Any directory, e.g., `/home/daniel/Public/UIkitCompletions`
3. Generate the completions database (see **Setup** below).
4. Restart Sublime Text.

*Note*: The plugin requires Sublime Text 4 (Python 3.8).

## Usage

### Class Completions
Inside `class` attributes in supported file types, the plugin suggests UIkit classes:
```html
<div class="uk-grid uk-child-width-1-3">
    <div class="uk-card uk-card-default">
        <!-- Content -->
    </div>
</div>
```

### Attribute Completions
In HTML tags in supported file types, the plugin suggests UIkit `uk-` attributes:
```html
<div uk-grid uk-sticky="offset: 80">
    <div>
        <!-- Content -->
    </div>
</div>
```

### Component Snippets
Insert UIkit components in two ways:
1. **Autocomplete**: In `<body>` or `<html>` contexts of supported file types, type the snippet’s trigger (e.g., `uikit-card`) and select it from the autocomplete dropdown. Press `Tab` to navigate editable fields. Snippets won’t trigger in inappropriate contexts like `<head>` or attribute values.
2. **Command Palette**: Use `Ctrl+Shift+P` (or `Cmd+Shift+P`) and select **UIkit: Insert Component** to choose from available snippets:
   - **Grid Layout**: A responsive grid with child width classes.
   - **Navigation Bar**: A navbar with navigation items.
   - **Modal Dialog**: A modal with a title and content.
   - **Slider**: A slider with navigation controls.
   - **Card**: A card component with title and content.

Snippets are stored as `.sublime-snippet` files in the `snippets/` directory, supporting tab-stops (e.g., `${1:Card Title}`) for quick navigation and placeholders for default content.

Example (Card Snippet via autocomplete):
```html
<body>
    <!-- Type "uikit-card" and select from autocomplete -->
    <div class="uk-card uk-card-default uk-card-body">
        <h3 class="uk-card-title">Card Title</h3>
        <p>Card content</p>
    </div>
</body>
```

To add custom snippets:
1. Create a new `.sublime-snippet` file in the `snippets/` directory (e.g., `UIkitCompletions/snippets/uikit-custom.sublime-snippet`).
2. Follow the format:
   ```xml
   <snippet>
       <content><![CDATA[
   <div class="uk-custom-component">
       ${1:Custom content}
   </div>
   ]]></content>
       <tabTrigger>uikit-custom</tabTrigger>
       <scope>text.html, text.html.vue, text.html.twig, text.html.php</scope>
       <description>UIkit Custom Component</description>
   </snippet>
   ```
3. Restart Sublime Text or reload the plugin (see **Troubleshooting**).

## Commands

Access via the **Command Palette**:
- **UIkit: Insert Component**: Insert a UIkit component snippet.

## Configuration

Customize settings via **Preferences -> Package Settings -> UIkitCompletions -> Settings**:
```json
{
    "uikit_css_path": "",
    "uikit_js_path": "",
    "supported_scopes": [
        "text.html",
        "text.html.vue",
        "text.html.twig",
        "text.html.php"
    ]
}
```

- **`uikit_css_path`**: Path to the UIkit CSS file (optional, for manual updates).
- **`uikit_js_path`**: Path to the UIkit JavaScript file (optional, for manual updates).
- **`supported_scopes`**: List of Sublime Text scope selectors for supported file types (e.g., `text.html.vue` for `.vue` files).

## Supported File Types
- `.html`, `.htm`
- `.vue` (Vue.js components)
- `.twig` (Twig templates)
- `.php` (PHP files with HTML content)

## Updating Completions

To update the completions database:
1. Run the update script with your UIkit CSS and JS files:
   ```bash
   python _update_completions.py path/to/uikit.min.css path/to/uikit.min.js
   ```
2. Restart Sublime Text to reload the plugin.

## Examples

### Grid System
```html
<div class="uk-grid-small uk-child-width-1-2@s uk-child-width-1-3@m" uk-grid>
    <div>
        <div class="uk-card uk-card-default uk-card-body">
            <h3 class="uk-card-title">Card 1</h3>
        </div>
    </div>
    <div>
        <div class="uk-card uk-card-primary uk-card-body">
            <h3 class="uk-card-title">Card 2</h3>
        </div>
    </div>
</div>
```

### Navigation
```html
<nav class="uk-navbar-container" uk-navbar>
    <div class="uk-navbar-left">
        <ul class="uk-navbar-nav">
            <li class="uk-active"><a href="#">Active</a></li>
            <li><a href="#">Item</a></li>
        </ul>
    </div>
</nav>
```

### Modal
```html
<div id="modal" class="uk-flex-top" uk-modal>
    <div class="uk-modal-dialog uk-modal-body uk-margin-auto-vertical">
        <button class="uk-modal-close-default" type="button" uk-close></button>
        <h2 class="uk-modal-title">Headline</h2>
        <p>Content goes here</p>
    </div>
</div>
```

### Card
```html
<div class="uk-card uk-card-default uk-card-body">
    <h3 class="uk-card-title">Card Title</h3>
    <p>Card content</p>
</div>
```

## Troubleshooting

### Completions Not Showing
1. Ensure you're in a supported file type (`.html`, `.vue`, `.twig`, `.php`).
2. Check the context:
   - Class completions: Inside `class=""`.
   - Attribute completions: Inside a tag, e.g., `<div uk-`.
   - Snippet completions: Inside `<body>` or `<html>` (not in `<head>` or attribute values).
3. Open the console (`Ctrl+``) and reload the plugin:
   ```python
   import sublime_plugin; sublime_plugin.reload_plugin("UIkitCompletions.uikit_completions")
   ```
   Check for errors.


## Contributing

Contributions are welcome! To contribute:
1. Clone the repository or download the source.
2. Modify the Python files or add new `.sublime-snippet` files in the `snippets/` directory.
3. Test changes in Sublime Text 4.
4. Submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Forked from uikit/uikit-sublime by YOOtheme GmbH, licensed under the MIT License.
- [UIkit Framework](https://getuikit.com/) for the CSS framework.
- [Sublime Text](https://www.sublimetext.com/) for the text editor.
- The Sublime Text community for plugin development resources.

## Version History

### v1.2.0
- Added autocomplete support for component snippets using their `tabTrigger` (e.g., `uikit-card`), restricted to `<body>` or `<html>` contexts.
- Fixed class and attribute completions to ensure they trigger correctly in their respective contexts.
- Updated plugin to use Python 3.8 features (e.g., f-strings) for Sublime Text 4 compatibility.
- Refactored component snippets to use `.sublime-snippet` files for better maintainability.
- Added dynamic snippet loading to support custom paths and Package Control installations.
- Added Card component snippet.
- Added support for `.vue`, `.twig`, and `.php` file types via configurable `supported_scopes`.
- Improved documentation for snippet usage and customization.

### v1.1.0
- Refactored component snippets to use `.sublime-snippet` files.
- Added dynamic snippet loading for custom paths and Package Control.
- Added Card component snippet.
- Added support for `.vue`, `.twig`, and `.php` file types.
- Improved documentation.

### v1.0.0
- Initial release with:
  - Class and attribute completions for HTML files.
  - Component snippets (Grid Layout, Navigation Bar, Modal Dialog, Slider).
  - Local file parsing for completions.
  - Settings integration.