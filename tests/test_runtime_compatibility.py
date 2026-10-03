"""Run inside Sublime Text using Vintageous's test runner."""
import importlib

import sublime
import sublime_plugin

from Vintageous.state import _init_vintageous
from Vintageous.tests import ViewTest


class TestModernPluginHost(ViewTest):
    def test_logger_is_available_without_package_root_exports(self):
        # Package Control strips the root __init__.py from installed archives.
        from Vintageous import state
        from Vintageous.vi import plugin_logging
        self.assertIs(state.PluginLogger, plugin_logging.PluginLogger)
        self.assertEqual(plugin_logging.PluginLogger.__module__,
                         'Vintageous.vi.plugin_logging')

    def test_private_commands_are_registered_with_their_original_names(self):
        registered = (sublime_plugin.text_command_classes +
                      sublime_plugin.window_command_classes)
        for module_name in ('xactions', 'xmotions', 'xsupport',
                            'ex_motions', 'jump_list_cmds', 'test_runner'):
            module = importlib.import_module('Vintageous.' + module_name)
            for name, cls in vars(module).items():
                if (name.startswith('_') and isinstance(cls, type) and
                        issubclass(cls, (sublime_plugin.TextCommand,
                                        sublime_plugin.WindowCommand))):
                    with self.subTest(command=name):
                        self.assertIn(cls, registered)
                        target = (self.view if issubclass(cls, sublime_plugin.TextCommand)
                                  else self.view.window())
                        self.assertEqual(cls(target).name(), name)

    def test_normal_mode_word_delete_and_end_of_line(self):
        self.write('alpha beta\ngamma delta\n')
        self.clear_sel()
        self.add_sel(0)
        _init_vintageous(self.view)
        self.assertTrue(self.view.settings().get('command_mode'))
        window = self.view.window()
        window.run_command('press_key', {'key': 'w'})
        self.assertEqual(self.first_sel().b, 6)
        window.run_command('press_key', {'key': 'x'})
        self.assertEqual(self.get_all_text(), 'alpha eta\ngamma delta\n')
        window.run_command('press_key', {'key': 'g'})
        window.run_command('press_key', {'key': '_'})
        self.assertEqual(self.first_sel().b, 8)
