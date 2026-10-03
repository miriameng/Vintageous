"""Compatibility exports for source checkouts.

Package Control omits this file, so plugin modules import vi.plugin_logging
directly. Keep runtime initialization out of the package root.
"""
from .vi.plugin_logging import LogDir, NullPluginLogger, PluginLogger
