import sublime
import sublime_plugin
import os
import re
from .completion_db import CLASSES, ATTRIBUTES

class UIkitCompletions(sublime_plugin.EventListener):
    def __init__(self):
        self.class_completions = [("%s \tUIkit Class" % s, s) for s in CLASSES]
        self.attr_completions = [("%s \tUIkit Attribute" % s, s) for s in ATTRIBUTES]
        self.snippet_completions = []
        self._load_snippet_completions()

    def _load_snippet_completions(self):
        """Load snippet completions from the snippets/ directory or .sublime-package."""
        package_name = "UIkitCompletions"
        snippets_rel_path = "snippets"
        self.snippet_completions = []

        # Try unzipped package
        packages_path = sublime.packages_path()
        package_dir = os.path.join(packages_path, package_name, snippets_rel_path)

        if os.path.exists(package_dir):
            for file_name in os.listdir(package_dir):
                if file_name.endswith(".sublime-snippet"):
                    file_path = os.path.join(package_dir, file_name)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            trigger = self._extract_trigger(content)
                            description = self._extract_description(content)
                            snippet_content = self._extract_snippet_content(content)
                            if trigger and description and snippet_content:
                                self.snippet_completions.append((
                                    f"{trigger}\tUIkit Snippet: {description}",
                                    snippet_content
                                ))
                    except Exception as e:
                        sublime.error_message(f"Error reading snippet {file_name}: {e}")
        else:
            # Try zipped package
            package_file = os.path.join(sublime.installed_packages_path(), package_name + ".sublime-package")
            if os.path.exists(package_file):
                try:
                    for resource in sublime.find_resources("*.sublime-snippet"):
                        if resource.startswith(f"Packages/{package_name}/{snippets_rel_path}"):
                            content = sublime.load_resource(resource)
                            trigger = self._extract_trigger(content)
                            description = self._extract_description(content)
                            snippet_content = self._extract_snippet_content(content)
                            if trigger and description and snippet_content:
                                self.snippet_completions.append((
                                    f"{trigger}\tUIkit Snippet: {description}",
                                    snippet_content
                                ))
                except Exception as e:
                    sublime.error_message(f"Error loading snippets from {package_file}: {e}")

    def _extract_trigger(self, content):
        """Extract the tabTrigger from a .sublime-snippet file."""
        match = re.search(r'<tabTrigger>(.*?)</tabTrigger>', content, re.DOTALL)
        return match.group(1).strip() if match else None

    def _extract_description(self, content):
        """Extract the description from a .sublime-snippet file."""
        match = re.search(r'<description>(.*?)</description>', content, re.DOTALL)
        return match.group(1).strip() if match else None

    def _extract_snippet_content(self, content):
        """Extract the snippet content from a .sublime-snippet file."""
        match = re.search(r'<content><!\[CDATA\[(.*?)\]\]></content>', content, re.DOTALL)
        return match.group(1).strip() if match else None

    def on_query_completions(self, view, prefix, locations):
        # Load supported scopes from settings
        settings = sublime.load_settings("UIkitCompletions.sublime-settings")
        supported_scopes = settings.get("supported_scopes", ["text.html"])

        current_scope = view.scope_name(locations[0])
        # Check if the current scope matches any supported scope
        if not any(scope in current_scope for scope in supported_scopes):
            return []

        # Class completions for class attributes
        if "meta.attribute-with-value.class.html" in current_scope:
            return self.class_completions

        # Attribute completions within tags, excluding quoted strings
        if "meta.tag" in current_scope and "string.quoted" not in current_scope:
            return self.attr_completions

        # Snippet completions only within <body> or <html> contexts
        valid_snippet_scopes = [
            "meta.tag.body.html",  # Inside <body>
            "meta.tag.html",       # Inside <html>, but not in <head>
            "meta.tag.body.vue",   # Vue equivalent
            "meta.tag.html.vue",
            "meta.tag.body.twig",  # Twig equivalent
            "meta.tag.html.twig",
            "meta.tag.body.php",   # PHP equivalent
            "meta.tag.html.php"
        ]
        if settings.get("enable_snippet_completions", True) and \
           any(scope in current_scope for scope in valid_snippet_scopes) and \
           "meta.tag.head" not in current_scope:
            return self.snippet_completions

        return []

class UikitInsertComponentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        package_name = "UIkitCompletions"
        snippets_rel_path = "snippets"
        self.snippets = []
        self.snippet_contents = []

        packages_path = sublime.packages_path()
        package_dir = os.path.join(packages_path, package_name, snippets_rel_path)

        if os.path.exists(package_dir):
            for file_name in os.listdir(package_dir):
                if file_name.endswith(".sublime-snippet"):
                    file_path = os.path.join(package_dir, file_name)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            description = self._extract_description(content)
                            if description:
                                self.snippets.append(description)
                                self.snippet_contents.append(self._extract_snippet_content(content))
                    except Exception as e:
                        sublime.error_message(f"Error reading snippet {file_name}: {e}")
        else:
            package_file = os.path.join(sublime.installed_packages_path(), package_name + ".sublime-package")
            if os.path.exists(package_file):
                try:
                    for resource in sublime.find_resources("*.sublime-snippet"):
                        if resource.startswith(f"Packages/{package_name}/{snippets_rel_path}"):
                            content = sublime.load_resource(resource)
                            description = self._extract_description(content)
                            if description:
                                self.snippets.append(description)
                                self.snippet_contents.append(self._extract_snippet_content(content))
                except Exception as e:
                    sublime.error_message(f"Error loading snippets from {package_file}: {e}")

        if not self.snippets:
            sublime.error_message(f"No UIkit snippets found in {package_name}")
            return

        self.edit = edit
        self.view.window().show_quick_panel(self.snippets, self.on_select)

    def _extract_description(self, content):
        match = re.search(r'<description>(.*?)</description>', content, re.DOTALL)
        return match.group(1).strip() if match else None

    def _extract_snippet_content(self, content):
        match = re.search(r'<content><!\[CDATA\[(.*?)\]\]></content>', content, re.DOTALL)
        return match.group(1).strip() if match else None

    def on_select(self, index):
        if index == -1:
            return

        snippet_content = self.snippet_contents[index]
        if snippet_content:
            try:
                self.view.run_command("insert_snippet", {"contents": snippet_content})
            except Exception as e:
                sublime.error_message(f"Error inserting snippet: {e}")
        else:
            sublime.error_message("Invalid snippet content")