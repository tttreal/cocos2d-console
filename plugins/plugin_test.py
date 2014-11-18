#!/usr/bin/python
# ----------------------------------------------------------------------------
# cocos2d "test" plugin
#
# Author: Ricardo Quesada
# Copyright 2014 (C) Chukong Technologies
#
# License: MIT
# ----------------------------------------------------------------------------
'''
"test" plugin for cocos2d command line tool
'''

__docformat__ = 'restructuredtext'

import re
import os
import cocos
import inspect


#
# Plugins should be a sublass of CCPlugin
#
class CCPluginTest(cocos.CCPlugin):

    @staticmethod
    def plugin_name():
        return "test"

    @staticmethod
    def brief_description():
        return "useful to test the plugin framework"

    def run(self, argv, dependencies):
        print("cocos2d path: %s" % self.get_cocos2d_path())
        print("templates path: %s" % self.get_templates_path())
        print("console path: %s" % self.get_console_path())