import sublime
import sublime_plugin


class _vi_cmd_line_a(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.sel().clear()
        self.view.sel().add(sublime.Region(1))


class _vi_cmd_line_k(sublime_plugin.TextCommand):
    def run(self, edit):
        text = self.view.substr(sublime.Region(0, self.view.sel()[0].b))
        self.view.replace(edit, sublime.Region(0, self.view.size()), text)
        self.view.sel().clear()
        self.view.sel().add(sublime.Region(self.view.size()))


# Sublime Text's modern plugin host skips private names unless exported.
__all__ = [
    '_vi_cmd_line_a',
    '_vi_cmd_line_k',
]
