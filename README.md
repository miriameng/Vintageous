[![Build Status](https://travis-ci.org/guillermooo/Vintageous.svg?branch=master)](https://travis-ci.org/guillermooo/Vintageous) [![Build status](https://ci.appveyor.com/api/projects/status/pvea8jg8bdoq2rmn/branch/master)](https://ci.appveyor.com/project/guillermooo/vintageous/branch/master)

## Vintageous

<a href='http://www.pledgie.com/campaigns/19122'><img alt='Click here to lend your support to: Vintageous and make a donation at www.pledgie.com !' src='http://www.pledgie.com/campaigns/19122.png?skin_name=chrome' border='0' /></a>


**Vintageous** is a comprehensive vi/Vim emulation layer for Sublime Text.

### Sublime Text 4215 / Python 3.14 fork

This fork targets Sublime Text 4205 and newer using `.python-version` set to
`3.14`. There is no need to re-enable the deprecated Python 3.3 host.
It explicitly exports Vintageous's private command classes for the modern
plugin loader and preserves the command name used by `g_`.
Logging lives in `vi/plugin_logging.py`, since Package Control removes the
root `__init__.py` when installing an archive.

To install and receive updates through Package Control:

1. Run **Package Control: Add Repository** and enter
   `https://github.com/miriameng/Vintageous/tree/master`.
2. Run **Package Control: Install Package** and select **Vintageous**.
3. Restart Sublime Text. Keep `Vintage` in `ignored_packages`.

Remove any manual `Packages/Vintageous` checkout before switching to this
method. When using this repository through Package Control, allow automatic
updates; `auto_upgrade_ignore` is only needed for the manual archive method
below.

Build an installable archive with a local Python 3 interpreter:

```sh
python bin/builder.py --release release
```

The result is `dist/Vintageous.sublime-package`. In Sublime, choose
**Preferences > Browse Packages**, go up one directory, and open
**Installed Packages**. Back up the existing Vintageous archive outside that
directory, replace it with the new archive, and restart Sublime. Keep `Vintage`
in `ignored_packages`, but remove `Vintageous` if it is listed there.
If Package Control manages Vintageous, add `Vintageous` to its
`auto_upgrade_ignore` setting so an upstream update cannot replace this fork.

Alternatively, place this checkout at `Packages/Vintageous` (the directory
name is required by the plugin's imports). Avoid keeping a second extracted
Vintageous copy elsewhere in Packages.

For development, the existing in-editor test runner includes
`tests/test_runtime_compatibility.py`, which checks command registration and
basic editing through `press_key`. Tests require Sublime's API; they cannot
run under a standalone Python interpreter.

The installation instructions below describe the original upstream release.

The original upstream Vintageous has been discontinued.

The successor to Vintageous is Sublime Six.

See you in Sublime Six.

https://github.com/guillermooo/Six

http://sublimesix.com/


### Installing

**Make sure that Vintage
is in the `ignored_packages` list
in your user preferences.**

You can install Vintageous in multiple ways:


##### Using Package Control

Search for 'Vintageous' and install.


##### Using a Pre-built Version

1. Download the [current build](https://bitbucket.org/guillermooo/vintageous/downloads/Vintageous.sublime-package)
2. Copy *Vintageous.sublime-package* to the *Installed Packages* folder located under the data directory.


##### Building from Source

1. Clone this repository
2. Optionally, update to a specific tag
3. Run `./bin/build.sh` (OS X/Linux) or `bin/Publish.ps1` (Windows).

Refer to the [wiki](https://github.com/guillermooo/Vintageous/wiki) for more information.


### Documentation

Refer to the [wiki](https://github.com/guillermooo/Vintageous/wiki).


### Settings

See [Vintageous/Preferences.sublime-settings](https://github.com/guillermooo/Vintageous/blob/master/Preferences.sublime-settings) for a comprehensive list of settings.
