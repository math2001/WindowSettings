# -*- encoding: utf-8 -*-

import sublime_plugin

class WindowSetting(sublime_plugin.EventListener):

    def on_activated(self, view):
        window = view.window()
        settings = view.settings()

        if settings.get('is_widget'):
            return

        show_tabs = settings.get('show_tabs')
        show_minimap = settings.get('show_minimap')
        show_status_bar = settings.get('show_status_bar')
        show_sidebar = settings.get('show_sidebar')
        show_menus = settings.get('show_menus')

        if show_tabs is not None:
            window.set_tabs_visible(show_tabs)
        if show_minimap is not None:
            window.set_minimap_visible(show_minimap)
        if show_status_bar is not None:
            window.set_status_bar_visible(show_status_bar)
        if show_sidebar is not None:
            window.set_sidebar_visible(show_sidebar)
        if show_menus is not None:
            window.set_menu_visible(show_menus)
