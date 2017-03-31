# WindowSettings

WindowSettings is a simple Sublime Text 3 plugin to control if the tabs, the minimap, the status bar, the side bar or the menus are shown with some *settings*.

Here is the list:

- `show_tabs`
- `show_minimap`
- `show_status_bar`
- `show_sidebar`
- `show_menus`

They should be booleans (`true` or `false`) or `null`.
If set to `null`, it won't do anything → leave the side bar, tabs etc as it is.

## Installation

The best way to install this package is by using Package Control.

*Because it's not yet available on the default channel, you need to add it to your custom package list. Here's how*

1. Open up the command palette (<kbd>ctrl+shift+p</kbd>) and search for `Package Control: Add Repository`.
2. Paste this URL in: `https://github.com/math2001/WindowSettings`

Now, it's just a normal install:

- Open up the command palette (<kbd>ctrl+shift+p</kbd>) and search for `Package Control: Install Package`
- Search for `WindowSettings`
