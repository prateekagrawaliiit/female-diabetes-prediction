# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2021-03-02 02:21:51
# @Last Modified by:   prateek
# @Last Modified time: 2021-03-02 03:03:04
"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st

class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # app = st.sidebar.radio(
        st.sidebar.title("Diabetes Detection")
        st.sidebar.success(
    "Dibetes Prediction with The power of **Artificial Intelligence**!")
        st.sidebar.header('Navigation')
        app = st.sidebar.radio(
            '',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()