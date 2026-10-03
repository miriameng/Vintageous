"""Adds jump list functionality.

   Wraps Sublime Text's own jump list.
"""


import sublime
import sublime_plugin

class _vi_add_to_jump_list(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        if view is not None:
            view.run_command('add_jump_record', {
                'selection': [[region.a, region.b] for region in view.sel()]
            })


# Sublime Text's modern plugin host skips private names unless exported.
__all__ = [
    '_vi_add_to_jump_list',
]
