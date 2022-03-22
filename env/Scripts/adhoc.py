#!d:\iba big data\lesson_3\env\scripts\python.exe
# -*- coding: utf-8 -*-
# Copyright (C) 2011, 2012, Wolfgang Scherer, <Wolfgang.Scherer at gmx.de>
#
# This file is part of AdHoc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>,
# or write to Wolfgang Scherer, <Wolfgang.Scherer at gmx.de>

# @:adhoc_uncomment:@
# @:adhoc_template:@ doc/index.rst
# AdHoc Standalone Python Script Generator
# ########################################
#
# The *AdHoc* compiler can be used as a program (see `Script Usage`_)
# as well as a module (see :class:`adhoc.AdHoc`).
#
# Since the *AdHoc* compiler itself is installed as a compiled *AdHoc*
# script, it serves as its own usage example.
#
# After installation of the *adhoc.py* script, the full source can be
# obtained in directory ``__adhoc__``, by executing::
#
#     adhoc.py --explode
#
# .. @@contents@@
#
# @:adhoc_template:@ doc/index.rst # off
# @:adhoc_uncomment:@

"""\
.. _Script Usage:

adhoc.py - Python ad hoc compiler.

======  ====================
usage:  adhoc.py [OPTIONS] [file ...]
or      import adhoc
======  ====================

Options
=======

  ===================== ==================================================
  -c, --compile         compile file(s) or standard input into output file
                        (default: standard output).
  -d, --decompile       decompile file(s) or standard input into
                        output directory (default ``__adhoc__``).
  -o, --output OUT      output file for --compile/output directory for
                        --decompile.

  -q, --quiet           suppress warnings
  -v, --verbose         verbose test output
  --debug[=NUM]         show debug information

  -h, --help            display this help message
  --documentation       display module documentation.

  --template list       show available templates.
  --eide[=COMM]         Emacs IDE template list (implies --template list).
  --template[=NAME]     extract named template to standard
                        output. Default NAME is ``-``.
  --extract[=DIR]       extract adhoc files to directory DIR (default: ``.``)
  --explode[=DIR]       explode script with adhoc in directory DIR
                        (default ``__adhoc__``)
  --implode             implode script with adhoc
  --install             install adhoc.py script

  -t, --test            run doc tests
  ===================== ==================================================

*adhoc.py* is compatible with Python 2.4+ and Python 3. (For Python
<2.6 the packages *stringformat* and *argparse* are needed and
included.)

.. _END_OF_HELP:

.. |=NUM| replace:: ``[=NUM]``

Script Examples
===============

Templates
---------

Sections marked by |adhoc_template| can be retrieved as templates on
standard output.

Additionally, all other files compiled into an adhoc file with one of

================ ======================
|adhoc|          ==> |adhoc_import|
|adhoc_verbatim| ==> |adhoc_template_v|
|adhoc_include|  ==> |adhoc_unpack|
================ ======================

are accessible as templates.

``python adhoc.py --template list`` provides a list of templates:

>>> ign = main('adhoc.py --template list'.split())
================================================= ================================ ================
                     Command                                  Template                   Type
================================================= ================================ ================
adhoc.py --template adhoc_test                    # !adhoc_test                    adhoc_import
adhoc.py --template adhoc_test.sub                # !adhoc_test.sub                adhoc_import
adhoc.py --template argparse_local                # !argparse_local                adhoc_import
adhoc.py --template namespace_dict                # !namespace_dict                adhoc_import
adhoc.py --template stringformat_local            # !stringformat_local            adhoc_import
adhoc.py --template use_case_000_                 # !use_case_000_                 adhoc_import
adhoc.py --template use_case_001_templates_       # !use_case_001_templates_       adhoc_import
adhoc.py --template use_case_002_include_         # !use_case_002_include_         adhoc_import
adhoc.py --template use_case_003_import_          # !use_case_003_import_          adhoc_import
adhoc.py --template use_case_005_nested_          # !use_case_005_nested_          adhoc_import
adhoc.py --template docutils.conf                 # docutils.conf                  adhoc_template_v
adhoc.py --template                               # -                              adhoc_template
adhoc.py --template README.txt                    # README.txt                     adhoc_template
adhoc.py --template adhoc_init                    # -adhoc_init                    adhoc_template
adhoc.py --template catch-stdout                  # -catch-stdout                  adhoc_template
adhoc.py --template col-param-closure             # -col-param-closure             adhoc_template
adhoc.py --template doc/USE_CASES.txt             # doc/USE_CASES.txt              adhoc_template
adhoc.py --template doc/index.rst                 # doc/index.rst                  adhoc_template
adhoc.py --template max-width-class               # -max-width-class               adhoc_template
adhoc.py --template rst-to-ascii                  # -rst-to-ascii                  adhoc_template
adhoc.py --template test                          # -test                          adhoc_template
adhoc.py --template MANIFEST.in                   # !MANIFEST.in                   adhoc_unpack
adhoc.py --template Makefile                      # !Makefile                      adhoc_unpack
adhoc.py --template README.css                    # !README.css                    adhoc_unpack
adhoc.py --template doc/Makefile                  # !doc/Makefile                  adhoc_unpack
adhoc.py --template doc/_static/adhoc-logo-32.ico # !doc/_static/adhoc-logo-32.ico adhoc_unpack
adhoc.py --template doc/adhoc-logo.svg            # !doc/adhoc-logo.svg            adhoc_unpack
adhoc.py --template doc/conf.py                   # !doc/conf.py                   adhoc_unpack
adhoc.py --template doc/make.bat                  # !doc/make.bat                  adhoc_unpack
adhoc.py --template doc/z-massage-index.sh        # !doc/z-massage-index.sh        adhoc_unpack
adhoc.py --template setup.py                      # !setup.py                      adhoc_unpack
================================================= ================================ ================

``python adhoc.py --template`` prints the standard template ``-``
(closing delimiter replaced by ellipsis):

>>> ign = main('./adhoc.py --template'.split()) #doctest: +ELLIPSIS
# @:adhoc_disable... allow modification of exploded sources in original place
sys.path.append('__adhoc__')
# @:adhoc_disable...
<BLANKLINE>
# @:adhoc_run_time... The run-time class goes here
# @:adhoc_run_time_engine... settings enabled at run-time
# @:adhoc_enable...
# RtAdHoc.flat = False
# @:adhoc_enable...
# @:adhoc_run_time_engine...
<BLANKLINE>
#import adhoc                                               # @:adhoc...

``python adhoc.py --template test`` prints the template named ``-test``.
the leading ``-`` signifies disposition to standard output:

>>> ign = main('./adhoc.py --template test'.split())
Test template.

Extract
-------

The default destination for extracting files is the current working
directory.

Files extracted consist of

- packed files generated by |adhoc_include|
- templates generated by |adhoc_verbatim|
- templates with a file destination other than standard output

``python adhoc.py --extract __adhoc_extract__`` unpacks the following files into
directory ``__adhoc_extract__``:

>>> import shutil
>>> ign = main('./adhoc.py --extract __adhoc_extract__'.split())
>>> file_list = []
>>> for dir, subdirs, files in os.walk('__adhoc_extract__'):
...     file_list.extend([os.path.join(dir, file_) for file_ in files])
>>> for file_ in sorted(file_list):
...     printf(file_)
__adhoc_extract__/MANIFEST.in
__adhoc_extract__/Makefile
__adhoc_extract__/README.css
__adhoc_extract__/README.txt
__adhoc_extract__/doc/Makefile
__adhoc_extract__/doc/USE_CASES.txt
__adhoc_extract__/doc/_static/adhoc-logo-32.ico
__adhoc_extract__/doc/adhoc-logo.svg
__adhoc_extract__/doc/conf.py
__adhoc_extract__/doc/index.rst
__adhoc_extract__/doc/make.bat
__adhoc_extract__/doc/z-massage-index.sh
__adhoc_extract__/docutils.conf
__adhoc_extract__/setup.py
__adhoc_extract__/use_case_000_.py
__adhoc_extract__/use_case_001_templates_.py
__adhoc_extract__/use_case_002_include_.py
__adhoc_extract__/use_case_003_import_.py
__adhoc_extract__/use_case_005_nested_.py
>>> shutil.rmtree('__adhoc_extract__')

Export
------

The default destination for exporting files is the
subdirectory ``__adhoc__``.

Files exported consist of

- imported modules generated by |adhoc|
- all files covered in section `Extract`_

``python adhoc.py --explode __adhoc_explode__`` unpacks the following files into
directory ``__adhoc_explode__``:

>>> import shutil
>>> ign = main('./adhoc.py --explode __adhoc_explode__'.split())
>>> file_list = []
>>> for dir, subdirs, files in os.walk('__adhoc_explode__'):
...     file_list.extend([os.path.join(dir, file_) for file_ in files])
>>> for file_ in sorted(file_list):
...     printf(file_)
__adhoc_explode__/MANIFEST.in
__adhoc_explode__/Makefile
__adhoc_explode__/README.css
__adhoc_explode__/README.txt
__adhoc_explode__/adhoc.py
__adhoc_explode__/adhoc_test/__init__.py
__adhoc_explode__/adhoc_test/sub/__init__.py
__adhoc_explode__/argparse_local.py
__adhoc_explode__/doc/Makefile
__adhoc_explode__/doc/USE_CASES.txt
__adhoc_explode__/doc/_static/adhoc-logo-32.ico
__adhoc_explode__/doc/adhoc-logo.svg
__adhoc_explode__/doc/conf.py
__adhoc_explode__/doc/index.rst
__adhoc_explode__/doc/make.bat
__adhoc_explode__/doc/z-massage-index.sh
__adhoc_explode__/docutils.conf
__adhoc_explode__/namespace_dict.py
__adhoc_explode__/rt_adhoc.py
__adhoc_explode__/setup.py
__adhoc_explode__/stringformat_local.py
__adhoc_explode__/use_case_000_.py
__adhoc_explode__/use_case_001_templates_.py
__adhoc_explode__/use_case_002_include_.py
__adhoc_explode__/use_case_003_import_.py
__adhoc_explode__/use_case_005_nested_.py
>>> shutil.rmtree('__adhoc_explode__')

File Permissions
================

- File mode is restored.
- File ownership is not restored.
- File modification times are restored.

  Since only naive datetimes are recorded, this only works correctly
  within the same timezone.

.. @:adhoc_index_only:@

AdHoc Module
============

.. @:adhoc_index_only:@
"""

# @:adhoc_uncomment:@
# @:adhoc_template:@ doc/index.rst
#
# Purpose
# =======
#
# *AdHoc* provides python scripts with
#
# - template facilities
# - default file generation
# - standalone module inclusion
#
# @:adhoc_index_only:@
# See also `Use Cases`_.
#
# @:adhoc_index_only:@
# *AdHoc* has been designed to provide an implode/explode cycle:
#
# ========  =======  =========  =======  =========
# source_0                               xsource_0
# source_1  implode             explode  xsource_1
# ...       ------>  script.py  ------>  ...
# source_n                               xsource_n
# ========  =======  =========  =======  =========
#
# where ``xsource_i === source_i``. I.e., ``diff source_i xsource_i``
# does not produce any output.
#
# Quickstart
# ==========
#
# module.py:
#
#     | # -\*- coding: utf-8 -\*-
#     | mvar = 'value'
#
# script.py:
#
#     | # -\*- coding: utf-8 -\*-
#     | # |adhoc_run_time|
#     | import module # |adhoc|
#     | print('mvar: ' + module.mvar)
#
# Compilation::
#
#     adhoc.py --compile script.py >/tmp/script-compiled.py
#
# Execution outside source directory::
#
#     cd /tmp && python script-compiled.py
#
# shows::
#
#     mvar: value
#
# Decompilation::
#
#     cd /tmp && \
#     mkdir -p __adhoc__ && \
#     adhoc.py --decompile <script-compiled.py >__adhoc__/script.py
#
# .. |@:| replace:: ``@:``
# .. |:@| replace:: ``:@``
# .. |adhoc_run_time| replace:: |@:|\ ``adhoc_run_time``\ |:@|
# .. |adhoc| replace:: |@:|\ ``adhoc``\ |:@|
#
# Description
# ===========
#
# The *AdHoc* compiler/decompiler parses text for tagged lines and
# processes them as instructions.
#
# The minimal parsed entity is a tagged line, which is any line
# containing a recognized *AdHoc* tag.
#
# All *AdHoc* tags are enclosed in delimiters (default: |@:| and |:@|). E.g:
#
#   |@:|\ adhoc\ |:@|
#
# Delimiters come in several flavors, namely line and section
# delimiters and a set of macro delimiters. By default, line and
# section delimiters are the same, but they can be defined separately.
#
# `Flags`_ are tagged lines, which denote a single option or
# command. E.g.:
#
#   | import module     # |@:|\ adhoc\ |:@|
#   | # |@:|\ adhoc_self\ |:@| my_module_name
#
# `Sections`_ are tagged line pairs, which delimit a block of
# text. The first tagged line opens the section, the second tagged
# line closes the section. E.g.:
#
#   | # |@:|\ adhoc_enable\ |:@|
#   | # disabled_command()
#   | # |@:|\ adhoc_enable\ |:@|
#
# `Macros`_ have their own delimiters (default: |@m| and |m>|). E.g.:
#
#   | # |@m|\ MACRO_NAME\ |m>|
#
# The implementation is realized as class :class:`adhoc.AdHoc` which
# is mainly used as a namespace. The run-time part of
# :class:`adhoc.AdHoc` -- which handles module import and file export
# -- is included verbatim as class :class:`RtAdHoc` in the generated
# output.
#
# Flags
# -----
#
# :|adhoc_run_time|:
#     The place where the *AdHoc* run-time code is added.  This flag must
#     be present in files, which use the |adhoc| import feature.  It
#     is not needed for the enable/disable features.
#
#     This flag is ignored, if double commented. E.g.:
#
#       | # # |adhoc_run_time|
#
# :|adhoc| [force] [flat | full]:
#     Mark import line for run-time compilation.
#
#     If ``force`` is specified, the module is imported, even if it
#     was imported before.
#
#     If ``flat`` is specified, the module is not recursively
#     exported.
#
#     If ``full`` is specified, the module is recursively
#     exported. (This parameter takes priority over ``flat``).
#
#     If neither ``flat`` nor ``full`` are specified,
#     :attr:`adhoc.AdHoc.flat` determines the export scope.
#
#     This flag is ignored, if the line is commented out. E.g.:
#
#       | # import module  # |adhoc|
#
# .. _adhoc_include:
#
# :|adhoc_include| file_spec, ...:
#     Include files for unpacking. ``file_spec`` is one of
#
#     :file:
#       ``file`` is used for both input and output.
#
#     :file ``from`` default-file:
#       ``file`` is used for input and output. if ``file`` does not
#       exist, ``default-file`` is used for input.
#
#     :source-file ``as`` output-file:
#       ``source-file`` is used for input. ``output-file`` is used for
#       output. If ``source-file`` does not exist, ``output-file`` is
#       used for input also.
#
#     This flag is ignored, if double commented. E.g.:
#
#       | # # |adhoc_include| file
#
# :|adhoc_verbatim| [flags] file_spec, ...:
#     Include files for verbatim extraction. See adhoc_include_ for
#     ``file_spec``.
#
#     The files are included as |adhoc_template_v| sections. *file* is used
#     as *export_file* mark. If *file* is ``--``, the template disposition
#     becomes standard output.
#
#     Optional flags can be any combination of ``[+|-]NUM`` for
#     indentation and ``#`` for commenting. E.g.:
#
#       | # |adhoc_verbatim| +4# my_file from /dev/null
#
#     *my_file* (or ``/dev/null``) is read, commented and indented 4
#     spaces.
#
#     If the |adhoc_verbatim| tag is already indented, the specified
#     indentation is subtracted.
#
#     This flag is ignored, if double commented. E.g.:
#
#       | # # |adhoc_verbatim| file
#
# :|adhoc_self| name ...:
#     Mark name(s) as currently compiling.  This is useful, if
#     ``__init__.py`` imports other module parts. E.g:
#
#       | import pyjsmo             # |@:|\ adhoc\ |:@|
#
#     where ``pyjsmo/__init__.py`` contains:
#
#       | # |@:|\ adhoc_self\ |:@| pyjsmo
#       | from pyjsmo.base import * # |@:|\ adhoc\ |:@|
#
# :|adhoc_compiled|:
#     If present, no compilation is done on this file. This flag is
#     added by the compiler to the run-time version.
#
# Sections
# --------
#
# :|adhoc_enable|:
#     Leading comment char and exactly one space are removed from lines
#     in these sections.
#
# :|adhoc_disable|:
#     A comment char and exactly one space are added to non-blank
#     lines in these sections.
#
# :|adhoc_template| -mark | export_file:
#     If mark starts with ``-``, the output disposition is standard output
#     and the template is ignored, when exporting.
#
#     Otherwise, the template is written to output_file during export.
#
#     All template parts with the same mark/export_file are concatenated
#     to a single string.
#
# :|adhoc_template_v| export_file:
#     Variation of |adhoc_template|. Automatically generated by |adhoc_verbatim|.
#
# :|adhoc_uncomment|:
#     Treated like |adhoc_enable| before template output.
#
# :|adhoc_indent| [+|-]NUM:
#     Add or remove indentation before template output.
#
# :|adhoc_import|:
#     Imported files are marked as such by the compiler. There is no
#     effect during compilation.
#
# :|adhoc_unpack|:
#     Included files are marked as such by the compiler. There is no
#     effect during compilation.
#
# :|adhoc_remove|:
#     Added sections are marked as such by the compiler. Removal is
#     done when exporting.
#
#     Before compilation, existing |adhoc_remove| tags are renamed to
#     |adhoc_remove_|.
#
#     After automatically added |adhoc_remove| sections have been
#     removed during export, remaining |adhoc_remove_| tags are
#     renamed to |adhoc_remove| again.
#
#     .. note:: Think twice, before removing material from original
#        sources at compile time. It will violate the condition
#        ``xsource_i === source_i``.
#
# :|adhoc_run_time_engine|:
#     The run-time class :class:`RtAdHoc` is enclosed in this special
#     template section.
#
#     It is exported as ``rt_adhoc.py`` during export.
#
# Macros
# ------
#
# Macros are defined programmatically::
#
#     AdHoc.macros[MACRO_NAME] = EXPANSION_STRING
#
# A macro is invoked by enclosing a MACRO_NAME in
# :attr:`adhoc.AdHoc.macro_call_delimiters`. (Default: |@m|, |m>|).
#
# :|MACRO_NAME|:
#     Macro call.
#
# Internal
# --------
#
# :|adhoc_run_time_class|:
#     Marks the beginning of the run-time class.  This is only
#     recognized in the *AdHoc* programm/module.
#
# :|adhoc_run_time_section|:
#     All sections are concatenated and used as run-time code.  This is
#     only recognized in the *AdHoc* programm/module.
#
# In order to preserve the ``xsource_i === source_i`` bijective
# condition, macros are expanded/collapsed with special macro
# definition sections. (See :attr:`adhoc.AdHoc.macro_xdef_delimiters`;
# Default: |<m|, |m@|).
#
# :|adhoc_macro_call|:
#     Macro call section.
#
# :|adhoc_macro_expansion|:
#     Macro expansion section.
#
# @:adhoc_template:@ doc/index.rst # off
# @:adhoc_uncomment:@

# @:adhoc_uncomment:@
# @:adhoc_template:@ doc/index.rst
# @:adhoc_index_only:@
#
# .. include:: USE_CASES.txt
# @:adhoc_index_only:@
#
# AdHoc Script
# ============
# @:adhoc_index_only:@
#
# .. automodule:: adhoc
#     :members:
#     :show-inheritance:
#
# .. _namespace_dict:
#
# NameSpace/NameSpaceDict
# =======================
#
# .. automodule:: namespace_dict
#     :members:
#     :show-inheritance:
#
# @:adhoc_index_only:@
# @:adhoc_template:@ doc/index.rst # off
# @:adhoc_uncomment:@

# @:adhoc_uncomment:@
# @:adhoc_template:@ doc/index.rst
#
# .. |adhoc_self| replace:: |@:|\ ``adhoc_self``\ |:@|
# .. |adhoc_include| replace:: |@:|\ ``adhoc_include``\ |:@|
# .. |adhoc_verbatim| replace:: |@:|\ ``adhoc_verbatim``\ |:@|
# .. |adhoc_compiled| replace:: |@:|\ ``adhoc_compiled``\ |:@|
# .. |adhoc_enable| replace:: |@:|\ ``adhoc_enable``\ |:@|
# .. |adhoc_disable| replace:: |@:|\ ``adhoc_disable``\ |:@|
# .. |adhoc_template| replace:: |@:|\ ``adhoc_template``\ |:@|
# .. |adhoc_template_v| replace:: |@:|\ ``adhoc_template_v``\ |:@|
# .. |adhoc_uncomment| replace:: |@:|\ ``adhoc_uncomment``\ |:@|
# .. |adhoc_indent| replace:: |@:|\ ``adhoc_indent``\ |:@|
# .. |adhoc_import| replace:: |@:|\ ``adhoc_import``\ |:@|
# .. |adhoc_unpack| replace:: |@:|\ ``adhoc_unpack``\ |:@|
# .. |adhoc_remove| replace:: |@:|\ ``adhoc_remove``\ |:@|
# .. |adhoc_remove_| replace:: |@:|\ ``adhoc_remove_``\ |:@|
# .. |adhoc_run_time_class| replace:: |@:|\ ``adhoc_run_time_class``\ |:@|
# .. |adhoc_run_time_section| replace:: |@:|\ ``adhoc_run_time_section``\ |:@|
# .. |adhoc_run_time_engine| replace:: |@:|\ ``adhoc_run_time_engine``\ |:@|
# .. |@m| replace:: ``@|:``
# .. |m>| replace:: ``:|>``
# .. |<m| replace:: ``<|:``
# .. |m@| replace:: ``:|@``
# .. |MACRO_NAME| replace:: |@m|\ ``MACRO_NAME``\ |m>|
# .. |adhoc_macro_call| replace:: |<m|\ ``adhoc_macro_call``\ |m@|
# .. |adhoc_macro_expansion| replace:: |<m|\ ``adhoc_macro_expansion``\ |m@|
#
# @:adhoc_template:@ doc/index.rst # off
# @:adhoc_uncomment:@

# --------------------------------------------------
# |||:sec:||| COMPATIBILITY
# --------------------------------------------------

import sys
# (progn (forward-line 1) (snip-insert-mode "py.b.printf" t) (insert "\n"))
# adapted from http://www.daniweb.com/software-development/python/code/217214
try:
    printf = eval("print") # python 3.0 case
except SyntaxError:
    printf_dict = dict()
    try:
        exec("from __future__ import print_function\nprintf=print", printf_dict)
        printf = printf_dict["printf"] # 2.6 case
    except SyntaxError:
        def printf(*args, **kwd): # 2.4, 2.5, define our own Print function
            fout = kwd.get("file", sys.stdout)
            w = fout.write
            if args:
                w(str(args[0]))
            sep = kwd.get("sep", " ")
            for a in args[1:]:
                w(sep)
                w(str(a))
            w(kwd.get("end", "\n"))
    del printf_dict

# (progn (forward-line 1) (snip-insert-mode "py.f.isstring" t) (insert "\n"))
# hide from 2to3
exec('''
def isstring(obj):
    return isinstance(obj, basestring)
''')
try:
    isstring("")
except NameError:
    def isstring(obj):
        return isinstance(obj, str) or isinstance(obj, bytes)

# (progn (forward-line 1) (snip-insert-mode "py.b.dict_items" t) (insert "\n"))
try:
    getattr(dict(), 'iteritems')
    ditems  = lambda d: getattr(d, 'iteritems')()
    dkeys   = lambda d: getattr(d, 'iterkeys')()
    dvalues = lambda d: getattr(d, 'itervalues')()
except AttributeError:
    ditems  = lambda d: getattr(d, 'items')()
    dkeys   = lambda d: getattr(d, 'keys')()
    dvalues = lambda d: getattr(d, 'values')()

import os
import re

# --------------------------------------------------
# |||:sec:||| CONFIGURATION
# --------------------------------------------------

dbg_comm = ((('dbg_comm' in globals()) and (globals()['dbg_comm'])) or ('# '))
dbg_twid = ((('dbg_twid' in globals()) and (globals()['dbg_twid'])) or (9))
dbg_fwid = ((('dbg_fwid' in globals()) and (globals()['dbg_fwid'])) or (23))

# (progn (forward-line 1) (snip-insert-mode "py.b.dbg.setup" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.b.strings" t) (insert "\n"))
def _uc(string):                                           # ||:fnc:||
    return unicode(string, 'utf-8')
try:
    _uc("")
except NameError:
    _uc = lambda x: x

uc_type = type(_uc(""))

def uc(value):                                             # ||:fnc:||
    if isstring(value) and not isinstance(value, uc_type):
        return _uc(value)
    return value

def _utf8str(string):                                      # ||:fnc:||
    if isinstance(string, uc_type):
        return string.encode('utf-8')
    return string

def utf8str(value):                                        # ||:fnc:||
    if isstring(value):
        return _utf8str(value)
    return value

def _nativestr(string):                                    # ||:fnc:||
    # for python3, unicode strings have type str
    if isinstance(string, str):
        return string
    # for python2, encode unicode strings to utf-8 strings
    if isinstance(string, uc_type):
        return string.encode('utf-8')
    try:
        return str(string.decode('utf-8'))
    except UnicodeDecodeError:
        return string

def nativestr(value):                                      # ||:fnc:||
    if isstring(value):
        return _nativestr(value)
    return value

# (progn (forward-line 1) (snip-insert-mode "py.f.strclean" t) (insert "\n"))
def strclean(value):
    '''Make a copy of any structure with all strings converted to
    native strings.

    :func:`strclean` is good for :meth:`__str__` methods.

    It is needed for doctest output that should be compatible with
    both python2 and python3.

    The output structure is not necessarily an exact copy of the input
    structure, since objects providing iterator or item interfaces are
    only copied through those!
    '''
    if isstring(value):
        return _nativestr(value)
    if hasattr(value, 'items'):
        try:
            out = type(value)()
        except:
            (t, e, tb) = sys.exc_info() # |:debug:|
            printf(''.join(traceback.format_tb(tb)), file=sys.stderr)
            printe('OOPS: ' + t.__name__ + ': ' + str(e) + ' [' + str(value.__class__.__name__) + '] [' + str(value) + ']')
        for k, v in value.items():
            out[strclean(k)] = strclean(v)
        return out
    if hasattr(value, '__iter__') or hasattr(value, 'iter'):
        if isinstance(value, tuple):
            out = []
        else:
            out = type(value)()
        for e in value:
            out.append(strclean(e))
        if isinstance(value, tuple):
            out = type(value)(out)
        return out
    return value

# (progn (forward-line 1) (snip-insert-mode "py.f.issequence" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.b.logging" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.b.ordereddict" t) (insert "\n"))

# (progn (forward-line 1) (snip-insert-mode "py.main.pyramid.activate" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.main.project.libdir" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.main.sql.alchemy" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.main.sql.ws" t) (insert "\n"))

# The standard template should be something useful

# @:adhoc_uncomment:@
# @:adhoc_template:@ -
# # @:adhoc_disable:@ allow modification of exploded sources in original place
# sys.path.append('__adhoc__')
# # @:adhoc_disable:@
# @:adhoc_template:@
# @:adhoc_uncomment:@

# @:adhoc_run_time:@
# @:adhoc_remove:@
# @:adhoc_run_time_engine:@
# -*- coding: utf-8 -*-
# @:adhoc_compiled:@ 2022-03-15 08:31:30.045781
import sys
import os
import re

# @:adhoc_uncomment:@
# @:adhoc_template:@ -catch-stdout
try:
    from cStringIO import StringIO as _AdHocBytesIO, StringIO as _AdHocStringIO
except ImportError:
    try:
        from StringIO import StringIO as _AdHocBytesIO, StringIO as _AdHocStringIO
    except ImportError:
        from io import BytesIO as _AdHocBytesIO, StringIO as _AdHocStringIO

# @:adhoc_template:@
# @:adhoc_uncomment:@
class RtAdHoc(object):                                     # |||:cls:|||
    line_delimiters = ('@:', ':@')
    section_delimiters = ('@:', ':@')

    template_process_hooks = {}
    extra_templates = []

    export_dir = '__adhoc__'
    extract_dir = '.'
    flat = True
    forced = False

    frozen = False

    quiet = False
    verbose = False
    debug = False

    include_path = []
    export_need_init = {}
    export_have_init = {}
    extract_warn = False

    def _adhoc_string_util():
        def isstring(obj):
            return isinstance(obj, basestring)
        try:
            isstring("")
        except NameError:
            def isstring(obj):
                return isinstance(obj, str) or isinstance(obj, bytes)
        def _uc(string):
            return unicode(string, 'utf-8')
        try:
            _uc("")
        except NameError:
            _uc = lambda x: x
        uc_type = type(_uc(""))
        def uc(value):
            if isstring(value) and not isinstance(value, uc_type):
                return _uc(value)
            return value
        return staticmethod(isstring), uc_type, staticmethod(uc)

    isstring, uc_type, uc = _adhoc_string_util()

    @staticmethod
    def adhoc_tag(symbol_or_re, delimiters, is_re=False):    # |:fnc:|
        ldlm = delimiters[0]
        rdlm = delimiters[1]
        if is_re:
            ldlm = re.escape(ldlm)
            rdlm = re.escape(rdlm)
        return ''.join((ldlm, symbol_or_re, rdlm))

    @classmethod
    def tag_split(cls, string, tag, is_re=False):            # |:fnc:|
        if not is_re:
            tag = re.escape(tag)
        ro = re.compile(''.join(('^[^\n]*(', tag, ')[^\n]*$')), re.M)
        result = []
        last_end = 0
        string = cls.decode_source(string)
        for mo in re.finditer(ro, string):
            start = mo.start(0)
            end = mo.end(0)
            result.append((False, string[last_end:start]))
            result.append((True, string[start:end+1]))
            last_end = end+1
        result.append((False, string[last_end:]))
        return result

    @classmethod
    def adhoc_parse_line(cls, tagged_line, symbol_or_re=None, # |:clm:|
                         delimiters=None, is_re=False, strip_comment=None):
        if delimiters is None:
            delimiters = cls.line_delimiters
        if symbol_or_re is None:
            dlm = delimiters[1]
            if dlm:
                symbol_or_re = ''.join(('[^', dlm[0], ']+'))
            else:
                symbol_or_re = ''.join(('[^\\s]+'))
            is_re = True
        if not is_re:
            symbol_or_re = re.escape(symbol_or_re)
        tag_rx = cls.adhoc_tag(''.join(('(', symbol_or_re, ')')), delimiters, is_re=True)
        mo = re.search(tag_rx, tagged_line)
        if mo:
            ptag = mo.group(1)
        else:
            ptag = ''
        strip_rx = ''.join(('^.*', tag_rx, '\\s*'))
        tag_arg = re.sub(strip_rx, '', tagged_line).strip()
        if strip_comment:
            tag_arg = re.sub('\\s*#.*', '', tag_arg)
        return (ptag, tag_arg)

    @classmethod
    def set_delimiters(cls, line_delimiters=None, section_delimiters=None): # |:clm:|
        delimiter_state = (cls.line_delimiters, cls.section_delimiters)
        if line_delimiters is None:
            line_delimiters = delimiter_state[0]
            if section_delimiters is None:
                section_delimiters = delimiter_state[1]
        elif section_delimiters is None:
            section_delimiters = line_delimiters
        cls.line_delimiters, cls.section_delimiters = (
            line_delimiters, section_delimiters)
        return delimiter_state

    @classmethod
    def reset_delimiters(cls, delimiter_state):              # |:clm:|
        cls.line_delimiters, cls.section_delimiters = delimiter_state

    @classmethod
    def inc_delimiters(cls):                                 # |:clm:|

        inc_first = lambda dlm: (((not dlm) and ('')) or (dlm[0] + dlm))
        inc_last = lambda dlm: (((not dlm) and ('')) or (dlm + dlm[-1]))
        outer_delimiters = [(inc_first(dlm[0]), inc_last(dlm[1]))
                            for dlm in (cls.line_delimiters,
                                        cls.section_delimiters)]
        return cls.set_delimiters(*outer_delimiters)

    @classmethod
    def line_tag(cls, symbol_or_re, is_re=False):            # |:clm:|
        return cls.adhoc_tag(symbol_or_re, cls.line_delimiters, is_re)

    @classmethod
    def section_tag(cls, symbol_or_re, is_re=False):         # |:clm:|
        return cls.adhoc_tag(symbol_or_re, cls.section_delimiters, is_re)

    @classmethod
    def tag_lines(cls, string, tag, is_re=False):            # |:clm:|
        result = []
        for section in cls.tag_split(string, tag, is_re):
            if section[0]:
                result.append(section[1])
        return result

    @classmethod
    def tag_partition(cls, string, tag, is_re=False, headline=False): # |:clm:|
        in_section = False
        body_parts = []
        sections = []
        tagged_line = ''
        for section in cls.tag_split(string, tag, is_re):
            if section[0]:
                in_section = not in_section
                tagged_line = section[1]
                continue
            if in_section:
                if headline:
                    sections.append((tagged_line, section[1]))
                else:
                    sections.append(section[1])
            else:
                body_parts.append(section[1])
        return body_parts, sections

    @classmethod
    def tag_sections(cls, string, tag, is_re=False, headline=False): # |:clm:|
        body_parts, sections = cls.tag_partition(string, tag, is_re, headline)
        return sections

    @classmethod
    def line_tag_parse(cls, tagged_line, symbol_or_re=None, is_re=False, # |:clm:|
                       strip_comment=None):
        return cls.adhoc_parse_line(tagged_line, symbol_or_re, cls.line_delimiters,
                                    is_re, strip_comment=strip_comment)

    @classmethod
    def line_tag_strip(cls, tagged_line, symbol_or_re=None, is_re=False, # |:clm:|
                       strip_comment=None):
        return cls.line_tag_parse(tagged_line, symbol_or_re, is_re, strip_comment)[1]

    @classmethod
    def section_tag_parse(cls, tagged_line, symbol_or_re=None, is_re=False, # |:clm:|
                       strip_comment=None):
        return cls.adhoc_parse_line(tagged_line, symbol_or_re, cls.section_delimiters,
                                    is_re, strip_comment=strip_comment)

    @classmethod
    def section_tag_strip(cls, tagged_line, symbol_or_re=None, is_re=False, # |:clm:|
                       strip_comment=None):
        return cls.section_tag_parse(tagged_line, symbol_or_re, is_re, strip_comment)[1]

    @classmethod
    def transform_lines(cls, transform, string,              # |:clm:|
                        symbol_or_re, is_re=False, delimiters=None):
        if delimiters is None:
            delimiters = cls.line_delimiters
        result = []
        in_section = False
        for section in cls.tag_split(
            string, cls.adhoc_tag(symbol_or_re, delimiters, is_re), is_re):
            blob = section[1]
            if section[0]:
                in_section = not in_section
                blob = transform(blob)
            result.append(blob)
        string = ''.join(result)
        return string

    @classmethod
    def transform_sections(cls, transform, string,           # |:clm:|
                           symbol_or_re, is_re=False):
        result = []
        in_section = False
        headline = ''
        for section in cls.tag_split(
            string, cls.section_tag(symbol_or_re, is_re), is_re):
            blob = section[1]
            if section[0]:
                in_section = not in_section
                if in_section:
                    headline = blob
                    continue
            elif in_section:
                blob, headline = transform(blob, headline)
                result.append(headline)
            result.append(blob)
        string = ''.join(result)
        return string

    @classmethod
    def line_tag_rename(cls, string, symbol_or_re, renamed, is_re=False, delimiters=None): # |:clm:|
        if is_re:
            transform = lambda blob: re.sub(symbol_or_re, renamed, blob)
        else:
            transform = lambda blob: blob.replace(symbol_or_re, renamed)
        return cls.transform_lines(transform, string, symbol_or_re, is_re, delimiters)

    @classmethod
    def line_tag_remove(cls, string, symbol_or_re, is_re=False, delimiters=None): # |:clm:|
        transform = lambda blob: ''
        return cls.transform_lines(transform, string, symbol_or_re, is_re, delimiters)

    @classmethod
    def section_tag_rename(cls, string, symbol_or_re, renamed, is_re=False): # |:clm:|
        if is_re:
            transform = lambda blob: re.sub(symbol_or_re, renamed, blob)
        else:
            transform = lambda blob: blob.replace(symbol_or_re, renamed)
        return cls.transform_lines(transform, string, symbol_or_re, is_re, cls.section_delimiters)

    @classmethod
    def section_tag_remove(cls, string, symbol_or_re, is_re=False): # |:clm:|
        transform = lambda blob: ''
        return cls.transform_lines(transform, string, symbol_or_re, is_re, cls.section_delimiters)

    @classmethod
    def indent_sections(cls, string, symbol_or_re, is_re=False): # |:clm:|
        result = []
        in_section = False
        indent = 0
        for section in cls.tag_split(
            string, cls.section_tag(symbol_or_re, is_re), is_re):
            blob = section[1]
            if section[0]:
                in_section = not in_section
                if in_section:
                    tag_arg = cls.section_tag_strip(blob)
                    if tag_arg:
                        indent = int(tag_arg)
                    else:
                        indent = -4
            else:
                if in_section and indent:
                    if indent < 0:
                        rx = re.compile(''.join(('^', ' ' * (-indent))), re.M)
                        blob = rx.sub('', blob)
                    elif indent > 0:
                        rx = re.compile('^', re.M)
                        blob = rx.sub(' ' * indent, blob)
                    indent = 0
            result.append(blob)
        string = ''.join(result)
        return string

    @classmethod
    def enable_sections(cls, string, symbol_or_re, is_re=False): # |:clm:|
        enable_ro = re.compile('^([ \t\r]*)(# ?)', re.M)
        enable_sub = '\\1'
        transform = lambda blob, hl: (enable_ro.sub(enable_sub, blob), hl)
        return cls.transform_sections(transform, string, symbol_or_re, is_re)

    adhoc_rx_tab_check = re.compile('^([ ]*\t)', re.M)
    adhoc_rx_disable_simple = re.compile('^', re.M)
    adhoc_rx_min_indent_check = re.compile('^([ ]*)([^ \t\r\n]|$)', re.M)

    @classmethod
    def disable_transform(cls, section, headline=None):      # |:clm:|
        if not section:
            return (section, headline)

        if cls.adhoc_rx_tab_check.search(section):
            # tabs are evil
            if cls.verbose:
                list(map(sys.stderr.write,
                         ('# dt: evil tabs: ', repr(section), '\n')))
            return (
                cls.adhoc_rx_disable_simple.sub(
                    '# ', section.rstrip()) + '\n',
                headline)

        min_indent = ''
        for mo in cls.adhoc_rx_min_indent_check.finditer(section):
            indent = mo.group(1)
            if indent:
                if (not min_indent or len(min_indent) > len(indent)):
                    min_indent = indent
            elif mo.group(2):
                min_indent = ''
                break
        adhoc_rx_min_indent = re.compile(
            ''.join(('^(', min_indent, '|)([^\n]*)$')), re.M)

        if section.endswith('\n'):
            section = section[:-1]
        dsection = []
        for mo in adhoc_rx_min_indent.finditer(section):
            indent = mo.group(1)
            rest = mo.group(2)
            if not indent and not rest:
                #leave blank lines blank
                dsection.append('\n')
            else:
                dsection.extend((indent, '# ', rest, '\n'))
        return (''.join(dsection), headline)

    @classmethod
    def disable_sections(cls, string, symbol_or_re, is_re=False): # |:clm:|
        return cls.transform_sections(
            cls.disable_transform, string, symbol_or_re, is_re)

    @classmethod
    def remove_sections(cls, string, symbol_or_re, is_re=False): # |:clm:|
        ah_retained, ah_removed = cls.tag_partition(
            string, cls.section_tag(symbol_or_re, is_re), is_re)
        return ''.join(ah_retained)

    @staticmethod
    def check_coding(source):                                # |:fnc:|
        if source:
            eol_seen = 0
            for c in source:
                if isinstance(c, int):
                    lt_ = lambda a, b: a < b
                    chr_ = lambda a: chr(a)
                else:
                    lt_ = lambda a, b: True
                    chr_ = lambda a: a
                break
            check = []
            for c in source:
                if lt_(c, 127):
                    check.append(chr_(c))
                if c == '\n':
                    eol_seen += 1
                    if eol_seen == 2:
                        break
            check = ''.join(check)
            mo = re.search('-[*]-.*coding:\\s*([^;\\s]+).*-[*]-', check)
        else:
            mo = None
        if mo:
            coding = mo.group(1)
        else:
            coding = 'utf-8'
        return coding

    @classmethod
    def decode_source(cls, source):                          # |:clm:|
        if not source:
            return cls.uc('')
        if not isinstance(source, cls.uc_type) and hasattr(source, 'decode'):
            source = source.decode(cls.check_coding(source))
        return source

    @classmethod
    def encode_source(cls, source):                          # |:clm:|
        if not source:
            return ''.encode('utf-8')
        if isinstance(source, cls.uc_type) and hasattr(source, 'encode'):
            source = source.encode(cls.check_coding(source))
        return source

    @classmethod
    def read_source(cls, file_, decode=True):                # |:clm:|
        source = None
        if not file_ or file_ == '-':
            # Python3 has a buffer attribute for binary input.
            if hasattr(sys.stdin, 'buffer'):
                source = sys.stdin.buffer.read()
            else:
                source = sys.stdin.read()
        else:
            try:
                sf = open(file_, 'rb')
                source = sf.read()
                sf.close()
            except IOError:
                for module in sys.modules.values():
                    if (module
                        and hasattr(module, '__file__')
                        and module.__file__ == file_):
                        if (hasattr(module, '__adhoc__')
                            and hasattr(module.__adhoc__, 'source')):
                            source = module.__adhoc__.source
                            break
        if source is None:
            raise IOError('source not found for `' + str(file_) + '`')
        if decode:
            return cls.decode_source(source)
        return source

    @classmethod
    def write_source(cls, file_, source, mtime=None, mode=None): # |:clm:|
        esource = cls.encode_source(source)
        if not file_ or file_ == '-':
            if hasattr(sys.stdout, 'buffer'):
                sys.stdout.buffer.write(esource)
            else:
                try:
                    sys.stdout.write(esource)
                except TypeError:
                    sys.stdout.write(source)
        else:
            sf = open(file_, 'wb')
            sf.write(esource)
            sf.close()
            if mode is not None:
                os.chmod(file_, mode)
            if mtime is not None:
                import datetime
                if cls.isstring(mtime):
                    try:
                        date, ms = mtime.split('.')
                    except ValueError:
                        date = mtime
                        ms = 0
                    mtime = cls.strptime(date, '%Y-%m-%dT%H:%M:%S')
                    mtime += datetime.timedelta(microseconds=int(ms))
                if isinstance(mtime, datetime.datetime):
                    ts = int(mtime.strftime("%s"))
                else:
                    ts = mtime
                os.utime(file_, (ts, ts))

    @classmethod
    def check_xfile(cls, file_, xdir=None):                  # |:clm:|
        if xdir is None:
            xdir = cls.extract_dir
        if not file_:
            file_ = '-'
        if file_ == '-':
            return file_
        file_ = os.path.expanduser(file_)
        if os.path.isabs(file_):
            xfile = file_
        else:
            xfile = os.path.join(xdir, file_)
        xfile = os.path.abspath(xfile)
        if os.path.exists(xfile):
            # do not overwrite files
            if (cls.extract_warn or (cls.verbose)) and not cls.quiet:
                list(map(sys.stderr.write, (
                    "# xf: ", cls.__name__, ": warning file `", file_,
                    "` exists. skipping ...\n")))
            return None
        xdir = os.path.dirname(xfile)
        if not os.path.exists(xdir):
            os.makedirs(xdir)
        return xfile

    @classmethod
    def pack_file(cls, source, zipped=True):                 # |:clm:|
        import base64, gzip
        if zipped:
            sio = _AdHocBytesIO()
            gzf = gzip.GzipFile('', 'wb', 9, sio)
            gzf.write(cls.encode_source(source))
            gzf.close()
            source = sio.getvalue()
            sio.close()
        else:
            source = cls.encode_source(source)
        source = base64.b64encode(source)
        source = source.decode('ascii')
        return source

    @classmethod
    def unpack_file(cls, source64, zipped=True, decode=True): # |:clm:|
        import base64, gzip
        source = source64.encode('ascii')
        source = base64.b64decode(source)
        if zipped:
            sio = _AdHocBytesIO(source)
            gzf = gzip.GzipFile('', 'rb', 9, sio)
            source = gzf.read()
            gzf.close()
            sio.close()
        if decode:
            source = cls.decode_source(source)
        return source

    @classmethod
    def unpack_(cls, mod_name=None, file_=None, mtime=None, # |:clm:||:api_fi:|
                mode=None, zipped=True, flat=None, source64=None):
        xfile = cls.check_xfile(file_, cls.extract_dir)
        if xfile is None:
            return
        if cls.verbose:
            list(map(sys.stderr.write,
                     ("# xf: ", cls.__name__, ": unpacking `", file_, "`\n")))
        source = cls.unpack_file(source64, zipped=zipped, decode=False)
        cls.write_source(xfile, source, mtime, mode)

    @classmethod
    def strptime(cls, date_string, format_):                 # |:clm:|
        import datetime
        if hasattr(datetime.datetime, 'strptime'):
            strptime_ = datetime.datetime.strptime
        else:
            import time
            strptime_ = lambda date_string, format_: (
                datetime.datetime(*(time.strptime(date_string, format_)[0:6])))
        return strptime_(date_string, format_)

    @classmethod
    def import_(cls, mod_name=None, file_=None, mtime=None, # |:clm:||:api_fi:|
                mode=None, zipped=True, flat=None, source64=None):
        import datetime
        import time

        module = cls.module_setup(mod_name)

        if mtime is None:
            mtime = datetime.datetime.fromtimestamp(0)
        else:
            # mtime=2011-11-23T18:04:26[.218506], zipped=True, flat=None, source64=
            try:
                date, ms = mtime.split('.')
            except ValueError:
                date = mtime
                ms = 0
            mtime = cls.strptime(date, '%Y-%m-%dT%H:%M:%S')
            mtime += datetime.timedelta(microseconds=int(ms))

        source = cls.unpack_file(source64, zipped=zipped, decode=False)

        mod_parts = mod_name.split('.')
        mod_child = mod_parts[-1]
        parent = '.'.join(mod_parts[:-1])
        old_mtime = module.__adhoc__.mtime
        module = cls.module_setup(mod_name, file_, mtime, source, mode)
        if len(parent) > 0:
            setattr(sys.modules[parent], mod_child, module)

        if module.__adhoc__.mtime != old_mtime:
            source = cls.encode_source(module.__adhoc__.source)
            exec(source, module.__dict__)

    @classmethod
    def module_setup(cls, module=None, file_=None, mtime=None, # |:clm:||:api_fi:|
                     source=None, mode=None):
        m = 'ms: '
        class Attr:                                          # |:cls:|
            pass

        import types, datetime, os
        if not isinstance(module, types.ModuleType):
            mod_name = module
            if mod_name is None:
                mod_name = __name__
            try:
                if mod_name not in sys.modules:
                    __import__(mod_name)
                module = sys.modules[mod_name]
            except (ImportError, KeyError):
                import imp
                module = imp.new_module(mod_name)
                sys.modules[mod_name] = module
        else:
            mod_name = module.__name__

        if mtime is None:
            if (file_ is not None
                or source is not None):
                # the info is marked as outdated
                mtime = datetime.datetime.fromtimestamp(1)
            else:
                # the info is marked as very outdated
                mtime = datetime.datetime.fromtimestamp(0)

        if not hasattr(module, '__adhoc__'):
            adhoc = Attr()
            setattr(module, '__adhoc__', adhoc)
            setattr(adhoc, '__module__', module)

            mtime_set = None
            mode_set = mode
            if hasattr(module, '__file__'):
                module_file = module.__file__
                if module_file.endswith('.pyc'):
                    module_file = module_file[:-1]
                if os.access(module_file, os.R_OK):
                    stat = os.stat(module_file)
                    mtime_set = datetime.datetime.fromtimestamp(
                        stat.st_mtime)
                    mode_set = stat.st_mode
            if mtime_set is None:
                # the info is marked as very outdated
                mtime_set = datetime.datetime.fromtimestamp(0)
            adhoc.mtime = mtime_set
            adhoc.mode = mode_set
        else:
            adhoc = module.__adhoc__

        if (mtime > adhoc.mtime
            or not hasattr(module, '__file__')):
            if file_ is not None:
                setattr(module, '__file__', file_)
                if os.access(file_, os.R_OK):             # |:api_fi:|
                    stat = os.stat(file_)
                    adhoc.mtime = datetime.datetime.fromtimestamp(
                        stat.st_mtime)
                    adhoc.mode = stat.st_mode
                    if adhoc.mtime > mtime:
                        # the file on disk is newer than the adhoc'ed source
                        try:
                            delattr(adhoc, 'source')
                        except AttributeError:
                            pass
                        source = None

        if (mtime > adhoc.mtime
            or not hasattr(adhoc, 'source')):
            if source is not None:
                adhoc.source = source
                adhoc.mtime = mtime
                adhoc.mode = mode

        if not hasattr(adhoc, 'source'):
            try:
                file_ = module.__file__
                file_, source = cls.std_source_param(file_, source)
                adhoc.source = source
            except (AttributeError, IOError):
                pass

        return module

    @classmethod
    def std_source_param(cls, file_=None, source=None): # |:clm:||:api_fi:|
        if file_ is None:
            file_ = __file__
        if file_.endswith('.pyc'):
            file_ = file_[:-1]
        if source is None:
            source = cls.read_source(file_)
        return (file_, source)

    @classmethod
    def export_source(cls, string, no_remove=False, no_disable=False): # |:clm:|
        string = cls.collapse_macros(string)
        if not no_remove:
            string = cls.remove_sections(string, 'adhoc_remove')
        string = cls.remove_sections(string, 'adhoc_import')
        string = cls.remove_sections(string, 'adhoc_unpack')
        string = cls.remove_sections(string, 'adhoc_template_v')
        if not no_disable:
            string = cls.enable_sections(string, 'adhoc_disable')
            string = cls.disable_sections(string, 'adhoc_enable')
        if not no_remove:
            string = cls.section_tag_rename(string, 'adhoc_remove_', 'adhoc_remove')
        return string

    @classmethod
    def unpack(cls, file_=None, source=None):                # |:clm:|
        file_, source = cls.std_source_param(file_, source)
        source_sections, unpack_sections = cls.tag_partition(
            source, cls.section_tag('adhoc_unpack'))
        sv_extract_warn = cls.extract_warn
        cls.extract_warn = True
        unpack_call = ''.join((cls.__name__, '.unpack_'))
        for unpack_section in unpack_sections:
            unpack_section = re.sub('^\\s+', '', unpack_section)
            unpack_section = re.sub(
                '^[^(]*(?s)', unpack_call, unpack_section)
            try:
                #RtAdHoc = cls # unpack_call takes care of this
                exec(unpack_section.lstrip(), globals(), locals())
            except IndentationError:
                sys.stderr.write("!!! IndentationError !!!\n")
        cls.extract_warn = sv_extract_warn

    @classmethod
    def extract(cls, file_=None, source=None):               # |:clm:|
        cls.unpack(file_, source)
        cls.extract_templates(file_, source, export=True)

    @classmethod
    def export__(cls, mod_name=None, file_=None, mtime=None, # |:clm:||:api_fi:|
                 mode=None, zipped=True, flat=None, source64=None):
        source = cls.unpack_file(source64, zipped=zipped, decode=False)
        if file_ is None:
            return
        file_base = os.path.basename(file_)
        if file_base.startswith('__init__.py'):
            is_init = True
        else:
            is_init = False

        parts = mod_name.split('.')
        base = parts.pop()
        if parts:
            module_dir = os.path.join(*parts)
            cls.export_need_init[module_dir] = True
        else:
            module_dir = ''
        if is_init:
            module_dir = os.path.join(module_dir, base)
            cls.export_have_init[module_dir] = True
        module_file = os.path.join(module_dir, file_base)

        cls.export_(source, module_file, mtime, mode, flat)

    @classmethod
    def export_(cls, source, file_, mtime, mode, flat=None): # |:clm:|
        cflat = cls.flat
        if flat is None:
            flat = cflat
        cls.flat = flat
        if not flat:
            # extract to export directory
            sv_extract_dir = cls.extract_dir
            cls.extract_dir = cls.export_dir
            cls.extract(file_, source)
            cls.extract_dir = sv_extract_dir

            source_sections, import_sections = cls.tag_partition(
                source, cls.section_tag('adhoc_import'))
            source = cls.export_source(''.join(source_sections))
            export_call = ''.join((cls.__name__, '.export__'))

            xfile = cls.check_xfile(file_, cls.export_dir)
            if xfile is not None:
                cls.write_source(xfile, source, mtime, mode)
                if cls.verbose:
                    list(map(sys.stderr.write,
                             ("# xp: ", cls.__name__, ".export_ for `", file_,
                              "` using `", export_call,"`\n")))

            for import_section in import_sections:
                # this calls RtAdHoc.export__
                import_section = re.sub('^\\s+', '', import_section)
                import_section = re.sub(
                    '^[^(]*(?s)', export_call, import_section)
                try:
                    #RtAdHoc = cls # export_call takes care of this
                    exec(import_section, globals(), locals())
                except IndentationError:
                    sys.stderr.write("!!! IndentationError !!!\n")
        else:
            xfile = cls.check_xfile(file_, cls.export_dir)
            if xfile is not None:
                cls.write_source(xfile, source, mtime, mode)
                if cls.verbose:
                    list(map(sys.stderr.write,
                             ("# xp: ", cls.__name__, ".export_ for `", file_,
                              "` using `", export_call,"`\n")))
        cls.flat = cflat

    @classmethod
    def export(cls, file_=None, source=None):                # |:clm:|
        file_, source = cls.std_source_param(file_, source)
        sv_import = cls.import_
        cls.import_ = cls.export__

        file_ = os.path.basename(file_)
        cls.export_(source, file_, None, None, False)
        sv_extract_dir = cls.extract_dir
        cls.extract_dir = cls.export_dir
        engine_tag = cls.section_tag('adhoc_run_time_engine')
        engine_source = cls.export_source(
            source, no_remove=True, no_disable=True)
        engine_source = cls.get_named_template(
            None, file_, engine_source, tag=engine_tag, ignore_mark=True)
        if engine_source:
            efile = cls.check_xfile('rt_adhoc.py')
            if efile is not None:
                cls.write_source(efile, engine_source)
        cls.extract_dir = sv_extract_dir
        for init_dir in cls.export_need_init:
            if not cls.export_have_init[init_dir]:
                if cls.verbose:
                    list(map(sys.stderr.write,
                             ("# xp: create __init__.py in `", init_dir, "`\n")))
                inf = open(os.path.join(
                    cls.export_dir, init_dir, '__init__.py'), 'w')
                inf.write('')
                inf.close()
        cls.import_ = sv_import

    @classmethod
    def dump__(cls, mod_name=None, file_=None, mtime=None, # |:clm:||:api_fi:|
               mode=None, zipped=True, flat=None, source64=None):
        if cls.verbose:
            list(map(sys.stderr.write,
                     ("# xf: ", cls.__name__, ": dumping `", file_, "`\n")))
        source = cls.unpack_file(source64, zipped=zipped, decode=False)
        return source

    @classmethod
    def dump_(cls, dump_section, dump_type=None):            # |:clm:|
        if dump_type is None:
            dump_type = 'adhoc_import'
        if not dump_section:
            return ''
        dump_call = ''.join(('unpacked = ', cls.__name__, '.dump__'))
        dump_section = re.sub('^\\s+', '', dump_section)
        dump_section = re.sub(
            '^[^(]*(?s)', dump_call, dump_section)
        dump_dict = {'unpacked': ''}
        try:
            #RtAdHoc = cls # dump_call takes care of this
            exec(dump_section.lstrip(), globals(), dump_dict)
        except IndentationError:
            sys.stderr.write("!!! IndentationError !!!\n")
        return dump_dict['unpacked']

    @classmethod
    def dump_file(cls, match, file_=None, source=None, tag=None, # |:clm:|
                  is_re=False):
        file_, source = cls.std_source_param(file_, source)
        if tag is None:
            tag = cls.section_tag('(adhoc_import|adhoc_update)', is_re=True)
            is_re = True
        source_sections, dump_sections = cls.tag_partition(
            source, tag, is_re, headline=True)
        dump_call = ''.join((cls.__name__, '.dump_'))
        for dump_section in dump_sections:
            tagged_line = dump_section[0]
            dump_section = dump_section[1]
            tag_arg = cls.section_tag_strip(tagged_line)
            check_match = match
            if tag_arg != match and not match.startswith('-'):
                check_match = ''.join(('-', match))
            if tag_arg != match and not match.startswith('!'):
                check_match = ''.join(('!', match))
            if tag_arg != match:
                continue
            dump_section = re.sub('^\\s+', '', dump_section)
            dump_section = re.sub(
                '^[^(]*(?s)', dump_call, dump_section)
            try:
                #RtAdHoc = cls # dump_call takes care of this
                exec(dump_section.lstrip(), globals(), locals())
            except IndentationError:
                sys.stderr.write("!!! IndentationError !!!\n")

    macro_call_delimiters = ('@|:', ':|>')
    macro_xdef_delimiters = ('<|:', ':|@')
    macros = {}

    @classmethod
    def expand_macros(cls, source, macro_call_dlm=None, macro_xdef_dlm=None): # |:clm:|
        if macro_call_dlm is None:
            macro_call_dlm = cls.macro_call_delimiters
        if macro_xdef_dlm is None:
            macro_xdef_dlm = cls.macro_xdef_delimiters
        import re
        for macro_name, macro_expansion in cls.macros.items():
            macro_tag = cls.adhoc_tag(macro_name, macro_call_dlm, False)
            macro_tag_rx = cls.adhoc_tag(macro_name, macro_call_dlm, True)
            macro_call = ''.join(('# ', macro_tag, '\n'))
            macro_call_rx = ''.join(('^[^\n]*', macro_tag_rx, '[^\n]*\n'))
            mc_tag = ''.join(('# ', cls.adhoc_tag('adhoc_macro_call', macro_xdef_dlm, False), "\n"))
            mx_tag = ''.join(('# ', cls.adhoc_tag('adhoc_macro_expansion', macro_xdef_dlm, False), "\n"))
            xdef = ''.join((
                mc_tag,
                macro_call,
                mc_tag,
                mx_tag,
                macro_expansion,
                mx_tag,
                ))
            rx = re.compile(macro_call_rx, re.M)
            source = rx.sub(xdef, source)
        return source

    @classmethod
    def has_expanded_macros(cls, source, macro_xdef_dlm=None): # |:clm:|
        if macro_xdef_dlm is None:
            macro_xdef_dlm = cls.macro_xdef_delimiters
        mx_tag = cls.adhoc_tag('adhoc_macro_expansion', macro_xdef_dlm, False)
        me_count = len(cls.tag_lines(source, mx_tag))
        return me_count > 0

    @classmethod
    def activate_macros(cls, source, macro_call_dlm=None, macro_xdef_dlm=None): # |:clm:|
        if macro_xdef_dlm is None:
            macro_xdef_dlm = cls.macro_xdef_delimiters
        if not cls.has_expanded_macros(source, macro_xdef_dlm):
            source = cls.expand_macros(source, macro_call_dlm, macro_xdef_dlm)
        sv = cls.set_delimiters (macro_xdef_dlm)
        source = cls.remove_sections(source, 'adhoc_macro_call')
        source = cls.section_tag_remove(source, 'adhoc_macro_expansion')
        cls.reset_delimiters(sv)
        return source

    @classmethod
    def collapse_macros(cls, source, macro_xdef_dlm=None):   # |:clm:|
        if macro_xdef_dlm is None:
            macro_xdef_dlm = cls.macro_xdef_delimiters
        if cls.has_expanded_macros(source, macro_xdef_dlm):
            sv = cls.set_delimiters (macro_xdef_dlm)
            source = cls.section_tag_remove(source, 'adhoc_macro_call')
            source = cls.remove_sections(source, 'adhoc_macro_expansion')
            cls.reset_delimiters(sv)
        return source

    @classmethod
    def std_template_param(cls, file_=None, source=None,     # |:clm:|
                           tag=None, is_re=False, all_=False):
        file_, source = cls.std_source_param(file_, source)
        if tag is None:
            is_re=True
            if all_:
                tag = cls.section_tag('adhoc_(template(_v)?|import|unpack)', is_re=is_re)
            else:
                tag = cls.section_tag('adhoc_template(_v)?', is_re=is_re)
        source = cls.activate_macros(source)
        return (file_, source, tag, is_re)

    @classmethod
    def get_templates(cls, file_=None, source=None,          # |:clm:|
                      tag=None, is_re=False,
                      ignore_mark=False, all_=False):
        file_, source, tag, is_re = cls.std_template_param(
            file_, source, tag, is_re, all_)
        source = cls.enable_sections(source, 'adhoc_uncomment')
        source = cls.indent_sections(source, 'adhoc_indent')
        source_sections, template_sections = cls.tag_partition(
            source, tag, is_re=is_re, headline=True)
        templates = {}
        for template_section in template_sections:
            tagged_line = template_section[0]
            section = template_section[1]
            tag, tag_arg = cls.section_tag_parse(tagged_line)
            if not tag_arg:
                tag_arg = '-'
            if tag_arg in cls.template_process_hooks:
                section = cls.template_process_hooks[tag_arg](cls, section, tag, tag_arg)
            if ignore_mark:
                tag_arg = '-'
            if tag_arg not in templates:
                templates[tag_arg] = [[section], tag]
            else:
                templates[tag_arg][0].append(section)
        if all_:
            result = dict([(m, (''.join(t[0]), t[1])) for m, t in templates.items()])
        else:
            result = dict([(m, ''.join(t[0])) for m, t in templates.items()])
        return result

    @classmethod
    def template_list(cls, file_=None, source=None,          # |:clm:|
                      tag=None, is_re=False, all_=False):
        file_, source, tag, is_re = cls.std_template_param(
            file_, source, tag, is_re, all_)
        templates = cls.get_templates(file_, source, tag, is_re, all_=all_)
        if all_:
            templates.update([(k, ('', v)) for k, v in cls.extra_templates])
            result = list(sorted(
                [(k, v[1]) for k, v in templates.items()],
                key=lambda kt: '||'.join((
                    kt[1],
                    (((not (kt[0].startswith('-') or kt[0].startswith('!')))
                      and (kt[0]))
                     or (kt[0][1:]))))))
        else:
            templates.update(filter(
                lambda tdef: (tdef[1] == 'adhoc_template'
                              or tdef[1] == 'adhoc_template_v'),
                cls.extra_templates))
            result = list(sorted(
                templates.keys(),
                key=lambda kt: '||'.join((
                    (((not (kt.startswith('-') or kt.startswith('!')))
                      and (kt)) or (kt[1:]))))))
        return result

    @classmethod
    def col_param_closure(cls):                              # |:clm:|
        mw = [0, "", ""]
        def set_(col):                                       # |:clo:|
            lc = len(col)
            if mw[0] < lc:
                mw[0] = lc
                mw[1] = " " * lc
                mw[2] = "=" * lc
            return col
        def get_():                                          # |:clo:|
            return mw
        return set_, get_

    tt_ide = False
    tt_comment = ''
    tt_prefix = ''
    tt_suffix = ''

    @classmethod
    def template_table(cls, file_=None, source=None,         # |:clm:|
                       tag=None, is_re=False):
        file_, source, tag, is_re = cls.std_template_param(
            file_, source, tag, is_re, all_=True)
        pfx = cls.tt_prefix
        sfx = cls.tt_suffix
        comm = cls.tt_comment
        if comm:
            comm = ''.join((comm, ' '))
            pfx = ''.join((comm, pfx))
        if cls.tt_ide:
            command = ''.join(('python ', file_))
        else:
            command = os.path.basename(file_)
        # Parse table
        table = []
        tpl_arg_name = (lambda t: (((not (t.startswith('-') or t.startswith('!'))) and (t)) or (t[1:])))
        col_param = [cls.col_param_closure() for i in range(3)]
        table.append((col_param[0][0]('Command'), col_param[1][0]('Template'), col_param[2][0]('Type')))
        table.extend([
            (col_param[0][0](''.join((
                pfx,
                command, ' --template ',
                tpl_arg_name(t[0])
                )).rstrip()),
             col_param[1][0](''.join((
                 '# ', t[0]
                 )).rstrip()),
             col_param[2][0](''.join((
                 t[1], sfx
                 )).rstrip()),)
            for t in cls.template_list(file_, source, tag, is_re, all_=True)])
        if cls.tt_ide:
            itable = []
            headers = table.pop(0)
            this_type = None
            last_type = None
            for cols in reversed(table):
                this_type = cols[2].replace('")', '')
                if last_type is not None:
                    if last_type != this_type:
                        itable.append((''.join((comm, ':ide: +#-+')), '', ''))
                        itable.append((''.join((comm, '. ', last_type, '()')), '', ''))
                        itable.append(('', '', ''))
                itable.append((''.join((comm, ':ide: ', cols[1].replace('#', 'AdHoc:'))), '', ''))
                itable.append(cols)
                itable.append(('', '', ''))
                last_type = this_type
            if last_type is not None:
                itable.append((''.join((comm, ':ide: +#-+')), '', ''))
                itable.append((''.join((comm, '. ', last_type, '()')), '', ''))
            table = [headers]
            table.extend(itable)
        # Setup table output
        mw, padding = (col_param[0][1]()[0], col_param[0][1]()[1])
        mw1, padding1 = (col_param[1][1]()[0], col_param[1][1]()[1])
        mw2, padding2 = (col_param[2][1]()[0], col_param[2][1]()[1])
        sep = ' '.join([cp[1]()[2] for cp in col_param])
        make_row_c = lambda row: ''.join((
            ''.join((padding[:int((mw-len(row[0]))/2)], row[0], padding))[:mw],
            ' ', ''.join((padding1[:int((mw1-len(row[1]))/2)],
                          row[1], padding1))[:mw1],
            ' ', ''.join((padding2[:int((mw2-len(row[2]))/2)],
                          row[2], padding2))[:mw2].rstrip()))
        make_row = lambda row: ''.join((''.join((row[0], padding))[:mw],
                                        ' ', ''.join((row[1], padding))[:mw1],
                                        ' ', row[2])).rstrip()
        # Generate table
        output = []
        output.append(sep)
        output.append(make_row_c(table.pop(0)))
        if table:
            output.append(sep)
            output.extend([make_row(row) for row in table])
        output.append(sep)
        return output

    @classmethod
    def get_named_template(cls, name=None, file_=None, source=None, # |:clm:|
                           tag=None, is_re=False, ignore_mark=False):
        if name is None:
            name = '-'
        file_, source, tag, is_re = cls.std_template_param(
            file_, source, tag, is_re, all_=True)
        templates = cls.get_templates(
            file_, source, tag, is_re=is_re, ignore_mark=ignore_mark, all_=True)
        check_name = name
        if check_name not in templates and not name.startswith('-'):
            check_name = ''.join(('-', name))
        if check_name not in templates and not name.startswith('!'):
            check_name = ''.join(('!', name))
        if check_name in templates:
            template_set = templates[check_name]
        else:
            template_set = ['', 'adhoc_template']
        template = template_set[0]
        template_type = template_set[1]
        if check_name.startswith('!'):
            template = cls.dump_(template, template_type)
        return template

    @classmethod
    def extract_templates(cls, file_=None, source=None,      # |:clm:|
                          tag=None, is_re=False, ignore_mark=False,
                          export=False):
        file_, source, tag, is_re = cls.std_template_param(
            file_, source, tag, is_re)
        templates = cls.get_templates(
            file_, source, tag, is_re=is_re, ignore_mark=ignore_mark)
        sv_extract_warn = cls.extract_warn
        cls.extract_warn = True
        for outf, template in sorted(templates.items()):
            if outf.startswith('-'):
                outf = '-'
            if outf == '-' and export:
                continue
            xfile = cls.check_xfile(outf, cls.extract_dir)
            if xfile is not None:
                cls.write_source(xfile, template)
        cls.extract_warn = sv_extract_warn


    def compileFile(self, file_name, for_=None, zipped=True, forced=None): # |:mth:|
        file_name, source = self.std_source_param(file_name, None)
        return source
# @:adhoc_run_time_engine:@
# @:adhoc_remove:@
# @:adhoc_remove:@
# @:adhoc_run_time_engine:@
# @:adhoc_run_time_engine:@
# @:adhoc_remove:@
# @:adhoc_template:@ -

# @:adhoc_run_time:@ The run-time class goes here
# @:adhoc_run_time_engine:@ settings enabled at run-time
# @:adhoc_enable:@
# RtAdHoc.flat = False
# @:adhoc_template:@
RtAdHoc.flat = False
# @:adhoc_template:@ -
# @:adhoc_enable:@
# @:adhoc_run_time_engine:@

#import adhoc                                               # @:adhoc:@
# @:adhoc_template:@

# (progn (forward-line 1) (snip-insert-mode "py.b.sformat" t) (insert "\n"))
try:
    ('{0}').format(0)
    def sformat (fmtspec, *args, **kwargs):
        return fmtspec.format(*args, **kwargs)
except AttributeError:
    try:
        import stringformat
    except ImportError:
        try:
            # @:adhoc_import:@ !stringformat_local
            RtAdHoc.import_('stringformat_local', file_='stringformat_local.py',
                mtime='2012-09-18T15:26:21', mode=int("100666", 8),
                zipped=True, flat=None, source64=
                'H4sIALIkMGIC/81abW/bRhL+rl+xlSqQtGVGdpO0FSIbQZoABi6NEaeHHhSF'
                'oMWVxJoiVe7Stqr4v9/M7JLcJWXZbVHc+UOkcGdnZ56dd6rHjg6O2CyL4nQx'
                'YoWcH/2ATzrdbvd1dBOmMx4xIXNYZfMsX4VS6q/sYiOXWcpOx+zEf+53Oq9T'
                'Fq/WCV/xVIYyhqVszuSSs/BhPu7F2wv23fHw2EMGBTDMR+xdkuXAg/0az5Ii'
                'DVGUTgdYZ7lkOe90giBMkiBgYzZx3ile4VXCL4m7M2BOnMbSmcKeOVuGApZz'
                'F46GhXWYyxhFc7xRh8FfxOeseuiKARN8rZfwL+eyyFMmfIMGCDo8EXwE670S'
                'BEDgKfxkvqn/g38Jn8sBy+PFUoI6whfrJJZ4xoAdexUlv5vxtWT/DpOCv81z'
                'wMhiUkoJCqL2TlN8dQgxpZMAQXUFAaAS5BxOzrk/y1brOOEu7c4dt+857NG/'
                'HnP6jt7x1XXPXn2z9dyz0XbrHToP7thu6y1no/t779A9++b+4eNgy/19uWML'
                'WyZftlP1cT89/Lqlz4N778A701x6oNA6CWdki2we8yTqeLXWxVVLa1C44uN4'
                'yCHlQoLNthlVbNZ89iB6pXhnk1en4y9T76xUr8fCJF6kyK+knRwdsunZDv17'
                'TABpSdZDEvj8HB2oL4OzUturUHC2zvk8vhuwFZj/KkzYbRzJ5QA8MCtEmEYC'
                'LcAQ77P/OTr0msf2kM0sFmC+Ja1/5n3r7L4XuVlzAhaBCdDwHwTkbOR+nnhf'
                'P/tfv9hHgpISNjKIKI7v0MfEqeV0j73Jl+n04Ovkiz+ZHnh6c4/crGIOVKjS'
                '9Ou3nkuEWjMwnanDQHsWpzcAfMRkGCcgshkbcg5eEwQ3PEe1g6AMDqaXgM2A'
                'Xrbf+PBQhYIOawQDNodjBJMZwil4fsMpEv6SxhBpucKtjBeNY1y0OHBXI2yA'
                'rHAjKeAEYRSjSqH4eDvjgF5028JWrL1miNhDa0EVp5KwitOI39VIkRqxgMeS'
                'L3ju3mCkasfRkgst23z2h9Qn8DYA0uyVsEmWLkDfThV6NTw179kyd9M2Q3rM'
                '+uzkxUuQTkXgn8OVDsCmpN+ZfDGMy1zZD7CA/8K/nU6HjoIVBXQpoxFKxt2u'
                'FgLy3Tkom6fgxHbK5DmkSSQ5l3WuFWRaKhGyS+AUz+OZSsDvIRQc/StMF0W4'
                '4H7JnD5XpjmrSObD99kSU6VrLGhjASNIM8lWBk5hDFGnTkquc659bJal2pmY'
                'MOVxFCsKgAOKbYMqauloBWFjFQ7qIDQwmY3Zyl/kWbEWrhZKBGmx4nk8g7W2'
                'dc2TDJQInIpY2xAQGzsxOrQNrFRayUdEqH9Ntw+I1wldn+R0ccztebQZypbs'
                'lmMsYn2h75Q5nQezq6PR47kDhug2ZHZIPRUxlZk49V01aE0Qx8xJnVr6HvuJ'
                'z8MikRitnMih2i5Gs6JDFuoBnSWqTdalGMDSlkjJtFCa8QTEwbu24pnGUsvY'
                'iGNNPLuXsL2JoOUZrEKq65nHNPSeOX/6pNtYLlmpXreztxrqNoXBE7vVnZBt'
                'm8B/+vDTh1GVoDE/h3kos7wiWYdCYW4VjsDKdfdfsIAaxuCDf65tvs1diCiX'
                'rjOLsrtfwZC8/Uj9CZAtWwHJrEVyNgxFGG4Nz6Mzb2DBhQKTHZZueFhHBvju'
                'GqzJC0BudBQVARSjPbVz+/Z/Sa/T7DYtjYrieT8nB8iufuMzSS0NJG942mX9'
                'h63BkGygdPSDYJbAdQYBfEshjwRB7a2itDq4BedIFSwKGeiuhqbJECVQuQ7D'
                'Wv/QacBF64fwvWRNcbXm8AfPM0SVHk+GU7qxocGFFtCpU6mINIxVmWNweRfC'
                '09bOoa6G3oVCrkN4dLvkaV31gg2Sqjn/vYhzHlmCsldjaFdSN7/x9oQLwscl'
                'jiT/mAKOS1KVgZpWH7Nit4t7a9H2hpjHnH9XCNK1hL6OeZxASaXlVp+T0dHx'
                'VD+bHB2PpmayRfpaAfwfbKu0hGsjq9cZBPbUiHwxfHAdRtjcw1YF8VGJsGFW'
                '8paH11RHGM15rNr3cj/cWxZF5q2UK1AkNXC+YYdjEti2zvzGn3EsbVyd7pHE'
                'q9PEU670b6SRf/iyQR7ltK/YEKVveHULIsQDXRDddQJX7+e/FUJ7HdzSsQlP'
                '2wdNUI2ND2BKIeMUQ8aYUkOrmtgFMDTBmkLppeYURAWYXW2wfsbKofNkeUwF'
                'SuJkN3HtOrp41jUp9ZplkYdNoFA14oDSLhSSYSqDq43kYkzxqS6qdYkctnt6'
                'v6yKMdJfK7YDFiBqdIJlc9f2HcRq4uPHIooXsXQbIcdMcvQ5wciKO7ypRdi+'
                '3fZW3DbdYw8l9YJLsxSm0zpGtq53lTtcyljkejkYCMWXfq4CTB+riUZaNXpC'
                'o95WN1S1hS0F/JrGpd6iNtMmN2yVZLziWhikfohpSUqdi9Gy2PhUlUarCasl'
                'wTRUmY8aG7TaynbvXc7fpFXB6Kf0BEyYkj9rjStdVVfURvqG6G6X8Wxptngr'
                'DmVipKOT6+k28BOE58YKu+LL8AakT+JrjjL51Qpac9lbvzzULE5PT3dIVTjb'
                'cPTi3vHK3eH4+YnSy/d9CAyXUMGwULCSsE1X4KDm+YnTqdpO1RQHIsmkoPGt'
                'o/p/jErB9W2WR4K+qskbfRXVTLceUOCDTt2+BzjtRXviybxuqInMuCNc9dVx'
                'VYlSP1eHw8L2vrGip4C0Yi9ZJwGB9f8Gl4qoOetRy1DTgovypvSmkvz3SsUM'
                'knL+4HSIVgftK909K9qlyVid4O9WqMfeZCuUlkH9RlNGSFZYJmSQHeJ6ZOF3'
                'nn6UoaiGQqtKAwkrIb2BjM3J2hkPwUXaodyoe3IcqhMPNTZwh16nEbYp4vWd'
                'neA4/b7TpNclM32Fys3ep2bbFDPv7+0+B5yaw2nlkSWrA6rF6vjckIDIRhUJ'
                'e/aMnUwNYNdYEBLRMdaRRqkISEACswZMmlS9mlDTPWdkVP5JDIVZmOg3BVbX'
                'Vu/TnJ1vHAtK2FJVEfXOx+oxDjugodIlF8S8hLMky67LN0yPFWHtOVOzHkPo'
                'aiqPnbLjR4W6A1bo8wAOC+eAydNnDGWxl4vw0UlD2WvuUoL1xd72kiILpBtD'
                'tVokai6pbKGAY47m/TlEQPAgV9+1jZV6NhkdT0kJf+I0zft1IbMjqAmvuBUT'
                'KiOoYyw0Cz9n6Y6Cpg3ELEwRNwGRBBx6nmcr8NkUYwvJ/pgVmOW4HntK6BlA'
                'UrgzKF0Vk0roru1oCJYa2bqG+DaNqRe0NcdNvVF6DV5b34gnxo2Az+8p37Qw'
                'Nbm/zjBoTY6nrTOBpi45VYlkw49S7b6CHnuv8LVQa5HZNzraeQtPus3mXTzh'
                'QulSqzvDC7VMwhK8caPtbI8o1Kiv1nITYKkZXxWSt6YYugOAdgLfFKEj1Ncx'
                '2nXzN21k2md8ygve3Iz8n+IfH9JkY7waAyQ2ICU2rvRy6ynuEVcjLQu/ZiQz'
                'Igca1DUlx4lTRfYyQkCqoaXpo0HufSwEXiAKWguh0r99dgOzxxi/RXJWQ7yf'
                'ubM1jg/sXkJfupEl7ffE/p46rWoc7JFljaOZR/dsM2tNX3Cp+2piNGCTqeeH'
                '6zVkS2tq88A44K+ermrgJ59etudQJLl94Ql8QxErkqqa0z2BquUOwnwBEh0c'
                'XN/iN6Oqg96gbCesfgXNTndbVhNzYTQxZeNeTsCAs42JOs0v1lEouRvFM+lS'
                'nxh7ejDrPeY/c5qWlNQoAKexCPIjTTxzkvY2pakxLBT65VzGXl++OT8foHyW'
                'jWKUpk6zHqHWzefYeuVrdBED3O2ZVW64arQuKLG6PHBYWIxT+47paXNQUfbH'
                'CrAJ7p82nYT4ITvi0A5erXEMqgGkuwhB6gldROQiiedNDdd7ZMjztATS+qvh'
                '9R7HSnvj/x4rvUYffY3c/zGgZrtXNnqV2J1Oj5pF8pErjjkMnKAQUG5jjs/S'
                'a74BWiwdroo4keABavhHzwL9LMBXMNWl9KrWE/IkFRxLKddi9OzZIhbShwJp'
                'WVzh71Genfz44mQ4ZO7rfAX38tHXQx/1y7IZMTWfiI3o6BPm8aKAljcr4Gn8'
                'B8euJbjYBAL/E8jmREyx8tWwJVxD7HCA+DyN5fssKhL+PHj53JyRGazw9wJq'
                '9wzf1L18vmOS9TC5EleNmoDqA82WSnEuZV7M4G7M0VX1grGi9pWpCPp5XUXn'
                'Ohnmwvkslc7AFMAb2DR4FFDoIy8+nP/86e1Ht+LuafppCaweSKkpQg6dfBNL'
                'uASAb8GlGpSJBm4NoSfDETbohuRKsgBES/mdfIJo9iZI+TdP3DS10P8JMs1F'
                'nt1tDGJDcgNk18GstPeQaZ1TAQn9IpFy2SwxM2lkzH5hhYaySBYEwB7LYKsq'
                'KiHGfh4aDWf3iMh64xPtbuxUffYJxNc/gFjENzzVUEQZV90IziVZyFAgKEjC'
                'fGPMEKDsoHhZ2XPlPP7FBrEMLrk8N8Nj2kh6PfaR33BoEZA/TkGh/GfVLdQQ'
                'rTEqVs99DBhBGEU5FwJDZ+S1hKr9OVBG6KbCG7DWUwJ4ACf4KEIrIqZighTT'
                'v1QflQVQk4odnepqoh5PflTnhdWvhiJWvSWfs8sBxFsMylDXCtCvwMsQulMD'
                'lqr0V1VTxRIHzTY9TgDjCCoc7CPoZdAVuq8Av9mqjsHB8bGpRBOQ9tgZkfAe'
                'UrUMGZ+WsTYq+nExhDS4dCt1ZDSMN+vH6uUOeIV+2VdN8mugd/jWRA+enWk1'
                '4tXvo3DsjL+TmnHrPZMq8mY4D9VGb/4AWTMzI8HOzKbPQDwguVYvlXRiwlIW'
                'X3jQs3fYwjaR7JTRoCT1qfw9GR4PB+zHAftez+iBokRIo4tZKg4TCO7qRNQS'
                'u1cNv55jvnMLt7sdjrb02u7e31Y/y7gX912vukNnyaFRZVB2JpFjx1faOf7B'
                '+K3X+IWHbWVR7mKs/MGYcSha4oaHOQai7dDHr+aBkWZh0aHa3R2s1GwfrAU0'
                '6f/nqL866ke7mVWUyOpo+OPR8PuujchePP4ROB4E409isQeJvwLEwzD8HRRq'
                'DKyzdgJgS93W3uawW/Umj116K7XXOb7QdZACQuQMQqCYF4mjfjdb/tSHVAiC'
                'VRjj74uVM9fO3fkvH0tTUIUxAAA=')
            # @:adhoc_import:@
            import stringformat_local as stringformat      # @:adhoc:@
        except ImportError:
            printf('error: (adhoc) stringformat missing.'
                   ' Try *easy_install stringformat*.', file=sys.stderr)
            exit(1)
    def sformat (fmtspec, *args, **kwargs):
        return stringformat.FormattableString(fmtspec).format(
            *args, **kwargs)

import base64
import urllib

#import something.non.existent                              # @:adhoc:@
try:
    import namespace_dict
except ImportError:
    # @:adhoc_import:@ !namespace_dict
    RtAdHoc.import_('namespace_dict', file_='namespace_dict.py',
        mtime='2012-10-02T21:18:04', mode=int("100666", 8),
        zipped=True, flat=None, source64=
        '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'
        'mKRFnJdDOoOzv7wJz8COK5LrPiuhBP8oc4U3B4Vn0t4UID1hcbEdiFicIqrbAYffw3mW'
        'LV3gAN5w439Q6ePHj6MinozgL3v645N37569ux2ojRs0CSnWcZHNwQ9X4bhtsGqCS3mY'
        'kHgRZjkAj6chJgdsBzQWz+OiaOgEJ7jhvlW0ATpoSpzVOeizaPKBQBQ3i7NsPsTstAPW'
        'BwUxXwCb+qPRtvr91ZOXz969efL0GUjA63c/vb21CAg9cBVHH/J41tN0heze0WM27PFr'
        'KF6Bknu3BAl49c7Pzv4VT8oOi2lIOL+NgitXF4YeDy14TwkNLmZMySYtEBnffocbUK0P'
        'IZ8Cji5i+pyJC8bLOJ9hNdrmFGtwCMYkStlZTBMjAstS9pCgzONLsFBHHOR+KArQXs/D'
        'vRFodl5dgadyB2a5/ZFViEivCOA8o5oPzZoHa2py/mv1Pbkq2NBhZHDiydjJxLI402zM'
        'b2YfL4rzygNt70mcH2fpRF9YLihq1vfq+8rhlT319wXtdEN8mml3w2N9PnlCvdrcKd0U'
        'wCZTK5sahYuvmzWs3iiBtQ9C4pW4nFsR2l+DfhrPt4weIMbAoG4UgA5bgmK6UYtowO+B'
        'LmLOg1/E6vbHXm1utwenkLlXTolU2JnAHnrajvgWCaUVMqgLkiQ0UAj/Q9oNUxAXOs/+'
        'BSJGSLUTpVS+yLGZ2DAen/Mz88djzoh1Eu72qKQBt4LG8R5FYsFuDxUC6hnAYt7HwumS'
        '0SKNmsAis6iTOWB026eTWjeZTvoqyDrQRgqLJgrF8fR3Y6STwgpyO/NUOfNkmUq02SO2'
        'bx3tQKRP6FQP7hE8iPJzwP7gAU7Q54XDqRKdzekLZW27niNdqaKUqgQuSsDdisB0uAs5'
        'FYjNaFL1XIThxgcYlXegq4KwEVmqmouq+Jc7EESVN6IFa7jIOI/vQAZV3ogMrOEmo7xj'
        'H1UQNiSobO6j8/IuBJUb01K6yUCX4Q6EiOobkcLruIjBHUR3IEZU34gYXsdFzPwu0jvf'
        'WHrncRMZ6Z3oSDcnJG2g5C4SO99YYucNEpvepV/SjfslbeiX4s5apbidVinatEqR/Bpn'
        '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')
    # @:adhoc_import:@
    import namespace_dict                                  # @:adhoc:@

# copy of ws_prop_dict.dict_dump
def dict_dump(dict_, wid=0, trunc=0, commstr=None, tag=None, out=None): # ||:fnc:||
    '''Dump a dictionary.'''

    if out is None:
        out = sys.stderr
    if commstr is None:
        commstr = ((('dbg_comm' in globals()) and (globals()['dbg_comm'])) or ('# '))

    dbg_twid = ((('dbg_twid' in globals()) and (globals()['dbg_twid'])) or (9))
    if tag is None:
        tag = ':DBG:'

    max_wid = 0
    for key in dict_.keys():
        _wid = len(key)
        if max_wid < _wid:
            max_wid = _wid

    dbg_fwid = ((('dbg_fwid' in globals()) and (globals()['dbg_fwid'])) or (max_wid))
    if dbg_fwid < max_wid:
        dbg_fwid = max_wid

    printf(sformat('{0}{1}', commstr, '-' * 30), file=out)
    indent = (sformat("{0}{3:^{1}} {4:<{2}s}:  ",
            commstr, dbg_twid, dbg_fwid,
            '', ''))

    for key, value in sorted(dict_.items()):
        value = str(value)
        value = value.replace('\n', '\\n')
        value = value.replace('\r', '\\r')
        value = value.replace('\t', '\\t')
        value = value.replace('\f', '\\f')
        if wid == 0:
            wid = 78 - len(indent) - 1
            if wid < 50:
                wid = 50
        start = 0
        limit = len(value)
        value_lines = []
        while start < limit:
            line = value[start:start+wid]
            space_pos = wid - 1
            if len(line) == wid:
                space_pos = line.rfind(' ')
                if space_pos > 0:
                    line = line[:space_pos + 1]
                else:
                    space_pos = wid - 1
            value_lines.append(line)
            start += space_pos + 1
        if trunc > 0:
            value_lines = value_lines[:trunc]
        value_lines[-1] = sformat('{0}[', value_lines[-1])
        printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}",
                commstr, dbg_twid, dbg_fwid,
                tag, key, value_lines[0]), file=out)
        for line in value_lines[1:]:
            printf(sformat('{0}{1}',indent, line), file=out)

def dump_attr(obj, wid=0, trunc=0, commstr=None,           # ||:fnc:||
              tag=None, out=None):
    if out is None:
        out = sys.stdout
    dict_dump(
        vars(obj), wid=wid, trunc=trunc, commstr=commstr, tag=tag, out=out)

printe = printf

# (progn (forward-line 1) (snip-insert-mode "py.b.posix" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.b.os.system.sh" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.b.prog.path" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.b.line.loop" t) (insert "\n"))

# --------------------------------------------------
# |||:sec:||| CLASSES
# --------------------------------------------------

# (progn (forward-line 1) (snip-insert-mode "py.c.placeholder.template" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.c.key.hash.ordered.dict" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.c.progress" t) (insert "\n"))

# --------------------------------------------------
# |||:sec:||| EXCEPTION
# --------------------------------------------------

class AdHocError(Exception):                               # ||:cls:||
    pass

# --------------------------------------------------
# |||:sec:||| ADHOC
# --------------------------------------------------

# @:adhoc_run_time_section:@ START
import sys
import os
import re

# @:adhoc_uncomment:@
# @:adhoc_template:@ -catch-stdout
try:
    from cStringIO import StringIO as _AdHocBytesIO, StringIO as _AdHocStringIO
except ImportError:
    try:
        from StringIO import StringIO as _AdHocBytesIO, StringIO as _AdHocStringIO
    except ImportError:
        from io import BytesIO as _AdHocBytesIO, StringIO as _AdHocStringIO

# @:adhoc_template:@
# @:adhoc_uncomment:@
# @:adhoc_run_time_section:@ off
if not hasattr(os.path, 'relpath'):
    def relpath(path, start=os.curdir):
        """Return a relative version of a path"""

        if not path:
            raise ValueError("no path specified")

        start_list = os.path.abspath(start).split(os.sep)
        path_list = os.path.abspath(path).split(os.sep)

        # Work out how much of the filepath is shared by start and path.
        i = len(os.path.commonprefix([start_list, path_list]))

        rel_list = [os.pardir] * (len(start_list)-i) + path_list[i:]
        if not rel_list:
            return os.curdir
        return os.path.join(*rel_list)
    os.path.relpath = relpath
    del relpath

AH_CHECK_SOURCE = '''\
not in section
# >:cmd:< arg0 arg1 # comment
# <:tag:> on
in section
# >:cmd:< arg2 arg3 # comment
in section
# <:tag:> off
not in section
# <:tag2:> on
in section
in section
# <:tag2:> off
not in section
'''

# @:adhoc_run_time_section:@ on
# @:adhoc_run_time_class:@
class AdHoc(object):                                     # |||:cls:|||
    # @:adhoc_run_time_section:@ off
    """
    :class:`AdHoc` is mainly used as a namespace, which is partially
    included verbatim as :class:`RtAdHoc` in the generated output.

    It is only instantiated for compiling adhoc output
    (:meth:`compileFile`, :meth:`compile`).

    **Attributes**

    The following class attrbutes determine the operation of AdHoc:

    - :attr:`line_delimiters`
    - :attr:`section_delimiters`
    - :attr:`template_process_hooks`
    - :attr:`extra_templates`
    - :attr:`export_dir`
    - :attr:`extract_dir`
    - :attr:`flat`
    - :attr:`frozen`
    - :attr:`quiet`
    - :attr:`verbose`
    - :attr:`debug`

    Run-time class attributes can be set like this:

    | # |adhoc_run_time|
    | # |adhoc_enable|
    | # RtAdHoc.flat = False
    | # RtAdHoc.frozen = True
    | # |adhoc_enable|

    or like this:

    | # |adhoc_run_time|
    | if 'RtAdHoc' in globals():
    |     RtAdHoc.flat = False
    |     RtAdHoc.frozen = True

    **Low-Level Functions**

    :meth:`adhoc_tag` constructs a delimited tag or tag regular
    expression:

    >>> adhoc_tag = AdHoc.adhoc_tag
    >>> delimiters = ('<:', ':>')

    >>> tag_sym = 'my_tag'
    >>> adhoc_tag(tag_sym, delimiters)
    '<:my_tag:>'

    >>> tag_rx = 'my_[^:]+'
    >>> adhoc_tag(tag_rx, delimiters, is_re=True)
    '\\\\<\\\\:my_[^:]+\\\\:\\\\>'

    :meth:`tag_split` splits a string into tagged line parts and
    untagged parts.

    :meth:`adhoc_parse_line` splits a tagged line into a tag symbol and
    additional arguments:

    >>> adhoc_parse_line = AdHoc.adhoc_parse_line
    >>> tagged_line = 'anything # <:my_tag:>  additonal arguments # end comment'

    >>> adhoc_parse_line(tagged_line, tag_sym, delimiters)
    ('my_tag', 'additonal arguments # end comment')

    >>> adhoc_parse_line(tagged_line, tag_rx, delimiters, is_re=True)
    ('my_tag', 'additonal arguments # end comment')

    >>> adhoc_parse_line(tagged_line, tag_rx, delimiters, is_re=True, strip_comment=True)
    ('my_tag', 'additonal arguments')

    **Low-Level Convenience Functions**

    *Tag Generation*

    :meth:`line_tag`, :meth:`section_tag`

    >>> class ah(AdHoc):
    ...     line_delimiters = ('>:', ':<')
    ...     section_delimiters = ('<:', ':>')

    >>> ah.line_tag('tag-symbol')
    '>:tag-symbol:<'

    >>> ah.line_tag('tag.?rx', True)
    '\\\\>\\\\:tag.?rx\\\\:\\\\<'

    >>> ah.section_tag('tag-symbol')
    '<:tag-symbol:>'

    >>> ah.section_tag('tag.?rx', True)
    '\\\\<\\\\:tag.?rx\\\\:\\\\>'

    *Tagged Line/Section Retrieval*

    :meth:`tag_lines`, :meth:`tag_partition`, :meth:`tag_sections`

    >>> source = AH_CHECK_SOURCE

    >>> line_tag = ah.line_tag('cmd')
    >>> tagged_lines = ah.tag_lines(source, line_tag)
    >>> adhoc_dump_list(tagged_lines, 40)
    #   :DBG:   elt[0]                 : ]'# >:cmd:< arg0 arg1 # comment\\n'[
    #   :DBG:   elt[1]                 : ]'# >:cmd:< arg2 arg3 # comment\\n'[

    >>> is_re = True
    >>> section_tag_rx = ah.section_tag('tag.?', is_re=is_re)
    >>> body, sections = ah.tag_partition(source, section_tag_rx, is_re=is_re)
    >>> adhoc_dump_list(body, 40)
    #   :DBG:   elt[0]                 : ]'not in section\\n# >:cmd:< arg0 arg1 #  ...'[
    #   :DBG:   elt[1]                 : ]'not in section\\n'[
    #   :DBG:   elt[2]                 : ]'not in section\\n'[
    >>> adhoc_dump_list(sections, 40)
    #   :DBG:   elt[0]                 : ]'in section\\n# >:cmd:< arg2 arg3 # comm ...'[
    #   :DBG:   elt[1]                 : ]'in section\\nin section\\n'[

    >>> body, sections = ah.tag_partition(source, section_tag_rx, is_re=is_re, headline=True)
    >>> adhoc_dump_sections(sections, 40)
    #   :DBG:   section[0]             : ]['# <:tag:> on\\n', 'in section\\n# >:cmd:< arg2 arg3 # comm ...'][
    #   :DBG:   section[1]             : ]['# <:tag2:> on\\n', 'in section\\nin section\\n'][

    >>> sections = ah.tag_sections(source, section_tag_rx, is_re=is_re, headline=True)
    >>> adhoc_dump_sections(sections, 40)
    #   :DBG:   section[0]             : ]['# <:tag:> on\\n', 'in section\\n# >:cmd:< arg2 arg3 # comm ...'][
    #   :DBG:   section[1]             : ]['# <:tag2:> on\\n', 'in section\\nin section\\n'][

    *Tagged Line Parsing*

    - :meth:`line_tag_parse`, :meth:`line_tag_strip`
    - :meth:`section_tag_parse`, :meth:`section_tag_strip`

    >>> strclean(ah.line_tag_parse(tagged_lines[0], 'cmd'))
    ('cmd', 'arg0 arg1 # comment')

    >>> strclean(ah.line_tag_strip(tagged_lines[0], 'cmd', strip_comment=True))
    'arg0 arg1'

    >>> strclean(ah.section_tag_parse(sections[1][0], 'tag.?', is_re=True))
    ('tag2', 'on')

    >>> strclean(ah.section_tag_strip(sections[1][0], 'tag.?', is_re=True))
    'on'

    **Tagged Line/Section Transformations**

    - :meth:`transform_lines`, :meth:`transform_sections`
    - :meth:`line_tag_rename`, :meth:`line_tag_remove`
    - :meth:`section_tag_rename`, :meth:`section_tag_remove`
    - :meth:`indent_sections`
    - :meth:`enable_sections`, :meth:`disable_transform`, :meth:`disable_sections`
    - :meth:`remove_sections`

    **IO Functions**

    - :meth:`check_coding`
    - :meth:`decode_source`, :meth:`encode_source`
    - :meth:`read_source`, :meth:`write_source`
    - :meth:`check_xfile`
    - :meth:`pack_file`, :meth:`unpack_file`

    **Run-Time Unpack/Import Interface**

    - :meth:`unpack_`
    - :meth:`import_`, :meth:`module_setup`

    **Export Tools**

    - :meth:`std_source_param`
    - :meth:`export_source`

    **Extract Interface**

    - :meth:`unpack`
    - :meth:`extract`

    **Export Interface**

    - :meth:`export__`, :meth:`export_`, :meth:`export`

    **Dump Interface (Import/Unpack Substitute)**

    - :meth:`dump__`, :meth:`dump_`, :meth:`dump_file`

    **Macro Interface**

    Naive macro expansion would violate the condition
    ``xsource_i === source_i``.

    Here is a simple macro system which preserves the bijectivity
    condition. It is quite useful for conditional templating. (See
    `Use Cases`_ generator scripts).

    *Limitations*

    - Macro expansions are not prefixed with the current indentation
    - Macros cannot be nested

    *Attributes*

    - :attr:`macro_call_delimiters`

      Delimiters for macros, e.g.: ``@|:MACRO_NAME:|>``

    - :attr:`macro_xdef_delimiters`

      Delimiters for macro expansion, e.g.::

          # <|:adhoc_macro_call\x3a|@
          # @|:MACRO_NAME:|>
          # <|:adhoc_macro_call\x3a|@
          # <|:adhoc_macro_expansion\x3a|@
          The macro definition ...
          The macro definition ...
          # <|:adhoc_macro_expansion\x3a|@

    - :attr:`macros`

      Macro definitions.

    *Methods*

    - :meth:`expand_macros`
    - :meth:`has_expanded_macros`
    - :meth:`activate_macros`
    - :meth:`collapse_macros`

    **Template Interface**

    - :meth:`std_template_param`
    - :meth:`get_templates`
    - :meth:`template_list`, :meth:`col_param_closure`, :meth:`template_table`
    - :meth:`get_named_template`
    - :meth:`extract_templates`

    **Template Extraction (uncompiled)**

    - Expand and activate macros for uncompiled source
    - Activate macros on compiled source

    **Compile**

    - Expand macros before compilation

    **Export**

    - Collapse macros on export of compiled source.

    **Compilation Attributes**

    - :attr:`include_path`

    **Compilation Interface**

    - :meth:`setup_tags`
    - :meth:`strquote`
    - :meth:`adhoc_run_time_sections_from_string`
    - :meth:`adhoc_run_time_section_from_file`
    - :meth:`adhoc_get_run_time_section`
    - :meth:`prepare_run_time_section`
    - :meth:`verbatim_`
    - :meth:`include_`
    - :meth:`encode_module_`
    - :meth:`compile_`

    **User API**

    - :meth:`encode_include`
    - :meth:`encode_module`
    - :meth:`compile`
    - :meth:`compileFile`

    .. \\|:here:|
    """
    # @:adhoc_run_time_section:@ on
    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Attributes
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    line_delimiters = ('@:', ':@')
    # @:adhoc_run_time_section:@ off
    '''Tag delimiters for lines.'''
    # @:adhoc_run_time_section:@ on
    section_delimiters = ('@:', ':@')
    # @:adhoc_run_time_section:@ off
    '''Tag delimiters for sections.'''
    # @:adhoc_run_time_section:@ on

    template_process_hooks = {}
    # @:adhoc_run_time_section:@ off
    '''Dictionary of ``template-name, hook-function`` items.

    If the name of a template section matches an item in this
    dictionary, the ``hook-function`` is called::

        section = hook-function(cls, section, tag, template_name)
    '''
    # @:adhoc_run_time_section:@ on
    extra_templates = []
    # @:adhoc_run_time_section:@ off
    '''List of additional templates::

        [(name, type), ...]
    '''
    # @:adhoc_run_time_section:@ on

    export_dir = '__adhoc__'
    # @:adhoc_run_time_section:@ off
    '''Export directory (for :meth:`export`, ``--explode``).'''
    # @:adhoc_run_time_section:@ on
    extract_dir = '.'
    # @:adhoc_run_time_section:@ off
    '''Export directory (for :meth:`extract`, ``--extract``).'''
    # @:adhoc_run_time_section:@ on
    flat = True
    # @:adhoc_run_time_section:@ off
    '''If True, do not export files recursively.'''
    # @:adhoc_run_time_section:@ on
    forced = False
    # @:adhoc_run_time_section:@ off
    '''If True, allow duplicate imports.'''
    # @:adhoc_run_time_section:@ on

    frozen = False
    # @:adhoc_run_time_section:@ off
    '''If True, do not attempt to load modules from external
    sources (\\|:todo:| not implemented).'''
    # @:adhoc_run_time_section:@ on

    quiet = False
    # @:adhoc_run_time_section:@ off
    '''If True, suppress warnings.'''
    # @:adhoc_run_time_section:@ on
    verbose = False
    # @:adhoc_run_time_section:@ off
    '''If True, display messages.'''
    # @:adhoc_run_time_section:@ on
    debug = False
    # @:adhoc_run_time_section:@ off
    '''If True, display debug messages.'''
    # @:adhoc_run_time_section:@ on

    include_path = []
    # @:adhoc_run_time_section:@ off
    '''Search path for include files. Only relevant during compilation.'''
    # @:adhoc_run_time_section:@ on
    export_need_init = {}
    export_have_init = {}
    extract_warn = False

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Low-Level Functions
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    def _adhoc_string_util():
        # @:adhoc_run_time_section:@ off
        '''Define string utilities.

        - static method :meth:`isstring`
        - unicode type :attr:`uc_type`
        - static method :meth:`uc`
        '''
        # @:adhoc_run_time_section:@ on
        def isstring(obj):
            return isinstance(obj, basestring)
        try:
            isstring("")
        except NameError:
            def isstring(obj):
                return isinstance(obj, str) or isinstance(obj, bytes)
        def _uc(string):
            return unicode(string, 'utf-8')
        try:
            _uc("")
        except NameError:
            _uc = lambda x: x
        uc_type = type(_uc(""))
        def uc(value):
            if isstring(value) and not isinstance(value, uc_type):
                return _uc(value)
            return value
        return staticmethod(isstring), uc_type, staticmethod(uc)

    isstring, uc_type, uc = _adhoc_string_util()

    @staticmethod
    def adhoc_tag(symbol_or_re, delimiters, is_re=False):    # |:fnc:|
        # @:adhoc_run_time_section:@ off
        '''Make a tag from symbol_or_re and delimiters.

        :param symbol_or_re: symbol string or regular expresssion.
        :param delimiters: tuple of delimiter strings
          ``(prefix, suffix)``.
        :param is_re: if True, escape the delimiters for regular
          expressions.
        '''
        # @:adhoc_run_time_section:@ on
        ldlm = delimiters[0]
        rdlm = delimiters[1]
        if is_re:
            ldlm = re.escape(ldlm)
            rdlm = re.escape(rdlm)
        return ''.join((ldlm, symbol_or_re, rdlm))

    @classmethod
    def tag_split(cls, string, tag, is_re=False):            # |:fnc:|
        # @:adhoc_run_time_section:@ off
        """Split string with tag line.

        :returns:
          a list of tuples with a flag and a section::

            [(is_tag, section), ... ]

        **Example**

        >>> source = AH_CHECK_SOURCE
        >>> printf(str(source), end='')
        not in section
        # >:cmd:< arg0 arg1 # comment
        # <:tag:> on
        in section
        # >:cmd:< arg2 arg3 # comment
        in section
        # <:tag:> off
        not in section
        # <:tag2:> on
        in section
        in section
        # <:tag2:> off
        not in section

        **Split on literal tag**

        >>> is_re = False
        >>> tag = AdHoc.adhoc_tag('tag', ('<:', ':>'), is_re)
        >>> parts = AdHoc.tag_split(source, tag, is_re)
        >>> adhoc_dump_sections(parts, 40)
        #   :DBG:   section[0]             : ][False, 'not in section\\n# >:cmd:< arg0 arg1 #  ...'][
        #   :DBG:   section[1]             : ][True, '# <:tag:> on\\n'][
        #   :DBG:   section[2]             : ][False, 'in section\\n# >:cmd:< arg2 arg3 # comm ...'][
        #   :DBG:   section[3]             : ][True, '# <:tag:> off\\n'][
        #   :DBG:   section[4]             : ][False, 'not in section\\n# <:tag2:> on\\nin secti ...'][

        **Split on tag regexp**

        >>> is_re = True
        >>> tag = AdHoc.adhoc_tag('tag.?', ('<:', ':>'), is_re)
        >>> parts = AdHoc.tag_split(source, tag, is_re)
        >>> adhoc_dump_sections(parts, 40)
        #   :DBG:   section[0]             : ][False, 'not in section\\n# >:cmd:< arg0 arg1 #  ...'][
        #   :DBG:   section[1]             : ][True, '# <:tag:> on\\n'][
        #   :DBG:   section[2]             : ][False, 'in section\\n# >:cmd:< arg2 arg3 # comm ...'][
        #   :DBG:   section[3]             : ][True, '# <:tag:> off\\n'][
        #   :DBG:   section[4]             : ][False, 'not in section\\n'][
        #   :DBG:   section[5]             : ][True, '# <:tag2:> on\\n'][
        #   :DBG:   section[6]             : ][False, 'in section\\nin section\\n'][
        #   :DBG:   section[7]             : ][True, '# <:tag2:> off\\n'][
        #   :DBG:   section[8]             : ][False, 'not in section\\n'][

        **Assemble section**

        >>> section = []
        >>> in_section = False
        >>> for part in parts:
        ...     if part[0]:
        ...         in_section = not in_section
        ...         continue
        ...     if in_section:
        ...         section.append(part[1])
        >>> section = ''.join(section)
        >>> printf(str(section), end='')
        in section
        # >:cmd:< arg2 arg3 # comment
        in section
        in section
        in section
        """
        # @:adhoc_run_time_section:@ on
        if not is_re:
            tag = re.escape(tag)
        ro = re.compile(''.join(('^[^\n]*(', tag, ')[^\n]*$')), re.M)
        result = []
        last_end = 0
        string = cls.decode_source(string)
        for mo in re.finditer(ro, string):
            start = mo.start(0)
            end = mo.end(0)
            result.append((False, string[last_end:start]))
            result.append((True, string[start:end+1]))
            last_end = end+1
        result.append((False, string[last_end:]))
        return result

    @classmethod
    def adhoc_parse_line(cls, tagged_line, symbol_or_re=None, # |:clm:|
                         delimiters=None, is_re=False, strip_comment=None):
        # @:adhoc_run_time_section:@ off
        """Parse a tagged line into tag-symbol and argument parts.

        :returns: a tuple ``(tag-symbol, tag-arguments)``.

        :param tagged_line: string to be parsed.
        :param symbol_or_re: symbol string or regular expresssion to
          be parsed, default is any sequence of characters except the
          first character of the suffix delimiter.
        :param delimiters: tuple of delimiter strings
          ``(prefix, suffix)``. Default is :attr:`line_delimiters`.
        :param strip_comment: If True, remove trailing ``#`` comment
          from arguments. Default: False.

        >>> tagged_line = ' # @:' 'adhoc_test' ':@   arg1 arg2  # comment'
        >>> AdHoc.adhoc_parse_line(tagged_line)
        ('adhoc_test', 'arg1 arg2  # comment')

        >>> AdHoc.adhoc_parse_line(tagged_line, 'adhoc_.*', is_re=True)
        ('adhoc_test', 'arg1 arg2  # comment')

        >>> AdHoc.adhoc_parse_line(tagged_line, strip_comment=True)
        ('adhoc_test', 'arg1 arg2')

        >>> AdHoc.adhoc_parse_line(tagged_line.replace('@', '<'))
        ('', '# <:adhoc_test:<   arg1 arg2  # comment')

        >>> AdHoc.adhoc_parse_line(tagged_line.replace('@', '|'), delimiters=('|:', ':|'))
        ('adhoc_test', 'arg1 arg2  # comment')
        """
        # @:adhoc_run_time_section:@ on
        if delimiters is None:
            delimiters = cls.line_delimiters
        if symbol_or_re is None:
            dlm = delimiters[1]
            if dlm:
                symbol_or_re = ''.join(('[^', dlm[0], ']+'))
            else:
                symbol_or_re = ''.join(('[^\\s]+'))
            is_re = True
        if not is_re:
            symbol_or_re = re.escape(symbol_or_re)
        tag_rx = cls.adhoc_tag(''.join(('(', symbol_or_re, ')')), delimiters, is_re=True)
        mo = re.search(tag_rx, tagged_line)
        if mo:
            ptag = mo.group(1)
        else:
            ptag = ''
        strip_rx = ''.join(('^.*', tag_rx, '\\s*'))
        tag_arg = re.sub(strip_rx, '', tagged_line).strip()
        if strip_comment:
            tag_arg = re.sub('\\s*#.*', '', tag_arg)
        return (ptag, tag_arg)

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Low-Level Convenience Functions
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    @classmethod
    def set_delimiters(cls, line_delimiters=None, section_delimiters=None): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Set line/section delimiters.

        :returns: saved delimiter state suitable for
          :meth:`reset_delimiters`.

        :param line_delimiters: the line delimiters. If None, line
          delimiters are not changed.
        :param section_delimiters: the section delimiters. If None,
          `line_delimiters` is used.

        If both `line_delimiters` and `section_delimiters` are None,
        the delimiter state is returned without any modification to
        the current delimiters.

        >>> AdHoc.set_delimiters()
        (('@:', ':@'), ('@:', ':@'))

        >>> sv = AdHoc.inc_delimiters()
        >>> sv
        (('@:', ':@'), ('@:', ':@'))

        >>> AdHoc.set_delimiters()
        (('@@:', ':@@'), ('@@:', ':@@'))

        >>> AdHoc.reset_delimiters(sv)
        >>> AdHoc.set_delimiters()
        (('@:', ':@'), ('@:', ':@'))

        >>> AdHoc.set_delimiters(('<:', ':>'))
        (('@:', ':@'), ('@:', ':@'))

        >>> AdHoc.set_delimiters()
        (('<:', ':>'), ('<:', ':>'))

        >>> AdHoc.reset_delimiters(sv)
        >>> AdHoc.set_delimiters()
        (('@:', ':@'), ('@:', ':@'))

        '''
        # @:adhoc_run_time_section:@ on
        delimiter_state = (cls.line_delimiters, cls.section_delimiters)
        if line_delimiters is None:
            line_delimiters = delimiter_state[0]
            if section_delimiters is None:
                section_delimiters = delimiter_state[1]
        elif section_delimiters is None:
            section_delimiters = line_delimiters
        cls.line_delimiters, cls.section_delimiters = (
            line_delimiters, section_delimiters)
        return delimiter_state

    @classmethod
    def reset_delimiters(cls, delimiter_state):              # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Reset line/section delimiters from saved state.

        :param delimiter_state: delimiter state as returned by
          :meth:`set_delimiters`.
        '''
        # @:adhoc_run_time_section:@ on
        cls.line_delimiters, cls.section_delimiters = delimiter_state

    @classmethod
    def inc_delimiters(cls):                                 # |:clm:|
    # @:adhoc_run_time_section:@ off
        '''Duplicate outer delimiter characters.

        :returns: saved delimiter state suitable for
          :meth:`reset_delimiters`.

        E.g.::

            "@:", ":@" => "@@:", ":@@"

        See :meth:`set_delimiters` for doctest example.
        '''
        # @:adhoc_run_time_section:@ on

        inc_first = lambda dlm: (((not dlm) and ('')) or (dlm[0] + dlm))
        inc_last = lambda dlm: (((not dlm) and ('')) or (dlm + dlm[-1]))
        outer_delimiters = [(inc_first(dlm[0]), inc_last(dlm[1]))
                            for dlm in (cls.line_delimiters,
                                        cls.section_delimiters)]
        return cls.set_delimiters(*outer_delimiters)

    @classmethod
    def line_tag(cls, symbol_or_re, is_re=False):            # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Make a line tag from symbol or regular expression.

        :returns: unicode string.

        :param symbol_or_re: symbol string or regular expresssion.
        :param is_re: if True, escape the delimiters for regular
          expressions.
        '''
        # @:adhoc_run_time_section:@ on
        return cls.adhoc_tag(symbol_or_re, cls.line_delimiters, is_re)

    @classmethod
    def section_tag(cls, symbol_or_re, is_re=False):         # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Make a section tag from symbol or regular expression.

        :returns: unicode string.

        :param symbol_or_re: symbol string or regular expresssion.
        :param is_re: if True, escape the delimiters for regular
          expressions.
        '''
        # @:adhoc_run_time_section:@ on
        return cls.adhoc_tag(symbol_or_re, cls.section_delimiters, is_re)

    @classmethod
    def tag_lines(cls, string, tag, is_re=False):            # |:clm:|
        # @:adhoc_run_time_section:@ off
        """Get lines matching tag.

        :returns: list of tag lines.

        See :meth:`tag_split`.
        """
        # @:adhoc_run_time_section:@ on
        result = []
        for section in cls.tag_split(string, tag, is_re):
            if section[0]:
                result.append(section[1])
        return result

    @classmethod
    def tag_partition(cls, string, tag, is_re=False, headline=False): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Split the string into body parts and sections.

        If `headline` is True, the starting tag line is included for
        sections.'''
        # @:adhoc_run_time_section:@ on
        in_section = False
        body_parts = []
        sections = []
        tagged_line = ''
        for section in cls.tag_split(string, tag, is_re):
            if section[0]:
                in_section = not in_section
                tagged_line = section[1]
                continue
            if in_section:
                if headline:
                    sections.append((tagged_line, section[1]))
                else:
                    sections.append(section[1])
            else:
                body_parts.append(section[1])
        return body_parts, sections

    @classmethod
    def tag_sections(cls, string, tag, is_re=False, headline=False): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Split the string into sections.

        If `headline` is True, the starting tag line is included.

        See :meth:`tag_partition`.
        '''
        # @:adhoc_run_time_section:@ on
        body_parts, sections = cls.tag_partition(string, tag, is_re, headline)
        return sections

    @classmethod
    def line_tag_parse(cls, tagged_line, symbol_or_re=None, is_re=False, # |:clm:|
                       strip_comment=None):
        # @:adhoc_run_time_section:@ off
        """Parse a line tag line into tag-symbol and argument parts.

        :returns: a tuple ``(tag-symbol, tag-arguments)``.

        See :meth:`adhoc_parse_line`.
        """
        # @:adhoc_run_time_section:@ on
        return cls.adhoc_parse_line(tagged_line, symbol_or_re, cls.line_delimiters,
                                    is_re, strip_comment=strip_comment)

    @classmethod
    def line_tag_strip(cls, tagged_line, symbol_or_re=None, is_re=False, # |:clm:|
                       strip_comment=None):
        # @:adhoc_run_time_section:@ off
        """Remove tag and optionally comment from line tag line.

        :returns: tag arguments.

        See :meth:`adhoc_parse_line`.
        """
        # @:adhoc_run_time_section:@ on
        return cls.line_tag_parse(tagged_line, symbol_or_re, is_re, strip_comment)[1]

    @classmethod
    def section_tag_parse(cls, tagged_line, symbol_or_re=None, is_re=False, # |:clm:|
                       strip_comment=None):
        # @:adhoc_run_time_section:@ off
        """Parse a section tag line into tag-symbol and argument parts.

        :returns: a tuple ``(tag-symbol, tag-arguments)``.

        See :meth:`adhoc_parse_line`.
        """
        # @:adhoc_run_time_section:@ on
        return cls.adhoc_parse_line(tagged_line, symbol_or_re, cls.section_delimiters,
                                    is_re, strip_comment=strip_comment)

    @classmethod
    def section_tag_strip(cls, tagged_line, symbol_or_re=None, is_re=False, # |:clm:|
                       strip_comment=None):
        # @:adhoc_run_time_section:@ off
        """Remove tag and optionally comment from section tag line.

        :returns: tag arguments.

        See :meth:`adhoc_parse_line`.
        """
        # @:adhoc_run_time_section:@ on
        return cls.section_tag_parse(tagged_line, symbol_or_re, is_re, strip_comment)[1]

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Tagged Line/Section Transformations
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    @classmethod
    def transform_lines(cls, transform, string,              # |:clm:|
                        symbol_or_re, is_re=False, delimiters=None):
        # @:adhoc_run_time_section:@ off
        """Split string into line tag lines and other sections; call
        transform callback on each tagged line.

        :returns: transformed string.

        :param transform: callback which receives argument ``tagged-line``.
        """
        # @:adhoc_run_time_section:@ on
        if delimiters is None:
            delimiters = cls.line_delimiters
        result = []
        in_section = False
        for section in cls.tag_split(
            string, cls.adhoc_tag(symbol_or_re, delimiters, is_re), is_re):
            blob = section[1]
            if section[0]:
                in_section = not in_section
                blob = transform(blob)
            result.append(blob)
        string = ''.join(result)
        return string

    @classmethod
    def transform_sections(cls, transform, string,           # |:clm:|
                           symbol_or_re, is_re=False):
        # @:adhoc_run_time_section:@ off
        """Split string into sections and call transform callback on each section.

        :returns: transformed string.

        :param transform: callback which receives and returns
          arguments ``section``, ``headline``.
        """
        # @:adhoc_run_time_section:@ on
        result = []
        in_section = False
        headline = ''
        for section in cls.tag_split(
            string, cls.section_tag(symbol_or_re, is_re), is_re):
            blob = section[1]
            if section[0]:
                in_section = not in_section
                if in_section:
                    headline = blob
                    continue
            elif in_section:
                blob, headline = transform(blob, headline)
                result.append(headline)
            result.append(blob)
        string = ''.join(result)
        return string

    @classmethod
    def line_tag_rename(cls, string, symbol_or_re, renamed, is_re=False, delimiters=None): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Rename tag-symbol.

        Default tag delimiters are :attr:`line_delimiters`.

        >>> tpl = AdHoc.get_named_template("col-param-closure")

        .. >>> printf(str(AdHoc.line_tag_rename(tpl, "adhoc_run_time_section", "should_be_kept")))
        '''
        # @:adhoc_run_time_section:@ on
        if is_re:
            transform = lambda blob: re.sub(symbol_or_re, renamed, blob)
        else:
            transform = lambda blob: blob.replace(symbol_or_re, renamed)
        return cls.transform_lines(transform, string, symbol_or_re, is_re, delimiters)

    @classmethod
    def line_tag_remove(cls, string, symbol_or_re, is_re=False, delimiters=None): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Remove tagged lines.

        Default tag delimiters are :attr:`line_delimiters`.

        >>> tpl = AdHoc.get_named_template("col-param-closure")

        .. >>> printf(str(AdHoc.line_tag_remove(tpl, "adhoc_run_time_section")))
        '''
        # @:adhoc_run_time_section:@ on
        transform = lambda blob: ''
        return cls.transform_lines(transform, string, symbol_or_re, is_re, delimiters)

    @classmethod
    def section_tag_rename(cls, string, symbol_or_re, renamed, is_re=False): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Rename tag-symbol of lines tagged with :attr:`section_delimiters`.

        >>> tpl = AdHoc.get_named_template("col-param-closure")
        >>> res = AdHoc.section_tag_rename(tpl, "adhoc_run_time_section", "should_be_kept")
        >>> res = '\\n'.join(res.splitlines()[:4])
        >>> printf(str(res)) #doctest: +ELLIPSIS
            # @:should_be_kept:@ on
            @classmethod
            def col_param_closure(cls):...
                # @:should_be_kept:@ off
        '''
        # @:adhoc_run_time_section:@ on
        if is_re:
            transform = lambda blob: re.sub(symbol_or_re, renamed, blob)
        else:
            transform = lambda blob: blob.replace(symbol_or_re, renamed)
        return cls.transform_lines(transform, string, symbol_or_re, is_re, cls.section_delimiters)

    @classmethod
    def section_tag_remove(cls, string, symbol_or_re, is_re=False): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Remove lines tagged with :attr:`section_delimiters`.

        >>> tpl = AdHoc.get_named_template("col-param-closure")
        >>> res = AdHoc.section_tag_remove(tpl, "adhoc_run_time_section")
        >>> res = '\\n'.join(res.splitlines()[:4])
        >>> printf(str(res)) #doctest: +ELLIPSIS
            @classmethod
            def col_param_closure(cls):...
                ...Closure for setting up maximum width, padding and separator
                for table columns.
        '''
        # @:adhoc_run_time_section:@ on
        transform = lambda blob: ''
        return cls.transform_lines(transform, string, symbol_or_re, is_re, cls.section_delimiters)

    @classmethod
    def indent_sections(cls, string, symbol_or_re, is_re=False): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''
        >>> section = """\\
        ... # prefix
        ...   # @:adhoc_indent_check:@ +4
        ...   #line 1
        ...   #  line 2
        ...   #
        ...   # line 3
        ...   # @:adhoc_indent_check:@
        ...   # suffix\\
        ... """

        >>> printf(AdHoc.indent_sections(section, "adhoc_indent_check"))
        # prefix
          # @:adhoc_indent_check:@ +4
              #line 1
              #  line 2
              #
              # line 3
              # @:adhoc_indent_check:@
          # suffix

        >>> printf(AdHoc.indent_sections(section.replace("+4", "-1"),
        ...        "adhoc_indent_check"))
        # prefix
          # @:adhoc_indent_check:@ -1
         #line 1
         #  line 2
         #
         # line 3
          # @:adhoc_indent_check:@
          # suffix

        '''
        # @:adhoc_run_time_section:@ on
        result = []
        in_section = False
        indent = 0
        for section in cls.tag_split(
            string, cls.section_tag(symbol_or_re, is_re), is_re):
            blob = section[1]
            if section[0]:
                in_section = not in_section
                if in_section:
                    tag_arg = cls.section_tag_strip(blob)
                    if tag_arg:
                        indent = int(tag_arg)
                    else:
                        indent = -4
            else:
                if in_section and indent:
                    if indent < 0:
                        rx = re.compile(''.join(('^', ' ' * (-indent))), re.M)
                        blob = rx.sub('', blob)
                    elif indent > 0:
                        rx = re.compile('^', re.M)
                        blob = rx.sub(' ' * indent, blob)
                    indent = 0
            result.append(blob)
        string = ''.join(result)
        return string

    @classmethod
    def enable_sections(cls, string, symbol_or_re, is_re=False): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''
        >>> section = """\\
        ... # prefix
        ...   # @:adhoc_enable_check:@
        ...   #line 1
        ...   #  line 2
        ...   #
        ...   # line 3
        ...   # @:adhoc_enable_check:@
        ...   # suffix\\
        ... """
        >>> printf(AdHoc.enable_sections(section, "adhoc_enable_check"))
        # prefix
          # @:adhoc_enable_check:@
          line 1
           line 2
        <BLANKLINE>
          line 3
          # @:adhoc_enable_check:@
          # suffix
        '''
        # @:adhoc_run_time_section:@ on
        enable_ro = re.compile('^([ \t\r]*)(# ?)', re.M)
        enable_sub = '\\1'
        transform = lambda blob, hl: (enable_ro.sub(enable_sub, blob), hl)
        return cls.transform_sections(transform, string, symbol_or_re, is_re)

    adhoc_rx_tab_check = re.compile('^([ ]*\t)', re.M)
    adhoc_rx_disable_simple = re.compile('^', re.M)
    adhoc_rx_min_indent_check = re.compile('^([ ]*)([^ \t\r\n]|$)', re.M)

    @classmethod
    def disable_transform(cls, section, headline=None):      # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Disable section transform callback.'''
        # @:adhoc_run_time_section:@ on
        if not section:
            return (section, headline)

        if cls.adhoc_rx_tab_check.search(section):
            # tabs are evil
            if cls.verbose:
                list(map(sys.stderr.write,
                         ('# dt: evil tabs: ', repr(section), '\n')))
            return (
                cls.adhoc_rx_disable_simple.sub(
                    '# ', section.rstrip()) + '\n',
                headline)

        min_indent = ''
        for mo in cls.adhoc_rx_min_indent_check.finditer(section):
            indent = mo.group(1)
            if indent:
                if (not min_indent or len(min_indent) > len(indent)):
                    min_indent = indent
            elif mo.group(2):
                min_indent = ''
                break
        adhoc_rx_min_indent = re.compile(
            ''.join(('^(', min_indent, '|)([^\n]*)$')), re.M)

        if section.endswith('\n'):
            section = section[:-1]
        dsection = []
        for mo in adhoc_rx_min_indent.finditer(section):
            indent = mo.group(1)
            rest = mo.group(2)
            if not indent and not rest:
                #leave blank lines blank
                dsection.append('\n')
            else:
                dsection.extend((indent, '# ', rest, '\n'))
        return (''.join(dsection), headline)

    @classmethod
    def disable_sections(cls, string, symbol_or_re, is_re=False): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''
        >>> section = """\\
        ... prefix
        ...   @:adhoc_disable_check:@
        ...   line 1
        ...     line 2
        ...
        ...   line 3
        ...   @:adhoc_disable_check:@
        ...   suffix\\
        ... """
        >>> printf(AdHoc.disable_sections(section, "adhoc_disable_check"))
        prefix
          @:adhoc_disable_check:@
          # line 1
          #   line 2
        <BLANKLINE>
          # line 3
          @:adhoc_disable_check:@
          suffix
        '''
        # @:adhoc_run_time_section:@ on
        return cls.transform_sections(
            cls.disable_transform, string, symbol_or_re, is_re)

    @classmethod
    def remove_sections(cls, string, symbol_or_re, is_re=False): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Remove sections.'''
        # @:adhoc_run_time_section:@ on
        ah_retained, ah_removed = cls.tag_partition(
            string, cls.section_tag(symbol_or_re, is_re), is_re)
        return ''.join(ah_retained)

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| IO Functions
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    @staticmethod
    def check_coding(source):                                # |:fnc:|
        # @:adhoc_run_time_section:@ off
        '''Determine coding for source.

        :returns: coding type for string.

        :param source: source string/unicode.

        If the ``source`` string contains a coding specification
        within the first two lines, the specified coding is used,
        otherwise, ``UTF-8`` is returned.
        '''
        # @:adhoc_run_time_section:@ on
        if source:
            eol_seen = 0
            for c in source:
                if isinstance(c, int):
                    lt_ = lambda a, b: a < b
                    chr_ = lambda a: chr(a)
                else:
                    lt_ = lambda a, b: True
                    chr_ = lambda a: a
                break
            check = []
            for c in source:
                if lt_(c, 127):
                    check.append(chr_(c))
                if c == '\n':
                    eol_seen += 1
                    if eol_seen == 2:
                        break
            check = ''.join(check)
            mo = re.search('-[*]-.*coding:\\s*([^;\\s]+).*-[*]-', check)
        else:
            mo = None
        if mo:
            coding = mo.group(1)
        else:
            coding = 'utf-8'
        return coding

    @classmethod
    def decode_source(cls, source):                          # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Decode source to unicode.

        :param source: source string (may already be unicode).

        If the ``source`` string contains a coding specification
        within the first two lines, the specified coding is used,
        otherwise, ``UTF-8`` is applied.
        '''
        # @:adhoc_run_time_section:@ on
        if not source:
            return cls.uc('')
        if not isinstance(source, cls.uc_type) and hasattr(source, 'decode'):
            source = source.decode(cls.check_coding(source))
        return source

    @classmethod
    def encode_source(cls, source):                          # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Encode source from unicode.

        :param source: source string (may already be encoded).

        If the ``source`` string contains a coding specification
        within the first two lines, the specified coding is used,
        otherwise, ``UTF-8`` is applied.
        '''
        # @:adhoc_run_time_section:@ on
        if not source:
            return ''.encode('utf-8')
        if isinstance(source, cls.uc_type) and hasattr(source, 'encode'):
            source = source.encode(cls.check_coding(source))
        return source

    @classmethod
    def read_source(cls, file_, decode=True):                # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Read source from file.

        :returns: unicode string.

        :param file_: If None, empty or ``-``, sys.stdin is used,
          otherwise the file is read from ``file_`` and decoded with
          :meth:`decode_source`.
        '''
        # @:adhoc_run_time_section:@ on
        source = None
        if not file_ or file_ == '-':
            # Python3 has a buffer attribute for binary input.
            if hasattr(sys.stdin, 'buffer'):
                source = sys.stdin.buffer.read()
            else:
                source = sys.stdin.read()
        else:
            try:
                sf = open(file_, 'rb')
                source = sf.read()
                sf.close()
            except IOError:
                for module in sys.modules.values():
                    if (module
                        and hasattr(module, '__file__')
                        and module.__file__ == file_):
                        if (hasattr(module, '__adhoc__')
                            and hasattr(module.__adhoc__, 'source')):
                            source = module.__adhoc__.source
                            break
        if source is None:
            raise IOError('source not found for `' + str(file_) + '`')
        if decode:
            return cls.decode_source(source)
        return source

    @classmethod
    def write_source(cls, file_, source, mtime=None, mode=None): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Write source to file.

        :param file_: If None, empty or ``-``, sys.stdout is used,
          otherwise the file is written to ``file_`` after encoding
          with :meth:`encode_source`.
        '''
        # @:adhoc_run_time_section:@ on
        esource = cls.encode_source(source)
        if not file_ or file_ == '-':
            # @:adhoc_run_time_section:@ off
            # For Python2, sys.stdout is effectively binary, so source
            # can be pre-encoded.
            #
            # With Python3 sys.stdout does automatic encoding (which
            # is unwanted).
            # Normal sys.stdout has a buffer member which allows
            # binary output, but not during doctest.
            # @:adhoc_run_time_section:@ on
            if hasattr(sys.stdout, 'buffer'):
                sys.stdout.buffer.write(esource)
            else:
                try:
                    sys.stdout.write(esource)
                except TypeError:
                    sys.stdout.write(source)
        else:
            sf = open(file_, 'wb')
            sf.write(esource)
            sf.close()
            if mode is not None:
                os.chmod(file_, mode)
            if mtime is not None:
                import datetime
                if cls.isstring(mtime):
                    try:
                        date, ms = mtime.split('.')
                    except ValueError:
                        date = mtime
                        ms = 0
                    mtime = cls.strptime(date, '%Y-%m-%dT%H:%M:%S')
                    mtime += datetime.timedelta(microseconds=int(ms))
                if isinstance(mtime, datetime.datetime):
                    # @:adhoc_run_time_section:@ off
                    # import calendar
                    # if mtime.utcoffset() is not None:
                    #     mtime = mtime - mtime.utcoffset()
                    # millis = int(calendar.timegm(mtime.timetuple()) * 1000 +
                    #                mtime.microsecond / 1000)
                    # ts = float(millis) / 1000
                    # @:adhoc_run_time_section:@ on
                    ts = int(mtime.strftime("%s"))
                else:
                    ts = mtime
                os.utime(file_, (ts, ts))

    @classmethod
    def check_xfile(cls, file_, xdir=None):                  # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Prepare extraction of a file.

        :returns: None, if the file already exists. Otherwise, the
          file directory is created and the absolute path name of the
          file is returned.

        :param file_: filename.
        :param xdir: extraction directory. If it is `None`,
          :attr:`extract_dir` is used.

        If ``file_`` is `None`, empty or ``-``, the filename ``-`` is
        returned.

        If ``file_`` starts with a slash ``/``, ``xdir`` is ignored,
        otherwise, ``xdir`` is prepended to ``file_``.
        '''
        # @:adhoc_run_time_section:@ on
        if xdir is None:
            xdir = cls.extract_dir
        if not file_:
            file_ = '-'
        if file_ == '-':
            return file_
        file_ = os.path.expanduser(file_)
        if os.path.isabs(file_):
            xfile = file_
        else:
            xfile = os.path.join(xdir, file_)
        xfile = os.path.abspath(xfile)
        if os.path.exists(xfile):
            # do not overwrite files
            if (cls.extract_warn or (cls.verbose)) and not cls.quiet:
                list(map(sys.stderr.write, (
                    "# xf: ", cls.__name__, ": warning file `", file_,
                    "` exists. skipping ...\n")))
            return None
        xdir = os.path.dirname(xfile)
        if not os.path.exists(xdir):
            os.makedirs(xdir)
        return xfile

    @classmethod
    def pack_file(cls, source, zipped=True):                 # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Optionally gzip a file and base64-encode it.

        :returns: base64-encoded unicode string.

        :param source: string to be packed.
        :param zipped: if True, gzip ``source`` before
          base64-encoding. (Default: True).
        '''
        # @:adhoc_run_time_section:@ on
        import base64, gzip
        if zipped:
            sio = _AdHocBytesIO()
            gzf = gzip.GzipFile('', 'wb', 9, sio)
            gzf.write(cls.encode_source(source))
            gzf.close()
            source = sio.getvalue()
            sio.close()
        else:
            source = cls.encode_source(source)
        source = base64.b64encode(source)
        source = source.decode('ascii')
        return source

    @classmethod
    def unpack_file(cls, source64, zipped=True, decode=True): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Base64-decode a file and optionally ungzip it.

        :returns: unicode string if ``decode`` is True.

        :param source64: base64 encoded unicode string to be unpacked.
        :param zipped: if True, ungzip ``source`` after
          base64-decoding. (Default: True).
        '''
        # @:adhoc_run_time_section:@ on
        import base64, gzip
        # @:adhoc_run_time_section:@ off
        if cls.debug:
            printf(sformat(
                "{0}{3:^{1}} {4:<{2}s}: ]{5:>7d}[ ]{6!s}[ {7}",
                dbg_comm, dbg_twid, dbg_fwid,
                ':DBG:', 'source64', len(source64), source64[:80],
                'b64decode ...'))
        # @:adhoc_run_time_section:@ on
        source = source64.encode('ascii')
        source = base64.b64decode(source)
        if zipped:
            # @:adhoc_run_time_section:@ off
            if cls.debug:
                printf(sformat(
                    "{0}{3:^{1}} {4:<{2}s}: ]{5:>7d}[ ]{6!s}[ {7}",
                    dbg_comm, dbg_twid, dbg_fwid,
                    ':DBG:', 'source (zip)', len(source), repr(source)[:80],
                    'unzipping ...'))
            # @:adhoc_run_time_section:@ on
            sio = _AdHocBytesIO(source)
            gzf = gzip.GzipFile('', 'rb', 9, sio)
            source = gzf.read()
            gzf.close()
            sio.close()
        if decode:
            source = cls.decode_source(source)
        # @:adhoc_run_time_section:@ off
        if cls.debug:
            printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5:>7d}[ ]{6!s}[",
                    dbg_comm, dbg_twid, dbg_fwid,
                    ':DBG:', 'source', len(source), repr(source)[:80]))

        # @:adhoc_run_time_section:@ on
        return source

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Run-Time Unpack/Import Interface
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    @classmethod
    def unpack_(cls, mod_name=None, file_=None, mtime=None, # |:clm:||:api_fi:|
                mode=None, zipped=True, flat=None, source64=None):
        # @:adhoc_run_time_section:@ off
        """Unpack adhoc'ed file, if it does not exist."""
        # @:adhoc_run_time_section:@ on
        xfile = cls.check_xfile(file_, cls.extract_dir)
        if xfile is None:
            return
        if cls.verbose:
            list(map(sys.stderr.write,
                     ("# xf: ", cls.__name__, ": unpacking `", file_, "`\n")))
        source = cls.unpack_file(source64, zipped=zipped, decode=False)
        cls.write_source(xfile, source, mtime, mode)

    @classmethod
    def strptime(cls, date_string, format_):                 # |:clm:|
        # @:adhoc_run_time_section:@ off
        """Python 2.4 compatible"""
        # @:adhoc_run_time_section:@ on
        import datetime
        if hasattr(datetime.datetime, 'strptime'):
            strptime_ = datetime.datetime.strptime
        else:
            import time
            strptime_ = lambda date_string, format_: (
                datetime.datetime(*(time.strptime(date_string, format_)[0:6])))
        return strptime_(date_string, format_)

    @classmethod
    def import_(cls, mod_name=None, file_=None, mtime=None, # |:clm:||:api_fi:|
                mode=None, zipped=True, flat=None, source64=None):
        # @:adhoc_run_time_section:@ off
        """Import adhoc'ed module."""
        # @:adhoc_run_time_section:@ on
        import datetime
        import time

        module = cls.module_setup(mod_name)

        if mtime is None:
            mtime = datetime.datetime.fromtimestamp(0)
        else:
            # mtime=2011-11-23T18:04:26[.218506], zipped=True, flat=None, source64=
            try:
                date, ms = mtime.split('.')
            except ValueError:
                date = mtime
                ms = 0
            mtime = cls.strptime(date, '%Y-%m-%dT%H:%M:%S')
            mtime += datetime.timedelta(microseconds=int(ms))

        source = cls.unpack_file(source64, zipped=zipped, decode=False)

        # @:adhoc_run_time_section:@ off
        # |:todo:| add to parent module
        # @:adhoc_run_time_section:@ on
        mod_parts = mod_name.split('.')
        mod_child = mod_parts[-1]
        parent = '.'.join(mod_parts[:-1])
        # @:adhoc_run_time_section:@ off
        printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                dbg_comm, dbg_twid, dbg_fwid, ':DBG:', 'parent', parent))

        # @:adhoc_run_time_section:@ on
        old_mtime = module.__adhoc__.mtime
        module = cls.module_setup(mod_name, file_, mtime, source, mode)
        if len(parent) > 0:
            setattr(sys.modules[parent], mod_child, module)

        if module.__adhoc__.mtime != old_mtime:
            # @:adhoc_run_time_section:@ off
            printf(sformat('{0}Executing source', dbg_comm))
            # @:adhoc_run_time_section:@ on
            source = cls.encode_source(module.__adhoc__.source)
            exec(source, module.__dict__)
        # @:adhoc_run_time_section:@ off

        msg = (((mod_name in sys.modules) and ('YES')) or ('NO'))
        printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                       dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                       mod_name + ' imported', msg))

        module_name = module.__name__
        printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                       dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                       'module_name', module_name))
        dump_attr(module, wid=80, trunc=5)
        # @:adhoc_run_time_section:@ on

    @classmethod
    def module_setup(cls, module=None, file_=None, mtime=None, # |:clm:||:api_fi:|
                     source=None, mode=None):
        # @:adhoc_run_time_section:@ off
        '''Setup module for `AdHoc`.
        \\|:todo:| various modes are possible:
        - always use newest version (development) (currently implemented)
        - always use adhoc\'ed version (freeze) (not implemented)
        '''
        # @:adhoc_run_time_section:@ on
        m = 'ms: '
        class Attr:                                          # |:cls:|
            pass

        import types, datetime, os
        if not isinstance(module, types.ModuleType):
            mod_name = module
            if mod_name is None:
                mod_name = __name__
            try:
                if mod_name not in sys.modules:
                    # @:adhoc_run_time_section:@ off
                    if cls.verbose:
                        printe(sformat('{0}{1}__import__({2})',
                                       dbg_comm, m, mod_name))
                    # @:adhoc_run_time_section:@ on
                    __import__(mod_name)
                module = sys.modules[mod_name]
            except (ImportError, KeyError):
                # @:adhoc_run_time_section:@ off
                if cls.verbose:
                    printe(sformat('{0}{1}imp.new_module({2})',
                                   dbg_comm, m, mod_name))
                # @:adhoc_run_time_section:@ on
                import imp
                module = imp.new_module(mod_name)
                sys.modules[mod_name] = module
        else:
            mod_name = module.__name__

        if mtime is None:
            if (file_ is not None
                or source is not None):
                # the info is marked as outdated
                mtime = datetime.datetime.fromtimestamp(1)
            else:
                # the info is marked as very outdated
                mtime = datetime.datetime.fromtimestamp(0)

        if not hasattr(module, '__adhoc__'):
            adhoc = Attr()
            setattr(module, '__adhoc__', adhoc)
            setattr(adhoc, '__module__', module)

            mtime_set = None
            mode_set = mode
            if hasattr(module, '__file__'):
                module_file = module.__file__
                if module_file.endswith('.pyc'):
                    module_file = module_file[:-1]
                if os.access(module_file, os.R_OK):
                    stat = os.stat(module_file)
                    mtime_set = datetime.datetime.fromtimestamp(
                        stat.st_mtime)
                    mode_set = stat.st_mode
            if mtime_set is None:
                # the info is marked as very outdated
                mtime_set = datetime.datetime.fromtimestamp(0)
            adhoc.mtime = mtime_set
            adhoc.mode = mode_set
        else:
            adhoc = module.__adhoc__

        if (mtime > adhoc.mtime
            or not hasattr(module, '__file__')):
            if file_ is not None:
                setattr(module, '__file__', file_)
                if os.access(file_, os.R_OK):             # |:api_fi:|
                    stat = os.stat(file_)
                    adhoc.mtime = datetime.datetime.fromtimestamp(
                        stat.st_mtime)
                    adhoc.mode = stat.st_mode
                    if adhoc.mtime > mtime:
                        # the file on disk is newer than the adhoc'ed source
                        try:
                            delattr(adhoc, 'source')
                        except AttributeError:
                            pass
                        source = None

        if (mtime > adhoc.mtime
            or not hasattr(adhoc, 'source')):
            if source is not None:
                adhoc.source = source
                adhoc.mtime = mtime
                adhoc.mode = mode

        if not hasattr(adhoc, 'source'):
            try:
                file_ = module.__file__
                file_, source = cls.std_source_param(file_, source)
                adhoc.source = source
            except (AttributeError, IOError):
                # @:adhoc_run_time_section:@ off
                # if hasattr(module, '__path__'): # |:debug:|
                #     list(map(sys.stderr.write,
                #         ('module path: ', module.__path__, '\n')))
                # else:
                #     sys.stderr.write('no module.__path__\n')
                #     list(map(sys.stderr.write,
                #         [''.join((attr, str(value), "\n")) for attr, value in
                #          filter(lambda i: i[0] != '__builtins__',
                #                 sorted(vars(module).items()))]))
                if cls.verbose:
                    (t, e, tb) = sys.exc_info()
                    import traceback
                    printe(''.join(traceback.format_tb(tb)), end='')
                    printe(sformat('{0}: {1}', t.__name__, e))
                    del(tb)
                # @:adhoc_run_time_section:@ on
                pass

        return module

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Export Tools
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    @classmethod
    def std_source_param(cls, file_=None, source=None): # |:clm:||:api_fi:|
        # @:adhoc_run_time_section:@ off
        '''Setup standard source parameters.

        :returns: tuple ``( file_, source )``

        :param file_: If None, `__file__` is used. If it ends with
          ``.pyc``, it is transformed to ``.py``.
        :param source: If None, the result of :meth:`read_source` is
          used.
        '''
        # @:adhoc_run_time_section:@ on
        if file_ is None:
            file_ = __file__
        if file_.endswith('.pyc'):
            file_ = file_[:-1]
        if source is None:
            source = cls.read_source(file_)
        return (file_, source)

    @classmethod
    def export_source(cls, string, no_remove=False, no_disable=False): # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''
        ============================ =========================
        check for |adhoc_remove|     sections and remove them!
        check for |adhoc_import|     sections and remove them!
        check for |adhoc_unpack|     sections and remove them!
        check for |adhoc_template_v| sections and remove them!
        check for |adhoc_disable|    sections and enable them!
        check for |adhoc_enable|     sections and disable them!
        check for |adhoc_remove_|    section markers and rename them!
        ============================ =========================
        '''
        # @:adhoc_run_time_section:@ on
        string = cls.collapse_macros(string)
        if not no_remove:
            string = cls.remove_sections(string, 'adhoc_remove')
        string = cls.remove_sections(string, 'adhoc_import')
        string = cls.remove_sections(string, 'adhoc_unpack')
        string = cls.remove_sections(string, 'adhoc_template_v')
        if not no_disable:
            string = cls.enable_sections(string, 'adhoc_disable')
            string = cls.disable_sections(string, 'adhoc_enable')
        if not no_remove:
            string = cls.section_tag_rename(string, 'adhoc_remove_', 'adhoc_remove')
        return string

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Extract Interface
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    @classmethod
    def unpack(cls, file_=None, source=None):                # |:clm:|
        # @:adhoc_run_time_section:@ off
        """Unpack all adhoc'ed files in |adhoc_unpack| sections."""
        # @:adhoc_run_time_section:@ on
        file_, source = cls.std_source_param(file_, source)
        source_sections, unpack_sections = cls.tag_partition(
            source, cls.section_tag('adhoc_unpack'))
        sv_extract_warn = cls.extract_warn
        cls.extract_warn = True
        unpack_call = ''.join((cls.__name__, '.unpack_'))
        for unpack_section in unpack_sections:
            unpack_section = re.sub('^\\s+', '', unpack_section)
            unpack_section = re.sub(
                '^[^(]*(?s)', unpack_call, unpack_section)
            try:
                #RtAdHoc = cls # unpack_call takes care of this
                exec(unpack_section.lstrip(), globals(), locals())
            except IndentationError:
                sys.stderr.write("!!! IndentationError !!!\n")
                # @:adhoc_run_time_section:@ off
                sys.stderr.write(''.join((unpack_section, "\n")))
                # @:adhoc_run_time_section:@ on
        cls.extract_warn = sv_extract_warn

    @classmethod
    def extract(cls, file_=None, source=None):               # |:clm:|
        # @:adhoc_run_time_section:@ off
        """Unpack all adhoc'ed files in |adhoc_unpack| sections and
        extract all templates."""
        # @:adhoc_run_time_section:@ on
        cls.unpack(file_, source)
        cls.extract_templates(file_, source, export=True)

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Export Interface
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    @classmethod
    def export__(cls, mod_name=None, file_=None, mtime=None, # |:clm:||:api_fi:|
                 mode=None, zipped=True, flat=None, source64=None):
        source = cls.unpack_file(source64, zipped=zipped, decode=False)
        # @:adhoc_run_time_section:@ off
        if cls.debug:
            sys.stderr.write(
                ''.join(("# xp: ", cls.__name__, ".export__ for `",
                         file_, "`\n")))
        # @:adhoc_run_time_section:@ on
        if file_ is None:
            return
        file_base = os.path.basename(file_)
        if file_base.startswith('__init__.py'):
            is_init = True
        else:
            is_init = False

        parts = mod_name.split('.')
        base = parts.pop()
        if parts:
            module_dir = os.path.join(*parts)
            cls.export_need_init[module_dir] = True
        else:
            module_dir = ''
        if is_init:
            module_dir = os.path.join(module_dir, base)
            cls.export_have_init[module_dir] = True
        module_file = os.path.join(module_dir, file_base)

        cls.export_(source, module_file, mtime, mode, flat)

    @classmethod
    def export_(cls, source, file_, mtime, mode, flat=None): # |:clm:|
        cflat = cls.flat
        if flat is None:
            flat = cflat
        cls.flat = flat
        if not flat:
            # extract to export directory
            sv_extract_dir = cls.extract_dir
            cls.extract_dir = cls.export_dir
            cls.extract(file_, source)
            cls.extract_dir = sv_extract_dir

            source_sections, import_sections = cls.tag_partition(
                source, cls.section_tag('adhoc_import'))
            source = cls.export_source(''.join(source_sections))
            export_call = ''.join((cls.__name__, '.export__'))

            xfile = cls.check_xfile(file_, cls.export_dir)
            if xfile is not None:
                cls.write_source(xfile, source, mtime, mode)
                if cls.verbose:
                    list(map(sys.stderr.write,
                             ("# xp: ", cls.__name__, ".export_ for `", file_,
                              "` using `", export_call,"`\n")))

            for import_section in import_sections:
                # this calls RtAdHoc.export__
                import_section = re.sub('^\\s+', '', import_section)
                import_section = re.sub(
                    '^[^(]*(?s)', export_call, import_section)
                try:
                    #RtAdHoc = cls # export_call takes care of this
                    exec(import_section, globals(), locals())
                except IndentationError:
                    sys.stderr.write("!!! IndentationError !!!\n")
                    # @:adhoc_run_time_section:@ off
                    sys.stderr.write(''.join((import_section, "\n")))
                    # @:adhoc_run_time_section:@ on
        else:
            xfile = cls.check_xfile(file_, cls.export_dir)
            if xfile is not None:
                cls.write_source(xfile, source, mtime, mode)
                if cls.verbose:
                    list(map(sys.stderr.write,
                             ("# xp: ", cls.__name__, ".export_ for `", file_,
                              "` using `", export_call,"`\n")))
        cls.flat = cflat

    # @:adhoc_run_time_section:@ off
    default_engine = False

    # @:adhoc_run_time_section:@ on
    @classmethod
    def export(cls, file_=None, source=None):                # |:clm:|
        file_, source = cls.std_source_param(file_, source)
        # @:adhoc_run_time_section:@ off
        # |:todo:| this chaos needs cleanup (cls.import_/cls.export__)
        # @:adhoc_run_time_section:@ on
        sv_import = cls.import_
        cls.import_ = cls.export__

        file_ = os.path.basename(file_)
        # @:adhoc_run_time_section:@ off
        if cls.verbose:
            list(map(sys.stderr.write,
                     ("# xp: ", cls.__name__, ".export for `", file_, "`\n")))
        # @:adhoc_run_time_section:@ on
        cls.export_(source, file_, None, None, False)
        sv_extract_dir = cls.extract_dir
        cls.extract_dir = cls.export_dir
        engine_tag = cls.section_tag('adhoc_run_time_engine')
        engine_source = cls.export_source(
            source, no_remove=True, no_disable=True)
        engine_source = cls.get_named_template(
            None, file_, engine_source, tag=engine_tag, ignore_mark=True)
        # @:adhoc_run_time_section:@ off
        if cls.default_engine and not engine_source:
            state = cls.set_delimiters(('@:', ':@'))
            ah = cls()
            engine_source = ah.prepare_run_time_section()
            engine_source = cls.get_named_template(
                None, file_, engine_source, tag=engine_tag, ignore_mark=True)
            cls.reset_delimiters(state)
        # @:adhoc_run_time_section:@ on
        if engine_source:
            efile = cls.check_xfile('rt_adhoc.py')
            if efile is not None:
                cls.write_source(efile, engine_source)
        cls.extract_dir = sv_extract_dir
        for init_dir in cls.export_need_init:
            if not cls.export_have_init[init_dir]:
                if cls.verbose:
                    list(map(sys.stderr.write,
                             ("# xp: create __init__.py in `", init_dir, "`\n")))
                inf = open(os.path.join(
                    cls.export_dir, init_dir, '__init__.py'), 'w')
                inf.write('')
                inf.close()
        cls.import_ = sv_import

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Dump Interface (Import/Unpack Substitute)
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    @classmethod
    def dump__(cls, mod_name=None, file_=None, mtime=None, # |:clm:||:api_fi:|
               mode=None, zipped=True, flat=None, source64=None):
        if cls.verbose:
            list(map(sys.stderr.write,
                     ("# xf: ", cls.__name__, ": dumping `", file_, "`\n")))
        source = cls.unpack_file(source64, zipped=zipped, decode=False)
        return source

    @classmethod
    def dump_(cls, dump_section, dump_type=None):            # |:clm:|
        if dump_type is None:
            dump_type = 'adhoc_import'
        if not dump_section:
            return ''
        dump_call = ''.join(('unpacked = ', cls.__name__, '.dump__'))
        dump_section = re.sub('^\\s+', '', dump_section)
        dump_section = re.sub(
            '^[^(]*(?s)', dump_call, dump_section)
        dump_dict = {'unpacked': ''}
        try:
            #RtAdHoc = cls # dump_call takes care of this
            exec(dump_section.lstrip(), globals(), dump_dict)
        except IndentationError:
            sys.stderr.write("!!! IndentationError !!!\n")
            # @:adhoc_run_time_section:@ off
            sys.stderr.write(''.join((dump_section, "\n")))
            # @:adhoc_run_time_section:@ on
        return dump_dict['unpacked']

    @classmethod
    def dump_file(cls, match, file_=None, source=None, tag=None, # |:clm:|
                  is_re=False):
        file_, source = cls.std_source_param(file_, source)
        if tag is None:
            tag = cls.section_tag('(adhoc_import|adhoc_update)', is_re=True)
            is_re = True
        source_sections, dump_sections = cls.tag_partition(
            source, tag, is_re, headline=True)
        dump_call = ''.join((cls.__name__, '.dump_'))
        for dump_section in dump_sections:
            tagged_line = dump_section[0]
            dump_section = dump_section[1]
            tag_arg = cls.section_tag_strip(tagged_line)
            check_match = match
            if tag_arg != match and not match.startswith('-'):
                check_match = ''.join(('-', match))
            if tag_arg != match and not match.startswith('!'):
                check_match = ''.join(('!', match))
            if tag_arg != match:
                continue
            dump_section = re.sub('^\\s+', '', dump_section)
            dump_section = re.sub(
                '^[^(]*(?s)', dump_call, dump_section)
            try:
                #RtAdHoc = cls # dump_call takes care of this
                exec(dump_section.lstrip(), globals(), locals())
            except IndentationError:
                sys.stderr.write("!!! IndentationError !!!\n")
                # @:adhoc_run_time_section:@ off
                sys.stderr.write(''.join((dump_section, "\n")))
                # @:adhoc_run_time_section:@ on

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Macros
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    macro_call_delimiters = ('@|:', ':|>')
    # @:adhoc_run_time_section:@ off
    """Macro delimiters"""
    # @:adhoc_run_time_section:@ on
    macro_xdef_delimiters = ('<|:', ':|@')
    # @:adhoc_run_time_section:@ off
    """Macro expansion delimiters"""
    # @:adhoc_run_time_section:@ on
    macros = {}
    # @:adhoc_run_time_section:@ off
    """Macros"""
    # @:adhoc_run_time_section:@ on

    @classmethod
    def expand_macros(cls, source, macro_call_dlm=None, macro_xdef_dlm=None): # |:clm:|
        # @:adhoc_run_time_section:@ off
        """
        >>> AdHoc.macros['uc_descr_end'] = (
        ...     '# o:' 'adhoc_template:>\\n'
        ...     '# <:' 'adhoc_uncomment:>\\n'
        ...     )

        >>> macro_source = '# ' + AdHoc.adhoc_tag('uc_descr_end', AdHoc.macro_call_delimiters) + '\\n'
        >>> ign = sys.stdout.write(macro_source) #doctest: +ELLIPSIS
        # @|:uc_descr_end...:|>

        >>> ign = sys.stdout.write(AdHoc.expand_macros(macro_source)) #doctest: +ELLIPSIS
        # <|:adhoc_macro_call...:|@
        # @|:uc_descr_end...:|>
        # <|:adhoc_macro_call...:|@
        # <|:adhoc_macro_expansion...:|@
        # o:adhoc_template...:>
        # <:adhoc_uncomment...:>
        # <|:adhoc_macro_expansion...:|@

        """
        # @:adhoc_run_time_section:@ on
        if macro_call_dlm is None:
            macro_call_dlm = cls.macro_call_delimiters
        if macro_xdef_dlm is None:
            macro_xdef_dlm = cls.macro_xdef_delimiters
        import re
        for macro_name, macro_expansion in cls.macros.items():
            macro_tag = cls.adhoc_tag(macro_name, macro_call_dlm, False)
            macro_tag_rx = cls.adhoc_tag(macro_name, macro_call_dlm, True)
            macro_call = ''.join(('# ', macro_tag, '\n'))
            macro_call_rx = ''.join(('^[^\n]*', macro_tag_rx, '[^\n]*\n'))
            mc_tag = ''.join(('# ', cls.adhoc_tag('adhoc_macro_call', macro_xdef_dlm, False), "\n"))
            mx_tag = ''.join(('# ', cls.adhoc_tag('adhoc_macro_expansion', macro_xdef_dlm, False), "\n"))
            xdef = ''.join((
                mc_tag,
                macro_call,
                mc_tag,
                mx_tag,
                macro_expansion,
                mx_tag,
                ))
            rx = re.compile(macro_call_rx, re.M)
            source = rx.sub(xdef, source)
        return source

    @classmethod
    def has_expanded_macros(cls, source, macro_xdef_dlm=None): # |:clm:|
        # @:adhoc_run_time_section:@ off
        """
        """
        # @:adhoc_run_time_section:@ on
        if macro_xdef_dlm is None:
            macro_xdef_dlm = cls.macro_xdef_delimiters
        mx_tag = cls.adhoc_tag('adhoc_macro_expansion', macro_xdef_dlm, False)
        me_count = len(cls.tag_lines(source, mx_tag))
        return me_count > 0

    @classmethod
    def activate_macros(cls, source, macro_call_dlm=None, macro_xdef_dlm=None): # |:clm:|
        # @:adhoc_run_time_section:@ off
        """
        """
        # @:adhoc_run_time_section:@ on
        if macro_xdef_dlm is None:
            macro_xdef_dlm = cls.macro_xdef_delimiters
        if not cls.has_expanded_macros(source, macro_xdef_dlm):
            source = cls.expand_macros(source, macro_call_dlm, macro_xdef_dlm)
        sv = cls.set_delimiters (macro_xdef_dlm)
        source = cls.remove_sections(source, 'adhoc_macro_call')
        source = cls.section_tag_remove(source, 'adhoc_macro_expansion')
        cls.reset_delimiters(sv)
        return source

    @classmethod
    def collapse_macros(cls, source, macro_xdef_dlm=None):   # |:clm:|
        # @:adhoc_run_time_section:@ off
        """
        """
        # @:adhoc_run_time_section:@ on
        if macro_xdef_dlm is None:
            macro_xdef_dlm = cls.macro_xdef_delimiters
        if cls.has_expanded_macros(source, macro_xdef_dlm):
            sv = cls.set_delimiters (macro_xdef_dlm)
            source = cls.section_tag_remove(source, 'adhoc_macro_call')
            source = cls.remove_sections(source, 'adhoc_macro_expansion')
            cls.reset_delimiters(sv)
        return source

    # @:adhoc_run_time_section:@ off
    # --------------------------------------------------
    # ||:sec:|| Template Interface
    # --------------------------------------------------

    # @:adhoc_run_time_section:@ on
    @classmethod
    def std_template_param(cls, file_=None, source=None,     # |:clm:|
                           tag=None, is_re=False, all_=False):
        # @:adhoc_run_time_section:@ off
        '''Setup standard template parameters.

        :param tag: If None, section tag `adhoc_template(_v)?` is
          used.

        See :meth:`std_source_param` for `file_` and `source`.
        '''
        # @:adhoc_run_time_section:@ on
        file_, source = cls.std_source_param(file_, source)
        if tag is None:
            is_re=True
            if all_:
                tag = cls.section_tag('adhoc_(template(_v)?|import|unpack)', is_re=is_re)
            else:
                tag = cls.section_tag('adhoc_template(_v)?', is_re=is_re)
        source = cls.activate_macros(source)
        return (file_, source, tag, is_re)

    @classmethod
    def get_templates(cls, file_=None, source=None,          # |:clm:|
                      tag=None, is_re=False,
                      ignore_mark=False, all_=False):
        # @:adhoc_run_time_section:@ off
        '''Extract templates matching section tag.

        :param ignore_mark: If True, all templates are mapped to
          standard output name ``-``.
        :param tag: If None, `adhoc_template` is used.
        '''
        # @:adhoc_run_time_section:@ on
        file_, source, tag, is_re = cls.std_template_param(
            file_, source, tag, is_re, all_)
        source = cls.enable_sections(source, 'adhoc_uncomment')
        source = cls.indent_sections(source, 'adhoc_indent')
        source_sections, template_sections = cls.tag_partition(
            source, tag, is_re=is_re, headline=True)
        templates = {}
        for template_section in template_sections:
            tagged_line = template_section[0]
            section = template_section[1]
            tag, tag_arg = cls.section_tag_parse(tagged_line)
            if not tag_arg:
                tag_arg = '-'
            if tag_arg in cls.template_process_hooks:
                section = cls.template_process_hooks[tag_arg](cls, section, tag, tag_arg)
            if ignore_mark:
                tag_arg = '-'
            if tag_arg not in templates:
                templates[tag_arg] = [[section], tag]
            else:
                templates[tag_arg][0].append(section)
        if all_:
            result = dict([(m, (''.join(t[0]), t[1])) for m, t in templates.items()])
        else:
            result = dict([(m, ''.join(t[0])) for m, t in templates.items()])
        return result

    @classmethod
    def template_list(cls, file_=None, source=None,          # |:clm:|
                      tag=None, is_re=False, all_=False):
        # @:adhoc_run_time_section:@ off
        """Sorted list of templates.

        See :meth:`std_template_param` for `file_`, `source`, `tag`, `is_re`.

        .. @:adhoc_disable:@

        # >>> for tpl in AdHoc.template_list():
        # ...     printf(tpl)
        # -
        # README.txt
        # -adhoc_init
        # -catch-stdout
        # -col-param-closure
        # doc/USE_CASES.txt
        # doc/index.rst
        # -max-width-class
        # -rst-to-ascii
        # -test

        # >>> for tpl in AdHoc.template_list(all_=True):
        # ...     printf(strclean(tpl))
        # ('-', 'adhoc_template')
        # ('README.txt', 'adhoc_template')
        # ('-adhoc_init', 'adhoc_template')
        # ('-catch-stdout', 'adhoc_template')
        # ('-col-param-closure', 'adhoc_template')
        # ('doc/USE_CASES.txt', 'adhoc_template')
        # ('doc/index.rst', 'adhoc_template')
        # ('-max-width-class', 'adhoc_template')
        # ('-rst-to-ascii', 'adhoc_template')
        # ('-test', 'adhoc_template')

        .. @:adhoc_disable:@
        """
        # @:adhoc_run_time_section:@ on
        file_, source, tag, is_re = cls.std_template_param(
            file_, source, tag, is_re, all_)
        templates = cls.get_templates(file_, source, tag, is_re, all_=all_)
        if all_:
            templates.update([(k, ('', v)) for k, v in cls.extra_templates])
            result = list(sorted(
                [(k, v[1]) for k, v in templates.items()],
                key=lambda kt: '||'.join((
                    kt[1],
                    (((not (kt[0].startswith('-') or kt[0].startswith('!')))
                      and (kt[0]))
                     or (kt[0][1:]))))))
        else:
            templates.update(filter(
                lambda tdef: (tdef[1] == 'adhoc_template'
                              or tdef[1] == 'adhoc_template_v'),
                cls.extra_templates))
            result = list(sorted(
                templates.keys(),
                key=lambda kt: '||'.join((
                    (((not (kt.startswith('-') or kt.startswith('!')))
                      and (kt)) or (kt[1:]))))))
        return result

    # @:adhoc_run_time_section:@ off
    # @:adhoc_template:@ -col-param-closure
    # @:adhoc_run_time_section:@ on
    @classmethod
    def col_param_closure(cls):                              # |:clm:|
        # @:adhoc_run_time_section:@ off
        '''Closure for setting up maximum width, padding and separator
        for table columns.

        :returns: a setter and a getter function for calculating the
          maximum width of a list of strings (e.g. a table column).

        >>> set_, get_ = AdHoc.col_param_closure()
        >>> i = set_("string")
        >>> get_()
        [6, '      ', '======']

        >>> i = set_("str")
        >>> get_()
        [6, '      ', '======']

        >>> i = set_("longer string")
        >>> get_()
        [13, '             ', '=============']

        >>> table_in = """\\
        ... Column1 Column2
        ... some text text
        ... some-more-text text text
        ... something text
        ... less"""

        A splitter and column parameters depending on column count:

        >>> col_count = 2
        >>> splitter = lambda line: line.split(' ', col_count-1)
        >>> col_params = [AdHoc.col_param_closure() for i in range(col_count)]

        Generic table processor:

        >>> process_cols = lambda cols: [
        ...     col_params[indx][0](col) for indx, col in enumerate(cols)]
        >>> table = [process_cols(cols) for cols in
        ...          [splitter(line) for line in table_in.splitlines()]]

        Generic table output parameters/functions:

        >>> mws = [cp[1]()[0] for cp in col_params]
        >>> sep = ' '.join([cp[1]()[2] for cp in col_params])
        >>> paddings = [cp[1]()[1] for cp in col_params]
        >>> pad_cols_c = lambda cols: [
        ...     (((paddings[indx] is None) and (col))
        ...      or ((paddings[indx][:int((mws[indx]-len(col))/2)]
        ...           + col + paddings[indx])[:mws[indx]]))
        ...     for indx, col in enumerate(cols)]
        >>> pad_cols = lambda cols: [
        ...     (((paddings[indx] is None) and (col))
        ...      or ((col + paddings[indx])[:mws[indx]]))
        ...     for indx, col in enumerate(cols)]

        Generic table output generator:

        >>> output = []
        >>> if table:
        ...     output.append(sep)
        ...     output.append(' '.join(pad_cols_c(table.pop(0))).rstrip())
        ...     if table: output.append(sep)
        ...     output.extend([' '.join(pad_cols(cols)).rstrip()
        ...                    for cols in table])
        ...     output.append(sep)

        >>> i = sys.stdout.write("\\n".join(output))
        ============== =========
           Column1      Column2
        ============== =========
        some           text text
        some-more-text text text
        something      text
        less
        ============== =========
        '''
        # @:adhoc_run_time_section:@ on
        mw = [0, "", ""]
        def set_(col):                                       # |:clo:|
            lc = len(col)
            if mw[0] < lc:
                mw[0] = lc
                mw[1] = " " * lc
                mw[2] = "=" * lc
            return col
        def get_():                                          # |:clo:|
            return mw
        return set_, get_
    # @:adhoc_run_time_section:@ off
    # @:adhoc_template:@ -col-param-closure
    # @:adhoc_run_time_section:@ on

    tt_ide = False
    tt_comment = ''
    tt_prefix = ''
    tt_suffix = ''

    @classmethod
    def template_table(cls, file_=None, source=None,         # |:clm:|
                       tag=None, is_re=False):
        # @:adhoc_run_time_section:@ off
        '''Table of template commands.

        See :meth:`std_template_param` for `file_`, `source`, `tag`, `is_re`.
        '''
        # @:adhoc_run_time_section:@ on
        file_, source, tag, is_re = cls.std_template_param(
            file_, source, tag, is_re, all_=True)
        pfx = cls.tt_prefix
        sfx = cls.tt_suffix
        comm = cls.tt_comment
        if comm:
            comm = ''.join((comm, ' '))
            pfx = ''.join((comm, pfx))
        if cls.tt_ide:
            command = ''.join(('python ', file_))
        else:
            command = os.path.basename(file_)
        # Parse table
        table = []
        tpl_arg_name = (lambda t: (((not (t.startswith('-') or t.startswith('!'))) and (t)) or (t[1:])))
        col_param = [cls.col_param_closure() for i in range(3)]
        table.append((col_param[0][0]('Command'), col_param[1][0]('Template'), col_param[2][0]('Type')))
        table.extend([
            (col_param[0][0](''.join((
                pfx,
                command, ' --template ',
                tpl_arg_name(t[0])
                )).rstrip()),
             col_param[1][0](''.join((
                 '# ', t[0]
                 )).rstrip()),
             col_param[2][0](''.join((
                 t[1], sfx
                 )).rstrip()),)
            for t in cls.template_list(file_, source, tag, is_re, all_=True)])
        if cls.tt_ide:
            itable = []
            headers = table.pop(0)
            this_type = None
            last_type = None
            for cols in reversed(table):
                this_type = cols[2].replace('")', '')
                if last_type is not None:
                    if last_type != this_type:
                        itable.append((''.join((comm, ':ide: +#-+')), '', ''))
                        itable.append((''.join((comm, '. ', last_type, '()')), '', ''))
                        itable.append(('', '', ''))
                itable.append((''.join((comm, ':ide: ', cols[1].replace('#', 'AdHoc:'))), '', ''))
                itable.append(cols)
                itable.append(('', '', ''))
                last_type = this_type
            if last_type is not None:
                itable.append((''.join((comm, ':ide: +#-+')), '', ''))
                itable.append((''.join((comm, '. ', last_type, '()')), '', ''))
            table = [headers]
            table.extend(itable)
        # Setup table output
        mw, padding = (col_param[0][1]()[0], col_param[0][1]()[1])
        mw1, padding1 = (col_param[1][1]()[0], col_param[1][1]()[1])
        mw2, padding2 = (col_param[2][1]()[0], col_param[2][1]()[1])
        sep = ' '.join([cp[1]()[2] for cp in col_param])
        make_row_c = lambda row: ''.join((
            ''.join((padding[:int((mw-len(row[0]))/2)], row[0], padding))[:mw],
            ' ', ''.join((padding1[:int((mw1-len(row[1]))/2)],
                          row[1], padding1))[:mw1],
            ' ', ''.join((padding2[:int((mw2-len(row[2]))/2)],
                          row[2], padding2))[:mw2].rstrip()))
        make_row = lambda row: ''.join((''.join((row[0], padding))[:mw],
                                        ' ', ''.join((row[1], padding))[:mw1],
                                        ' ', row[2])).rstrip()
        # Generate table
        output = []
        output.append(sep)
        output.append(make_row_c(table.pop(0)))
        if table:
            output.append(sep)
            output.extend([make_row(row) for row in table])
        output.append(sep)
        return output

    @classmethod
    def get_named_template(cls, name=None, file_=None, source=None, # |:clm:|
                           tag=None, is_re=False, ignore_mark=False):
        # @:adhoc_run_time_section:@ off
        '''Extract templates matching section tag and name.

        :param name: Template name. If None, standard output name ``-`` is used.
        :param tag: If None, `adhoc_template(_v)?` is used.
        :param ignore_mark: If True, all templates are mapped to
          standard output name ``-``.

        If a named template cannot be found and `name` does not start
        with ``-``, the template name `-name` is tried.

        >>> ign = main("adhoc.py --template adhoc_test.sub".split())
        # -*- coding: utf-8 -*-
        <BLANKLINE>
        ADHOC_TEST_SUB_IMPORTED = True

        '''
        # @:adhoc_run_time_section:@ on
        if name is None:
            name = '-'
        file_, source, tag, is_re = cls.std_template_param(
            file_, source, tag, is_re, all_=True)
        templates = cls.get_templates(
            file_, source, tag, is_re=is_re, ignore_mark=ignore_mark, all_=True)
        check_name = name
        if check_name not in templates and not name.startswith('-'):
            check_name = ''.join(('-', name))
        if check_name not in templates and not name.startswith('!'):
            check_name = ''.join(('!', name))
        if check_name in templates:
            template_set = templates[check_name]
        else:
            template_set = ['', 'adhoc_template']
        template = template_set[0]
        template_type = template_set[1]
        if check_name.startswith('!'):
            template = cls.dump_(template, template_type)
        return template

    @classmethod
    def extract_templates(cls, file_=None, source=None,      # |:clm:|
                          tag=None, is_re=False, ignore_mark=False,
                          export=False):
        # @:adhoc_run_time_section:@ off
        '''Extract template.

        # @:adhoc_template_check:@ -mark
        A template ...
        # @:adhoc_template_check:@

        # @:adhoc_template_check:@ -other
        Another interleaved
        # @:adhoc_template_check:@

        # @:adhoc_template_check:@ -mark
        continued
        # @:adhoc_template_check:@

        >>> AdHoc.extract_templates(
        ...     tag=AdHoc.section_tag("adhoc_template_check"))
                A template ...
                continued
                Another interleaved

        >>> rt_section = AdHoc.get_templates(
        ...     __file__, None,
        ...     tag=AdHoc.section_tag("adhoc_run_time_section"),
        ...     ignore_mark=True)
        >>> rt_section = ''.join(rt_section.values())

        .. >>> printf(rt_section)
        '''
        # @:adhoc_run_time_section:@ on
        file_, source, tag, is_re = cls.std_template_param(
            file_, source, tag, is_re)
        templates = cls.get_templates(
            file_, source, tag, is_re=is_re, ignore_mark=ignore_mark)
        sv_extract_warn = cls.extract_warn
        cls.extract_warn = True
        for outf, template in sorted(templates.items()):
            if outf.startswith('-'):
                outf = '-'
            if outf == '-' and export:
                continue
            xfile = cls.check_xfile(outf, cls.extract_dir)
            if xfile is not None:
                cls.write_source(xfile, template)
        cls.extract_warn = sv_extract_warn

    # @:adhoc_run_time_section:@ off

    # --------------------------------------------------
    # ||:sec:|| COMPILER DATA
    # --------------------------------------------------

    # tags are generated from symbols on init
    run_time_flag = None                      # line
    import_flag = None                        # line
    include_flag = None                       # line
    verbatim_flag = None                      # line
    compiled_flag = None                      # line
    run_time_class_flag = None                # line

    rt_engine_section_tag = None              # section
    indent_section_tag = None                 # section
    uncomment_section_tag = None              # section
    enable_section_tag = None                 # section
    disable_section_tag = None                # section
    remove_section_tag = None                 # section
    import_section_tag = None                 # section
    unpack_section_tag = None                 # section
    template_v_section_tag = None             # section
    template_section_tag = None               # section
    run_time_section_tag = None               # section

    run_time_section = None

    run_time_flag_symbol = 'adhoc_run_time'   # line
    import_flag_symbol = 'adhoc'              # line
    include_flag_symbol = 'adhoc_include'     # line
    verbatim_flag_symbol = 'adhoc_verbatim'   # line
    compiled_flag_symbol = 'adhoc_compiled'   # line
    run_time_class_symbol = 'adhoc_run_time_class' # line

    rt_engine_section_symbol = 'adhoc_run_time_engine' # section
    indent_section_symbol = 'adhoc_indent'             # section
    uncomment_section_symbol = 'adhoc_uncomment'       # section
    enable_section_symbol = 'adhoc_enable'             # section
    disable_section_symbol = 'adhoc_disable'           # section
    remove_section_symbol = 'adhoc_remove'             # section
    import_section_symbol = 'adhoc_import'             # section
    unpack_section_symbol = 'adhoc_unpack'             # section
    template_v_section_symbol = 'adhoc_template_v'     # section
    template_section_symbol = 'adhoc_template'         # section
    run_time_section_symbol = 'adhoc_run_time_section' # section

    run_time_class_prefix = 'Rt'
    import_function = 'AdHoc.import_'
    modules = {}
    compiling = []

    file_include_template = (                             # |:api_fi:|
        "{ind}"
        "# {stg}\n{ind}"
        "{rtp}{ahc}("
        "{mod},"
        " file_={fnm},\n{ina}"
        " mtime={mtm},"
        " mode={fmd},\n{ina}"
        " zipped={zip},"
        " flat={flt},"
        " source64=\n"
        "{src}"
        ")\n{ind}"
        "# {etg}\n"
        )

    # --------------------------------------------------
    # ||:sec:|| Setup
    # --------------------------------------------------

    def __init__(self):                                      # |:mth:|
        self.modules = {}
        self.compiling = []
        self.setup_tags()
        self.run_time_section = self.prepare_run_time_section().rstrip() + '\n'

    @classmethod
    def setup_tags(cls):                                     # |:mth:|
        cls.run_time_flag = cls.line_tag(cls.run_time_flag_symbol)
        cls.import_flag = cls.line_tag(cls.import_flag_symbol)
        cls.verbatim_flag = cls.line_tag(cls.verbatim_flag_symbol)
        cls.include_flag = cls.line_tag(cls.include_flag_symbol)
        cls.compiled_flag = cls.line_tag(cls.compiled_flag_symbol)
        cls.run_time_class_flag = cls.line_tag(cls.run_time_class_symbol)

        cls.rt_engine_section_tag = cls.section_tag(cls.rt_engine_section_symbol)
        cls.indent_section_tag = cls.section_tag(cls.indent_section_symbol)
        cls.uncomment_section_tag = cls.section_tag(cls.uncomment_section_symbol)
        cls.enable_section_tag = cls.section_tag(cls.enable_section_symbol)
        cls.disable_section_tag = cls.section_tag(cls.disable_section_symbol)
        cls.remove_section_tag = cls.section_tag(cls.remove_section_symbol)
        cls.import_section_tag = cls.section_tag(cls.import_section_symbol)
        cls.unpack_section_tag = cls.section_tag(cls.unpack_section_symbol)
        cls.template_v_section_tag = cls.section_tag(cls.template_v_section_symbol)
        cls.template_section_tag = cls.section_tag(cls.template_section_symbol)
        cls.run_time_section_tag = cls.section_tag(
            cls.run_time_section_symbol)

    # --------------------------------------------------
    # ||:sec:|| Tools
    # --------------------------------------------------

    @staticmethod
    def strquote(source, indent=(' ' * 4)):                  # |:fnc:|
        source = source.replace("'", "\\'")
        length = 78 - 2 - 4 - len(indent)
        if length < 50:
            length = 50
        output_parts = []
        indx = 0
        limit = len(source)
        while indx < limit:
            output_parts.extend((
                indent, "    '", source[indx:indx+length], "'\n"))
            indx += length
        return ''.join(output_parts)

    # --------------------------------------------------
    # ||:sec:|| Run-Time Section
    # --------------------------------------------------

    @classmethod
    def adhoc_run_time_sections_from_string(cls, string, symbol): # |:clm:|
        tag = sformat('(#[ \t\r]*)?{0}', cls.section_tag(symbol, is_re=True))
        def_sections = cls.tag_sections(string, tag, is_re=True)
        return def_sections

    @classmethod
    def adhoc_run_time_section_from_file(cls, file_, symbol): # |:clm:|
        if file_.endswith('.pyc'):
            file_ = file_[:-1]
        string = cls.read_source(file_)
        def_sections = cls.adhoc_run_time_sections_from_string(
            string, symbol)
        return def_sections

    @classmethod
    def adhoc_get_run_time_section(                          # |:clm:|
        cls, symbol, prolog='', epilog=''):
        import datetime

        adhoc_module_places = []

        # try __file__
        adhoc_module_places.append(__file__)
        def_sections = cls.adhoc_run_time_section_from_file(
            __file__, symbol)
        if len(def_sections) == 0:
            # try adhoc.__file__
            try:
                import adhoc
                adhoc_module_places.append(adhoc.__file__)
                def_sections = cls.adhoc_run_time_section_from_file(
                    adhoc.__file__, symbol)
            except:
                pass
        if len(def_sections) == 0:
            # try adhoc.__adhoc__.source
            try:
                adhoc_module_places.append('adhoc.__adhoc__.source')
                def_sections = cls.adhoc_run_time_sections_from_string(
                    adhoc.__adhoc__.source, symbol)
            except:
                pass

        if len(def_sections) == 0:
            adhoc_dump_list(def_sections)
            raise AdHocError(sformat('{0} not found in {1}',
                    cls.section_tag(symbol),
                    ', '.join(adhoc_module_places)))

        def_ = ''.join((
                sformat('# {0}\n', cls.remove_section_tag),
                sformat('# {0}\n', cls.rt_engine_section_tag),
                sformat('# -*- coding: utf-8 -*-\n'),
                sformat('# {0} {1}\n', cls.compiled_flag,
                                     datetime.datetime.now(),
                                     # |:todo:| add input filename
                                     ),
                prolog,
                ''.join(def_sections),
                epilog,
                sformat('# {0}\n', cls.rt_engine_section_tag),
                sformat('# {0}\n', cls.remove_section_tag),
                ))
        return def_

    @classmethod
    def prepare_run_time_section(cls):                       # |:mth:|
        rts = cls.adhoc_get_run_time_section(
            cls.run_time_section_symbol)
        rtc_sections = cls.tag_split(
            rts, cls.run_time_class_flag)
        transform = []
        done = False
        use_next = False
        for section in rtc_sections:
            blob = section[1]
            if section[0]:
                use_next = blob
                continue
            if use_next:
                if not done:
                    mo = re.search('class[ \t\r]+', blob)
                    if mo:
                        blob = (blob[:mo.end(0)]
                              + cls.run_time_class_prefix
                              + blob[mo.end(0):])
                        done = True
                    else:
                        #transform.append(use_next)
                        pass
                use_next = False
            transform.append(blob)
        transform.append(sformat('# {0}\n', cls.remove_section_tag))
        transform.append(sformat('# {0}\n', cls.rt_engine_section_tag))
        transform.append(sformat('# {0}\n', cls.rt_engine_section_tag))
        transform.append(sformat('# {0}\n', cls.remove_section_tag))
        rts = ''.join(transform)
        if not done:
            raise AdHocError(
                sformat('run-time class(tag) `{0}` not found in:\n{1}',
                        cls.run_time_class_flag, rts))
        return rts

    # --------------------------------------------------
    # ||:sec:|| Internal Includer (verbatim)
    # --------------------------------------------------

    def verbatim_(self, string, name=None):                  # |:mth:|
        '''Entry point for verbatim inclusion.

        :returns: string with verbatim included files.

        :param string: input string, with |adhoc_verbatim| flags.
        :param name: ignored. (API compatibility with
          :meth:`AdHoc.compile_`).

        .. note:: double commented flags, e.g. ``##``
           |adhoc_verbatim|, are ignored.

        .. \\|:here:|

        >>> section = """\\
        ... some
        ...     @:""" """adhoc_verbatim:@ {flags} my_verbatim{from_}
        ... text\\
        ... """

        >>> adhoc = AdHoc()

        **Non-existent File**

        >>> sv_quiet = AdHoc.quiet
        >>> AdHoc.quiet = True
        >>> source = adhoc.verbatim_(sformat(section, flags="-2#", from_=""))
        >>> printf(source) #doctest: +ELLIPSIS
        some
            @:adhoc_verbatim... -2# my_verbatim
        text
        >>> AdHoc.quiet = sv_quiet

        **Empty File**

        >>> source = adhoc.verbatim_(sformat(section, flags="", from_=" from /dev/null"))
        >>> printf(source) #doctest: +ELLIPSIS
        some
            @:adhoc_verbatim...  my_verbatim from /dev/null
            # @:adhoc_remove...
            # @:adhoc_indent... -4
            # @:adhoc_template_v... my_verbatim
            # @:adhoc_template_v...
            # @:adhoc_indent...
            # @:adhoc_remove...
        text

        **Empty file, with negative indent, commented**

        >>> source = adhoc.verbatim_(sformat(section, flags="-2#", from_=" from /dev/null"))
        >>> printf(source) #doctest: +ELLIPSIS
        some
            @:adhoc_verbatim... -2# my_verbatim from /dev/null
          # @:adhoc_remove...
          # @:adhoc_uncomment...
          # @:adhoc_indent... -2
          # @:adhoc_template_v... my_verbatim
          # @:adhoc_template_v...
          # @:adhoc_indent...
          # @:adhoc_uncomment...
          # @:adhoc_remove...
        text

        **Empty file, with overflowing negative indent, commented**

        >>> source = adhoc.verbatim_(sformat(section, flags="-8#", from_=" from /dev/null"))
        >>> printf(source) #doctest: +ELLIPSIS
        some
            @:adhoc_verbatim... -8# my_verbatim from /dev/null
        # @:adhoc_remove...
        # @:adhoc_uncomment...
        # @:adhoc_template_v... my_verbatim
        # @:adhoc_template_v...
        # @:adhoc_uncomment...
        # @:adhoc_remove...
        text

        **Existing file, without newline at end of file, commented.**

        >>> mvf = open("my_verbatim", "w")
        >>> ign = mvf.write("no end of line")
        >>> mvf.close()
        >>> source = adhoc.verbatim_(sformat(section, flags="-4#", from_=""))
        >>> printf(source) #doctest: +ELLIPSIS
        some
            @:adhoc_verbatim... -4# my_verbatim
        # @:adhoc_remove...
        # @:adhoc_uncomment...
        # @:adhoc_template_v... my_verbatim
        # no end of line
        # @:adhoc_template_v...
        # @:adhoc_uncomment...
        # @:adhoc_remove...
        text

        **Existing file, with extra newline at end of file, commented.**

        >>> mvf = open("my_verbatim", "w")
        >>> ign = mvf.write("extra end of line\\n\\n")
        >>> mvf.close()
        >>> source = adhoc.verbatim_(sformat(section, flags="-4#", from_=""))
        >>> printf(source) #doctest: +ELLIPSIS
        some
            @:adhoc_verbatim... -4# my_verbatim
        # @:adhoc_remove...
        # @:adhoc_uncomment...
        # @:adhoc_template_v... my_verbatim
        # extra end of line
        <BLANKLINE>
        # @:adhoc_template_v...
        # @:adhoc_uncomment...
        # @:adhoc_remove...
        text

        **Existing file, without newline at end of file, not commented.**

        >>> mvf = open("my_verbatim", "w")
        >>> ign = mvf.write("no end of line")
        >>> mvf.close()
        >>> source = adhoc.verbatim_(sformat(section, flags="-4", from_=""))
        >>> printf(source) #doctest: +ELLIPSIS
        some
            @:adhoc_verbatim... -4 my_verbatim
        # @:adhoc_remove...
        # @:adhoc_template_v... my_verbatim
        no end of line
        # @:adhoc_template_v...
        # @:adhoc_remove...
        text

        **Existing file, with extra newline at end of file, not commented.**

        >>> mvf = open("my_verbatim", "w")
        >>> ign = mvf.write("extra end of line\\n\\n")
        >>> mvf.close()
        >>> source = adhoc.verbatim_(sformat(section, flags="", from_=""))
        >>> printf(source) #doctest: +ELLIPSIS
        some
            @:adhoc_verbatim... my_verbatim
            # @:adhoc_remove...
            # @:adhoc_indent:@ -4
            # @:adhoc_template_v... my_verbatim
            extra end of line
        <BLANKLINE>
            # @:adhoc_template_v...
            # @:adhoc_indent:@
            # @:adhoc_remove...
        text

        **Existing file, but override with source /dev/null.**

        >>> source = adhoc.verbatim_(sformat(section, flags="/dev/null as", from_=""))
        >>> printf(source) #doctest: +ELLIPSIS
        some
            @:adhoc_verbatim... /dev/null as my_verbatim
            # @:adhoc_remove...
            # @:adhoc_indent... -4
            # @:adhoc_template_v... my_verbatim
            # @:adhoc_template_v...
            # @:adhoc_indent...
            # @:adhoc_remove...
        text

        **Existing file, override with non-existing source /not-here/.**

        >>> if os.path.exists("not-here"):
        ...     os.unlink("not-here")
        >>> source = adhoc.verbatim_(sformat(section, flags="not-here as", from_=""))
        >>> printf(source) #doctest: +ELLIPSIS
        some
            @:adhoc_verbatim... not-here as my_verbatim
            # @:adhoc_remove...
            # @:adhoc_indent... -4
            # @:adhoc_template_v... my_verbatim
            extra end of line
        <BLANKLINE>
            # @:adhoc_template_v...
            # @:adhoc_indent...
            # @:adhoc_remove...
        text

        >>> os.unlink("my_verbatim")
        '''
        m = 'is: '

        import datetime

        # # check for @: adhoc_compiled :@
        # adhoc_compiled_lines = self.tag_lines(
        #     string, self.line_tag('adhoc_compiled'))
        # if len(adhoc_compiled_lines) > 0:
        #     sys.stderr.write(sformat(
        #         '{0}{1}' 'warning: {2} already AdHoc\'ed `{3}`\n',
        #         dbg_comm, m, name, adhoc_compiled_lines[0].rstrip()))
        #     return string

        # handle @: adhoc_verbatim :@
        result = []
        verbatim_cmd_parts = self.tag_split(string, self.verbatim_flag)
        for part in verbatim_cmd_parts:
            verbatim_def = part[1]
            result.append(verbatim_def)
            if part[0]:
                # skip commented verbatim includes
                if re.match('\\s*#\\s*#', verbatim_def):
                    if self.verbose:
                        printe(sformat(
                            '{0}{1}Skipping disabled verbatim `{2}`',
                            dbg_comm, m, verbatim_def.rstrip()))
                    continue

                indent = ''
                mo = re.match('\\s*', verbatim_def)
                if mo:
                    indent = mo.group(0)

                verbatim_def = self.line_tag_strip(
                    verbatim_def, self.verbatim_flag_symbol)
                verbatim_specs = []
                for verbatim_spec in re.split('\\s*,\\s*', verbatim_def):
                    verbatim_spec1 = re.split('\\s+from\\s+', verbatim_spec)
                    verbatim_spec2 = re.split('\\s+as\\s+', verbatim_spec)
                    default = None
                    source = None
                    output = None
                    flags = None
                    if len(verbatim_spec1) > 1:
                        output = verbatim_spec1[0]
                        default = verbatim_spec1[1]
                        fields = re.split('\\s+', output, 1)
                        if len(fields) > 1:
                            flags = fields[0]
                            output = fields[1]
                        else:
                            flags = ''
                        source = output
                    if len(verbatim_spec2) > 1:
                        source = verbatim_spec2[0]
                        output = verbatim_spec2[1]
                        fields = re.split('\\s+', source, 1)
                        if len(fields) > 1:
                            flags = fields[0]
                            source = fields[1]
                        else:
                            flags = ''
                        default = output
                    if flags is None:
                        source = verbatim_spec
                        fields = re.split('\\s+', source, 1)
                        if len(fields) > 1:
                            flags = fields[0]
                            source = fields[1]
                        else:
                            flags = ''
                            source = fields[0]
                        default = source
                        output = source
                    verbatim_specs.append([flags, source, default, output])

                for verbatim_spec in verbatim_specs:
                    vflags = verbatim_spec.pop(0)
                    ifile = verbatim_spec.pop()
                    found = False
                    for lfile in verbatim_spec:
                        lfile = os.path.expanduser(lfile)
                        blfile = lfile
                        for include_dir in self.include_path:
                            if not os.path.exists(lfile):
                                if not (os.path.isabs(blfile)):
                                    lfile = os.path.join(include_dir, blfile)
                                    continue
                            break
                        if os.path.exists(lfile):
                            stat = os.stat(lfile)
                            mtime = datetime.datetime.fromtimestamp(
                                stat.st_mtime)
                            mode = stat.st_mode

                            exp_source = self.read_source(lfile)
                            source_len = len(exp_source)

                            start_tags = []
                            end_tags = []
                            prefix = []
                            tag_prefix = ['# ']

                            mo = re.search('[-+]?[0-9]+', vflags)
                            if mo:
                                uindent = int(mo.group(0))
                            else:
                                uindent = 0

                            tindent = (len(indent) + uindent)
                            if tindent < 0:
                                tindent = 0
                            if tindent:
                                tag = self.indent_section_tag
                                start_tags.insert(
                                    0, ''.join((tag, ' ', str(-tindent))))
                                end_tags.append(tag)
                                prefix.insert(0, ' ' * tindent)
                                tag_prefix.insert(0, ' ' * tindent)

                            if '#' in vflags:
                                tag = self.uncomment_section_tag
                                start_tags.insert(0, tag)
                                end_tags.append(tag)
                                exp_source, hl = self.disable_transform(exp_source)

                            tag = self.remove_section_tag
                            start_tags.insert(0, tag)
                            end_tags.append(tag)

                            tag = self.section_tag('adhoc_template_v')
                            start_tags.append(''.join((tag, ' ', ifile)))
                            end_tags.insert(0,tag)

                            prefix = ''.join(prefix)
                            tag_prefix = ''.join(tag_prefix)
                            if prefix and exp_source:
                                if exp_source.endswith('\n'):
                                    exp_source = exp_source[:-1]
                                exp_source = re.sub('^(?m)', prefix, exp_source)
                            if exp_source and not exp_source.endswith('\n'):
                                exp_source = ''.join((exp_source, '\n'))

                            output = []
                            output.extend([''.join((
                                tag_prefix, tag, '\n')) for tag in start_tags])
                            output.append(exp_source)
                            output.extend([''.join((
                                tag_prefix, tag, '\n')) for tag in end_tags])
                            result.append(''.join(output))
                            found = True

                            # |:debug:|
                            if self.verbose:
                                printe(sformat(
                                    "{0}{3:^{1}} {4:<{2}s}: ]len: {5:>6d}"
                                    " exp: {6:>6d} ]{9}[",
                                    dbg_comm, dbg_twid, dbg_fwid, ':INF:',
                                    'source stats', source_len, len(exp_source),
                                    0, 0, ifile))
                            # |:debug:|
                            break
                    if not found and not self.quiet:
                        list(map(sys.stderr.write,
                                 ("# if: ", self.__class__.__name__,
                                  ": warning verbatim file `", ifile,
                                  "` not found from `",
                                  ', '.join(verbatim_spec), "`\n")))
        #adhoc_dump_list(result)
        return ''.join(result)

    # --------------------------------------------------
    # ||:sec:|| Internal Includer (packed)
    # --------------------------------------------------

    def include_(self, string, name=None, zipped=True, flat=None): # |:mth:|
        '''Entry point for inclusion.

        :returns: string with packed included files.

        :param string: input string, with |adhoc_include| flags.
        :param name: ignored. (API compatibility with
          :meth:`AdHoc.compile_`).
        :param zipped: if True, :mod:`gzip` included files.

        .. note:: double commented flags, e.g. ``##``
           |adhoc_include|, are ignored.

        .. \\|:here:|

        >>> section = """\\
        ... some
        ... @:""" """adhoc_include:@ Makefile
        ... text\\
        ... """

        .. @:adhoc_disable:@

        # >>> adhoc = AdHoc()
        # >>> source = adhoc.include_(section)
        # >>> printf(source) #doctest: +ELLIPSIS
        # some
        # @:adhoc_include... Makefile
        # # @:adhoc_unpack...
        # RtAdHoc.unpack_(None, file_='Makefile',
        #     mtime='...', mode=...,
        #     zipped=True, flat=None, source64=
        # ...
        # # @:adhoc_unpack...
        # text

        .. @:adhoc_disable:@
        '''
        m = 'is: '

        import datetime

        # # check for @: adhoc_compiled :@
        # adhoc_compiled_lines = self.tag_lines(
        #     string, self.line_tag('adhoc_compiled'))
        # if len(adhoc_compiled_lines) > 0:
        #     sys.stderr.write(sformat(
        #         '{0}{1}' 'warning: {2} already AdHoc\'ed `{3}`\n',
        #         dbg_comm, m, name, adhoc_compiled_lines[0].rstrip()))
        #     return string

        # handle @: adhoc_include :@
        result = []
        include_cmd_sections = self.tag_split(string, self.include_flag)
        for section in include_cmd_sections:
            include_def = section[1]
            result.append(include_def)
            if section[0]:
                # skip commented includes
                if re.match('\\s*#\\s*#', include_def):
                    if self.verbose:
                        printe(sformat(
                            '{0}{1}Skipping disabled include `{2}`',
                            dbg_comm, m, include_def.rstrip()))
                    continue

                indent = ''
                mo = re.match('\\s*', include_def)
                if mo:
                    indent = mo.group(0)

                include_def = self.line_tag_strip(
                    include_def, self.include_flag_symbol)
                include_specs = []
                for include_spec in re.split('\\s*,\\s*', include_def):
                    include_spec1 = re.split('\\s+from\\s+', include_spec)
                    include_spec2 = re.split('\\s+as\\s+', include_spec)
                    default = None
                    source = None
                    output = None
                    if len(include_spec1) > 1:
                        output = include_spec1[0]
                        default = include_spec1[1]
                        source = output
                    if len(include_spec2) > 1:
                        source = include_spec2[0]
                        output = include_spec2[1]
                        default = output
                    if source is None:
                        source = include_spec
                        output = source
                        default = source
                    include_specs.append([source, default, output])

                for include_spec in include_specs:
                    ifile = include_spec.pop()
                    found = False
                    for lfile in include_spec:
                        lfile = os.path.expanduser(lfile)
                        blfile = lfile
                        for include_dir in self.include_path:
                            if not os.path.exists(lfile):
                                if not (os.path.isabs(blfile)):
                                    lfile = os.path.join(include_dir, blfile)
                                    continue
                            break
                        if os.path.exists(lfile):
                            stat = os.stat(lfile)
                            mtime = datetime.datetime.fromtimestamp(
                                stat.st_mtime)
                            mode = stat.st_mode

                            exp_source = self.read_source(lfile, decode=False)
                            source64 = self.pack_file(exp_source, zipped)
                            output = self.strquote(source64, indent)
                            file_include_args = dict([    # |:api_fi:|
                                ('ind', indent),
                                ('ina', ''.join((indent, "   "))),
                                ('stg', ''.join((self.unpack_section_tag, ' !', ifile))),
                                ('etg', self.unpack_section_tag),
                                ('rtp', self.run_time_class_prefix),
                                ('ahc', 'AdHoc.unpack_'),
                                ('mod', 'None'),
                                ('fnm', repr(str(ifile))),
                                ('mtm', (((mtime is not None)
                                          and repr(mtime.isoformat()))
                                         or repr(mtime))),
                                ('fmd', (mode is not None and sformat('int("{0:o}", 8)', mode)) or mode),
                                ('zip', zipped),
                                ('flt', flat),
                                ('src', output.rstrip()),
                            ])
                            output = sformat(
                                self.file_include_template,
                                **file_include_args
                                )
                            result.append(output)
                            found = True
                            # |:debug:|
                            if self.verbose:
                                source_len = len(exp_source)
                                exp_source_len = len(exp_source)
                                source64_len = len(source64)
                                printe(sformat(
                                    "{0}{3:^{1}} {4:<{2}s}: ]len: {5:>6d}"
                                    " exp: {6:>6d} b64: {8:>6d}[ ]{9}[",
                                    dbg_comm, dbg_twid, dbg_fwid, ':INF:',
                                    'source stats', source_len, exp_source_len,
                                    0, source64_len, ifile))
                            # |:debug:|
                            break
                    if not found and not self.quiet:
                        list(map(sys.stderr.write,
                                 ("# if: ", self.__class__.__name__,
                                  ": warning include file `",
                                  ifile, "` not found from `",
                                  ', '.join(include_spec), "`\n")))
        #adhoc_dump_list(result)
        return ''.join(result)

    # --------------------------------------------------
    # ||:sec:|| Internal Compiler
    # --------------------------------------------------

    def encode_module_(                                      # |:mth:|
        self, module, for_=None, indent='', zipped=True, flat=None, forced=None):
        m = 'gm: '

        if for_ is None:
            for_ = self.import_function

        if forced is None:
            forced = self.forced

        module = self.module_setup(module)
        module_name = module.__name__

        # no multiple occurences
        if (not forced
            and (module_name in self.modules
                 or module_name in self.compiling)):
            if self.verbose:
                 # |:check:| what, if the previous import was never
                 # executed?
                sys.stderr.write(sformat(
                        '{0}{1}`{2}` already seen. skipping ...\n',
                        dbg_comm, m, module_name))
            return ''

        self.compiling.append(module_name)

        result = []
        # |:todo:| parent modules
        parts = module_name.split('.')
        parent_modules = parts[:-1]
        if self.verbose and len(parent_modules) > 0:
            sys.stderr.write(sformat(
                    '{0}{1}Handle parent module(s) `{2}`\n',
                    dbg_comm, m, parent_modules))
        for parent_module in parent_modules:
            result.append(self.encode_module_(
                parent_module, for_, indent, zipped, flat, forced))

        if (module_name in self.modules):
            if self.verbose:
                sys.stderr.write(sformat(
                    '{0}{1}{1} already seen after parent import\n',
                    dbg_comm, m, module_name))
            return ''.join(result)

        if hasattr(module, '__file__'):
            module_file = module.__file__
            if module_file.endswith('.pyc'):
                module_file = module_file[:-1]
        else:
            module_file = None

        if hasattr(module.__adhoc__, 'source'):
            source = module.__adhoc__.source
        else:
            if not self.quiet:
                printf(sformat(
                    '{0}{1}|' 'warning: `{2}` does not have any source code.',
                    dbg_comm, m, module_name), file=sys.stderr)
            source = ''
            return ''.join(result)

        # recursive!
        exp_source = self.compile_(source, module_file, for_, zipped, forced)
        source64 = self.pack_file(exp_source, zipped)
        output = self.strquote(source64, indent)

        mtime = module.__adhoc__.mtime
        mode = module.__adhoc__.mode
        # |:todo:| make Rt prefix configurable
        file_include_args = dict([                        # |:api_fi:|
            ('ind', indent),
            ('ina', ''.join((indent, "   "))),
            ('stg', ''.join((self.import_section_tag, ' !', module_name))),
            ('etg', self.import_section_tag),
            ('rtp', self.run_time_class_prefix),
            ('ahc', for_),
            ('mod', repr(module.__name__)),
            ('fnm', (((module_file is not None)
                      and repr(str(os.path.relpath(module_file))))
                     or module_file)),
            ('mtm', (((mtime is not None)
                      and repr(mtime.isoformat()))
                     or repr(mtime))),
            ('fmd', (mode is not None and sformat('int("{0:o}", 8)', mode)) or mode),
            ('zip', zipped),
            ('src', output.rstrip()),
            ('flt', flat),
            ])
        output = sformat(
            self.file_include_template,
            **file_include_args
            )
        result.append(output)

        # |:debug:|
        if self.verbose:
            source_len = len(source)
            exp_source_len = len(exp_source)
            source64_len = len(source64)
            printe(sformat(
                "{0}{3:^{1}} {4:<{2}s}: ]len: {5:>6d} exp: {6:>6d}"
                " b64: {8:>6d}[ ]{9}[",
                dbg_comm, dbg_twid, dbg_fwid, ':INF:',
                'source stats', source_len, exp_source_len, 0,
                source64_len, module_file))
        # |:debug:|
        return ''.join(result)

    def compile_(self, string, name=None, for_=None,         # |:mth:|
                 zipped=True, forced=None):
        '''Entry point for compilation.

        :returns: string with fully compiled adhoc source. Includes
          run-time class, imports, packed includes, verbatim includes,
          enabled/disabled sections.

        :param string: input string, with |adhoc| flags.
        :param name: for messages.
        :param for_: :class:`RtAdHoc` method call.
        :param zipped: if True, :mod:`gzip` included files.

        .. note:: for |adhoc|, commented lines, e.g.
           ``# import module # @:``\\ ``adhoc:@``, are ignored.

        .. \\|:here:|
        '''
        m = 'cs: '
        if name is None:
            name = repr(string[:50])
        # check for @: adhoc_compiled :@
        string = self.expand_macros(string)
        adhoc_compiled_lines = self.tag_lines(
            string, self.line_tag('adhoc_compiled'))
        if len(adhoc_compiled_lines) > 0:
            if not self.quiet:
                list(map(sys.stderr.write,
                         ('# ', m,  'warning: ', name, ' already AdHoc\'ed `',
                          adhoc_compiled_lines[0].rstrip(), '`\n',)))
            return string

        # check for @: adhoc_self :@ (should not be taken from any templates)
        adhoc_self_tag = self.line_tag('adhoc_self')
        adhoc_self_lines = self.tag_lines(
            string, adhoc_self_tag)
        if len(adhoc_self_lines) > 0:
            for line in adhoc_self_lines:
                line = re.sub(''.join(('^.*', adhoc_self_tag)), '', line)
                line = line.strip()
                selfs = line.split()
                if self.verbose:
                    printe(sformat(
                        '{0}{1}|' ':INF:| {2} found self: `{3}`',
                        dbg_comm, m, name, ', '.join(selfs)))
                self.compiling.extend(selfs)

        # check for @: adhoc_remove :@
        string = self.section_tag_rename(string, 'adhoc_remove', 'adhoc_remove_')

        # check for @: adhoc_verbatim :@ (templates can define the run-time flag, includes, imports)
        string = self.verbatim_(string, name)

        # search for @: adhoc_run_time :@ and put run-time section there!
        result = []
        ah_run_time_sections = self.tag_split(
            string, self.line_tag(self.run_time_flag_symbol))
        good = False
        for section in ah_run_time_sections:
            config_def = section[1]
            if not good and section[0]:
                # ignore double commented tagged lines
                if not re.match('\\s*#\\s*#', config_def):
                    config_def = sformat('{0}{1}',
                        config_def, self.run_time_section)
                    good = True
            result.append(config_def)
        string = ''.join(result)

        # check for @: adhoc_include :@
        string = self.include_(string, name, zipped)

        # handle @: adhoc :@ imports
        result = []
        import_cmd_sections = self.tag_split(string, self.import_flag)
        if not good and len(import_cmd_sections) > 1:
            adhoc_dump_sections(import_cmd_sections)
            raise AdHocError(sformat('{0} not found',
                    self.line_tag(self.run_time_flag_symbol)))
        for section in import_cmd_sections:
            import_def = section[1]
            if section[0]:
                # skip commented imports
                if re.match('\\s*#', import_def):
                    if self.verbose:
                        printe(sformat(
                            '{0}{1}Skipping disabled `{2}`',
                            dbg_comm, m, import_def.rstrip()))
                    result.append(import_def)
                    continue
                import_args = self.line_tag_strip(import_def, self.import_flag_symbol)
                module = ''
                mo = re.match(
                    '(\\s*)from\\s+([a-zA-Z_][.0-9a-zA-Z_]*)\\s+'
                    'import', import_def)
                if mo:
                    indent = mo.group(1)
                    module = mo.group(2)
                else:
                    mo = re.match(
                        '([ \t\r]*)import[ \t\r]+([a-zA-Z_][.0-9a-zA-Z_]*)',
                        import_def)
                    if mo:
                        indent = mo.group(1)
                        module = mo.group(2)
                if len(module) > 0:
                    module_flat = ((('flat' in import_args.lower().split()) and (True)) or (None))
                    module_flat = ((('full' in import_args.lower().split()) and (False)) or (module_flat))
                    module_forced = ((('force' in import_args.lower().split()) and (True)) or (forced))
                    source = self.encode_module_(module, for_, indent, zipped, module_flat, module_forced)
                    import_def = sformat('{0}{1}',source, import_def)
                else:
                    if self.verbose:
                        list(map(sys.stderr.write,
                                 ('# ', m, 'warning: no import found! `',
                                  import_def.rstrip(), '`\n')))
            result.append(import_def)
        string = ''.join(result)

        # These are last, to avoid enabling/disabling the wrong imports etc.

        # check for @: adhoc_enable :@
        string = self.enable_sections(string, 'adhoc_enable')
        # check for @: adhoc_disable :@
        string = self.disable_sections(string, 'adhoc_disable')

        #adhoc_dump_list(result)
        return string

    # --------------------------------------------------
    # ||:sec:|| User API
    # --------------------------------------------------

    def encode_include(                                      # |:mth:|
        self, file_, as_=None, indent='', zipped=True):
        m = 'if: '

    def encode_module(                                       # |:mth:|
        self, module, for_=None, indent='', zipped=True, flat=None, forced=None):
        if hasattr(module, __name__):
            name = module.__name__
        else:
            name = module
        if self.verbose:
            sys.stderr.write(sformat(
                '{0}--------------------------------------------------\n',
                dbg_comm))
            sys.stderr.write(sformat(
                '{0}Get module `{1}`\n',
                dbg_comm, name))
            sys.stderr.write(sformat(
                '{0}--------------------------------------------------\n',
                dbg_comm))
        return self.encode_module_(module, for_, indent, zipped, flat, forced)

    def compile(self, string, name=None, for_=None,          # |:mth:|
                zipped=True, forced=None):
        '''Compile a string into adhoc output.'''
        if self.verbose:
            if name is None:
                name = repr(string[:50])
            sys.stderr.write(sformat(
                    '{0}--------------------------------------------------\n',
                    dbg_comm))
            sys.stderr.write(sformat(
                    '{0}Compiling string `{1}`\n',
                    dbg_comm, name))
            sys.stderr.write(sformat(
                    '{0}--------------------------------------------------\n',
                    dbg_comm))
        return self.compile_(string, name, for_, zipped, forced)
    # @:adhoc_run_time_section:@ on

    def compileFile(self, file_name, for_=None, zipped=True, forced=None): # |:mth:|
        # @:adhoc_run_time_section:@ off
        """Compile a file into adhoc output.

        Since a module that has RtAdHoc defined is already adhoc'ed,
        the run-time RtAdHoc method returns the file source as is.
        """
        # @:adhoc_run_time_section:@ on
        # @:adhoc_run_time_section:@ off
        if self.verbose:
            sys.stderr.write(sformat(
                '{0}--------------------------------------------------\n',
                dbg_comm))
            sys.stderr.write(
                sformat('{0}Compiling {1}\n',dbg_comm, file_name))
            sys.stderr.write(sformat(
                '{0}--------------------------------------------------\n',
                dbg_comm))
        # @:adhoc_run_time_section:@ on
        file_name, source = self.std_source_param(file_name, None)
        # @:adhoc_run_time_section:@ off
        source = self.compile_(source, file_name, for_, zipped, forced)
        # @:adhoc_run_time_section:@ on
        return source
    # @:adhoc_run_time_section:@ END

# (progn (forward-line -1) (insert "\n") (snip-insert-mode "py.s.class" t) (backward-symbol-tag 2 "fillme" "::"))

# --------------------------------------------------
# |||:sec:||| FUNCTIONS
# --------------------------------------------------

# (progn (forward-line 1) (snip-insert-mode "py.f.hl" t) (insert "\n"))
hlr = None
def hlcr(title=None, tag='|||' ':CHP:|||', rule_width=50, **kwargs): # ||:fnc:||
    comm = ((('dbg_comm' in globals()) and (globals()['dbg_comm'])) or ('# '))
    dstr = []
    dstr.append(''.join((comm, '-' * rule_width)))
    if title:
        dstr.append(sformat('{0}{2:^{1}} {3!s}',
                comm, ((('dbg_twid' in globals()) and (globals()['dbg_twid'])) or (9)),
                tag, title))
        dstr.append(''.join((comm, '-' * rule_width)))
    return '\n'.join(dstr)

def hlsr(title=None, tag='||' ':SEC:||', rule_width=35, **kwargs): # |:fnc:|
    return hlcr(title, tag, rule_width)

def hlssr(title=None, tag='|' ':INF:|', rule_width=20, **kwargs): # |:fnc:|
    return hlcr(title, tag, rule_width)

def hlc(*args, **kwargs):                                    # |:fnc:|
    for line in hlcr(*args, **kwargs).splitlines():
        printf(line, **kwargs)

def hls(*args, **kwargs):                                    # |:fnc:|
    for line in hlsr(*args, **kwargs).splitlines():
        printf(line, **kwargs)

def hlss(*args, **kwargs):                                   # |:fnc:|
    for line in hlssr(*args, **kwargs).splitlines():
        printf(line, **kwargs)

def hl(*args, **kwargs):                                     # |:fnc:|
    for line in hlr(*args, **kwargs).splitlines():
        printf(line, **kwargs)

def hl_lvl(level=0):                                         # |:fnc:|
    global hlr
    if level == 0:
        hlr = hlssr
    elif level == 1:
        hlr = hlsr
    else:
        hlr = hlcr

hl_lvl(0)

# (progn (forward-line 1) (snip-insert-mode "py.f.single.quote" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.f.remove.match" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.f.printenv" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.f.uname-s" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.f.printe" t) (insert "\n"))
def printe(*args, **kwargs):                               # ||:fnc:||
    kwargs['file'] = kwargs.get('file', sys.stderr)
    printf(*args, **kwargs)

# (progn (forward-line 1) (snip-insert-mode "py.f.dbg.squeeze" t) (insert "\n"))
# (progn (forward-line 1) (snip-insert-mode "py.f.dbg.indent" t) (insert "\n"))

# (progn (forward-line -1) (insert "\n") (snip-insert-mode "py.s.func" t) (backward-symbol-tag 2 "fillme" "::"))

# --------------------------------------------------
# |||:sec:||| UTILTIES
# --------------------------------------------------

def adhoc_dump_list(list_, max_wid=None):                  # ||:fnc:||
    if max_wid is None:
        max_wid = 78
    for indx, elt in enumerate(list_):
        elt = str(elt)
        if len(elt) > max_wid:
            elt = elt[:max_wid-3] + ' ...'
        printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                dbg_comm, dbg_twid, dbg_fwid, ':DBG:', sformat('elt[{0}]', indx), repr(elt)))

def adhoc_dump_sections(sections, max_wid=None):           # ||:fnc:||
    if max_wid is None:
        max_wid = 78
    for indx, section in enumerate(sections):
        cut_section = list(section)
        if len(cut_section[1]) > max_wid:
            cut_section[1] = cut_section[1][:max_wid-3] + ' ...'
        printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                dbg_comm, dbg_twid, dbg_fwid, ':DBG:', sformat('section[{0}]', indx), strclean(cut_section)))

# @:adhoc_uncomment:@
# @:adhoc_template:@ -catch-stdout
def catch_stdout():                                        # ||:fnc:||
    """Install a string IO as `sys.stdout`.

    :returns: a state variable that is needed by
      :func:`restore_stdout` to retrieve the output as string.
    """
    output_sio = _AdHocStringIO()
    sv_stdout = sys.stdout
    sys.stdout = output_sio
    return (sv_stdout, output_sio)

def restore_stdout(state):                                 # ||:fnc:||
    """Restore capturing `sys.stdout` and get captured output.

    :returns: captured output as string.

    :param state: state variable obtained from :func:`catch_stdout`.
    """
    sys.stdout, output_sio = state
    output = output_sio.getvalue()
    output_sio.close()
    return output
# @:adhoc_template:@
# @:adhoc_uncomment:@

# @:adhoc_uncomment:@
# @:adhoc_template:@ -max-width-class
class mw_(object):
    mw = 0
    def __call__(self, col):
        if self.mw < len(col):
            self.mw = len(col)
        return col
class mwg_(object):
    def __init__(self, mwo):
        self.mwo = mwo
    def __call__(self):
        return self.mwo.mw
# mws = [mw_(), mw_()]
# mwg = [mwg_(mwo) for mwo in mws]
# @:adhoc_template:@
# @:adhoc_uncomment:@

# @:adhoc_template:@ -rst-to-ascii
RST_HEADER = '''\
.. -*- mode: rst; coding: utf-8 -*-
.. role:: mod(strong)
.. role:: func(strong)
.. role:: class(strong)
.. role:: attr(strong)
.. role:: meth(strong)

'''

RST_FOOTER = '''
.. :ide: COMPILE: render reST as HTML
.. . (let* ((fp (buffer-file-name)) (fn (file-name-nondirectory fp))) (save-match-data (if (string-match-t "[.][^.]*$" fn) (setq fn (replace-match "" nil t fn)))) (let ((args (concat " " fp " | ws_rst2html.py --traceback --cloak-email-addresses | tee " fn ".html "))) (save-buffer) (compile (concat "PATH=\\".:$PATH\\"; cat " args))))

.. 
.. Local Variables:
.. mode: rst
.. snip-mode: rst
.. truncate-lines: t
.. symbol-tag-symbol-regexp: "[-0-9A-Za-z_#]\\\\([-0-9A-Za-z_. ]*[-0-9A-Za-z_]\\\\|\\\\)"
.. symbol-tag-auto-comment-mode: nil
.. symbol-tag-srx-is-safe-with-nil-delimiters: nil
.. End:
'''

def rst_to_ascii(string, header_footer=False):             # ||:fnc:||
    '''Convert ReST documentation to ASCII.'''
    string = re.sub(
        '^\\s*[.][.]\\s*(note|warning|attention)::(?im)', '\\1:', string)
    string = re.sub(
        '^\\s*[.][.]\\s*automodule::[^\\n]*\\n(\\s[^\\n]+\\n)*\\n(?m)',
        '', string + '\n\n')
    string = re.sub('^\\s*[.][.]([^.][^\\n]*|)\\n(?m)', '', string)
    string = re.sub('\\\\\\*', '*', string)
    string = re.sub('^(\\s*)\\|(\\s|$)(?m)', '\\1', string)
    if header_footer:
        string = ''.join((RST_HEADER, string, RST_FOOTER))
    string = re.sub('\\n\\n\\n+', '\\n\\n', string)
    return string
# @:adhoc_template:@

# --------------------------------------------------
# |||:sec:||| SYMBOL-TAG TOOLS
# --------------------------------------------------

def compile_(files=None):                                  # ||:fnc:||
    '''Compile files or standard input.'''
    if files is None:
        files = []
    if len(files) == 0:
        files.append('-')
    compiled_files = []
    for file_ in files:
        sys_path = sys.path
        file_dir = os.path.abspath(os.path.dirname(file_))
        sys.path.insert(0, file_dir)
        ah = AdHoc()
        compiled = ah.compileFile(file_)
        compiled_files.append(compiled)
        sys.path = sys_path
    return ''.join(map(lambda c:
                       (((c.endswith('\n')) and (c)) or (''.join((c, '\n')))),
                       compiled_files))

# --------------------------------------------------
# |||:sec:||| TEST
# --------------------------------------------------

doc_index_rst_tag_symbols = ('adhoc_index_only',)

def tpl_hook_doc_index_rst(cls, section, tag, tag_arg):    # ||:fnc:||
    tag_sym_rx = '|'.join([re.escape(tag_sym) for tag_sym in doc_index_rst_tag_symbols])
    return cls.section_tag_remove(section, tag_sym_rx, is_re=True)

def tpl_hook_readme(cls, section, tag, tag_arg):           # ||:fnc:||
    section = section.replace('@@contents@@', 'contents::')
    tag_sym_rx = '|'.join([re.escape(tag_sym) for tag_sym in doc_index_rst_tag_symbols])
    return cls.remove_sections(section, tag_sym_rx, is_re=True)

def adhoc_rst_to_ascii(string):                            # ||:fnc:||
    '''Transform ReST documentation to ASCII.'''
    string = rst_to_ascii(string)
    string = string.replace('|@:|\\\\? ', '@:')
    string = string.replace('\\\\? |:@|', ':@')
    string = string.replace('|@:|', '`@:`')
    string = string.replace('|:@|', '`:@`')
    string = re.sub('^:[|]_?(adhoc[^|]*)_?[|]([^:]*):(?m)', '@:\\1:@\\2', string)
    string = re.sub('[|]_?(adhoc[^|]*)_?[|]', '@:\\1:@', string)
    return string

def inc_template_marker(cls, as_template=False):           # ||:fnc:||
    sv = AdHoc.inc_delimiters()
    template_tag = ''.join((
        '# ', AdHoc.section_tag('adhoc_template_v'),
        ' ', as_template, '\n'))
    AdHoc.reset_delimiters(sv)
    return template_tag

def get_readme(file_=None, source=None, as_template=False, transform=True): # ||:fnc:||
    file_, source = AdHoc.std_source_param(file_, source)

    template_name = 'doc/index.rst'
    tpl_hooks = AdHoc.template_process_hooks
    AdHoc.template_process_hooks = {template_name: tpl_hook_readme}
    template = AdHoc.get_named_template(template_name, file_, source)
    AdHoc.template_process_hooks = tpl_hooks

    template = template + '\n\n' + __doc__ + '\n'
    template = AdHoc.remove_sections(template, 'adhoc_index_only')

    if transform:
        template = adhoc_rst_to_ascii(template).strip() + '\n'
    if as_template:
        template_tag = inc_template_marker(AdHoc, as_template)
        output = []
        output.append(template_tag)
        output.append(RST_HEADER)
        output.append(template)
        output.append(RST_FOOTER)
        output.append(template_tag)
        template = ''.join(output)
    return template

# @:adhoc_import:@ !use_case_000_
RtAdHoc.import_('use_case_000_', file_='use_case_000_.py',
    mtime='2012-10-02T11:03:59', mode=int("100666", 8),
    zipped=True, flat=None, source64=
    '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'
    '/jeT0e79+PkAAA==')
# @:adhoc_import:@
import use_case_000_ as use_case                           # @:adhoc:@

def get_use_cases(as_template=None):                       # ||:fnc:||
    output = []
    if as_template is not None:
        template_tag = inc_template_marker(AdHoc, as_template)
    else:
        template_tag = ''
    output.append(template_tag)
    import use_case_000_ as use_case
    state = catch_stdout()
    use_case.main('script --docu'.split())
    output.append(restore_stdout(state))
    # @:adhoc_import:@ !use_case_001_templates_
    RtAdHoc.import_('use_case_001_templates_', file_='use_case_001_templates_.py',
        mtime='2012-09-30T09:09:53', mode=int("100666", 8),
        zipped=True, flat=None, source64=
        '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')
    # @:adhoc_import:@
    import use_case_001_templates_ as use_case             # @:adhoc:@
    state = catch_stdout()
    use_case.main('script --docu'.split())
    output.append(restore_stdout(state))
    # @:adhoc_import:@ !use_case_002_include_
    RtAdHoc.import_('use_case_002_include_', file_='use_case_002_include_.py',
        mtime='2012-09-30T09:09:58', mode=int("100666", 8),
        zipped=True, flat=None, source64=
        'H4sIALIkMGIC/+1923bcRpLge539iBQ5PgCoqhJJuz1e2FRLo7HbOmNbPpI8ffpQZRBE'
        'oUiMqoBaAMVLj/pv9hv2ad/6xzYib8grCkXS9O5sl7vFqrxERkZGRkZkRkbuP3m2aepn'
        '50X5LC+vyPq2vazK0T6ZHExIVs2L8iImm3Yx+QpTIP1Vtb6ti4vLloSvInJ8eHQ8Jn+u'
        'louLtLwg77LLvM7rMflGJE15EklbcrG6mc7z56N9APP+smjIoljmBP6u07ol1YK8nH9f'
        'ZdMuf11XF3W6wiKLOs9JUy3a67TOvya31YZkaUnqfF40bV2cb1qA1JK0nD+rarICxBe3'
        'AAaSNuUcmm8vc9Lm9arBdvDHn376hfwpL/M6XZKfN+fLIiM/FFleNjlJoWVMaS7zOTlH'
        'MFjhO8TgHceAfFcB3LQtqvJrkheQX5OrvG7gN/lcNMHhjUlVA4wQKABo16RaY7UIcL0l'
        'y7Ttarp73nVwToqSAr6s1tCbSwAI/bsulktynpNNky82yzGBkgDlz6/ff//ml/fk5U9/'
        'IX9++fbty5/e/+VrKAuju2lJfpUzSMVqvSwAMPSpTsv2FlCHyj9++/bV91Dj5b+8/uH1'
        '+78A/uS71+9/+vbdO/Ldm7fkJfn55dv3r1/98sPLt+TnX97+/Obdt1NC3uW5oCzA8NB2'
        'QUcHCDjP27RYNqzPf4HhbACz5Zxcplc5DGuWF1eAVwo8uL7dPmYAI11WwIHYQyjbkXBK'
        'Xi9IWbVj0gB+31y27Tp+9uz6+np6UW6mVX3xbMlANM+ejwEM4HddF8BNbbUrX+/t7X0Y'
        'wTAkWQr/HB4eJ0WZLTfzPJlCHybkF+g/ZpGz1yx9Tr6DGdCcMaznVbZZ5WVLuWo6Gp3Q'
        'DyEnjg80k17kMSHe5k7f/Pz+9Zuf3s1G0CP6gbGuYJ45a/Q3NnpDWbYZyQRCJhMNX9YE'
        'uaCjA9T75d23yauXwBftTWv2DCu3OXAeFlQ+svI5zrAmq4t1S0RBVi2rVmsUGuonnV9W'
        'GRE5rNqUong5hiqX+XKtFof5BABvGZPQzFXeIDVHoz/z6YEzk83SZkwZj+Myr/KGXOO8'
        'w0S9/016C8w8erNp1wABQNN66Yqx/Kbk+M1RRBH5Q2ALrIMyd+cPVHrxKd5kyTwHUMl5'
        'fhF/AgFLdAazQNNJJ8ugGG4I0px1Ol0ub8lfi/WaY3sO3PLlF5Mc+gDFYaa/v8xvUfwC'
        'EBA86aatVkCEjNbblOs0+5jPUerJH+SqSJEgUCFe5e1lfEYHbcoEfn7T1mnWnmFj7hIX'
        'eZuUQMt5ItjhDEYtu0zLolk1Qm4iqZfL6hrWLPIzXcfEwHE2p2PCent2xtPmR2ei4S7t'
        '+OwMuqmXgSH19bRYoCBG7gAoIGtAFtV5Or8l+Q0I7zGwDIiKtNEbQIBVCXDSKxCE6fmS'
        'cgoAyG9AJmcAkNNFrgzqSAObspFWE/Nyjol35aRPnz7FTZ7F8JeL2ZYidAdgI5UlyQkJ'
        'Rzj1gn3yTRyQgA5tQucETqD4+YcyEAWqroAYay2/6MuPRiqB1HaHVgMSqtW2YdPfHQoX'
        'J41JBQWbAtQTrEO+cIP1YEuhGsh+M5x0olUbZluYyLZbwN5/xETDO4+ZqLjjqLX9gFdp'
        'VlcNAPxPVkHl5QC0YeXn2CgBPVBLwE+zBKCqloCfXQnBKqyA+GXkSwDil5HPBlApwhLs'
        'UhJXJcEupTfHElipv41Gr3969cMv//rtEdCKKj+62QB0Lcojajek5xn5+//8+//6+/8e'
        'LVBfRb18DdrdsmhbEHzTKVsCBcBjN8DODtkR3rtuMLkEPoJOCezHWs5xl3MsOzrPF2SV'
        'FmWY1hdXUcwqBAFfx2u6TKIu8Sy/SYGh8me6csAleVVDHVr3YlmdgxL7tqXrG03i36eS'
        '+9iXEc2EFWaZ89bJc3LEMOA5mHp6NJs2LdhRDeqSYTC5DCJcgZ15mNlBwM+6Lso2TBJA'
        'O0kiLavO201dkiO1xdANNgv0qt7250MLtkFkYIrLdwLKPFhSWQ5UEmRr2nnCEhMwJ9MV'
        'dIYWNXoDyLOZH9CFGgwqNhRNGNFBDOo28eTreOBHqnEnHB+rhIUmLO6ghHNMQ/ZHxzBf'
        'NrndVA/edmH87DMFl1qHq6ppSZbXYHGhwrEAfcNZZ1FXK65Oc2OBIo0Gscqp5sfHuT3k'
        '+qkqc3NcvBxgd3CfYH52iUYaaIugW6YXdnvNlcofoELO82WxAtuubkgYBrBcjkkQPwcW'
        's6ri9IVFck0XJAECdbErWCsS1j/n6FmVux/TOoelBkY9UNYfREFZt4M7QNvo0F4MhyY6'
        'ZqvXvG8nXfGBoJZFCatEepHU+aq6ysOuEKB2+ms8ewo4vq83+ZiEQbXrCOwEveiBLgBS'
        'U1/MxmACFfp6LGrVuc5NYXNlF7bkJmdzOQtgduI0sLkbDUa+GIFtwUUIzHixmE2h0ZV3'
        '4hd0u4NUzXSdtpdTaoI0IYfnqcPrXaZN2rZ1yNsE6s1zXPaDnmq0qhRz/NuU1QPexBXb'
        'wYa942D2PeqTJBxCGE15ImfdYfMj6iO+SnM3AYDImxKY8qOk7zChlrko6udJ0d2uTy/0'
        'Pm36++RjRe/i/F9O4hb/kLhbJe4wmXi3gRMc/LsPXfVfghF+j+Vrla7D5rZBRTuva9Y0'
        'shT8qGqwzcqPZXVd8i1Ecga4NLCUcBETAXXOwMJW2A4WpjY8Yr95Y4cPsnX1ju753XHf'
        '6iE3YQ8Ofum2fRlWBwdyr5JvTTLZy04AzuiuW5Fxtft1WbRFuiz+So3IsySO/duABwev'
        'nC25tweL2Nx8kkWVLQO+wcjL1psS0ld5/EJNpDJHT+LloLkLEE00z3eYKOoIKsUvyPHh'
        '8fHk8PPJ0R/I4Vfx50fx54fTwy/+8M9fHY24TQJMKL5W8ludjxR43V6cipnc63lBJlkK'
        'i9kEeBkoOGrrW7biUQMoe9eCNXzx+o0wguRvsIMSOjT/ctvmzes3Y0eWSBnlN1kO4/ua'
        'wviWThLahmxMNvgw7bE55W5TNlVUohEOcrc2nMT00D1bpo20G8Pq/D/yrI1iMuTD5nO2'
        'bHA+0w7QRU5RJk4I1YFwLXvBRS1Mf5wmPaUY+Tneybqusrxpksuq+kg3+/7GSdjWqewd'
        'ZpzORjyHmu7zoobEIGHbBEkSdNUymTtlqQuAAT9x9R1x5TKjWut3YLnnI8Fzf81LPe1/'
        'bIq8lUmYcpXX51WTa2nz/HxzoVcU53mo+jPUFczLHJaZAoSK2luag4euVg7r0HVaG8jh'
        'XhjvfEMZI9m0xVI1R7BE0bBMHHlDn+TSvmiKEqRfCUsXlBnTYyZWp1sktMnCTA0Odm9P'
        'XUoo2/8E66jB9AOw6cEI6tBNNAtTnCqR1t1kk4UceWdnN2VBLSJWBlV2wzKyeooQh3cS'
        'SsMoLdPV+TwlNzG5kbkg09vbNXIO/gk5WB17SLtKlxvTPCwUwrF8ukdGN6A6ktCcsWjH'
        'T91EtuIiEM0ZGYkN7p9meB5YzUOBSiTbGusFNhmf46KkUpCSx8W1rMYLFZDkci7p0gtQ'
        'fFbn1TKpaljxQMmSIgZtVEg6odODSTcQXvGiBFVEdmY5X65QgZS1Tg9nXU+tzKPZSBsA'
        'gK/TlMOr8yks6ymMKSYYRDWL1FoRTt4gmP5HVZQhBQDE1DpJawjyUGFuUAdtjma9BC0O'
        'JDWdLJTkkOygiiLaDerw/QpHPwGS1gf4rXShYnnC6pd9CX49/fVDOTsIA45LELGEfwLt'
        'c4xVflQJ0WyWbScpKXnTpuUnSocykfUOkqCvfHdDbuIaMou5uODmAbS1ABULhzWsK0Ei'
        'Y4ZQBRA3TStmh4eHxn4wxQRy4YuZx9Cfpus1ZoaU3qKZU9GPmIKdRb1VmYHIa9IKMaQ/'
        'PTKrKcSh+aPdUFHBcSZkFXv4jM3CdVo3eYJ6AGM3GNoLWM4wQefcE9xUG1NGy5YrhdGs'
        'TzfneB2Faxnq64TrM7RApJ26KHqGcydP00OQawwdRoWl4u+B1iMlBELQW3tHRoV80s34'
        '4PRXtBaXK5BFMEVmT80dAfcxRA+4Dx8aGwqlqKoB9c94A3w39dUMZc3EXY8bTt5OWHdY'
        'oQzQpVoQUSlgS3DEsIO84tKlydM6uwxZQxrTRWp3VpVxnMZEF0zai7rarIWZ66YrL8xP'
        'BoWwWbOeKWJtesAkGsUkAHIfqNTGDDC2Odqb81AAgbKBjvmUZoVaDzRut8SwDpm2vU/R'
        '4aAx35rY4ZqKX5ntn+HGdgSd38Zs4TPUVvL5zHTMd1kmwcUd+Sl0TMMxZR4brkYd0/xw'
        'TlHbRjEwUJd9QXbbaPEeCzgNHLMJRSxAzvAGnMB9EmsHMkq3DA+VXENqcZLRyR5Osra2'
        'KC8Z9U0r1Gad3To4HD0wzwzkBljEHXodSwKcRVE3bafzo/QnYRiiZEXNjWrqIAojasGE'
        'TNKTp4RpdSogXJx3gcOAnE403aDaYP81spyGEk3ePAhe0SBNsbQL12EMtgi6lHPujsjA'
        'j2eOz0xOY+U0Djowu9YnycRmPFeJtaWnVyfW+U/BxmeDOFmUNtEvaRkNdkLxzvjZFB+A'
        'Iq4X2LFmV7PCRNHW7JGdOE7IUohiZ8TYDdnWMK8MrOyyclUFWJQEFt9Z4UWc8EpEgRD6'
        'qTAml3k6R3JJqtikKMpE9FrdPsLPeTW/pW01OqV4eSNVUSJ0heU3JayGPnN+EQlWWR3D'
        'bhAcJ8hlW5Qbywmlg+30wRHUdh8HC6pJK0g3UjqWsKWeW912AXVxlh9CN8ADOLMrLLFt'
        'tm0A8GIPwKau1rlur88Iu5UOvtWnAf2QJ6jUxhxmXmqd22pr9tqSljBVTF0vGu4FYNB6'
        'yCmm46T9GrLCJcyI+B2JZQxbD6lcPY5QKgxaKP/fYwvHuvsInKGS7HdnDnv8HpY/2jot'
        'G1j2VqquIhM7SbjF0OjbXzFIY5m8v8lmlEtt6tEfehf+kTlwSJA+ndHWE90Kw/myOvcv'
        '7w+oTvCG5LiGmNC3j6rny01jsYvDCttrFC03iNv09baX4QbsgJI+/f+uPCGW4h1URC+n'
        'qPaKA9Xfmz+2KIwGNRAtZxmnMkq3b/qgI7ixCl9nU5dO5GZad7lHYWzFeQ29oHQt0jiP'
        'oiXm26Siy/5xnqJJanV7H9jJWO6fulvXCWEr3V6w+K/0HHMCj1wLmbnQOKa8czHbbb9C'
        'OA/20H9nsnspoUiFR+uoqg/cjdf+wVqC4r4N86HU34HTfk/G2r2bzJ3OYxPv1scd11zW'
        'snZi/f/rgtsdV5l2ADNKbBVOAc4r99ySEITG+3LWydewHR0NzuSLYbe/FCrhjjz33PT1'
        'g4P/hhz6UaDni24PCjzZg/8OSDhhkCLbdcKjK9c37IwwMOWZQ7ehOD7fCUdEbSc8aDdY'
        'U30YOSbQoylBIKLPl/mDiA0OynKO+TU8JR/aD/XsIAr3yR8ji4oChw3SLvjw4SjYJm5B'
        'v1zGJJQtUnJ3YDixsdSWxUf2e5hg5gKYOxvfwMw+T7LLPPvo6PLs4EOr91VWmxcNQxVD'
        '4OS9XCbrrGASchnvbzEKT3+ltP5Qzj79U9e6f/wFKp3+zjiA0UXZO+Wqlse6424VTuEo'
        'juQtmMqFDrybJo1zlbDCC4JXNmT/PgjNcxY+JL8yLpZykNx51Z7my6JpQ+fFAr/NGgb7'
        'ZN7GtDHaNKz7SON1LRFE9wi8a+B0NAxHrsNBD19QpnbiAlgEcoymNXepiMhT2raNv4Pg'
        'HTvZpjJzINMwM7mv8y1zD4wE7XJD0dYJ54JDT4AVFAEpvILepeBFdEwRK4RbimudZF9s'
        'M1dieOyA4iOTFPh1nn4cadGAdHLp01Srr6x56CvU1QEW+oQzGR0HI9VzcGRrNeiZx2/P'
        'Ids5HSsU7SieKPrRvMs3DioZBzi6c+9xh3VKyz622IJpYRSMcPjFSo5rgcsc43WdL9Py'
        'IzUmG/bdvvwkaMWXUkqpAZqPrJfftPRITQ7PPpv2GF8n0G8WiYkuBnfeyQVjFvaK44dR'
        '4/sWvJEphayVYMhK6HGEQSvrQfqQXkI+hg5AG5X+QNBz59Hcve0Kn4uygkSvyzaVjAm7'
        'aySui251sXE6JbPKOkfmgHaT09saup6IEzbD+eqqJTcKpMt8ho4wrUdiLtuk07RS0KNi'
        'koIm79k6vKzV0jEmhOku58uO5jRvzd7W0i3SmFViqtLpbGeSAW5Iq6Pjf/bQii2EXKYg'
        'dmHmOFxHNYScnFA54YYjB/bpiXFNWoHRjf4JOfbbLH4KCGamv3U0DYfTYHJ6MJtMD/il'
        'OXS4hMXoa+pjG00PaC5eDNcB2YNMwWrBNhzeqqyRwf6qsji/w2IJO5rfJ2A193kmmbbO'
        'VL++62AfRexuMnRes32P5VwUsQ5YYXaHhcXz4dEQtgRDkLEP9NAHCM4ljGzzkEWO6TMP'
        'H4lcwJ6sLTtugy6+hpOMwdtGMt7qw5EMo+9pBONRg9jYMF/veDvJJJ7mDEJCUpCoFbMv'
        'KF4mgWkasTCEnyNhQIifbxYLGjJURKxFGXhelGl9S9jN8pEnIge3jwqw3AIGxRWkoaOr'
        'KD5lhadIkHCQg78Nwqjr2pe+dQBaAJAK5HLIaR/U545L8V17CxeSDNI0W4L5aOLP77q+'
        'cdyG63To+WZJ43hgd9gvMEfxqllf/JSQlfRKeJXVWdExXghl8aZ6op1gPVZ+Kkoj39Bv'
        '/ZFZQkdz4v5pvwutjetUVgUwjP5BtCXCixwmE8TUE/jKvyBK1crtqVCnRZOLUQ05fmzC'
        'YchlOqxnAZjZGF2AUQ5t7jNdWLGJ7l0UjAtcRlSRoVJGi76gihkh/lZ4D567uaxQ8HjP'
        'ynJJYERPl/gmesPljy1AKhoVpEeCyGJCctBOhvnwSGVOaWDA7gGqTO33sK54JrcTngnO'
        'xs8WStemUAJp04OdRxZRpWpOORqHxn1/o8LVDYqJtrGGDQZZph8Ov8A/T9scCzu1XWAi'
        'eXOXgvTMb+9gUR5PMcLHikZ0QxhTdnYUTD0ihw/bv6N47Rk3AVqA9RaiLR+6d5UomfgR'
        'T1uv8WfI8A0++8vks9Xks/n7z76PP/sx/uydB10GAxR+Qckp/jPPl20argoMWwNSopw3'
        'J3jUs2rcdoWiFVF44w6a+OIjfcNPkTht23pBe7H3WbO3k4Nw23gpifGpKFDOciH61rZN'
        '77VepoHdYA1NqN3Mi1rbgd6qbmINt5C/YWESqKzrAic4JZwj+iOhok4t7ReBXJbTAiMT'
        'ShcjbQ3L5KbJxYqiwhaFcGumCV1rNaUVOTEasQdMlBMQqS2IpOA07po1S0LL+Dek6U7s'
        'eJg3VsDUQucVCwl3ldcstj2NgW2KnlAdDhr2AS/8KPv3UXf9H1NpkIpd9vSJeyd9bx/6'
        'G5M9Zk8kNBwS6iZ7MT5LUKKtSclxtid40Q3mjIXbbqak+Vis11hvOp1+KPc8BwGaUs85'
        'UpATflEfEZvgjth6WNegOZRYpR9zyODZpnJBAffMQgwtnnRzUGgULCq7x4BxzUK2VrAI'
        '7mNyAfXVzjBwxhpZ4J6BFhPGWO0u/orLKMKa/gn++Y4dHrPFdEz++xhBWDX4qupVb+wK'
        'roW2MxeKCmNnUVXeLANZZl2HKjBc4ZJFGRmn519+wS1Wb0kjDGLaZEUR7K5hshDzFh/g'
        'UCqcYNq1u7GBgTP0T2wCmFg76MA76FBRh7KWS8vyMljtYzCJGjKOw4708pODVzzmg8Yw'
        'D2NA8OFlQwvqIBV93F6gkk7YDoodIQf3U5yuC2ANh3+vtDUMNsFwROIiNR9s05dcrDzd'
        'XgzTBLgSYKzYGtFuxHM+DqOOEmQ05Fh41yPhsGf5YPTFhaBbO2CdMJYEbWDVGWdNNvZH'
        'Tjd2ZKJdGtZMQkoQwxoUan+Pr5xQZ9nVZQxVJQ5S8EQobZNdJL9lJSg2oaWp4n4Ab93a'
        'suPpqDZZ9aQK3iNvOT6WmqoCFleQHX2OHcqDhUd4EGrohE7qnR7GX86iyOWnwzBxV+vz'
        '+6N9+79qHnuHXxkGJdoF3SZjM4D9SBogyjoUndHPvaWRas90YZjZPILx5/ALWEurtRrI'
        'xuaVfU6p48Ojown87/jz90dfxYdfxMdfnk6Pj776w+GXswEk2b5JOdTCHWDZ9lq0Dkv2'
        'Phbs7pbrgwk7lWfkxWHBJS7yYV52WSznvBytc6q6QEAK9+2Y8vOxrhz6SihBBpbzRNDN'
        '2ojUKb+dpeWCwOWyFNPatgx/eIHhGNnOigBT7q/x/eVTVng27vo+5vgY08jZBfLkpOvo'
        'YJ3Vsy9rsnGehUo/WY15AYt5r3zT6CeEHKQ8gIhT+mVvlHajidyxQk8vZbXF8JIvgfbD'
        'Ykoqy2Rj4LEGSCNLQt6u86bbzRmTquk5RBTb8rTW9Ef6670dDU/wnuRfxy4iK+CNAqOA'
        'ELrOdjmnQubPRygM695WShK+rCXKKuDAhk0zlf9F8ZlLhoZKcNIx+bf8ln6LvNuc8Mff'
        'KmROy/w6YQk9eDrRs0fBdYBujJjUMIeuiLizwjaclF1de6euVk5FRClnHHb6bGO5qLDg'
        'Kq3xdbW0wfgryKrzkW+ndNuCfDRkb9/XOmjyt/dH4VAXj0iFvmMvHT32bMkJlQimkcdl'
        'tAPImNVzl6dZtDgXgFjeEuSyhygfXU+brKiYzpnL3Tz3ndA4DhJjD+cn3EgzzhI9015U'
        'UNwUp+vbzPeog6sJ+kt3XNT3INMMY+mGSmkUmNO3yZt/8zSD3ltsww2/qTV7dus5Gbcx'
        'kv96NTQF7bG1NfJ1XzQjSztGrUPHK6nvMVkG9tOIBsleTJQKkgDkKoOHVSeyrz3yT0wr'
        'U7/QZio7wgDlSMHAfN/JM5sFq9shYSyZ6YqI1nrgWTvqTnblCqBkVEtX6FVbDA72NGgP'
        'zG/JvdrwevlXIYaK2nPi0DltjqaSoSrRT/YjHZ/8mj6wnLInhdkrVfi2ab9nQO/RI9M8'
        'l5oYFq4K3kpcw3gp3Gu2nEFK1W+r0wMV6fdheLMLjgBI1uJvI84aM/ZrR/3M5rZHLSng'
        'XXhNzAd4/ojTtW2rk/mSG7OEjVfctELRHUgi1E6dK8bCw8SxOunmAN8c4opi37adgXl3'
        'dqrtS1g+IA4po0o/mxUEfS3CimpbFnpRn/7VF/UtvjnaUKk+dobsEw74xuD1uDhqr+Jp'
        'vuplxR3OxdVzSOBu8j0+61q45qxaLtN1070iZARs5iwvW4odXuyy07pbvQznrj6HEUSj'
        'u1RmBs8dK7OtnDtWlm8iXAUuqnBy95DFvMFowOcATE8bLaS2eenCAMFaCO40aI67/85x'
        'o2/4eAZy6F1ONg7bJv/W3fv7yEZeRlByLI6ZemOqOea5fXHD4DWlyavEeC/C9CXQTkmM'
        'stp1A44sPrGthj/Wz3YCsXWpIrGQD44nyr13o/M6mxjFuwjHGM36KY9vrBeKBgGwFhWM'
        'Sh/ODsI/NlEHEjvZD9+5wO7zR1UYmYF7VJq16ce8IRl9zX1B3wB1uNflWai3Ol3yC4zj'
        '7l3RMVlWGf3mdrylF7Ho00QeRcs8wQv3njx5YtUjkIgncn0cYvBX70pCi+02Ad0BgPlU'
        '9swyFUv5WkxoOICydY3HFt+6/D38AdJ9TpAe6li0X5kxToZpSXQvUHxx8CcV2rZvliyu'
        'PWGY0KdskgSUH1P3KRrxzI0mdBzHlbKg8vINP63YeubBO8DCbq4rI9Q6TbZ2GXH3Q/dB'
        'ooLvgJaOrJuC5pM+px2I2fbeae0FgRHOBuENxa/LYQ/4eDGVTwz1YarvPXkbksOubMMp'
        'TRlHHHw7Sjl+Z/w/YEbqzlf6eVEHyO/WnfEHoBA5/KrxLma5FXxeSashQKDibkCivpKQ'
        'Zh6icvGET3ay/oDJXuf4DPmtvtx30rXfL9OUe2pp8TaWr3CfJWfD1FEaObQTRb/h5xTD'
        '9ZsBOo5QxqOeAzjNaBGaioGdtXbSOtu0G7EgBJGx0TzIPUcMheVcLj10/HsMOzmxeDzP'
        'veEe7uLfo/n5rF1+PqLH7GpIv5Oo5i66aYRrkDIsY+kfZN1W1fkMlUuD89x7wAWqY8tl'
        'Y74Bn3iOvLaoo3qhaDAQdxQLTS1VybC1He/+naWeqkw/QD2VKqqOwQDNdCft9B4aqt+1'
        '+x/z8refl44VkS2V25bz39cqv+JrCq/HmVvrDU/T1xflqMW8t+DTjF26EEeL9Zv9ayjq'
        'g9WAwSoAewE2Ye8beRZa47nYIDJr96y5zk2LbsOQmTrKfqH+xpMLvuM5Zq0RxSQb6wBo'
        'oOuTrscgQC/KqsZNx/qj0TLGElDrGkEmPLIkgI6z/W60a0wZkt9BhuRMhmi4RKPBWpm2'
        'NqLFRe/7lE77JHaFmHGaBwLSLP5d5FhW5+jJp9iQ2CUURgIxhwuxRLCUFww148Udu0Kb'
        'NCp83YLFixWBsy2+aAWeXNOxXRcxUiD1RWrYrNYPvy1xH7fWR/Icx44/lt/40NsCdDC4'
        'Vzh+lXoR/YWeZ46FzHkxT1bwBIuX2SfG2YRpdap4eEJKjDSopuETMLrRaEKBOQ7BlPGf'
        'aoWpLXoUZLXItoojvzIs8e2FiM6T+Giy7EiAYWj/5n/W19KOO7ps0Y2pTqyi4t60lWhZ'
        'Twf368R31IXFE22i1dOOErNtzNzda1rhc+xe3Yytrdvf9XSHr7+P1sZCwrqniUetCdUZ'
        '84mfmKzR1wO5yvXYpETd3A6zdjrU0d/hHMf1UI6Bg3N2OqejeeSiTayi1HG0KKa8zqQW'
        'NJ9GNGarVtRwQtsW79f5ZiddDqluRTkP93Pxr6mkCNhPeL68/0p/aZvOE5c/nd5EJ/Uw'
        'dhNNjaJ7NPlklyafDG8yHvZa1p1F8UBxfAeRPPzIbLDU3UHyPu5xGa1PPRpoP4w3N4MX'
        'n2IchPjTc64dsqI3IHzNot+Ioi/Uopj3n3/rN6qBN4VThbZTrqK1XAktUUGAJ/pi6uv1'
        'PTeN9DL8poeLHjZkgUQfZFlGhWyQz7w0UOsv47A67LIJ+05p1igh2Rn1pgBtZUUkYlW6'
        'ZaZ7NscGLOhgWfUaINdryX2w7HWqK6FJFxqMUzZjReQ0xst82ZiFWVUhsHeLWboDVJaI'
        'N5M1BIxnoNnXrt3A5EFBLFDuqW6vN3KzcyNydHdrCQup7dg+wbQt24zpujYeXuemD5bs'
        'wfCKZnAFI2K7Nuyu2O1SL+MR25EatiI21Ei6TBvWiXneJ5p2kEIPLiskY92LkzpweZJV'
        'G3qBDm+qCZWQvXUhe03btO+8ysrPyWEPVVNY9a7QQey3E/YPL5K7PSYXU7j5IYp7z/uU'
        '9c7dewuesrsqNVT1eWESeivozpaGA58IsGjJOA8AxwssThgd4+n7RtbD2s3V7pPTdMQc'
        'MDHJY/PM/fhl10G+8zgZY303hnEN9oMOOJrZ0rl0u1v02LNl5bo9IDcEtHepcBo+2gZA'
        'Z8ubFhWiEbseJ/afg4TywCG5iv74iW8fsL2UbuPACJLtv6nX25bWlA+2Ri5zAfAsz6b/'
        'm/Lkcw+X4KFL50K3nUEGcYmbQTyF1aOawZykdk/hKoPfR94rD/q+DLbnIb7lXa3P5U3J'
        'nyz1yX7zWSqjPssOehyIZZfus/V00r8BJRmAmZ2qGWU2j7aThVLfTpNZ2Nxt6vYhrJL2'
        'ZtO4Z8fJemnW+bKC95GpDrAa387YpRFveUk2qyu8zJZcVtXHxnVHTvTNX+uUw54ZD8+o'
        'vbWfDunmzB17wm+iy5F3gBFZEkOMI3/KEZxR5GZDpKEFB1jAeBBdk/m2AJcPsuEmd3ga'
        'gqonfb5agAamXUufdmeWP/zS+iYs/FmfF4mjDa2J4bC5PGYA+x6WFfxAD89+U9H7O0tU'
        'Vb6Ik36v37YJ5kSH5WSQbjjYbj+M30fKI2NyxUcOfl91B+RtnXYYzCI3J9BxaUAVyOf2'
        'vgBt4Qq5TgNvM4a97n3Mb094uKWPbUyCT5+8uw+0OPK2e/UMQ/pSUPgRWdTcEseLkHbG'
        'k8B1eM5v9JVzDstXBKNS0gKnRzHGcVJhOYKTm8MCQ41v59hxKxk1WpgWMQnxD3SZxhTV'
        'laZgiwMTLljeynjDajxyewJo/BDdhR+6vsLw4pb0fYe9G1v3wO46qlEkRs8euqEiC4xI'
        'JggS9G/Y1PQEcdsbL7bIWl3jUnI4Jnt7+H/lRSb6Xin6flfLaGhsGQa/MkTiMhObMtXS'
        'jvR8DSxMvoFCjjAPNA/qZq4s5CyyB/8deAoc0wInjgLyiY6l1l8UhmG0cyAds79iU+na'
        'MhQB/pi2wga2bZOC3j3uXjGFJK7GdlcSIG1d54viRktqNguZNGBla1F5Hri0bTU9nUvb'
        '4y1nhs68XojtfEmpTolX8xjJug0dIHSXycmubYJAkvnoC63SHQ3Db/pIqDHlGUpGMUiM'
        'InOThfGA3QqKCnXTfU2f0CAypEP/0zSi/jYXyX3yM+rqhHJHpyTgL/2pona9RIVRBAEK'
        'xTIRS+HolI0O0ciEoJCBQgQqg8LlGrbPry0bgo4t8wWu8XVaXuTh59FMx13otKGsjOvk'
        '4SwMXjHSoDtZl3fE8t6LpU3LPOaZt+tck+ysIf4e26lGf7tZ7/ICPOFYCBmSyFiTiZgn'
        'xPGaojoqTDd2nEt0rzIaACwC+BdBdubTmhbj8BaOt7VANSucrlsaiKz7CK1lC1LtYJAM'
        'mQ2aj4VjQuAHbXh2esyYAe+4GcFo8CBdOJFZIZFAXrfeTPowWLVsKJvnV9AO6Dq0HYe7'
        'g9oMVgJ6y5fQg72I+iE4HeI7FHp9Zq3ST066NnuebNFnoyk2Y6Q0ebo/eUpflgwYmtFd'
        'wU2RRyWKkBBGd4TbU2dQl4IxG4UjZRT2ESL1voiDqBctvQkENACNHngqm8lBG92NER5o'
        'RB9yJOXk5NNxZucKMc2aVZe/dxjMkYOoNu160yqqMSzZ6Zy/8qbL9KNZGMFfdZ0QqWqk'
        'ztX1kYRxpAM5cgI5cgI5lkCOdSDHTiDHDiBNvkZ1gnBCn2ZrVgZ0ZCpo1lSIChBq6+lH'
        'fNb6Osm6yMTwM/ac08tUjvBpjMFXw9X1BA0AqEgt2mfHYIwT9kv2LYpO49W1YV4HJBhb'
        'QI8k1CMJ9kiA7bFLWbluRFiLR0OaPJZNHssmjwc2edw1ecyaROksVjSb1D5Cyy9DCNf3'
        '0XtoUMVNlK3gBEFkx5RJ9qe8zGtUYXQ1k803fVllad2e5DryZHV8GaqLb2ScWVkBW3oa'
        'ULKFWidaQSIxtRPHBzeXEPIsGoI3N/64dOk//zEu3VBzzXPbQLPc7nNYaJ366BcN/HFY'
        'uS2gbm0/ruHXv5k5DLA4j1GpoHx3tsucS3n38Y+mRHaZ5s6+dGJlERP63Ga1JnSPWRra'
        'Nbp3k08GNvlkW5P+swvlGKlVTpWa0672bMCeJa9+GgRWqKZgZjGDfnylmSzdZghXhtRy'
        'evyvDsN+oimt0vhN9HKKSBzrLVoiQeRuD+Sy28HwEGkwVBj0LQM8rsuj7f486sz/TcI6'
        '4QoCC8Gi4wz29DPdyLYOLOz4iFh3u789lnKfObIcmkUlAxvBgZ7uvtvdrEPeN1Huf7tb'
        'EGa34EjKVjn1waTv5zT5csGnD49+X9WJ8xZeBQjMVY+9VXtpXoJmILq4iwDc41LDSlJo'
        'HvehffIidt4Fjl+oeSzK27akPgi7QRdR7zANNblWxG8gGK6VB8ZFvYjfyoVi3Au8arrv'
        'zS3+qJoEdyPZviSMDP7AMgsS/Pzy/fcBzoUKHT2uihpv0u0zblZr8bxTVmEGRQC0yMer'
        'Axym+Co0OQ6Ehyni26KopkVQmN6V2Fc92EVX6Eh3/eS5rP+pDGUx2pfXG7qo7gKiAlx1'
        'ke/IJTkK2xHpolzXgnqJwm6FxWRqGqXrjCAJJ4g9npj4Kd5kCX1AoS0SmMfxp+dWMpCP'
        'JRex6ikTP0cIsFylZF1XF8DpIxhIcU+KCpkEBGlRJgl/jDBtEhmyvjvxwCL0rmpaX1xF'
        'XCrBGB1Go04lUKtSgcp9SGQ6K8ZilsKAGpiSyReYPNn5I4kxz5usTs7zC0aKs7OizJab'
        'eX50dqaEtWZXwCGD3m1IWyF66EMzU0LeQSbIQAx4hAO1Wa+rBqrRyERFA90pb6/TW7ys'
        'T5p1nhXpkt3IgRbwfk7JSrJwRgilHLFYxNT3CRuaE0CzWLcx8IWBuxxdE/d001artC3Q'
        'l/JWgAdIBQtkvB0yZxBI/SbW1TPgEaaPbOSA0JbjF0Tg4Kn224zW8fDR6qPgeyALwFww'
        'LgaY5znAyvV21rhpW7YKfQVt8ZbwHago2otH2oTvzGwvkY99RJbOuiImj/DiMpyC/dn0'
        '5tSGXZzCe1MPOm5AZ8b8QLQN5U6Y85e4H6fOg3L3KfDaydpjfQCvi+USGrwGC7CpYIi7'
        'qTHGyUuncozqenzG4lGIsEa01BloCOW8QfORSH9B5hJHUHWjbKkGEj07uwtTiJGhr5Cq'
        '2mYXZYnFHRNhkqM+Xugd5+bqzqPbOlYOtlX86s2PP7/+4duYvN2UlC7QAB8WKDMlIa4t'
        'JQmb9CqfsLe4I9wBZRMVvpQZTNw9fjo6fbbHnG8nuApNyqqUod5IyGpPZHYUkb2uNRbr'
        'agBa5PmmyZMshX8OD4/FZJuubx8XXy8a2zsizc7HQVg0tx2xOVV0HgMnaGkQOuQTmReL'
        'xeNhBQ2GdOcyB3VgUpNNBqP7NUqrkuTZZUWCf3393XfB1xQtMtmwAmTyNd0/4UXevX/z'
        '9lsog/g85xAWRbS9x5f5cv1IfcWmtiHEwH++O0af745SHy7PKgLKafMYlNHReDrZf0pb'
        'fSXgY+Z/g6Qf8JI1+fe0LlCbb9AMwHgyMacZ/OT+LBO6WxCTvf09M3GCD0RjzlM1K6uW'
        'm1UZk0NqGG2wO/mEXqOLSQtp38KSNPo/wPZACi/dAAA=')
    # @:adhoc_import:@
    import use_case_002_include_ as use_case               # @:adhoc:@
    state = catch_stdout()
    use_case.main('script --docu'.split())
    output.append(restore_stdout(state))
    # @:adhoc_import:@ !use_case_003_import_
    RtAdHoc.import_('use_case_003_import_', file_='use_case_003_import_.py',
        mtime='2012-09-30T11:38:54', mode=int("100666", 8),
        zipped=True, flat=None, source64=
        'H4sIALIkMGIC/+19fX/bNpLw//o9HwKxrz+SjqTYTrbtsXE2bjZpctsmaeJsr+e4MiXR'
        'FmtJ1JKUX3rZ7/7M4I14pSjbcW7vVruNJRIYDAaDwcxgMNi892BZFg+G2fxBOj8ni6tq'
        'ks87m6S31SOjfJzNT2OyrE563+ITeP4sX1wV2emkIuGziOxu7+x2yS/59OQ0mZ+S96NJ'
        'WqRFlzwWj/r8EUkqcjq77I/TJ51NAHMwyUpykk1TAn8XSVGR/ITsj1/mo379flHkp0Uy'
        'wyInRZqSMj+pLpIi/Y5c5UsySuakSMdZWRXZcFkBpIok8/GDvCAzQPzkCsDAo+V8DM1X'
        'k5RUaTErsR388cPrD+SHdJ4WyZS8XQ6n2Yj8mI3SeZmSBFrGJ+UkHZMhgsEKLxCD9xwD'
        '8iIHuEmV5fPvSJrB+4Kcp0UJv8lD0QSH1yV5ATBCoACgXZB8gdUiwPWKTJOqrunued3B'
        'McnmFPAkX0BvJgAQ+neRTadkmJJlmZ4sp10CJQHKL68OXr75cED2X/9Kftl/927/9cGv'
        '30FZGN1lRdLzlEHKZotpBoChT0Uyr64Adaj80/N3z15Cjf3vX/346uBXwJ+8eHXw+vn7'
        '9+TFm3dkn7zdf3fw6tmHH/ffkbcf3r198/55n5D3aSooCzA8tD2howMEHKdVkk1L1udf'
        'YThLwGw6JpPkPIVhHaXZOeCVAA8urlaPGcBIpjlwIPYQytYk7JNXJ2SeV11SAn6PJ1W1'
        'iB88uLi46J/Ol/28OH0wZSDKB0+6AAbwuygy4KYqX5evNzY2PnZgGAajBP7Z3n44APLm'
        'RTXoQxd65AN0H9+Q41fz0XQ5hu69gAlQHjOkx/loOUvnFWWqfqezRz+E7Dk+0EpymsaE'
        '+Fo7fPP24NWb1++POtAf+mEvnRWam+q8ofxaduQDQno9DVvWAjmlQwOk+/D++eDZPjBF'
        'dVmZ/cLKVQpshwWVj6w8xOlVjopsURFRkFUb5bMFSgz1k4wn+YiIN6xan6I46UKVSTpd'
        'qMVhMgHAK8Yh9OUsLZGWnc4vfG7gtGRTtOxSruO4jPO0JBc46fCh3v8yuQJO7rxZVguA'
        'AKBpvWTG+H055/iNUT4R+UNgC3yDAnftD1R6+ilejgbjFEANhulp/OkJTt98vARivKKj'
        'W1qg6YxjLwGJGS1cEqQ663YynV6RP7LFguM7BHb5+lEvhV4Az8JEP5ikV1geJ92yymdA'
        'gxGttJwvktEZlVMg1hgghFCmwHgLlKuitQyXmBKIJpsvYdL/fZmBQBdiEBpBEZ9My5zK'
        'NwH8PEsofeNZWk3iY8oBfbZ0pJdVkYyqY2wVYDhKnKbVYA4DMx4I3joGFhhNknlWzkrZ'
        'NIzbdJpfwOpH3tIVUXABmzJsgBnu5Jg1AADLql8uh8fHfSHGKe4gvU9PQcILgZuzxU6t'
        'dnzcBdbKRhPOO0UKfMOEGgDIuLjoKyPHuYixX4bEGy1hETlPQd71036XZCcgPDmGoxwY'
        'NZsD2QHz/AJpz+ZNlZwyJqfjyVoDuTmCOSGa6/dReqZxTH6ZwKKRXjK+6WqMAyUQgyJN'
        'kKX4FMmh3xkwAQCBzzQfJXxSwQpFfyJ7DFMgMy3OIMMMBUBVXlyx5lUGh9nJGFx9mM7H'
        '+PC6E+jTp09xmY5i+MuXloqu1tcA1lFnItkjYQf7HWySx3FAAjbYVBSg3IiffJwHokBe'
        'FxBcqb3Pmt5HHZVAarttqwEJ1WqrsGnuDoWLksKkgoJNBioZ1iGP3GA92FKoBrKP25NO'
        'tFrDnCWjIi8B3H+z4uoABqD2Kj+7RgkgtVoCfpolAFG1BPysSwj6sALil/FeAhC/2Pt/'
        'dDrj9ITMYEKHSXF6HsWsWhDwhaWgMhcXtwfpZQI0SR/oqxWXknkBdWjd02k+BJXqXUVl'
        'JH3Ev/clidiXDn0JsmWa8tbJE7LDMOBv8OnhzlG/rECrL1G1CYPeJIhQs3K+w5c1BPws'
        'ClhAwsEA0B4MIu1VkVbLYk521BZDN9hRoFf1tj9uW7BqW7AIIqNLaOoMQAcFA2CUAjkF'
        'fctqPGAPB2AFJTPoNS1qdBt6ybg4oLIW7AA2ZmUY0dEOQI3zvNfxwI9UQPY4PlYJC00m'
        'nDmmIfujY5hOy9RuqgFvuzB+NplqRo2aWV7COpcWuHbBUnEC9oKzzkmRz/iCxpdXijTq'
        'FCpLmx8fizeQ63U+T81x8bKK3UFQeeA9rPJgW4BqktD11yb+ucofoK+M02k2A5MEVIgw'
        'DEDidUkQPwEWs6riPAc5t6DrgAABUz07B7k4YP1zjp5Vuf7RL1IQqzDqQSVlKWJQS97g'
        'GrCWGqynrWGJTtl6HO/XXl28JahpNk8HMBKDIp3l52lYFwLMDn+Lj+4DigfFEgz5MMjX'
        'pf5a0LMG6AIgtU7FTAx6UKGpx6JWkeqcFJbndmFLuHIWlzMAZiZOgUaRwlsMoz5/yAem'
        'zdhH7SZX4ZpcfOqXk2XlkBMV6JWAXOCyf1EDD+waXOP3VAIr264zukAK5CWyJ3wPI5dA'
        'hNeLpJqATM3KqgwRM48wZH3pF7OqSFNW0AUQJWt7oFBydgavPfDg9Wjif+3kQk6qrmSD'
        'eqyfamO99I41bxpMQpjPYRD0f89BvwnRREwvwbapkuEUpghU74qRiaIG7IH6d0B834Tx'
        'KiTxGtP6ZsRcD7Xx/8LlKvvXctW4XLVbUK43aIJ3v/Cw5f/0LPAlVv1ZsqCCF2yTtChY'
        '08hM8CMvwCKdn83zizn3FpJjwKWsCmGERUCcYzCxFYYDWVuFO+w3b2z7Vhw27+k6cE1v'
        'zW16XLe2PtQ+XobV1pb0JXJFgklc5uw/pr6mbMQtlVfzrMqSafYHNdCPB3Hsd35tbT1z'
        'tuR2irGnwsPAIOSx6TDBgvxhsZwPqmyWxk/Vh1TU6I94OWjrFCQSfefbMxR1BInip2R3'
        'e3e3t/2wt/Mnsv1t/HAnfrjd3370p2++3ekIRe6qFF9z+a1IOwq82v2kYia79ZT0Rgms'
        'Xz1gZCBfpyqu2CJHDcbR+6oATF+9EZqj/A1244COy/dXoBq+etN1vBJPOunlKIXBZV7Z'
        '53SG0DZkY7LB22mPTSh3m7KpLBeNcJDrteEkpofuo2lSSjs7zIe/p6MqikmbD5vMo2mJ'
        'k5l2gK5tiv6wR6jSg0vYUy5nYe7jHGkoxcjP8R5wd/Zgkudn1NX3D07Cqkhk7/DF4VGH'
        'v6H6PbcXBsytMhgEdbWRfNtnT08ABvzERZf9zkFKoyXwIpmWaUfw3B/pXH/292WWVvIR'
        'PjlPi2FeptqzcTpcnuoV+Y7AAFVZhrqC+TyFNSYDiaL2lr7BvVXrDevQRVIYyKGTkXe+'
        'pIwxQH1Y9dtgiaxkL3HkDRWSi/qszOYg+uawbkGZLt1OYnXqFUKbLLSDAuzGhrqOULZ/'
        'DYuowfQtsGnACOpQ76SFKU6VSOvuYDkKOfLOzi7nGcpaXgaVdBSDQUNPEWL7TkJpGKVp'
        'MhuOE3IZk0v5FqR8dbVAzsE/IQerYw/PzpPpMjVwzxTCsffUp0gddjVJ6JuuaMdP3YFs'
        'xUUg+qZjPCzRMT3Czbp8HApUItlWVy+wHPE5LkoqBSl5XFzLajxVAUku55IuOQWtZzbM'
        'p4O8gBUPNCwpYrrQFjzao9ODSTcQXvHJHPQQ2ZnpeDpD3VHWOtw+qntqvdw56mgDAPB1'
        'mnJ4RdqHNT2BMcUHBlHNIoVWhJNXWtMIAIipdZLWEOShwtygDpoa5WIKKhxIajpZKMnh'
        'sYMqimg3qMP9FI5+AiStD/Bb6ULO3glfkuxL8Nvhbx/nR1thwHEJIvbg30D17GKVn1RC'
        'lMtpVUtKSt6krPhu0rZ8yHoHj6Cv/XFK9Sbh9DZkFotkQZc2tHWSzcc4rGGRCxIZM4Rq'
        'f+hkzpnpHW4b/nOKCbyFL+Y7hn4/WSzwZUjpLZo5FP2IKdijqLEqswt5TVohhuf3d8xq'
        'CnHo+856qKjgOBOyig18xmbhIinKdIB6AGM3GNpTWM7wgc65e+iI7FJGG01nCqNZn3rO'
        '8ToK1zLUFwOuz9ACkbadpegZTu+npocg1xg6jApLxd8DrUFKCISgt7YTRoW8V8/44PA3'
        'NBWnM5BFMEWO7puOAPe2TQO4jx9LGwqlqKoBNc94A3w99dUXypqJzo5LTt5aWNdYoQzQ'
        'pVoQUSlgS3DEsIY849KlTJNiNAlZQxrTRWp3ZrmxT8lEF0za0yJfLoSN66YrLxwEmrBZ'
        'sJ4pYq2/xSQaxSQAcm+p1MYXYGlztJfDUACBsoGOeZ++CrUeaNxuiWEdMm17k6LDQeN7'
        'a2KHCyp+5Wv/DDd8EXR+G7OFz1Bbyecz0zHfZZkBLu7IT6FjGnYp89hwNeqY5odzito2'
        'ioGBuuwLsttGi3crxWngmE0oYgHetG/ACdwnsdYgowzJ8FDJNaQWJxmdbOAky69Fecmo'
        'b1qhNuus18H26IF5ZiDXwiKu0atZEuCcZEVZ1To/Sn8ShiFKVtTcqKYOojCiFkzIJD25'
        'T5hWpwLCxXkdOAzIYU/TDfIl9l8jy2Eo0eTNg+AVDdInlnZhbeBDk9gi6FLOudshLT+e'
        'OX5kchorp3HQltm1JkkmfPBcJdaWnkadWOc/BRufDeJkUdpEs6RlNFgLxWvjZ1O8BYq4'
        'XmDHynXNChNFW7NHduI4IUshirURYzdkW8O8MrCyy8pVFWBRElh8bYUXccKTDxlCaKZC'
        'l0zSZIzkklSxSZHNB6LXqvsIP8N8fEXbKnVK8fLGU0WJ0BWWz0pYDX0WLCQe2HvzGob1'
        'IDjiEuZVNl9aQTs1bGfMkqC2Z2eYU01aQbqRUrOELfXc6rYLqIuz/BDqAW7BmXVhiW25'
        'ygHAi90Cm7pa57q9PiPsVmr4Vp9a9ENunFIbs515qXVupa3ZaEtawlQxdb1ouBeAVush'
        'p5iOk/arzQo3YEbEFySWMWwNpHL1OEKp0Gqh/OdjC8e6ewecoZLsizOHPX63yx9VkcxL'
        'WPZmqq4iH9aScIWh0eRfMUhjmbyfxRnlUpsa9IfGhb9jDhwSpElntPVEt8IwnOZD//J+'
        'i+oEb0iOa4gPmvyo+nvpNBZeHFbYXqNouVbcpq+3jQzXwgNKmvT/6/KEWIrXUBG9nKLa'
        'Kw5UvzR/rFAYDWogWs4yTmWUum+aoCO4rgpfZ1OXTuRmWne5O2FsJWYNQ6B0LdLYj6Il'
        'xqukosv+ce6iSWrVvg/sZCz9p+7WdULYSrcXLP4rg8acwCPXQmYuNI4p71zM1vNXiJjB'
        'BvqvTXYvJRSpcGcdVfWB6/Hav1hLUNznMG9L/TU47Usy1vrdZAcJPTbxen1cc81lLWs7'
        '1v9XF9x6u8q0A5hRYqtwCnBeOfaqTJLQeBDR2vlq59HR4PQetTstp1AJPfL8zKqvHxz8'
        'Y7LtR4HuL7ojKAJ6oIJskbDHIEV26IRHVy4u2R5hYMozh25DcXyyFo6I2lp40G6wppow'
        'ckygO1OCQEQPp+mtiA0OygqO+S08JB+rj8XRVhRukj9HFhUFDkukXfDx406wStyCfjmN'
        'SShbpOSuwXBiY6kVi4/sdzvBzAUwDza+hJk9HIwm6ejM0eWjrY+V3ldZbZyVDFXMdJM2'
        'cpmsM4NJyGW8v8UoPPyN0vrj/OjTv9Wt+8dfoFLr74wDGF0U3ylXtTzWHQ+rcApHsSVv'
        'wVTOceB5Pmmcq4QVURC8siH7N0FoDlm2h/TcOGDHQfLgVXuaT7OyCp2nCvw2axhsknEV'
        '08Zo0zGhNF4UEkEMj8CDBs5Aw7Dj2hz08AVlaicugEUgx6hf8JCKiNynbdv4Owhes5Nt'
        'KrMAMg0zk/vq2DL3wEjQrjAUbZ1wLjh0B1hBEZDCs/31Ezzhj0/ECuGW4lon2RfbzJUY'
        '7jqg+MgkBX6RJmcdLe+PTi59mmr1lTUPY4XqOsBCn3AmY+BgpEYOdmytBiPz+IE5ZDtn'
        'YIWiHcU9RT8a1++NjUrGAY7u3HjcYZ3SXu9abMG0MApGBPxiJcdJwGmKabmG02R+Ro3J'
        'kn23Tz4JWvGllFKqheYj66WXFd1Sk8OzyaZ9WYnZbsUficEd13LBmIWN4vh21PimBa9j'
        'SiFrJWizEnoCYdDKupU+JBN4j6kW0EalPxD02Lk1d2O7wheirCDRGLJNJeOAnTUSJ0RX'
        'htg4g5JZZZ0jU0C7TOlpDV1PxAk7wvnqqiUdBTJkfoSBMJVHYk6rQa1pJaBHxSQBTd7j'
        'OpwUaukYH4TJOvvLjua0aM3G1pIV0phVYqrS4dHaJAPckFY7u994aMUWQi5TELtwFDmP'
        'd4/I3h6VE244cmDv7xknoxUY9ejvkV2/zeKngGBm+ltH0wg4DXqHW0e9/hY/NIcBl7AY'
        'fUdjbKP+Fn2LJ8F1QPYgU7BachJHtCprpHW8qizOz7BYwo6+bxKwWvg8k0wrZ6pf33Ww'
        'jyJ2lyMMXrNjj+VcZPW7vDA7w8ISJSVlUlWFLBAwvK0FXqTE4dksWCkaruYSRrZ5yDLt'
        'NJmHd0QuYE/WVmidTtLFV3uSMXirSMZbvT2SwQwcawTjWZbY2LBY73g1ySSe5gxCQlKQ'
        'qBWzLyheeoFpGrEcgQ+RMCDEh8uTE5oZVCSmRRk4zOZJcUXYoXJTEZMEZfZRBpZbwKC4'
        '8jLUdBXF+6xwHwkStgrwt0EYdV1+6SsHoBNMeAJyOeS0D4qh40R83d6JC0kGqT+agvlo'
        '4s/Pur5xnIardWia5hAXmTqlZJ8eNfMmmkLTh5X0SniV1VnRLh4IZfm5gqixHivfF6WR'
        'b+i3qMFXCBg5mhPnT5tDaG1c+7IqgGH0D6KG5rVhMkH0PYnC/AuiVK3ckQpFkpWpGNWQ'
        '48cmHGZWpsN6HICZjakFGOXQ5j7WhRWb6N5FwTjAZSQSaStltNQLqpgR4m+G5+B5mMsM'
        'BY93ryyVBEb0dIlvotde/tgCJKfJQBokiCwmJAftZJi2z+zmlAYG7AagytQ+gHXFM7md'
        '8ExwNn62ULowhRJImwbsPLKIKlVjytE4NO7zGzQFERQTbWMNGwyyTDMcfoB/nFQpFnZq'
        'u8BE8uQuBemZ397BojyeYHqPGc2AhzD6bO8o6HtEDh+2v6F4bRg3AVqA9RaiLW+7vUqU'
        'THyLpyoW+DNk+AZf/dr7atb7anzw1cv4q5/ir9570GUwQOEXlOzjP+N0WiXhLMNsNSAl'
        '5uNyD7d6ZqXbrlC0IgqvW0MTX3ykL/kuEqdtVZzQXmx8VW6sFSBclV5KAsstKVDOciHG'
        '1lZl47FepoFdYg1NqF2Os0LzQK9UN7GGW8hfsjQJVNbViROcEs6RLZNQUaeW9otALstp'
        'gY4Jpc75tYBlclmmYkVRYYtC6JopQ9daTWlF9oxG7AET5QREagsiKTiN62bNktAy/g3p'
        'cyd2PG0ZK2BqoeOcpYI7TwuWwh5LlaboCdXhoGkf8MCP4r+P6uP/+JQmqVjHp0/cnvSN'
        'TehvTDaYPTGguZBQN9mI8faBOdqalBzHG4IX3WCOCSNCn5Rn2WKB9fr9/sf5hmcjQFPq'
        'OUcKcsIvGiNiE9yRU+/SzhWHufSSsxRe8NemckEBN8xCTGk+qOeg0ChY9nWPAeOahWyt'
        'YJnau+QU6qudYeCMNTJDn4GWE8ZY7U7/wGUUYfV/gH9esM1jtph2yb93EYRVg6+qXvXG'
        'ruBaaGtzIcsxcRZV5c0y8Mqs61AF2itcsigjY3/49SNusXpL6r6AIClHWRasr2Gy1PYW'
        'H+BQKpxg2rXrsYGBM/RPOAFMrB104B10qKhtWculZXkZrPAxmEQNGcdhR3r5ycErHvNB'
        'Y5jbMSD48LKhBXWQij5uL1BJJ2wHxY6Qg/spThYZsIYjvlfaGgabYDoicZCaD7YZSy5W'
        'ntoXwzQBrgQYK7ZGtEtxa4/DqKME6bTZFl53SzhsWD4YfXEhqNcOWCeMJUEbWHXGWZON'
        '/ZHTjW2ZaIeGNZOQEsSwBoXa3xArJ9RZdnQZU1WJjRTcEUqqwTqS37ISFJvQ0lTRH8Bb'
        't1x2/DmqTVY9qYI3yFuOj6WmqoDFEWRHn2OH8mDhEW6FGjqhk3qH2/HXR1HkitNhmLir'
        'NcX9scy//5PmsXf4lWFQsl1QNxmbAezHoASiLELRGX3fWxqp9kwXhpnNI5h/Dr+AtTRb'
        'qIlsbF7Z5JTa3d7Z6cH/dx8e7Hwbbz+Kd78+7O/ufPun7a+PWpBktZOyrYXbwrJttGgd'
        'luxNLNj1LddbE3Yqz8iDw4JLXOTDd6NJNh3zcrTOoRoCAU94bEef74/V5TBWQkkyMB0P'
        'BN0sR6RO+dUsLRcELpelmNbcMvxGC4ZjZAcrAkzpX+P+5UNW+Khb911cimNMI2cXyL29'
        'uqOtdVaPX9Zk43QUKv1kNcYZLOaN8k2jnxBy8OQWRJzSL9tRWo8mcscMI72U1RbTS+4D'
        '7dvllFSWydLAYwGQOpaEvFqkZe3N6ZK8bNhEFG55WqvP7tk6sLPhCd6T/OvwIrIC3iww'
        'Cgih66yWcypkft2GwrBut9JAJLQfKKuAAxs2zVT+F8WPXDI0VJKTdslf0yv6zZ+2H/74'
        'W4WX/Xl6MWAPGvB0omePgmsD3RgxqWG2XRHRs8IcTopX1/bUFcquiCjlTL1OLwubn+RY'
        'cJYUePFZUmL+FWTVccfnKV21IO+08e37WgdN/urmKGzr4hGp0LTtpaPHrnnZoxLBNPK4'
        'jHYA6bJ67vL0FS3OBSCWtwS57CHKR9dVMDMqplMWcjdOfTs0jo3E2MP5A26kGXuJnmkv'
        'Kihhiv3FlfPOAV8T9JceuKj7IJMR5tINldIoMPvvBm/+6rtFoaKpcfFqB/im1mzw1nMy'
        'rmIk//FqaAraY2tr5Ou+aEaWdoxajY5XUt9gsrTsp5ENkl1nKBUkAchVBjer9mRfG+Sf'
        'mFamfqHNVLaFAcqRgoF5H5ZnNgtWt1PCWDLTlRGt8sCzPOpOduUKoGRUS1doVFsMDvY0'
        'aA/M5+RebXi9/KsQQ0XtCXHonDZHU8mQzzFO9oyOT3pB71FO2M3B7O4DvMW0OTKgceuR'
        'aZ5TTQyLUAVvJa5h7IvwmhV7kFL1Wxn0QEX6TRje7IIjAZK1+NuIs8YMf22nmdnc9qgl'
        'BbwLr4l5i8gfsbu2anUyb75jlrBx651WKLoGSYTaqXNFV0SYOFYn3RzgziGuKDa57QzM'
        '671TzS9hxYA4pIwq/WxWEPS1CCuqrVjoRX36V1/UV8TmaEOlxtgZsk8E4BuD1xDiqN0i'
        'qMWqz3MecC6OnsMDHibfELOupWse5dNpsijri4OMhM2c5WVLsSOKXXZaD6uX6dzV6zCC'
        'qHOdyszguWZl5sq5ZmV5J8J54KIKJ3cDWcwTjAZ8DsCMtNFSapuHLgwQrIXgWoPmOPvv'
        'HDdUG3wD2fYsJxuHVZN/pff+JrKRlxGU7Iptpsacao55bh/cMHhNafJ8YNwXYcYSaLsk'
        'RlntuAFHFi+BVtMf63s7gXBdqkiwG9XVrqKfw+i8ziZG8TrDMWazvs/zG+uFolYArEUF'
        's9KHR1vhn8uoBomdbIbvXGA3+aUqjMzAPSrNquQsLcmI3tp+Qu9MdYTXpaNQb7U/5QcY'
        'u/U9rF12Fzd8cwfe0oNY9F4ij6Jl7uCFG/fu3bPqEXiIO3JNHGLwV+NKQoutNwHdCYD5'
        'VPbMMhVLeVtMaASAsnWN5xZfufzd/gbSTXaQbmtbtFmZMXaGaUkML1BicfAnFdp2bJYs'
        'rt1aOKBX2QzoTZympl2Ka240oePYrpQFlZtv+G7Fyj0P3gGWdnORG6nW6WPLy4jeDz0G'
        'iQq+LVo6sk4Kmlf6HNYgjlb3TmsvCIx0NgivLX71G3aBjxdTecVQE6a678nbkBx2xQ2n'
        'NGVscXB3lLL9zvi/xYzUg6/0/aIakD+se8QvgELk8KvGu/jKreDzSloNAQIVdwMSjZWE'
        'Z+YmKhdPeEsn6w+Y7EWK97tf6ct9LV2b4zJNuaeWFndj+Qo3WXI2TB2ljkM7UfQbvk/R'
        'Xr9poeMIZTxq2IDTjBahqRjYWWsnrbNKuxELQhAZjuZW4TliKKzgchmh4/cxrBXE4ok8'
        '96Z7uE58jxbns3DF+Yges6MhzUGiWrjoshShQcqwdGV8kHVaVeczVC4NznP7gDNUx6ZT'
        'eReeHF3PltcKdVQvFLUG4s5ioamlKhlWtuP131nqqcr0LdRTqaLqGLTQTNfSTm+gofpD'
        'u/81Lz//vHSsiGypXLWcf1mr/JyvKbweZ26tN/yZvr4oWy3muQWfZuzShTharN/sX0NR'
        'b60GtFYB2A2wA3a/kWehNa6LDSKzdsOa63Ra1A5DZuoo/kL9jicXfMddzFojiknW1QHQ'
        'RNd7dY9BgJ7O8wKdjsWZ0TLmElDrGkkmPLIkgI4zfzfaNaYMSa8hQ1ImQzRcok5rrUxb'
        'G9Hioud95k77JHalmHGaBwLSUfxF5NioSDGST7EhsUsojARijhBiieBcHjDUjBd37gpt'
        '0qjwdQsWD1YEzrb4ohV43pqB7bqIkQKpKVPDcra4fbfETcJa7yhyHDt+V3HjbU8L0MHg'
        'UeH4VepF9BdGnjkWMufBPFnBkyxevt4z9iZMq1PFw5NSoqNBNQ2fgNGNZhMKzHEI+oz/'
        'VCtMbdGjIKtFVlXs+JVhiW8jRAyexEuTZUcCTEP7D/+1vpZ2XNNlhW5MdWIVFbfTVqJl'
        'XR3crBNfUxcWV7SJVg9rShytYub6XNMMr2P36mZsbV19r6c7ff1NtDaWEtY9TTxqTajO'
        'mE98x2SBsR7IVa7LJiXqpjvM8nSoo7/GPo7rohwDB+fsdE5Hc8tFm1jZXMfRophyO5Na'
        '0Lwa0ZitWlEjCG1Vvl/nnZ10OaS6FeU89OfiX1NJEbDv8ffy/Cv9pTmde654Or2JWuph'
        '7ib6NIpu0OS9dZq8177JuN1tWdcWxS3F8TVEcvsts9ZSdw3Je7fbZbQ+jWig/TDu3Aye'
        'fopxEOJPT7h2yIpegvA1iz4WRZ+qRfHdf/+j2agG3hRBFZqnXEVrOhNaooIAf+jLqa/X'
        '95w00svwkx4uetiQBRJNkGUZFbJBPvPQQKHfjMPqsMMm7DulWamkZGfU6wO0mZWRiFWp'
        'l5n62hwbsKCDZdVrgFy3JTfBstepuoQmXWgyTtmMlZHTGC/zZmOWZlWFwO4tZs8doEYD'
        'cWeyhoBxDTT7WrcbmDwoiAXKPdXt9UYu125Eju56LWEhtR07Jpi2ZZsxdde67etcNsGS'
        'PWhf0UyuYGRs14bdlbtd6mU8YztSw1bE2hpJk6RknRinTaJpDSl067JCMtaNOKkGlw5G'
        '+ZIeoMOTakIlZHddyF7TNu0zr7LyE7LdQNUEVr1zDBD7fML+9kVy7WNyMYWbH6K4cb9P'
        'We/cvbfgKd5VqaGq1wuT0FtBD7Y0AvhEgkVLxnkAOG5gccKoGU/3G1kXa5fn609OMxCz'
        'xcQkd80zN+OXdQf52uNkjPX1GMY12Lc64Ghmy+DS1WHRXY/LynV6QDoEtHupcBremQOg'
        'tuVNiwrRiF2XE/v3QUK54TA4j/78ibsPmC+ldhwYSbL9J/Ua29Ka8sHWyGUuAJ7l2Yx/'
        'U658buAS3HSpQ+hWM0grLnEziKewulXTmpPU7ilcZfB7x3vkQffLYHse4lvR1fpcXs75'
        'laU+2W9eS2XUZ6+DhgBi2aWbuJ72mh1QkgGY2amaUWbzaDtZKDV5mszCprep9kNYJW1n'
        'U7fB42TdNOu8WcF7yVQNWM1vZ3hpxF1eks2KHA+zDSZ5fla6zsiJvvlrHXLYR8bFM2pv'
        '7atD6jlzzZ7wk+hy5B1gxCuJIeaRP+QIHlHkjtpIQwsOsIBxIbom820BLi9kQyd3eBiC'
        'qidjviqABqZdRa92Z5Y//NL6Jiz8o6YoEkcbWhPtYXN5zAA2XSwr+IFunn1W0fuFJaoq'
        'X8ROvzdu2wSzp8NyMkg9HMzbD+N3RnmkS875yMHv83qDvCqSGoOjyM0JdFxKUAXSse0X'
        'oC2cI9dp4G3GsNe9s/Rqj6dbOqtiEnz65PU+0OLI2+7VMwzpTUHhGbKo6RLHg5D2i3uB'
        'a/Ocn+ibjzksXxHMSkkLHO7EmMdJheVITm4OCww13p1j561k1KhgWsQkxD/QZZpTVFea'
        'ghUBTLhgeSvjCatuxx0JoPFDdB1+qPsKw4su6ZsOez227oFdd1SjSIyePXRtRRYYkUwQ'
        'DDC+YVnQHcRVd7zYImt2gUvJdpdsbOB/yo1M9L5SjP3Op1Hb3DIMfm6IxOlIOGXyqZ3p'
        '+QJYmDyGQo40D/Qd1B25XiFnkQ3435anwC4tsOcoIK/omGr9RWEYRmsn0jH7K5xKF5ah'
        'CPC7tBU2sFU1yOjZ4/oWU3jE1dj6SAI8WxTpSXapPSqXJ/JRi5WtQuW55dK20vR0Lm13'
        't5wZOvPiRLjzJaVqJV59x0hWO3SA0PVLTnbNCQKPzEtfaJV6axh+00tCjSnPUDKKwcMo'
        'Mp0sjAfsVlBUqE73Bb1Cg8iUDs1X04j6q0IkN8lb1NUJ5Y5aScBf+lVF1WKKCqNIAhSK'
        'ZSKWwtEpGx2ikQlBIQOFCFQGhcs1bJ8fWzYEHVvmM1zji2R+moYPoyMdd6HThrIyrpPb'
        'R2HwjJEGw8nqdzvs3YFY2rSXu/zl1SLVJDtriN/HdqjR327Wu7wATzgWQoYkMlavJ+YJ'
        'cdymqI4K040d+xL1rYwGAIsA/kWQ7flUpsXYvoXdVS1QzQqn64oGIus8QmXZglQ7aCVD'
        'jlrNx8wxIfCDNjzbPWbMgGfcjGQ0uJEugsislEggryvvS3oxWD4tKZun59AO6Dq0HUe4'
        'g9oMVgJ6y5vQg42IxiE4A+JrFBpjZq3S9/bqNhuubNFnoyk2Y6Q0ub/Zu09vlgwYmtF1'
        'wfWRRyWK8CCMrgm3oU6rLgVdNgo7yihsIkQafREHUSNaehMIqAUaDfBUNpOD1rkeI9zS'
        'iN7mSMrJyafjkf1WiGnWrLr8vcdkjhxEvqwWy0pRjWHJTsb8ljddpu8chRH8VdcJ8VTN'
        '1Dm72JEwdnQgO04gO04guxLIrg5k1wlk1wGkTBeoThBO6MPRgpUBHZkKmgUVogKE2npy'
        'htdaXwxGdWZi+Bl79unlU47wYYzJV8PZRQ8NAKhILdoHu2CME/ZL9i2KDuPZhWFeByTo'
        'WkB3JNQdCXZHgG2wS1m5ekRYizttmtyVTe7KJndbNrlbN7nLmkTpLFY0m9Q+QssvbQjX'
        '9NF7aFDFTZSV4ARBZMeUSfZDOk8LVGF0NZPNN31ZZc9qn+Qi8ryq+TJUF9/I2LOyErY0'
        'NKC8FmqdaAWJxNROHB90LiHko6gN3tz449Klef/HOHRDzTXPaQPNcrvJZqG166MfNPDn'
        'YeW2gOravlvDr9mZ2Q6w2I9RqaB8d7bLgkt59/GPpkTWL03PvgxiZRkTmsJmtSb0iFma'
        '2jW6cZP3WjZ5b1WT/r0LZRupUnaVysO69lELnyWvfhgEVqqm4MhiBn37SjNZamcIV4bU'
        'cnr+rxrDZqIprdL8TfRwinjY1Vu0RIJ4uzqRy3obw22kQVth0LQM8Lwud+b9udOZ/1nS'
        'OuEKAgvBSc0Z7Opn6si2Nizs/IhYd3W8PZZy7zmyN/QVlQxsBFtGuvtOd7MOee9Eufnp'
        'bkGY9ZIjKa5yGoNJ788p0+kJnz48+31eDJyn8HJAYKxG7M2qiXkImoGo8y4CcE9IDStJ'
        'oXnChzbJ09h5Fjh+qr5jWd5WPWqC0AY6PMtjXdTGT7Dgp3g5GtCM+6DnxJ+eYMksViMo'
        '4ifkETysXNWdMDNnQ7GWM49iiYpkJdJHEMwWy/PyolrGDwUjPBaEnpf19/IKf+TlAJ2h'
        'zC0KjIE/sMwJCd7uH7wMcCrmGGdynhV4kG+TTSa1Fn93yCocQREALd7jyQUOU3wViiQH'
        'wrMkca8saokRkgqPamyqAfSiK5TR6n7yt6z/icyk0dmUpyvqpPICogJcjdCvySUZGtsR'
        'z0W5ugX1DIfdCksJVZZK1xlBBpwg9nj6Rt7JI1UT4wi+Q5CwfCZkUeSnMPM6MLLi3BYV'
        'egMQ7Nl8MOCXIyblQKbQr3dgsAg9O5sUp+cRl5IwaNtRp1ZR1KpUwPOYFvmcFWM5VGv0'
        '5Qzp4RTprf2RM3CclqNiMExPcQpukuNjlXGASmWFQeTHx0rKbXY8fTRd0nMXSSXEIr0E'
        'J4aBNICDVGfA2TUO0EYNnAFeFCne8UGzeXNqVJMiX57igMeoyMSsTp8lfOGHro+xfJH+'
        'fZmBuMGNrmEKuKUit+ym1pLoBkuqzFEeE0AwW1R9cgAP8yIDQZZMJRWOj5ENK2ATCh4q'
        '4s2X83FJYQDWPVYO4KBblYZN2f2v5dtjm/mYliWYmoGLn5J7NeK0iEh1I25GCur3YiNn'
        'T3n28aN64r3WvNjB8mB3e2e3t/3vvZ1vD3b+FO9+He/uBPyiEPRNbOxsb3/99dcbXfKt'
        '4odvfz1Q8PJR+Wr/x1dnP/3w6tmDnde/bL/+z/d/+/D7m4Nv5z+9/2b8/q/Pdv5j+5sP'
        '+9l/fn/5Zrh4dP8v5y8n35z+MPn23Tf3T4ePvn/0y6Na4wiW2e+//jX/+cM0+a+r/Z+/'
        '//Hn4aR6vY+fvT3ujLZJ2IKyyBKrqItl3BSGF/+0ZP755eSP4kX6IP9BIfP9/fTF8sc8'
        '33329+cv/uOX2ej0+f7P+fDn8vdTSutmUjvlRl0YKE8VIc806MhobzEWIgzQiCr3v6ZH'
        '75bs5B0evFMakhGd/iXgsevh88sFNAOzmzuYQFSZIqW//5eXb54NDp6/Pxi8//D94NVP'
        'b9+8O3j+l5hK8+NjLg8et16LXDj7RceiQE4K2uKkqvHsxvd2NaPIN26fn8gKSl+cuE5c'
        'GonqqPE5icl2IY6Pl2U6GCXwz/b2wwGzzY7pcmkmLvzMJBTTld5trNqwRu42njnTgXbg'
        'By508smyylj8jX2Bs92OmpKV1uwXs6pIU1fR1R3jmbBE7vjPObST/EIMHwvqKj/z4K1J'
        'TZq8ICvQRbIc4k3NbNksuTV0kUzPmgEIIDy9rXRnUCiuy3vq3DQgO+Sl2FqmIIYQC1aR'
        'x2i9Y3R7ijTqk5TKqppJ0pMTXLfO0+kVqKCLDIlTobGPF9fnvnnbBXhDkIzjPGVOD55T'
        'CZVQQ5nmNgPjC/w4AD7QnnGdBxQYv+L+fVpm8Ig2KJVkrvHiIX/Wh65LsyZgDuUAAsQN'
        'Rbo0MUazyK+nM4yhvimw1u6bt0bd9ANFm2tXAXDVK3lU/5WaS3ne+TwC7LpMXTlMYrYn'
        '/+zNT29f/fg8Ju+Wc4K+Q2iADzqU6ZMQjeY5CcvkPO0Nl8DxRYRbzcxGhC/zEdiMGzwM'
        'rf9gg51y6qF53ZvncznSJGS1e/J1FJGNujWWVLQFWuSJgyvYGN8huj4sVnejWM4FkPEd'
        '4aw2uRpBuf1wN8iJ5lYjNqYep7vACVpqhQ75BKLs5OTusIIGQ7qDDfKK9AqyHAH3fcd8'
        'GelokpPgL69evAi+o2iR3pIVIL3v6D4aL/L+4M2751AG8XnCIZxk0eoeT9Lp4o76ik2t'
        'QoiBf7g+Rg/XR6kJlwc5SYrT8i4oo6Nxv7d5n7b6TMDHl/8PHv2IyXbI35IiQ7dqif5Y'
        '9FTEnGbwk6uMPbprFJONzQ3zYa88yzB17eZ99dUony5n85hsUw/1EruT9mg6hZjg0v4c'
        'FsnO/weEUNRHHucAAA==')
    # @:adhoc_import:@
    import use_case_003_import_ as use_case                # @:adhoc:@
    state = catch_stdout()
    use_case.main('script --docu'.split())
    output.append(restore_stdout(state))
    # @:adhoc_import:@ !use_case_005_nested_
    RtAdHoc.import_('use_case_005_nested_', file_='use_case_005_nested_.py',
        mtime='2012-09-30T09:21:59', mode=int("100666", 8),
        zipped=True, flat=None, source64=
        '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'
        'bjznnPEAAA==')
    # @:adhoc_import:@
    import use_case_005_nested_ as use_case                # @:adhoc:@
    state = catch_stdout()
    use_case.main('script --docu'.split())
    output.append(restore_stdout(state))
    output.append(template_tag)
    output = ''.join(output)
    return output

# --------------------------------------------------
# |||:sec:||| TEST
# --------------------------------------------------

def adhoc_run_time_module():         # ||:fnc:|| |:todo:| experimental
    import imp
    if 'adhoc.rt' in sys.modules:
        return

    file_ = __file__
    source = None
    exec_ = False
    if file_.endswith('.pyc'):
        file_ = file_[:-1]
    if 'adhoc' in sys.modules:
        adhoc = sys.modules['adhoc']
    else:
        adhoc = imp.new_module('adhoc')
        setattr(adhoc, '__file__', file_)
        sys.modules['adhoc'] = adhoc
        exec_ = True

    if not hasattr(adhoc, '__adhoc__'):
        __adhoc__ = {}
        adhoc.__adhoc__ = __adhoc__

    if 'source' not in adhoc.__adhoc__:
        adhoc.__adhoc__['source'] = AdHoc.read_source(file_)
    if exec_:
        source = AdHoc.encode_source(adhoc.__adhoc__['source'])
        exec(source, adhoc)

    RT = imp.new_module('adhoc.rt')
    setattr(adhoc, 'rt', RT)

# @:adhoc_import:@ !adhoc_test
RtAdHoc.import_('adhoc_test', file_='adhoc_test\\__init__.py',
    mtime='2012-09-18T15:26:21', mode=int("100666", 8),
    zipped=True, flat=None, source64=
    'H4sIALIkMGIC/1NW0NXSVUjOT8nMS7dSKC1J07UAiXBxObp4+DvHh7gGh8R7+gb4B4W4uijY'
    'KoQUlaZyAQBLQbhtNAAAAA==')
# @:adhoc_import:@
# @:adhoc_import:@ !adhoc_test.sub
RtAdHoc.import_('adhoc_test.sub', file_='adhoc_test\\sub\\__init__.py',
    mtime='2012-09-18T15:26:21', mode=int("100666", 8),
    zipped=True, flat=None, source64=
    'H4sIALIkMGIC/1NW0NXSVUjOT8nMS7dSKC1J07UAiXBxObp4+DvHh7gGh8QHhzrFe/oG+AeF'
    'uLoo2CqEFJWmcgEAQobQsjgAAAA=')
# @:adhoc_import:@
import adhoc_test.sub                                # @:adhoc:@ force

def adhoc_check_modules():                                 # ||:fnc:||

    hl_lvl(0)
    hlc('adhoc_check_modules')

    printf(sformat('{0}--------------------------------------------------',
                   dbg_comm))
    msg = ((('adhoc_test' in sys.modules) and ('SEEN')) or ('NOT SEEN'))
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'PRE  sub import', 'adhoc_test ' + msg))
    msg = ((('adhoc_test' in sys.modules) and ('SEEN')) or ('NOT SEEN'))
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'POST sub import', 'adhoc_test ' + msg))

    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'dir(adhoc_test.sub)', dir(adhoc_test.sub)))
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'adhoc_test.sub.__file__', adhoc_test.sub.__file__))
    if 'adhoc_test' in sys.modules:
        printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                       dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                       'dir(adhoc_test)[auto]', dir(adhoc_test)))

    printf(sformat('{0}--------------------------------------------------',
                   dbg_comm))
    import adhoc_test                                      # @:adhoc:@
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'dir(adhoc_test)', dir(adhoc_test)))
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'adhoc_test.__file__', adhoc_test.__file__))
    if hasattr(adhoc_test, '__path__'):
        printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                       dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                       'adhoc_test.__path__', adhoc_test.__path__))

def adhoc_check_module_setup():                            # ||:fnc:||
    '''

    >>> state = catch_stdout()
    >>> adhoc_check_module_setup()
    >>> contents = restore_stdout(state)
    >>> contents = re.sub('(mtime.*\\])[^[]*(\\[)', r'\\1\\2', contents)
    >>> contents = re.sub(' at 0x([0-9a-f]+)', '', contents)
    >>> contents = re.sub(r'adhoc\\.pyc', 'adhoc.py', contents)
    >>> contents = '\\n'.join([l.strip() for l in contents.splitlines()])

    .. >>> ign = open('adhoc_check_module_setup.t', 'w').write(
    .. ...     re.sub('^(?m)', '    ', contents)
    .. ...     .replace('\\\\', '\\\\\\\\') + '\\n')

    .. @:adhoc_expected:@ adhoc_check_module_setup.e

    >>> printf(contents, end='') #doctest: +ELLIPSIS
    # --------------------------------------------------
    # |||:CHP:||| adhoc_check_module_setup
    # --------------------------------------------------
    # -----------------------------------
    # ||:SEC:|| no:module:found
    # -----------------------------------
    #   :DBG:   module                 : ]['__adhoc__', '__doc__', '__name__'...][
    # ------------------------------
    #   :DBG:   __adhoc__              : ]...
    #   :DBG:   __doc__                : ]None[
    ...
    # --------------------
    #  |:INF:|  no:module:found.__adhoc__
    # --------------------
    #   :DBG:   __adhoc__              : ]...
    # ------------------------------
    #   :DBG:   __module__             : ]<module 'no:module:found' (built-in)>[
    #   :DBG:   mode                   : ]...[
    #   :DBG:   mtime                  : ][
    # -----------------------------------
    # ||:SEC:|| adhoc_test.sub
    # -----------------------------------
    #   :DBG:   module                 : ]['ADHOC_TEST_SUB_IMPORTED',...
    # ------------------------------
    #   :DBG:   ADHOC_TEST_SUB_IMPORTED: ]True[
    #   :DBG:   __adhoc__              : ]...
    ...
    #   :DBG:   __doc__                : ]None[
    #   :DBG:   __file__               : ]...adhoc_test/sub/__init__.py...[
    ...
    # --------------------
    #  |:INF:|  adhoc_test.sub.__adhoc__
    # --------------------
    #   :DBG:   __adhoc__              : ]...
    # ------------------------------
    #   :DBG:   __module__             : ]<module 'adhoc_test.sub' from...
    ...
    #   :DBG:   source                 : ]...# -*- coding: utf-8 -*-\\n\\nADHOC_TEST_SUB_IMPORTED = True\\n...[
    # -----------------------------------
    # ||:SEC:|| adhoc
    # -----------------------------------
    #   :DBG:   adhoc                  : ]...
    # ------------------------------
    #   :DBG:   AH_CHECK_SOURCE          : ]...
    ...
    #   :DBG:   AdHoc                    : ]<class 'adhoc.AdHoc'>[
    #   :DBG:   AdHocError               : ]...adhoc.AdHocError...[
    ...
    #   :DBG:   RST_HEADER               : ]...
    ...
    #   :DBG:   __adhoc__                : ]...
    ...
    #   :DBG:   __file__                 : ].../adhoc.py...[
    #   :DBG:   __name__                 : ]adhoc[
    ...
    #   :DBG:   _nativestr               : ]<function _nativestr>[
    #   :DBG:   _quiet                   : ]False[
    #   :DBG:   _uc                      : ]<function ...>[
    #   :DBG:   _utf8str                 : ]<function _utf8str>[
    #   :DBG:   _verbose                 : ]False[
    #   :DBG:   adhoc_check_encode_module: ]<function adhoc_check_encode_module>[
    #   :DBG:   adhoc_check_module_setup : ]<function adhoc_check_module_setup>[
    #   :DBG:   adhoc_check_modules      : ]<function adhoc_check_modules>[
    #   :DBG:   adhoc_check_packing      : ]<function adhoc_check_packing>[
    #   :DBG:   adhoc_dump_list          : ]<function adhoc_dump_list>[
    #   :DBG:   adhoc_dump_sections      : ]<function adhoc_dump_sections>[
    #   :DBG:   adhoc_rst_to_ascii       : ]<function adhoc_rst_to_ascii>[
    #   :DBG:   adhoc_run_time_module    : ]<function adhoc_run_time_module>[
    #   :DBG:   adhoc_test               : ]<module 'adhoc_test' from '...adhoc_test/__init__.py...'>[
    #   :DBG:   base64                   : ]<module 'base64' from '.../base64.py...'>[
    #   :DBG:   catch_stdout             : ]<function catch_stdout>[
    #   :DBG:   compile_                 : ]<function compile_>[
    #   :DBG:   dbg_comm                 : ]# [
    #   :DBG:   dbg_fwid                 : ]23[
    #   :DBG:   dbg_twid                 : ]9[
    #   :DBG:   dict_dump                : ]<function dict_dump>[
    #   :DBG:   ditems                   : ]<function <lambda>>[
    #   :DBG:   dkeys                    : ]<function <lambda>>[
    #   :DBG:   doc_index_rst_tag_symbols: ]('adhoc_index_only',)[
    #   :DBG:   dump_attr                : ]<function dump_attr>[
    #   :DBG:   dvalues                  : ]<function <lambda>>[
    #   :DBG:   file_encoding_is_clean   : ]True[
    #   :DBG:   get_readme               : ]<function get_readme>[
    #   :DBG:   get_use_cases            : ]<function get_use_cases>[
    #   :DBG:   hl                       : ]<function hl>[
    #   :DBG:   hl_lvl                   : ]<function hl_lvl>[
    #   :DBG:   hlc                      : ]<function hlc>[
    #   :DBG:   hlcr                     : ]<function hlcr>[
    #   :DBG:   hlr                      : ]<function hlssr>[
    #   :DBG:   hls                      : ]<function hls>[
    #   :DBG:   hlsr                     : ]<function hlsr>[
    #   :DBG:   hlss                     : ]<function hlss>[
    #   :DBG:   hlssr                    : ]<function hlssr>[
    #   :DBG:   inc_template_marker      : ]<function inc_template_marker>[
    #   :DBG:   isstring                 : ]<function isstring>[
    #   :DBG:   main                     : ]<function main>[
    #   :DBG:   mw_                      : ]<class 'adhoc.mw_'>[
    #   :DBG:   mwg_                     : ]<class 'adhoc.mwg_'>[
    #   :DBG:   namespace_dict           : ]<module 'namespace_dict' from '...namespace_dict.py...'>[
    #   :DBG:   nativestr                : ]<function nativestr>[
    #   :DBG:   os                       : ]<module 'os' from '.../os.py...'>[
    #   :DBG:   printe                   : ]<function printe>[
    #   :DBG:   printf                   : ]<...function print...>[
    #   :DBG:   re                       : ]<module 're' from '.../re.py...'>[
    #   :DBG:   restore_stdout           : ]<function restore_stdout>[
    #   :DBG:   rst_to_ascii             : ]<function rst_to_ascii>[
    #   :DBG:   run                      : ]<function run>[
    #   :DBG:   setdefaultencoding       : ]<function setdefaultencoding>[
    #   :DBG:   sformat                  : ]<function sformat>[
    ...
    #   :DBG:   sys                      : ]<module 'sys' (built-in)>[
    #   :DBG:   tpl_hook_doc_index_rst   : ]<function tpl_hook_doc_index_rst>[
    #   :DBG:   tpl_hook_readme          : ]<function tpl_hook_readme>[
    #   :DBG:   uc                       : ]<function uc>[
    #   :DBG:   uc_type                  : ]<...>[
    #   :DBG:   urllib                   : ]<module 'urllib' from '.../urllib...'>[
    #   :DBG:   utf8str                  : ]<function utf8str>[
    # --------------------
    #  |:INF:|  adhoc.__adhoc__
    # --------------------
    #   :DBG:   __adhoc__              : ]...
    # ------------------------------
    #   :DBG:   __module__             : ]<module 'adhoc' from '.../adhoc.py...'>[
    #   :DBG:   mode                   : ]...[
    #   :DBG:   mtime                  : ][
    #   :DBG:   source                 : ]#!...python...\\n# -*- coding: utf-8 -*-\\n# Copyright (C)...
    ...

    .. @:adhoc_expected:@ adhoc_check_module_setup.e
    .. \\|:here:|
    '''
# :ide-menu: Emacs IDE Menu - Buffer @BUFFER@
# . M-x `eIDE-menu' ()(eIDE-menu "z")

# also remove __builtins__, _AdHocStringIO ...
# (progn
# (goto-char point-min) (replace-string "/home/ws/project/ws-util/adhoc" "..." nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string "/home/ws/project/ws-util/lib/python" "..." nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string "/home/ws/project/ws-util" "..." nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string ".pyc" ".py" nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string ".py" ".py..." nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string ".../urllib.py..." ".../urllib..." nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string "/usr/lib/python2.7" "..." nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string-regexp "#   :DBG:   __adhoc__\\( *\\): \\].*" "#   :DBG:   __adhoc__\\1: ]..." nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string-regexp "#   :DBG:   adhoc\\( *\\): \\].*" "#   :DBG:   adhoc\\1: ]..." nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string-regexp "#   :DBG:   module                 : ..'ADHOC_TEST_SUB_IMPORTED',.*" "#   :DBG:   module                 : ]['ADHOC_TEST_SUB_IMPORTED',..." nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string "<function _uc>" "<function ...>" nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min) (replace-string "<type 'unicode'>" "<...>" nil (if (and transient-mark-mode mark-active) (region-beginning)) (if (and transient-mark-mode mark-active) (region-end)))
# (goto-char point-min)
# (goto-char point-min)
# (goto-char point-min)
# )
    wid = 100
    trunc = 10
    hl_lvl(0)
    hlc('adhoc_check_module_setup')

    mod_name = 'no:module:found'
    hls(mod_name)
    module = AdHoc.module_setup('no:module:found')
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'module', str(dir(module))[:wid]))
    dump_attr(module, wid=wid, trunc=trunc)

    hl(sformat('{0}.__adhoc__',mod_name))
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   '__adhoc__', str(dir(module.__adhoc__))[:wid]))
    dump_attr(module.__adhoc__, wid=wid, trunc=trunc)

    hls('adhoc_test.sub')
    import adhoc_test.sub                                  # @:adhoc:@
    module = AdHoc.module_setup('adhoc_test.sub')
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'module', str(dir(module))[:wid]))
    dump_attr(module, wid=wid, trunc=trunc)

    hl('adhoc_test.sub.__adhoc__')
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   '__adhoc__', str(dir(module.__adhoc__))[:wid]))
    dump_attr(module.__adhoc__, wid=wid, trunc=trunc)

    try:
        import adhoc
        hls('adhoc')
        module = AdHoc.module_setup('adhoc')
        printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                       dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                       'adhoc', str(dir(module))[:wid]))
        dump_attr(module, wid=wid, trunc=trunc)

        hl('adhoc.__adhoc__')
        printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                       dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                       '__adhoc__', str(dir(module.__adhoc__))[:wid]))
        dump_attr(module.__adhoc__, wid=wid, trunc=trunc)
    except ImportError:
        pass

def adhoc_check_encode_module():                           # ||:fnc:||

    wid = 100
    trunc = 10
    hl_lvl(0)
    hlc('adhoc_check_encode_module')

    module = AdHoc.module_setup('no:module:found')

    hl('IMPORT SPEC')
    ahc = AdHoc()
    import_spec = '\n'.join(ahc.run_time_section.splitlines()[:5])
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'ahc.run_time_section', import_spec))

    for_=None

    module_name = 'no:module:found'
    #hl(sformat('GET MODULE {0}',module_name))
    module_import = ahc.encode_module(module_name, for_)
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'module_import',
                   '\n'.join(module_import.splitlines()[:5])))

    module_name = 'ws_sql_tools'
    #hl(sformat('GET MODULE {0}',module_name))
    module_import = ahc.encode_module(module_name, for_)
    printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                   dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
                   'module_import',
                   '\n'.join(module_import.splitlines()[:5])))

    hl('EXECUTE')
    exec(module_import)

def adhoc_check_packing():                                 # ||:fnc:||
    """
    >>> source = AdHoc.read_source(__file__)
    >>> AdHoc.write_source('write-check', source)
    >>> rsource = AdHoc.read_source('write-check')
    >>> os.unlink('write-check')
    >>> (source == rsource)
    True
    >>> psource = AdHoc.pack_file(source, zipped=False)
    >>> usource = AdHoc.unpack_file(psource, zipped=False)
    >>> (source == usource)
    True
    >>> psource = AdHoc.pack_file(source, zipped=True)
    >>> usource = AdHoc.unpack_file(psource, zipped=True)
    >>> (source == usource)
    True
    """

def run(parameters, pass_opts):                            # ||:fnc:||
    """Application runner, when called as __main__."""

    # (progn (forward-line 1) (snip-insert-mode "py.bf.sql.ws" t) (insert "\n"))
    # (progn (forward-line 1) (snip-insert-mode "py.bf.file.arg.loop" t) (insert "\n"))

    # @: adhoc_enable:@
    if not (parameters.compile or parameters.decompile):
        parameters.compile = True
    # @: adhoc_enable:@

    if not parameters.args:
        parameters.args = '-'
    if _debug:
        printe(sformat(
            "{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
            dbg_comm, dbg_twid, dbg_fwid, ':DBG:', 'parameters.args', parameters.args))

    # |:here:|
    if parameters.compile:
        output = parameters.output
        if _verbose:
            printe(sformat(
                "{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                dbg_comm, dbg_twid, dbg_fwid, ':INF:', 'output', output))
        if output is None:
            output = '-'
        compiled = compile_(parameters.args)
        if _debug:
            printe(sformat(
                "{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                dbg_comm, dbg_twid, dbg_fwid, ':DBG:', 'compiled', compiled))
        AdHoc.write_source(output, compiled)
        return

    if parameters.decompile:
        AdHoc.default_engine = True
        export_dir = parameters.output
        if export_dir is not None:
            AdHoc.export_dir = export_dir
        if _verbose:
            printe(sformat(
                "{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
                dbg_comm, dbg_twid, dbg_fwid, ':INF:', 'export_dir', export_dir))
        for file_ in parameters.args:
            AdHoc.export(file_)
        return

    # |:here:|
    # @:adhoc_disable:@ -development_tests
    # myfile = __file__
    # if myfile.endswith('.pyc'):
    #     myfile = myfile[:-1]
    # myself = AdHoc.read_source(myfile)

    # if False:
    #     adhoc_check_modules()       # |:debug:|
    #     adhoc_check_module_setup()  # |:debug:|

    #     # import ws_sql_tools
    #     # ws_sql_tools.dbg_fwid = dbg_fwid
    #     ws_sql_tools.check_file()

    #     import_cmd_sections = AdHoc.tag_lines(
    #         myself, AdHoc.line_tag('adhoc'))
    #     printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
    #                    dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
    #                    'import_cmd_sections', import_cmd_sections))

    #     import_cmd_sections = AdHoc.tag_split(
    #         myself, AdHoc.line_tag('adhoc'))
    #     adhoc_dump_sections(import_cmd_sections)

    #     pass
    # # |:here:|
    # @:adhoc_disable:@

    # @:adhoc_disable:@ -more_development_tests
    # # @:adhoc_remove_:@
    # ah_retained, ah_removed = AdHoc.tag_partition(
    #     myself, AdHoc.section_tag('adhoc_remove'))
    # hl('REMOVED')
    # adhoc_dump_list(ah_removed)
    # hl('RETAINED')
    # adhoc_dump_list(ah_retained)
    # # @:adhoc_remove_:@

    # # |:debug:| def/class
    # ah = AdHoc()
    # ah_run_time_section = ah.prepare_run_time_section()
    # printf(sformat("{0}{3:^{1}} {4:<{2}s}: ]{5!s}[",
    #                dbg_comm, dbg_twid, dbg_fwid, ':DBG:',
    #                'ah_run_time_section', ah_run_time_section))

    # # adhoc_check_modules()       # |:debug:|
    # # adhoc_check_module_setup()  # |:debug:|
    # # adhoc_check_encode_module() # |:debug:|

    # # |:debug:| compiler
    # ah = AdHoc()
    # compiled = ah.compile(myself, 'myself')
    # printf(compiled, end='')
    # @:adhoc_disable:@

    # |:here:|
    return

# --------------------------------------------------
# |||:sec:||| MAIN
# --------------------------------------------------

_quiet = False
_verbose = False
_debug = False

# (progn (forward-line 1) (snip-insert-mode "py.f.setdefaultencoding" t) (insert "\n"))
file_encoding_is_clean = True
def setdefaultencoding(encoding=None, quiet=False):
    if file_encoding_is_clean:
        return
    if encoding is None:
        encoding='utf-8'
    try:
        isinstance('', basestring)
        if not hasattr(sys, '_setdefaultencoding'):
            if not quiet:
                printf('''\
Add this to /etc/python2.x/sitecustomize.py,
or put it in local sitecustomize.py and adjust PYTHONPATH=".:${PYTHONPATH}"::

    try:
        import sys
        setattr(sys, '_setdefaultencoding', getattr(sys, 'setdefaultencoding'))
    except AttributeError:
        pass

Running with reload(sys) hack ...
''', file=sys.stderr)
            reload(sys)
            setattr(sys, '_setdefaultencoding',
                    getattr(sys, 'setdefaultencoding'))
        sys._setdefaultencoding(encoding)
    except NameError:
        # python3 already has utf-8 default encoding ;-)
        pass

def main(argv):                                            # ||:fnc:||
    global _quiet, _debug, _verbose
    global RtAdHoc, AdHoc
    global adhoc_rst_to_ascii

    _parameters = None
    _pass_opts = []
    try:
        # try system library first
        import argparse
    except ImportError:
        # use canned version
        try:
            # @:adhoc_import:@ !argparse_local
            RtAdHoc.import_('argparse_local', file_='argparse_local.py',
                mtime='2012-09-18T15:26:21', mode=int("100666", 8),
                zipped=True, flat=None, source64=
                'H4sIALIkMGIC/+19/XPbypHg7/wrsPK5QNgk1363V3elhC+nfc9JvLuxXbaz'
                'VxVZy4JISEJMAVwCtKyX5H+/6Y+Z6fkCSdl+m2zl3W0sApienp6enp6e/niU'
                'ne36m3Z7mr3rq09Vk/3LLPvnqr8pt6vslx0+ml3S7/97fVvW69myvf1+Nhqd'
                'nJz80N7els1quq6bKtuU265urrN1fbktt/ej0fubustu29VuXWXqr7LJ2k0P'
                'X1XTuuk29bZaZcsBCJnqtD8djTL13zS7UZ+tqy67bPsbAFS3TblWQFfZpu1q'
                '/XN7vbutmr7jRput6n6pWt3U1zfr+6xurtrtbdnXn6ps15XXVXZbdfCvbtDt'
                'Npt223eIS7XtEIdsVXebsl/eZH2rvric8ksYYpVdtet1ewd4wyCzrr7drDX0'
                '6nOJvxBKt7vtFAZ9dQ2Ar7btrXpejRwSwHjutnVfQc9Vtq263bqHbsvsql5X'
                'p0wOQiCbw4Dx79kZj/wNvhnjV/DfquqW2xrJNc8VBgjWIKGwgt+MQgYo5IXo'
                'YVauVgtNVAs01wDyiSJgX34qt3N4pn426utunj9Vf/b3m2qunk5Mu5tqvZnn'
                'ihG4PQzssgLC3FargzqeTtfttYK9qq5KRZl5d9/Nun7V7nruzxDk14pc79WT'
                'cX6XFz4KMGigZ3Z3U20rpAHQprtpd+sVoARz0FcN4wRjUsRm1PAfQK4b29cz'
                'hdcMZ26cP+7y7DEAHOMbTazC+3q5brtKgUAu4nWybJu+VKsDUbKctdldrutl'
                'tlyXXVd1Zk24k55NpxmCUgAy9VStoE2rOldwttGFNsvOsCNDHM2u5WWrFoii'
                'xl03QUyc2Shgzm/aFfD7rlOLWM3ipt3s1mVvQUEr5tK7Wq3Ycgks2CEue1fv'
                'DMbRhLCY6KL/uvnUfiQUFOk+VVtiaJwwYm4DxaGAIkuLEunyj9WyZxT7fltf'
                '7tTam/kEfrHdtoa+1edlhSPItmUN47+892eCwHbAXs4wtoCaggDgOurVEirv'
                'NJVm2Qv6gju4u1G8auBoMSlWLgsPBXpZ7q5v+ghKQOvqFrh6ZSCVnQtAC0Mz'
                'fr2IYOhn2ZVCr1VcBXOoFmDdIBbqdZe1V7ieOl7Ry22lmGF1GIMpdu/LZklQ'
                'TI8wGAW7XpZrJbg3wPgrhbDDFLjiDdtAc49RobGYTaSunsbLsqtoReGAmFnN'
                'DLw3fWvWVRiZ3rtqrSaY5h5wA0p0in0axXfr+mOV5Z0iVbXot7sqzxT4vNxs'
                'qma1UFza9bkikzMQ6mJoKLPst+2d2oy3E8T2Ggm8tcy9U/3d1j+VOELV2p99'
                'GsMEti+WIvgVUeS2vDeQ1Ozh3AK1YXlqwkfxNKT9rRKrv8attQcU35Z3P9qN'
                'J3z5vvrcu09N/xrxH0nCd85nMHf2hx6IWh7LGwNADQYG4SJ+pRstsJGgtGJY'
                'yaEe3XC6tjvg+5k7SJA+AJl3IjuAgbEjRWPDz/pqvRaiwABrWsRwqbSf60qO'
                'BBgOGAH2M9X6s9r/FPADqahYq7O6kGIAtR53vaUJj0ksNiQSdqam/Ezh2oI0'
                'MzOgNpxeaHsoiBTl6lUFSh5qRACYOlspjaGGZTk+W3ctDJEVpCit0rRUnbTN'
                '+n4keuJ9Uk06C/amVDINuAbQP3vzEpje4Qcjqutu1PW1GpkAB5pKDPdZAdrv'
                'aLRYqAXZqeeLhVIP8uez72bPc/VUiQ18co4EzF2eyifuUxT1/kMQgc4LLRf1'
                'b4cWfuvorOuPBmgqPglYVL97BRTdlEuDCckQ/ev1qxeL128Xv3v99oV59Ob9'
                'y9evzv5N/35z9vbdi7emrxe/O3v56kf74N3v37x5++LdO/37Dy/evhYgL0aj'
                'kZoUpaSrmdrcw1wv4A/9sO3wUdvpB7DnqgdKePMDpTPiE/WvfgQL6G5bbvC5'
                '/jEaoY5+XfXwJONP9U/4cjRSStbpiDaEfkSKQQYUwrmjN49oe7lXKkuT/TL7'
                'bvZPsOmq80R9Wa/r/j4bq7byoER6gtpSlpX6+n8WBAZxwS8ZkXcVIgEdWzRg'
                'U6N9KIGN/UDxp/pDDkFBVcrBw0ZBXynBwWDGShPelpfraqImAFZJNf91ue4q'
                'Hg38x4ebudowu958X3jvZwBvbJ/WVxqghSS+5ndjCabfbRt+r5gHcFzAzg69'
                'jdXyZ5T4u5uyA0UQXkyyfIFfLhZ5AZu4/w6JCS8VWM22IAjmc/1rPs9HI70A'
                '4NWv8pFkaHj0JB+JVQNPnuYjWiTw42w2m+Ujs0zgET5Z/P7V2xc/vP7Nq5d/'
                'ePHj4uztb94tzt6/x/eLXbOtlu11U/9UoRLRKSweZfOh/9T73/fEkFe7Rqs8'
                'SgazjN/bfkS61OJMq9G/bddKjI5JwDKRldg8u1RspxQJqYCh+FeH9U9K8CoQ'
                'arFutosFaxegrOlHWvWnycLzNjEz7kBarp9a1vgB4AMvj2Hm5rAfTDLxpyJl'
                'YXqxJwDcXZSwr7a3qApVNe53StsrCeXpWjHa2rZgYbX4eKfIvcBtRx1TW2wC'
                '1g5FAq2za31XDWpVL3sYJ5NmZBaRHq+SDesrsWZA40Xoaprhb3o/W+CzxcJq'
                '9goJrY+qfejCvIBVrF4CvaDpbKHkGR+r3PUkIMxIdx0DSnCkLQoHHBHyU7ne'
                'VS5YpMUhgNWJef54C4fmsQBWBGtYfTd+3BX4oaGEWonq/8/+qI66YwFbtbbU'
                'FNh4BGXILLQIdz0tSiTdKvR9QANgzi+0gKmabqf0fxwIDgr3zIkkFjdXAk1B'
                'RbkSfPeqbaoC9gT441ScPhLfE1wpzhKgQWIFC1o9+bXVLmH3j3zDy9zRDYI1'
                'brU0PKxUjZLtCNQ1uqF8MVonqrKaM4jmr5V+h2sGWR51N0UMwgD+EKqa1v2U'
                'kqeOnaxNk7QgPZbFCx7Z8OiMUDxVNanxxZaoOgD3vEQnDotn3N915HHdrBRs'
                '1VadkaGX+XeRj27Lzwsgx0JbR+bf/VPks7t61d/MkUnYJkRbNevvwCfmoIDf'
                'yl0UH4S8hVJGqwRBZ0qY1Oo4qtSrWdV8qrdtc57/8Prffv+7V+/yi8Jpw3rE'
                '+F+re9QjJtm/A3fi30Ua/P95NgofT+fZdyN5+FarFOgLRjn1j/fGJzEi7T7y'
                'WgT0Vk2CZ14bjTAR1nu53G231OGKEHjmfUDbR/icTtiI0LpqrrGHZz70bdv2'
                'i65aMqb08B39JnYkyZFAym8pwfldqbN1T4JD4dQvb9DqrDYnuAXYqDPJeJt/'
                '6J7mflfrtrleXG6r8mO6WQP/D5qygjkf/o+/4mGi6CDq0jqVS/0wWLiICYQv'
                'zqOT+HSe4K/o1KqvnwthoQTPof1M9/YDChkcZGKtv1f8ovbDl/RrVYEpDo2U'
                '1bq9y54pxTGG7dRgy1qc5iYj2cWNgi/77Gl6AvYL1e9ECfNypUSPFk5ySWO/'
                '9gA+t83Dzwgc2d4lBcwH3I/6gv8KP8FtnLQgZxDULa5xf17MieeWb0iIuIqM'
                'epk4Iv3KQVaJVDDbhGI1HLye47ErOkGX0atTfAuPF6oTYZjROhio7BMye2sV'
                'DIcdIgBfjp/Al26f8DnSQnWMutS5+HKwD0/ufwk1eJUUI28mWJlRgG5Q2Scj'
                'jpZjd+oYXN1u+nsfD+jYjCvsXWuVud9duVqxvYuYK9Jf0zbTaJ8OV/LgzdkQ'
                'hFbsgzh1gk3EJ5f7QdDero388ZPucXf6oUHV2W2mhIVSoCVW3j6+7iK4CdgB'
                '+ZB9BcGmICzqcp011R3cM0wc4gJNtHFxFJkeYka1XeRGqkzsrCrs1ZsLqaOD'
                '4Rzea+Fk2DYpeBlPYmd9KBmLhnv3KH79O1Jss8tdvcbBHbYrWdtJr1a3Rofx'
                '15NyGtVyxnLnHVIIoiO20H01xNKQSCOE5URJ0kNUC6FPwNjg9kOObN9smHH4'
                's+RtBfSRKzmgPxgCWOp4/PCn6BKWNFr1IitUvghXZkAg+MnkIUP8Ofxz4aGC'
                'Jx/GBf+e2EuZ622726h/N9vqqv7s75kKVTo2ebgGx2rY5IZBHzwQDQa3CWcc'
                '5kqKhkIdudjSsxluJgHO/h5bwxFQHdfgJneJqpy7u8GJ274zTMF4srpsP3DF'
                'sYUJ+78LasyoXwSbabe7pHfWnAHWyYVWAhbmg24cjD/St5YoXv8GShHsd7vN'
                'quzpvkedBOrb3S1KvIyOBIkx2gODajM+V7/GvHPjhi0Q8nZsJqJpHoJ8GtU1'
                'Y9wUOb4ANom3kTNt8j8HyyK1ZSOZ+LoK7MoHc3zJAvGc/rhIsH3n8L3cUtCy'
                'ZtiG30dEh7OImAH2bC/8FmwuU3H/d9DmMjpA3WW1LzwNSrHv2uBDjcoBEp7/'
                'Zordx3jow318vSlirfGGEWxAG/g2LxTnwb++nQ11BbvjW8WYZ2eD2ygbAgMr'
                'Xc7WwnP4LMmB7BTQw2xKeMkGiir4PV2bb4O9xVFSpJw9aFdwRSw9i1tv+J06'
                'b49zhHma5YU0D8kNBSzT9VVdraB/uodNbjxhV/Sadx2lWoLhdAwWmbm10fhd'
                'N61xAOrAQG4dgMgaV34q6zXdHJne/7jretfSU60ldoAZ0h3QjC49jWn+GPEr'
                '0EXrEHQtrq63UoDsslwv0QeK+hrA1J+u9vpIxAi5brOue4Ef3hAKBJ3P7WfO'
                'dQAiIMYUvDxAqrm7PnWkF8tpdLUYZPTOqMWg/2H87OEh7QPxyIS6uDoFKB2D'
                'ZoHvR71Rwkk/qlx0C3c+xV6kmYq+H1saP5X46ZVcxBlS312cd3avPkfjsdPN'
                'BR4uL4Lh4bU17HYEEKUgfFr3OXhjtRmIYte6q7RTY72Utszp/l1eAQa9gkWS'
                'Gif8wp6L7HsB2dPzeCZgP9BLARzwAPcNrJ4stGqwp1u/2FbX1WfYG7b5h/Hs'
                'ya8+FE///OEc/rhQf7x7mo8i7JWcmvhkMEf5rfZOou6NqE4WTtBolUI7FshP'
                'LErxfve2N8iF7dkYaPjI4FMolcB2vLedwQPbmQ5jEwnbL9/t4BSS03ZThTMI'
                'ex2ovfgWh4QOf2R3iB935H/YLBRK8nX6rbNNpq0sEhhol+CQIFh8mj2PNkmL'
                'pggwGnEamK9rdKdDWoYB/jR7zksQGvkrcEiZRsJqwant25YX4HVR7IWQpv0D'
                '6aCbaMxwWPuJ/HQuiPA0AZsJNzxnD6PJAzitO392ga4v9Oe5oM5pnKSsvNI6'
                'iyxKRKJFk2J30277CfuPq52API1TWldsMw+FPKog2S/n2bPZ//5f2ZO9nGaM'
                'loqA6vNxCqKariRRjSjbQ0vVixUyuHdeKLimtS9xij0soEamj+sst7Ro1JAS'
                'fICqnvn4QUgHXQ0jvV8KofhE6HuYBvQE1dkOTOYZqHtqR2rviOGOUMy8eRfT'
                'HtfjeOezu6igwegw4rlTk1z8Fa3hDuTk8wOIdnEsmwQMV3wzTnNnFhZUSiyg'
                'MZ4+R50rrgwYbVQdtq2465zDEIs4lCV8sMwjHjqPOzzkw0UDteBzXOT06yjY'
                'rmHF6FunI89YiM+BOvWSPUhqIFR9ZT311YiptWmLP3V/qPY6PoUNqELw/E9/'
                'cew5ui8Gd4CXBFrwITCL4whgFj+Psfls4WChpH7UYcJ6SURuhFo10GZXHXBB'
                'o/gKPTwBHZK3MSSK9EmuO8fGpwrQBWiEseanSW3GnhkPbxdMFNjKkmdDccdH'
                'XWyr/9xBUOGg7kQEQXMozvmwmsQfESUuQM/Is/M82WRYGkcAKngD4PTHNANZ'
                'fpE/YA/4KmMef90xjw8fc5EnWayGIW0hMGKs2fz5BPi+ON0Lvkbgf86lfFsq'
                'dQliBuA2QoSrgWHAN/3pXctzrKwngu+rZncLbm/V2NqKfQvObqNEJMWpaPsy'
                'mpVuyy1EtaGoBV0yuA6/hfipPysxpjApewgVo4uLEN4obqbRlzPxyyQzRq0O'
                'u+5EAhwTdKa2sHGNJ0dF1ZRmQJ9u2o36dBRVnhxwqBseDpJUSY9UHAFMk7q9'
                'zmJGXOzZWg73mrA2JOJdWxE4heo7BIazqrq+SGhdaJ4BixoJrwkiRoacdgdu'
                'MRH1w8yeEavD8pQN0njSQEljTNPn0+f07CJPrxUeJn7//FS1iA1F37swYuyN'
                'nbqACfiKDniJOaMo3W2nzi/lPcCkaE8i0kYT4nJbLj9WfXfAnuhMrNmkvflW'
                '5ErMGfT7Wseurtqqa/I+60uFUUmet9oTSi2s0wgIiJTDwxdEMXtGOXd1NnSb'
                'qw5bp6OBqeFIYwf/Q3AHnLujkIbwAos5/jziTKD9UedyZcyUsKq24/jGDuO3'
                '85ReaQy52EOljAg1dig1kb1E1+ktzK06Da3b9qONWtarFySG1jmANnY1jxJ6'
                'Co/eNEL3Z1o46Kp00KrWozp/3F3AoPAS65uvzEcsazP0wDKZA5pqCS4v23ut'
                'kI+CHVrHA5GotuFA77c73+yHCJzXp7g7n9u9+kLigQeakh28tTxEFz/cLtFX'
                'VUQugi+HtLLjBTEiB39oextNKjywBpwLZ/jLdVU2mToNeHvu7a7fYZiwUt/X'
                'uw4yS3hnj3aD9q9tfv7hfCx0OIz/5xcXhXjBOIMxGC5NtzkEPWS00ivF9Nv8'
                'w/OcPVrSjTIdKoH9HNpKrZUnZrFAZ9i6gOb7G38Yj8//488XT4oPRT7cIfzD'
                '97wOlfkYicHd6hP/eInPgmPkoJePvlfLMURIvT4NLkMYn+S925denHgmkcFv'
                'dTwKSbx6vabRkWORRcCYB+iCHK7IE6frlJ/OIxvexKlGWCjRkLRXHuWRWJeX'
                '1dpxF3A85esm5eCh0Ptu2Mkj4YBfuL3FqR53z2ckdBMX22nC5zr7zm8PnnHo'
                'njzscBReOz7KblolGNebX/DJC6QvxK+YDC8gmiGhS2N9IkfxrSJ0s+h3m8Az'
                'TjpyOtjHLi3NuMgplEw1CqocABqQzdakcBdDQcdOZzibUvHKXeuLXlSrwfDg'
                'dIw2ZDlFDxoeL4IjBzt90mWZHm4kKIeUTSfg4hHaRQdI0YDkcGYw1IO+3ZwN'
                'DMJdHJFzLqYbqCtOvCF2U8cT1xx1HVQuPC8JilkGx2g8WMLGaAFOkOHJBtle'
                '2ZQFCZ/B0K1owVKaKFh93iiuI5+kmHEIW2gDKTVBVwk2sRqAEyFailFSEZIk'
                'H0sa09zZ3sCgVwTOE5xuRn73/PRiz3Hb6dOZSOqU76LEHLRbliosT7TOL/I/'
                'mSMLmAbpRqjx3FSs5OF5nqlvO/iW3LFOB8gE76NcgX4yzT1mzjLWXdZOa85g'
                'oRjnrlqvR1/VDdPBLyLF4x6YRgmBXF7N9TpwGHG2aOF6RpfnqX3Y8fxMus4e'
                'aIXgpFsTw+D8YGGCA6K2iLF31cYj4cajAQkmDF6jr3gu5uPlJHYiPuw0THPM'
                '9yhRyhX7MD7sNCxPwpPkOTh+Bj7u/PvFZ1+bY2tho+OPcM/yRNEhp2ePyPo2'
                'yARmB2sjZFi5KMzg9HdRB3N+l750Nxkm3AauzON3y5sWL5SSwOgDGDAuBPXv'
                'mB6RjzX9LSjNAC/iGOV/etz9BaiaT5hEAn4xsBINBI9Csdi2sVIR1gpk/ZN/'
                '0objbqcTEYwJ5iTDz4tkoBSn0NjP7/y9gVuAv4BBxRekhGtEbuo4+0O4Aq5Q'
                'NT/sF4o+nFFK6EQ9Nu0k0sIQfUsJK7nLiDCdCyQFUVt1joEpE4oMwM3g/2az'
                '2UXQwXf7kLbpSdKUMOCPhW5Sm6RgY7qTQRCULWUANwAxRFWfi4llcKHjJMMK'
                'X9j7Jtl/kVrhWvYxrMLr34GRylZj1oRUehPqA5ilMNAVrRiqC6MWTbKkTUMn'
                '8MjQS6DrxwQlFBf0/By+vRi+OFpVa+fr4/vSeXYkFEy4Q1lO8iKqB1j05s7P'
                'MDuKGQ7eM+UsqfNin/DH7Q6mdmKddmEb4B2ArYnQsYF5cREcLdz3CpwAHlcy'
                'gW3wFEC7rZ5WMv4qcIJPkhpygmkCJwboyzaze+fCfTHyvBZM1p+I5wKk4htY'
                'a4lwxugxwEViHGGE+7par2yjSE9hqKBzPrSGxAnZwiS15Dk0TI1AMS6ZNnoa'
                'A6c3qSbD2Az+Zyy7krugMf4FGBnr37fDDHofe11iEC9P1JztF0cEcMGkdNV/'
                '7qz1Y65dttwEO5LVE2yrj2jWajDSmWkG8tuNnV82XQ081klpRGpAzCsJXWFG'
                'XjjCiuCrupFn67+JhDXHcZQfLGU8YtG8IE0bZMyHJUQrCG924PbEzkiQTnA8'
                'ME1HToyYFEibqihpLEx/C7NyqOwRVyCS2JbMg9kfH8T6mCdUH17xeIwJfp2M'
                'TX8LJD5QqHAMohQq7kWSPnHn+ro2abW0Oqom32DwtjASKPwWrNdm5/q0MHF0'
                '/IuDw68y44mnzzNN0E/cBoC0IN8vbnCaWQJ0RSIkM5UlUD0newt5bJ4Z76TU'
                '9yObbo3MZw3m8ON2NnWa4cXgpMZ4GfcpOjjoxMUpOwi3yvJ/tCnlYi2KCEx9'
                '/mTmQKepiZnxyO7lNYyABEPR8fCg1ShUtiRFfKGBatv4hU5tLtI1NpSunMIL'
                'MbE3StpttusofYedAxNm5UYYFCKRIxukKFugFhM2ozonVWaBpNbo7vqWEu+A'
                'EZomPchbzBnfOZ8zpJJclpiYvu735m0zDSe6Uz8vhf5Ap11MM6XbTgvVuQYs'
                'UVBkCJM76uwxbo9RE4QJWFRSSePd5XsPtNDAUOrx2Omo6GCFR4A5Zhp9Sc7f'
                'zeVQ9yiDTm/zcKThTmayIO9nTHWOYfcWXQegdMpaCP+XEjNnzoApzOkkFFzq'
                'AWdHTyVANdjSZYKf+NRi+jLg2Jv2TqIaQRQ32jeUbpdTVPMqYqx03mrYFndc'
                'hUCtRS9/uQICWTurjpZGJVcPQmuqasUlHKCFvfQwbILkhfhqcHZptxZBU8GE'
                'PNPtELB8Q/axur9rt9KzlX2PNFltanW6Ilp3lBQfXTVtJlabpt4UCmBK/Cv3'
                'YHYT4WA7zbydECsYgNUBADpVD9iVUH/oZpPH5WzKgqjpbpd1qeURSS/eYGXf'
                'KLa5zoBViESCWaDFjWIT0m+oWgJP6VjeWEypoIqBtbu9hJzlV37hB0NiLDSj'
                '8R15sQOd+mo1y/753mStx4k1U30H+c8vK/MpOSswRzjASH7r79lhU4HOXmOe'
                'XNYV62a53q0iBuJp9iob2zowhe5RiToxmDE6F+gSPiXOXhGBlf8qtwB+qrYt'
                'sKocWBdr9CTSCPn7AQg8FbDkUjkG1CuTBx/vbeurK6XnQprgy6q/q6pGVhug'
                'XAdYauc57Zll76XN5NIiZqLNwo5P3YSKjNhtVv/HvUwYZ12hBrf+YZDOisDV'
                'rtmYvqdSIfprfS3XGkXApKbQzkiRhAYg+rC0FJuIiH54ode0zIbeyiQCHoUJ'
                'KGAGGwdcz8VR3nM1Ej44RUqzaEawwoSlv6jHgoacdiK+QWa6gmoiIJzA7khl'
                'lvKrdVviH5BQc119xiIjpbvgOce5roWAtCmXsJF2/uW21R2zl1eob7ibuUYA'
                'a1x1JEec6eXbM5SyzCIkqPSx0RFMIOPbOxAYL6+MxdXtsbzCIg9xMoKFWIGp'
                'GktEvbuUGzWPm20tixEhXdXsQI0MoWxqhuUqO+gCqqe7VFqblrUg5T1Rih40'
                'vtQ3LnTAENud8cFg3ryFJCbl+q6877DqlWXvPuBufzut8RQN5S4UXiWsvqvd'
                '2i2mJAk1iuld7kLAAx5zrsi8zEatS52s3Kv0Qm31QUfucLSGUBPR3j+EGpQ1'
                'shsMiaUw9Q/1brkPAeSwj+aeeNmJsi7Q8wNSM7uqQeQD6DfymGRhyKtmf+1T'
                'L3W9ssRrLGSUgktLK/VaMx2VV4h8gBXPEo118TYvBQPq5p7+NPeo5n6MCs88'
                'MwdP80KbMvBf9xVtCXMinA9OO0zwX+5rlLSUAN8DyWLI3Km4r80CnRuyuR+I'
                'LFT+YU5fLTvX7XuSy1P1GV0HxshSl5C5J2mR571nSD3/IZWSClojvfzHvS0d'
                'Y9vzFZT3GAbvP+NBi8cXQep7Tt2vE87T6RrPdYVz84dEuZCLlUps2NRdHSQS'
                'FgnraQuZuAzo8ywKcVCiXmqrYLWis+NinM9MJwVKd65wlRf2zLl4BwW7+Cx3'
                'pk2DfxcpX0mkgG9bwo2LZs6GPY+J3enyr0c1mi8jcQdVW8D32bNfAMT7dpfl'
                'w0aH/Kb8VJnEwVC/EyCaMPOs24Gdu+OO9gGDcm6ZQYsEGNcbI33fKh+541RC'
                'n4rrZavBZ/+Q9ApJEEaT4fGWCpJuNkot4MJyjw0sYY7agaOZZHBKBwt1Q5ir'
                'R2leng+xNnD1PGRt4mr838ko5Gj8Xx8QcXNQTs3wMipwsUv5Of87GUWZWP8x'
                'CZSOOWazjTlWzo1j0NcWU5HSHWYD1SB8ofQDkOtnl0yRSTpE7nwTfUQwsCDG'
                'z8PFz74GBx/KjT83w1lFzGc6OMBoy6ZP+J+D/TQ5U2x0OJ8lGMkO8FvzEbEM'
                '9PdtOMaZNyTHX8PEheP9OvMmBvjzTFwE0a89c2foa/135fOvS/kkD/ik9gnp'
                'JPYpjPr0DBccaEVEZU0bV4z1kXqa7Nc/ycAFWJFGWZoCvn8bOqhk9L8rof9V'
                'SqiuiIOFU2fwP+NkwTqhLJzL+DanVobWWw9TOrBpIP3+ruXKJfLfW839W+d3'
                'qTY/jOd/aHfNz8/tX42rQ7YVA/ovYdi/0uNXU90prtth+odDeO6Zm8B2mKkM'
                'cMFY4ND5bfnKFDceYLCBTwZ4yOL+rVlokFui/PUNeYTazZTO1gSlNvhd9bnu'
                'havv4t+p7vy3m2gubJ/W/78OH5x04AoFIUnb8jbvdLfa0QUUVBj6ScgrDgX+'
                'qtnFuUjSA5zroX51brI9yA7lQUB/EfUstM2Z9XwAsnIjf4JXYDbKsgi/nZlq'
                'XAwuzuHaq9C2cwrQSFvH7pJc3LroGtC7LCnlb7pqt2qjHya8QukuC+fPC1ai'
                'VB5sj/CQmMU6ZN70oVhe9djz/GJCbGhxCOXOF67uRG1imooFEu8Bi/4InTdS'
                'y3dh6tZESvpKzAzf0U/vSwz14/e35cbN6cspWDjezsa4ybQGibn9eZQaCmSN'
                'nzCj4/tCBRuWJQFzGP/JE7rQdvJFKV2EkoVrx08QzR16g3vV5ZSMofYUXwmN'
                '8iIubui7c/rmws3WF/CGqV0uktmg7yQEleCSm2o/MOleSZH5QTwHXnTDjTTh'
                'EK1mxcOA/KL0fRHLCVC6BQtjUkcIlEhIoseR+pjhgI8NG1P4kKevzitV99oT'
                'SnGHJ2QNhnL9jM1kD68kGVvbVUGkKj913SK8+NMwZCE6/G+kYGkHfmoCaT6F'
                'h5Twc+H3z0+dJEfA/YLc5M1whScLtZaFI4n24keXmMGon2HlXiBduIjY7E3u'
                'TASxvN6s+xMqerjw43l11fZYIivRbiJioaOduNx+211zXbLmYwPFBRjDx9uM'
                'mR2CEChtoeqriJgi3YAV4gsF1s1UT67sHFq2rW7ZYbXd6PzwvEQM5SV9yeWg'
                'uc92zbZattdN/RM4Z3NbTvtFPpVqwlrrs9u3G5k3DAtr8wCXJQReLesVeIiW'
                'uERXrXGHu3U9hogVXKbUZwT4Z4G042Qw9iuxLtyEFvYTT9WDFAG2zUzxIyu4'
                '48XvX7198cPr37x6+YcXPy4gzc3i7P37t27pVw4X93k40bYwWXosPkU88ALi'
                'PvaGXfy6XlfwoS1Rzn6Avy4hpuCeYvJ1vNJVLRxhVSsWMi91SAH4eWqIaK1X'
                'H9VLTOwJASLscggm4CCggaIy3LgLp8hjwdGN6bAF4VrZriryojWpe1b1ksaA'
                'USOYE3mNYUHkcglpOsGT9ow9e333SszVx1647DYJJdEURGyqsINCx+TMavG4'
                '3F1Brhbt4gld5hAL2qH/nHp7pUYJXzgde525smNfx0NRWkCWeb5VwoYRi7os'
                'LpB6c/zae6PHM9cAkpsMZzSSmg+ODNx1y7X1ZT2ZnqAvbpd1992s61d/qptJ'
                'u+v/4uwEnMZJ6TXTPAgRVQOyuc0A6WQqnQX3UTdh5vL87lgoCssDsvgYYe0M'
                'GWUW0vnxFsS07TaMjAguj3xBDSK6xYgRN/+99vFFTkfREmyvekZPY4mnkL90'
                'niqL4cRtOpxmaQiQcxaDAKswmE+H8CZ7d9SPSGYRAAuykrwn4bKxbggq3z26'
                'qYr9sP3Hnc7/OwaxNdanF0qFYrN3FcmYXS9yF3hf6ZhvTFhnBrIOEuMNt2dx'
                '/UpvEAOBcu8woluLae3/h+EJJh6Mhajx8uwypYGV67q/xwg4E2BFvreAsVYR'
                'OQIHQssp/gFAIDBepSZSrjxMKEVOSdLRNXas6ALv2Ik+AqEaxoy1WNyU3c1i'
                'oTiConUtBtV/mv5x5YQ6NW7rON0gd/AXfSnBNNU+MMBb+AWWEQwAcJBHZ8B8'
                'rO5DIOqhlU0LiBxdLMTFH+n7P+h4EbuVH2zqEDk4onYOODaq84UiQuS1CT+N'
                '2vX0PdjVGtC+Ueyzduik7+u8QQSGgmIU+MqblJxzOYBE3LHIHug9chvIwaIV'
                'xf4MHO+dMZEPvvPIP/kovX9bXdewUHyn+oV9QcYWJ5MmvKp0EoLAHZ/eqh0G'
                'XyvhR7Ef0lW12NsmR409f1izBXvRh66WB0MAp2ADwHqVHdz+Ci7bDADh3nQA'
                'BDIUQGPpWXFwQzv64Nb5ABh49QSNxd3fAc0owEDeVB3QiM3G0M6x/B/QlI5O'
                'HVLYM+q5aV9RW3EixDiAS6+OTC8YCMdq1L5Se/EjlGmEPnIT25sqDO1W1l+T'
                'adO9gkL0yrFriA/ddeZVHHCSsdO7GGxdumBhShc4Hzup4imlTAJ/89rHy6SY'
                'h7DqihS9JjuhQZ1gXY0uW9eYKbaprtW++0kHOfvGKH67oLc6rxWXH4AgSKUq'
                'jrf5f0w/rJ7+jz/DP08+zOBvNyuxRqOlNB1uhmJbIRPP9Fj2A7HTvQtAhAdG'
                'PFIMKoXHdi1Y4OC4DyF+SvZy+Gq1qns/2gg2+WBgXqHuEfUW1azo1VsSv5Re'
                'QKbRGWgFO6tZKrR9sxS/Z7MOJ8N1zta0r9Nnxqhkpb+0H3jQ/vSXIoBwjl2A'
                'QZE6EXu+aQ3m4yH0pD9DyrhoETx3gFygcdoFVAzRO0p9o9ba0OwllESBCPC9'
                'c5GYGUVHs6TSqqa79Ga7zQpqjWlTbpCIu6vsKsbFgxxvLPjm/AWk3qxdkxja'
                'GrfVp7rd2XxQjiHMBpw31Z2TV9wtBujIu3TKpK5PKdCotrmZlbSV/lw0F/Fl'
                '15aaTEzMhX36xRjOKd5RVPHxkz3FywC7uet8Vc7hXTO7wKpkFqZKbHv4lN+e'
                'rVZybh0tbLitvhsyNixmQ3SmjHGjzqaC8yMbEtaz2YyOO3NecOpBEW/gZZn2'
                'fg4DMqc1w/lNKxIR0fEZpD06rNZUtwmjqsEdFnIO6OdqUiWg3uQ1t5tC2bip'
                'QyYmhYrtUWoAPEBb/4cV9UB5DxLCbymTF9bSALID6z0nvttiwTIo8cZZohBC'
                'yLc4cNWAQ6oHVlfo8YtcbijT38Ft2pWT4ckMzrsfoz7MXgFL0TbSQbM+Uzll'
                'DWCDvquhftFdlcM2zSzd2MD3gLChNSeCh25+CBbER3pxQ5ULTQ2obSuv4aZk'
                '9fcXNVjpdGSunqgY/TmMWl+K4lxd+HOpxaMrIsKJtFCo4wszft3mnERlYFGM'
                'nz8HhVqys+DMGr/FLGVWo0nkNtO762LlVjsE8LVmq2un8dWmf7HJC2qhU2OM'
                '5dfFPs93fWnFuJ487k7AvubA8BA06QSDu9bowQPzWblZIzDWnUmv0R5Jn/QF'
                'WNF9dYxUJw771lsNp8CwPwYIYyDvpcrjrY8e3t6Z9qP41oYyfxlWUPJ3HjqS'
                '7N1/qFKzOg3oW5XfDDQbOijpu3f8FZhVqbyfg2jqFJXW3Ayuv+OmL3TL38Qa'
                'HnpqOwpzSf9khbBt1bXrT3Q20mfgLnCmqZYfF/ptrBoWlnppTRiNU3rQ0bb0'
                'APyiPrqggkkrQ8zuFidcVZ/lssFsaPd+bq8aM8c4mt9DCmUMHM3PnacXZv3H'
                'XAmu1uU1bs4houHRUx84vxh5c4GSOFLP8F9XDYvk2WaJccBBNp5g9ICGmh8w'
                'n3CiSqDOneZl+3Z0bOdkCZWT9zC+y5TUJBRSuIIMTy7cPOvmubOedOUttrJA'
                'etu6X8tqlfCTS6UHzmtOQfqI5AqmmcqiI0xM0+wCH7jwW5YNzO1ttb22yRem'
                'WOONUcd4thJSxD3e5odd/MFNlMDIK5XlIXcuvoRFJKQXkRKoU5VwijUOX7U6'
                '2brlVw8hpJmpgJph2SAu72oPu0RbPER3WhUs+4lVWz0YxlsNTskEC1ebDgg0'
                'yORdpJKsN6WsR+6d1j2kJS0t3HGjqxZbzQWESaLgr7nU4I+H72kiFy3cLrh/'
                '8acFZtfKfe2TUW8tiYOKAl4R7dliT9VdSzr6BKg2RFR/85Ozur9c7KPs1ev3'
                'L06R3wbUiwzK6GbXmAGdZsU7s8o5AJI0nJIbru4xlxak/mQfEqouQnfu5WX7'
                'qdq7VpJaiFeobNdXnxda4TGsltSZRsmQJCKw/nkcGyAW35AZxCj9ucdkphIn'
                'Soau8+NtGUsXNxevQEJ5WBmM0EpUut7KQ2p24jxujWQJR2Asiw2RTDbjnZ8k'
                '0Tn56q+SZge98ZzITzGtI9+yiGy0jt2hO4m5CNq0wb6/yW25/RgzW6BnlB3M'
                'FaTkW1clJItFu5DjsoIJ/IL8YZ7PM2XsKrSQTmVyjztDGyoAc4H2s68XrwiU'
                'tvTsNzike4yrW2FSX9wLm9ZTYH1FDHNGU2cT4QGfBbEPPnv6Zpp950BZ1pir'
                '2EIaxdZ4fwYYBnnuxD0ZtFsMfRBXwgMyP+KjvdDw8YZp1YJJkerJIiEhk6mN'
                '3/f96oXe7XQK5j+tE0pD4oCKpxeWQxSlzJ0O5CDIMehfYovWRiVX0IU3ogeS'
                'v7Bnwk3bO/eoj+gR7NFVkxOxgiGQbqY0VQ4nMRiS0io4oRuI4NBHD/cU5E/E'
                'AyeByyK7sLPvs+fxk1LQ0fNDOxpg48QAnSM1uHjCMq2bkkvPTqdXbTu9LLd5'
                'Nv0+y9WPBf5AeTP9TE8/56OoPZOiKCi9IV9jBFbNWIgIkCscQKyARte7H6mu'
                'Iy2l53/a+zEKbRiQSILptpytqd5SMGVFbGlD+4GVi9ITKGX2KyuE+DL9mDPZ'
                'AIeL8cz4UnCcT8GlYpGnzuN0DbkKN4oH7gjRWq64OwTGXnZDMyCjV8PGLCt5'
                '0viKBCVVYzfJbFs1jdxKu0ExK/YG8dxD5T6l3aC5xIbvbOKVH+bHaFzVIS05'
                'd2PscAsKoYq6e6XjRbSp0HFSDPorjqn9Fmw4Bhs0Lu5w3HiVdxqybYJlo6OS'
                'dPdskp6ZR8zBVd2Qiq6XD1UP0TNgc/y3roMefuG7anwFw1zQbMDSGIoIFytz'
                'JXCInXIPLLNd+Lez7md+Ge0h6zElJJJ9nI6G7AHO5Z11sRpqYs5CXkeSVfx1'
                'U4mwIqe5einIJ1ayrfMCljP7qatajVUTiGssRgG2ZncRzt8OmQ+rsRew3SSL'
                'lEBM/kcHTX+c0rE8En6lKaRp8Ngf1RCpmT8OIrbDVmCPxVUbUnvAPD5xj9R+'
                'J4G9j/uR/n+2n1HEH8VTsNhuPLC/DixP3Jc89NnzI7BKiloFTXuHqfH989hE'
                'j6bu3bIt0jatjRIQOIvip49pJwfWEffvbGae6d1slsYX3Lm3C7yq0z7hFvMJ'
                'G8LIiVjav+hJ9LiIRholoW7rDutZhSfcSyW+YEMJjLQGCik9VqmwjnDeJ1ZA'
                'aBmVC/wje5rfXCqPTtO4Vqmb+ZfwTlP/pZe0DYltcx448+T7ukdajuU8SCtw'
                '3NWCTIU23MNL/I6Gb7a++q630m4XeLCiK2Z224K/lq0tZAz54ZxGfNsdZk44'
                'w9v+Q7Pdga69omH0k7TzrWipnx7pcfrB31A1vMGGR10r22D5IYaK2C0Hpjt1'
                'c/xl14BD+MWl2RCK/j2iFnwJJwC338PEn5u/KxxKvKsgYMVeXh5ZPmEhr+jt'
                'kjqGO6yPpe4icZ6IXKRYka2zU2oOPeBcEfHc8cb018GUPk5fjRHdCOYgSm+S'
                'xfZkdrp8bSP2NhQUGK9ph4H30ap2g0HRmHUkUk6N80aJEqUQ4KrY4NP5M6G5'
                'goc+aKcYVk1/aoXVtix3fTu9rtSw0H6BWpJhqMKt7WbCtxCifKAQu9PpADR2'
                '4Dkq2lebes3DgZrdVy2UQvLL7Ti1pSUl1C4GDK5acyCL6q/tUgWmNuCwydkO'
                'sH5QJWCZJEvsRadgOkWCOYkSTiqkJsMQdFEu2MFLxp4pQD9YqyseqdkYG/hs'
                'ShhAcgj4XRwIDL7tRD0yVydfreqBvgLnRuYup9gx3cOt4xCC86mC8C4est+y'
                'DSVyCp7iHa+uxXQGumg2vfnHKT4RR42jyhsB46XyMCH7D2R1c1Xm8BPi3tTb'
                'PVnjmHshxdUodn6V7Dh3eHFPbOcczJIRkDGOSiHns8RAXmzXUSFHm0Gsfz23'
                'mAtdnmLdJGxxr9r6dgPXV0pFbpz7KvhPP5zBH+GlueIWYOYT7uNEVMdt/UwV'
                'NUR0KPosQezNHD9+Ae4N3IZiXH7qixPHiR/d9GmHmYvYPc0fJ69OyHP/JAUO'
                'an1W5Ur9Ncl+ZPxUy/9HAy+8dF3OEcUd4PARZfCEEjGcOIy0J7o45KgD4o1D'
                '9hrwgDGBeeBSSGlOUFiL9GmK03D3jN6s4BulTbXdbFP2N7NLNcdY0njh7KN+'
                'mDE2CpO07dgMhv+6r3jPm7P42JcS0Xntb1NzX1J4n0d3kXlcFngR11oUz83K'
                'HTkxKoEfi+sy5eess24KDJF8XJTyGnNByIsiekCMNA+30bBxt7vkwFcniYAX'
                'l02pcGQixHql4NX9/Tjq+anvQ1y7pBd6y17nZHTR8AKXYKQ05mfg+bcqDJia'
                'KoiiK7f3otWYKo5XnzdqPdS9YX4l1JRCu91CdqXrdXspCBPaNMAhZYqeKOm7'
                'U25kMxKqFgPRJcHnErK8JDShFcxdEa9iR4qOEmlVuaen+Y29s+JnT757Gqvg'
                'Zs81cx1/vT9FK25dit06SjykRIhU/0xyVsl7eoQ8p188wE/RAZoNJTlGu+Xs'
                'H6belCTiSWIcnLA24HdSfqTLkfo2MNPwEQq+rButMMW8z+Pex9TAc631r/kE'
                'oTm1GBT4DE1GB17xkWbXdQdcqsdjVvXv4rCoxjdKCPX3JvHOYXG2X1CuEVNT'
                'egURcY+LVG7UuoP/Ks6xubeTRSo8esZi972WI1+9LuMRAdA6OdA/isRAHKT3'
                '4ABoGJfdv9KBNCaUQWx2SX2aFBFdEZJd3LE64K1ivhoSDxkw7sbqx7LYLJCk'
                'kejKw3L/UmKREOGUQiPX407GyucyG6eSWDZdU+GcGHK0egsnSnAfdZgu5eWn'
                'zeaLsfR6IHCQhmR3ydYaR4/wToRBe4fd6XYqdr/lKCIpZ3PyJZfdDSXnSgGW'
                'KpeTDxJUViPxeLpcQxCXeTYpRruP9WYjdZxHEeMFinDtAHmCAE9PviAZrkyt'
                'bS+7Y4m1UeY6+mU0wlZvC0XoMGzbJF2547jh9OFYx1btn0hsJtyDYq1oPLDI'
                '9ptI9D0jf6nhlLedttRGgkUFaZx4M255WNyoyB0TsQ47oGJJvFMBfJZv0+7Z'
                'yTgnd+h7bcrHGNwPjXgDd5AhU3hqvYpJGWyfGovjDjycVvg84fkwkOoh5qUZ'
                'JcxF2oH+Z0EqeQl/xN5tt+8fpJnemIm0Ef/YHVxu4pSqVjht22JzNlFt4J6H'
                'yw4sDyYxQiTj7VCq20+nqYzDIpmvkeCeT46nJ5C7Wa69cgB6EfIpFDb3Ri3Q'
                'PXzsjyhLgzjVYt7Re3Wovs2c8uk6oUN0E+FMB9aE4yWy1vBt5hrMyko3HqzX'
                'BEcBrKCnv492a1/PRa7HQHkCVwtmdrshg1EfDiF5qC49OH3MUOJtsZJuys7P'
                'XyzAFEmP7HjCl3R33rnLxAUH+V8ifdVdzWmKx26jSQYWu2SIbrxfqyhQHSLt'
                'eBVYSsLDWz9AKj+HkjvlHl/tnfJDclykZzAxdZEBiCq4XlaMSEJxV8nXR312'
                'wRJpxFB4dGk3WzfJd+dm5T9I1PHwI0NPJd+OeGiBSsopuY/I4l1ETAnrQxvH'
                'bIkeNQLnYulw6I5C0VkLOvXxom6u2nFx/vwiJc7VQhmrvwrHizwpr2Np1d3k'
                'COgRj6l4naAeYANMXKzOAYotILt4cGKNW6mTZ1c3F7x2TSrxGNUtANgCb0O9'
                '3OpueCTcZA56TfCO4yVkdvOA3UNuO7Vo2+Vyt8WzT5CSRV9yhkHXMhrUZqw+'
                'LJLUd+8SsDwHhyDEs57w13YjqRo1OLjpH6fhFAkPax6bP1x5pJfdhTnzHUhm'
                'Ccquz0/r49vUUDnu1BVcnoM7XU3rZMg2AoElm3Y02+CRrHHSJtbLG3QtLZss'
                'f51boUdxmgweuL+hZBwTuQuoNmdBG81hE7BjlGSVl19AuFEeD9Nb8DhcFgtH'
                'AMu799zzxRJZ1HTWhn/cpeOxj33nMo8Pqwi8iNl9QA3nqicnASoF3ExjQWhO'
                'tQbKGu+njR8aqPY4UqQs4scMZxw+9nENYm9nZ3nglSzSdmmLGYhJaygLojA1'
                'o6xAAhJDUk4XtKVhzi3DZgcYmplb+t0GDV9yf9VHSDF5xSgdc0cgoiqvNSog'
                'WeCe6CyMnowjmGTp8/rCBpph5/v6fJ0fzSD80BEVcMQh40kNd29qsq4pVaqa'
                'NTDOsOXFlQyShQRK9sAURcO167TNp2qLif/FRsqcImJhgTcojUH5sepEsL8w'
                'r1SN2CGUPB4X7ku17rSaF3zo3IJCH659YmLvFI1iMFh0yMcI7GaBrcNxE+C6'
                'GYGK3iVRCBaeyCBWd/Y8z4pFCa5mFZssaZvXaT3X935grUJdZgUtu253S25q'
                'ZW9TGsAPnQIvdpR5xK5UFOmsdJY11gmHgqhqSZ+w7n8SkYIOTfQAnONPTMOP'
                'T3KS9lowmpsWqyIE+7vMrqC29OTRMAIrhVf6zGbsFsG8mUkNLBfhRaiOD0Re'
                'Eo/GHo5pOINRP2geEWADdoRlJLNyKercKV6oV8QMywoVUHNsJl7xYIyr2fWM'
                '/THjh9Q0v6TP445R1D2CSECTLB0gbcI2lbBiIeYo6uh36SSqdMUVyBnIv676'
                's5sSxrEvcOsLlYlrThxmIJJzxRUmLO1pzWPT0cBeGN91RL8XkeCmIA+rdsKA'
                'E4i/X/khSoTkvfTJtK4tvOlg4SC7A0R5YPr5/iese2S+79SzbHqfTX/iHJ0m'
                'watNFOOsKki2ZO6e7A2I8zgyfBqYp0iiI94NHPTAvc+bLBOddQdupDvUa3xO'
                'oFsmP87KMTANKx7qGLAtrZ+55T1nOuOL23jymA+x8HR8EFJtN+43Vn+HfOCK'
                '1ymttB9a5l6e5Z3ONeGcOzEHL/BvjBQOrw1mIdUqia647U6sEVyhyhoE1Fny'
                'Q6WY5npdTVdld2MOOqCMoB7StAlAYu9k+pAV6RbKy4Ugu8yvyiSIRzj1Zb3W'
                'fzvhffGEWnvTC0dOHky4efYMhxjknUgnGU4uGhM6bPdOX6qmtx/oyJdZftqF'
                'pEoNQSjQ/qnDQUPNoaC6J9mcpup4DYfVV9KRPo6CEm2ceG4g2GvI6BuEgjtw'
                'h4295o7SabMv5NuVLA4RfLok26YPO2FCgOumhWCiQJ7E01ccp5RIZA9c6qoJ'
                'xLBUn9VvTghuJdxdlX+qEmC6HWb8v9qBaktJNFdijf6CrMTwYN22m7ggX/vr'
                '73mail3fIl95kjvJDFyITJLk4oFLlwzShy7eS6Xuf0wR35xUlFLX7i49+apU'
                'RJQ1fLRIwfBZZ3Q8T34pP34xL7obrNISvv4Ga8JcbbBRzP5isLEcPdnDvGna'
                'Upqow9iUStpWK20l6KjWlW9ZIK3m9OKh237QTTHat74UygbwaGB1BbrXKUBJ'
                'YPqVllhkeVkHNVOzjy0pWJwGtnThU0KTog4OaN31j24CiMNTWARIIb1y9eSu'
                'w/OPHFsi12J0jOLETY0jeUzjNpnwjBZVc1snNaMhiVKn3khnoeqq55yYqK2t'
                'fsGnqg5qXrqpDR9hZgA+wAnnFmF0OspF69ijpQwi8PQJebSUmLmnS3fCuSgM'
                'VIdp7h2iqGcKSFdferZIWmZg0atFuhl38XX6/WhowQ+td0LXW/VmUXZmuXM/'
                'Y8cRze8ozB+3hmoW7dVVaG8U5khgXsw2/Cas7GEt13rtSU/YZoV5iXHdiKU4'
                'tDRYjKkF8VO9cYdjh5240I2JIiagJ4kNqFBIOR/OBwRgakXuobLkLTQgqjPy'
                'HyFim5acJ6Z8a4IjtHx4+V5BJeh5forl7MUDrrBiaHwxGj4ye3ZsWG/uylEj'
                'eW1MHeUaWFDx1vp+kqkO1GlOjRxckB1XA6w2jYyCCUijBz06+XtF3cS0qQPc'
                'KHWY0DYfz1Gq/LwIPkNI6s04CmDI5S8Nbmp1ALKeSLx/OU+1DIxhmt6+tIJY'
                'wWqlA6obiLGOXBvB89R4IQFTaIcI7GrmfpDuqZo4lWMGDWrxvaMcXQQ2TUmX'
                'f5gnMY4EY1hqLKDIox7Yvh0hppuSYUbaLzyqghVSWnW5kwiowGyRrXZbPU9y'
                'p2Tvwxjl4kP7XtJqQB01lIiCSaUl7+tmVx2r+e7pahSzEzLp6MLeJwq+h8B+'
                '9DnHWkjqgOTvQr1Q7NqrSIkqOmjcwf+gDIn4eUTYj80+B4gRIoD2VEntRSle'
                'DvciNnGyw0NwPx+neQp8SoSELI3bObgqmjMUrnSX3m6ng6b82EaBfnFiht1M'
                'ECj89d4xkmeTB6znR9E1avjMnHTNzabPJt0oPiHuBGvcPCcUp2840et+haLE'
                '2UCcnvu2za6qO9dB1mb85RJcs1FcPgxF/zDkZJiPzXAOqJq8N/rWE7H7Cp6q'
                '8RQ37gUALz15kxwXO6mrvqEbPpcq4mZR5pfNi+xx5l3vJUnEsSU35QotaCx9'
                'YrR6mBuYqYGRpt1Dsvp7ly4PubFNWLt09TiHd9QiWGGhTcjwACsB5+CIPcaE'
                'Kh413UeQaLi9ZWGMCPZuW+NmD2NoQ7648rxpfZbbx66eaz7So9iXlNj6qLMz'
                'SXIPDH1TWQzKdE0R/8vAe9RxGaUyG2LU2kMUUzfU0mQCFnfX69PLMJt05QoU'
                'Zfh6W13v1uVWXkrhiYuPrLfZZbn8qDMFRY6ojmOaqDaZdmYN+dYbUnhtWYQp'
                'OI2LbYpgwrZZU4ad3rcDx1dRNCpaH6NxNvH+pJJeTOfoXhlrlIQWeu+ep43v'
                'el4xGIcLCSAqM2A2CItTO14Pb7vxHn9/BmXmiK1ICw1+0bfGxxwf7IHnjUNM'
                'XnHguA/1Wh66m5MYhBpIvO1V3cC+Mjg9TOXluu2qcRFRQtEV/eXrRPT7wc7o'
                '+53SA9mlzY5WSXMWpxZULnGsmErOu5VU3uybaDV+JePdPMO6m7k3YsHzysbw'
                '7YVxXrzC+jd1J4p4pfxDsdKJMBdaW6rzJtj+qFOqEk+F7Zzv41jHi3MiE1gv'
                'JtjIQaGFipfoI4mu1tShVEkJg0TMFKBC4SLgyhzwCjaBPZMuJ6uVcy2ZF2Ga'
                'Cl1nxm2lzoWY+nRv61cvdA2ZAICth5OC8JdRPOJIAnpsvRLHXYGqJWsSjRP9'
                'YTUGSSThg0ffJ8KW9lzKpdYaJ/For2QqSbrQ9ZcHWArx1YwC2J87USUJG7iz'
                'YLr9KwbTjFQdKMPreypnUzVOmSu8w7i8RwMrZqcmE6sbAWAvCKzVMcqtqi+a'
                'MU/XqGEb2ZbNdTVGCynHR0yyZ5Ns+tzbOfjtgmy+Ok4CQxpGCQ9mnfX80EV9'
                'kFbr4HER8QNzpMKwPPBUIbOkh4q8Ayn1JoWGZV3oBdC0mptgIrWpR9QL71zh'
                'MKy+wrISk3xrA0WW0AninqytwtNbHTbU6SxACN5u+ntjTGLH/NuqbPStWbT4'
                'ua1jzuCjSaX8JFXk+a/rrjtlh0jRjCJwSPeHlepJoxVaMutOn3G1Q6NOJCFm'
                'y/P/dIM9jin24GWojRd4sLCjtxjhrj2Jz4CaeDoqsNOarah0BP3Xjh5dRDxc'
                'jqH2ZXUFTnTw4mR+Ioi/h9z5PHcPS6fpElCBi6ttRWr4WEGbZM+Lr1vD46Cp'
                '3ePI5c3wwLDcqsTlFvUzJYqub9Cqo299eb2p09ag9yHfgoqKh85a0LX7CKQ6'
                'a1ZbBbcvXXuD9CR2L82dN/FjI/KLSeejsUARO4nwEUYV3V7W17t21/ns6nQX'
                'Kc+l3TaPqNshL3qHmM2a2ql3b1egqmpy4cZiyTzbnh4mfwuJD/hCgXYziCYI'
                'aqw9Ivdb4RFH7MlK0YS09666BjWn1B6z1227kuF/XSuXpb7kdVcnesBFyB4K'
                'CvnBxHM972IiJe6b/khElsHuQE7aMsxskl3uevgEinFzZa3S1OMWgEhtPFQa'
                'PlJKmMK0E0HjGuaUIE2xK39OD6zbHd3DxS74oILdgzs0Z6FDT2mylR2hF+TZ'
                'oEhOdRzpQARawLxJj7put7zxL4EfkXAyKZ+ycX+Dgk/Bvq2vb3rC2qmSCIja'
                'JGFBJhDK7xHfUL0MNlqKkd6VqrUu9fEgEdXRpQ/hKleuStjE9I2h2stGhzuO'
                'J0ofUsOo33jcZ9xuyU6DZDinVvviwSd7N+fBUFGTvHNYhHtdB57g0eJfR2kA'
                'PnFnOL8dTO7YwTVhsfsaGoTYZQ5QIuLhJXj+YTOhv6v4mqTZTJdqGWPm+gby'
                'UTdotdcW3jqelAAWu9nyQ4hcrxcT/WEmdqrpJIA5OpBa2qpTd1s6ktfTMRKH'
                's9o+NkNbwGIQ3vnpdxeRNkNr5/w7mSro27Az7OgR7P8LeTmky6EcHXXj/++/'
                'eLHABJzJqQR91Wew1+7L/2ZU0V1jrZlyJzvVOmg65FImxGvXaweIpwCmDB+h'
                'dSmRGA8VBDjMKP33Fg8jl9W6vZtonz2QJhiYi4sEEjW4+Wt00gyKRuQDaoUq'
                'JiegjgXUN9qLUxpFPcdlbVkdY8Q5xqh15DikdS2Wr4GEwzReycxhvo09H0+f'
                'nE2fFLmT0QmH/FO1bTMsaF1FhDKuAx7J3Jqk93f2q+HeMHRuX3eyEPr+Ls/P'
                'phfRPvGW+sAupdl8/yCTXYJDkDVBm7DA7d7+37743dnLVz++eLuv9/Pp2ev0'
                'cM0NE3kiKX66vH84Um/O3r7bjxHQI44UJSiQ9WzAZHBdbbsBSRPr4HEHXAXe'
                'AtMnfE6HbDRP6OMisDaRu38YuD2B7C1uJoUjs2j62Dm/RYnlJ3mYOvXQttw0'
                'LjR9aWPcHASsfVkk+TVWz+LrRcyAfliuSFcQc3qL5D2iI47RCV/1dq+mCIyA'
                'Su8jHuMoEMwZC1G0buIgOzXEmqyenVPbiV08F0M5t87JA7DznC3wVA7eudBl'
                '5JAmsgXDbc5qB5lVTBoDtUNUTTRLdGCyJl3TGUhStB7GjPAf5eaYi2qd3SG+'
                'E16zWN4PN20hNtiTrVADTeUnxF9FIqU8VXyONnA25IqZfZ4/yTOI4xZmiYkN'
                'xEMnrabVRcymcA/u5emc+GlP2BqCooNZlFKs9Ddl42rwKCjHh0yw3MzgA2/4'
                'yVywRTo5ppOwMn55dcD87mEM4Yrw0MnydJjMnEQSa4q/d1OIGLOiFCpoVAzJ'
                'DUKBTDh6WSUlwmRgjPv4OJV26hjaGJklLqpNnJjaOnXyElO3tgnYz+e0hA6h'
                'R3OeXJZ0ofnJE4yOLLRiegBXkOeIr04GAZfUWyGPomjHtIyH43zEfLiVkYTG'
                'QjV1QFkiJJlFFYc6jjvhAvo6aJsvsO3pMfIyfdTC2VL6oLu4+BN6GNnYk/u6'
                'kE5ArAWEOwoPMSyte7/AdPlcS4inHX45Pwp/x1ws1USAS87YQC4SGaEfb7UU'
                '1G3yo7xI4LbE9BHJaIa0o0mNpDODpukUscbya3pIXXhp9N6rD1+QJxHXH6z8'
                'RLReRlXTIsxOqzrWKWEdyucLdDJeLHL0XnbeelHKRGbwbgt94h7urCNGqfjc'
                'VnAFO1/X7hv52DSfiLbFNxw/5BVo6A7hccdLMswnsJ/RuIiL4IEHLtbAHiIl'
                'gbteads5DRlbw7Zldq1H9/KmxcScY1CMN9USfReLiDKuPxSKCFUDQ8ispLvf'
                'nkZuQVmztFewt+VmDFMz8Rrvmx76DCYnG6u/oaYq5hx7zF5q/W7zAK7dV8sI'
                'ilxOuQjGwQn3zeRxzQxbjEPM1uG1RPZV9nBCWSaDTlh7QjmCG7NE+Y+RP0J8'
                'fPQA5ZWrU5Pw5xyxk3nfVLdJoNJXn8mrduZUwpEugTIc3GZRg5WjziPbqSKa'
                'OqvoOJxIcJKfflk+7RLlaMiKvegqGerNOZOxck8xUCoGx+Q0iVb5CRsaddFt'
                '7SVpTgCAUEuNr0NArwJliv70mTd9Ol0yBr2gdKDmWXnZfqoeytxsQPH5O1X/'
                'daD2a/4ec7xIqCxR3DKvYMjqnQKxuVdYbLBerDoYr9vmWv2AGDxwSl3NvNJk'
                'sZKtXyqZ7OQw2seLE6+neJ2WWNXRMdZUNvVPh6W7lO2mcvYBkt0WEYFGQi5N'
                'MLjFTzCr9lIMU4mXkqIAFtS9un4lc8txMmTsg8tfjcWYud+COhXEoxZGFP+8'
                'SNFMJnCSKyiB1gMXkwP/r3At7SObpkxIuUijia6Glpxafh8Yl9JTHpl2pZsH'
                'XDG729aQjJ/gp5YXP33xud6/pMxAIYEVD09tY/2umz8zAz10iDEyG1qJcdmJ'
                '4UMPdI2dCspz3I8kuEDh5OSEIxwZkSw49L0BPMDk5Zawq5tlu1UsRJXnMXaI'
                '3yjOI/wcEyJg180s2JdX2X27s6V0OZ0suTyhFETPLr6PAQ2dBSZci4iVTO+r'
                'Go0hmD4MAhCDMJqZHLJfYtrKvyh1aYsG6n43waN8d0pkhTvkDw0q7GMjrS2Z'
                'i9H/BywSRHHvVgEA')
            # @:adhoc_import:@
            import argparse_local as argparse              # @:adhoc:@
        except ImportError:
            printe('error: argparse missing. Try `easy_install argparse`.')
            sys.exit(1)

    parser = argparse.ArgumentParser(add_help=False)
    # parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                    const=sum, default=max,
    #                    help='sum the integers (default: find the max)')
    # |:opt:| add options
    class AdHocAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            list(map(lambda opt: setattr(namespace, opt, False),
                     ('implode', 'explode', 'extract', 'template', 'eide',
                      # |:special:|
                      'compile', 'decompile'
                      # |:special:|
                      )))
            setattr(namespace, option_string[2:], True)
            setattr(namespace, 'adhoc_arg', values)
    # |:special:|
    parser.add_argument(
        '-c', '--compile', nargs=0, action=AdHocAction, default=False,
        help='compile file(s) or standard input into file OUT (default standard output).')
    parser.add_argument(
        '-d', '--decompile', nargs=0, action=AdHocAction, default=False,
        help='decompile file(s) or standard input into DIR (default __adhoc__).')
    parser.add_argument(
        '-o', '--output', action='store', type=str, default=None,
        help='output file/directory for --compile/--decompile.')

    # |:special:|
    parser.add_argument(
        '-q', '--quiet', action='store_const', const=-2,
        dest='debug', default=0, help='suppress warnings')
    parser.add_argument(
        '-v', '--verbose', action='store_const', const=-1,
        dest='debug', default=0, help='verbose test output')
    parser.add_argument(
        '--debug', nargs='?', action='store', type=int, metavar='NUM',
        default = 0, const = 1,
        help='show debug information')
    parser.add_argument(
        '-t', '--test', action='store_true',
        help='run doc tests')
    parser.add_argument(
        '--implode', nargs=0, action=AdHocAction, default=False,
        help='implode script with adhoc')
    parser.add_argument(
        '--explode', nargs='?', action=AdHocAction, type=str, metavar='DIR',
        default=False, const='__adhoc__',
        help='explode script with adhoc in directory DIR'
        ' (default: `__adhoc__`)')
    parser.add_argument(
        '--extract', nargs='?', action=AdHocAction, type=str, metavar='DIR',
        default=False, const = '.',
        help='extract files to directory DIR (default: `.`)')
    parser.add_argument(
        '--template', nargs='?', action=AdHocAction, type=str, metavar='NAME',
        default=False, const = '-',
        help='extract named template to standard output. default NAME is ``-``')
    parser.add_argument(
        '--eide', nargs='?', action=AdHocAction, type=str, metavar='COMM',
        default=False, const = '',
        help='Emacs IDE template list (implies --template list)')
    parser.add_argument(
        '--expected', nargs='?', action=AdHocAction, type=str, metavar='DIR',
        default=False, const = '.',
        help='extract expected output to directory DIR (default: `.`)')
    parser.add_argument(
        '-h', '--help', action='store_true',
        help="display this help message")
    # |:special:|
    parser.add_argument(
        '--documentation', action='store_true',
        help="display module documentation.")
    parser.add_argument(
        '--install', action='store_true',
        help="install adhoc.py script.")
    # |:special:|
    parser.add_argument(
        '--ap-help', action='store_true',
        help="internal help message")
    parser.add_argument(
        'args', nargs='*', metavar='arg',
        #'args', nargs='+', metavar='arg',
        #type=argparse.FileType('r'), default=sys.stdin,
        help='a series of arguments')

    #_parameters = parser.parse_args()
    (_parameters, _pass_opts) = parser.parse_known_args(argv[1:])
    # generate argparse help
    if _parameters.ap_help:
        parser.print_help()
        return 0

    # standard help
    if _parameters.help:
        # |:special:|
        help_msg = __doc__
        help_msg = re.sub(
            '^\\s*[.][.]\\s+_END_OF_HELP:\\s*\n.*(?ms)', '', help_msg)
        sys.stdout.write(adhoc_rst_to_ascii(help_msg).strip() + '\n')
        # |:special:|
        return 0

    _debug = _parameters.debug
    if _debug > 0:
        _verbose = True
        _quiet = False
    elif _debug < 0:
        _verbose = (_debug == -1)
        _quiet = not(_verbose)
        _debug = 0
    _parameters.debug = _debug
    _parameters.verbose = _verbose
    _parameters.quiet = _quiet

    if _debug:
        cmd_line = argv
        sys.stderr.write(sformat(
                "{0}{3:^{1}} {4:<{2}s}: ]{5!s}[\n",
                ((('dbg_comm' in globals()) and (globals()['dbg_comm'])) or ('# ')),
                ((('dbg_twid' in globals()) and (globals()['dbg_twid'])) or (9)),
                ((('dbg_fwid' in globals()) and (globals()['dbg_fwid'])) or (15)),
                ':DBG:', 'cmd_line', cmd_line))

    # at least use `quiet` to suppress the setdefaultencoding warning
    setdefaultencoding(quiet=_quiet or _parameters.test)
    # |:opt:| handle options

    # adhoc: implode/explode/extract
    adhoc_export = (_parameters.explode or _parameters.extract)
    adhoc_op = (_parameters.implode or adhoc_export
                or _parameters.template or _parameters.eide
                # |:special:|
                or _parameters.documentation
                or _parameters.install
                or _parameters.expected
                # |:special:|
                )
    if adhoc_op:
        # |:special:|
        #          compiled   AdHoc RtAdHoc
        # compiled                    v
        # implode     req      req
        # explode     req            req
        # extract     req            req
        # template    req(v)         req
        #
        # uncompiled --- AdHoc ---> implode   --> (compiled)
        # compiled   -- RtAdHoc --> explode   --> __adhoc__
        # compiled   -- RtAdHoc --> extracted --> .
        # compiled   -- RtAdHoc --> template  --> stdout
        # |:special:|
        file_ = __file__
        source = None

        have_adhoc = 'AdHoc' in globals()
        have_rt_adhoc = 'RtAdHoc' in globals()

        # shall adhoc be imported
        if _parameters.implode or not have_rt_adhoc:
            # shall this file be compiled
            adhoc_compile = not (have_rt_adhoc
                                 # |:special:|
                                 or _parameters.documentation
                                 # |:special:|
                                 )
            os_path = os.defpath
            for pv in ('PATH', 'path'):
                try:
                    os_path = os.environ[pv]
                    break
                except KeyError:
                    pass
            os_path = os_path.split(os.pathsep)
            for path_dir in os_path:
                if not path_dir:
                    continue
                if path_dir not in sys.path:
                    sys.path.append(path_dir)
            if not have_adhoc:
                try:
                    import adhoc
                    AdHoc = adhoc.AdHoc
                except ImportError:
                    adhoc_compile = False
                    try:
                        from rt_adhoc import RtAdHoc as Adhoc
                    except ImportError:
                        pass
            # |:special:|
            AdHoc.flat = False
            # |:special:|
        else:
            adhoc_compile = False
            AdHoc = RtAdHoc

        AdHoc.quiet = _quiet
        AdHoc.verbose = _verbose
        AdHoc.debug = _debug
        AdHoc.include_path.append(os.path.dirname(file_))
        AdHoc.extra_templates = [
            # |:special:|
            ('README.txt', 'adhoc_template'),
            ('doc/USE_CASES.txt', 'adhoc_template'),
            ('-adhoc_init', 'adhoc_template'),
            # |:special:|
            ]
        AdHoc.template_process_hooks = {
            # |:special:|
            'doc/index.rst': tpl_hook_doc_index_rst
            # |:special:|
            }

        if _parameters.eide:
            AdHoc.tt_ide = True
            AdHoc.tt_comment = _parameters.adhoc_arg or ''
            AdHoc.tt_prefix = '. (shell-command "'
            AdHoc.tt_suffix = '")'
            _parameters.template = True
            _parameters.adhoc_arg = 'list'

        if adhoc_compile:
            ah = AdHoc()
            source = ah.compileFile(file_)
        else:
            file_, source = AdHoc.std_source_param(file_)

        # implode
        if _parameters.implode:
            # @:adhoc_enable:@
            if not _quiet:
                list(map(sys.stderr.write,
                    ["warning: ", os.path.basename(file_),
                     " already imploded!\n"]))
            # @:adhoc_enable:@
            AdHoc.write_source('-', source)
        # explode
        elif (_parameters.explode
              # |:special:|
              or _parameters.install
              # |:special:|
              ):
            # |:special:|
            if _parameters.install:
                _parameters.adhoc_arg = '__adhoc_install__'
            # |:special:|
            AdHoc.export_dir = _parameters.adhoc_arg
            AdHoc.export(file_, source)
            # |:special:|
            README = get_readme(file_, source, as_template='README.txt', transform=False)
            USE_CASES = get_use_cases(as_template='doc/USE_CASES.txt')
            sv = AdHoc.inc_delimiters()
            AdHoc.export(file_, README)
            AdHoc.export(file_, USE_CASES)
            AdHoc.reset_delimiters(sv)
            # |:special:|
        # extract
        elif _parameters.extract:
            AdHoc.extract_dir = _parameters.adhoc_arg
            AdHoc.extract(file_, source)
            # |:special:|
            # imports, that should be extracted
            for imported in (
                'use_case_000_',
                'use_case_001_templates_',
                'use_case_002_include_',
                'use_case_003_import_',
                'use_case_005_nested_',
                ):
                ximported = ''.join((imported, '.py'))
                ximported = AdHoc.check_xfile(ximported)
                if ximported:
                    simported = AdHoc.get_named_template(imported, file_)
                    AdHoc.write_source(ximported, simported)
            README = get_readme(file_, source, as_template='README.txt', transform=False)
            USE_CASES = get_use_cases(as_template='doc/USE_CASES.txt')
            sv = AdHoc.inc_delimiters()
            AdHoc.extract(file_, README)
            AdHoc.extract(file_, USE_CASES)
            AdHoc.reset_delimiters(sv)
            # |:special:|
        # template
        elif _parameters.template:
            template_name = _parameters.adhoc_arg
            if not template_name:
                template_name = '-'
            if template_name == 'list':
                sys.stdout.write(
                    '\n'.join(AdHoc.template_table(file_, source)) + '\n')
            # |:special:|
            elif template_name == 'README.txt':
                README = get_readme(file_, source, as_template=template_name, transform=False)
                sv = AdHoc.inc_delimiters()
                AdHoc.write_source('-', AdHoc.get_named_template(template_name, file_, README))
                AdHoc.reset_delimiters(sv)
            elif template_name == 'doc/USE_CASES.txt':
                USE_CASES = get_use_cases()
                AdHoc.write_source('-', USE_CASES)
            elif template_name == 'adhoc_init':
                import use_case_000_ as use_case
                use_case.main('script --template'.split())
            # |:special:|
            else:
                template = AdHoc.get_named_template(
                    template_name, file_, source)
                # |:special:|
                try:
                    template = AdHoc.decode_source(template)
                except UnicodeDecodeError:
                    pass
                else:
                    template = AdHoc.section_tag_remove(template, "adhoc_run_time_section")
                # |:special:|
                AdHoc.write_source('-', template)
        # |:special:|
        # expected
        elif _parameters.expected:
            AdHoc.extract_dir = _parameters.adhoc_arg
            AdHoc.extract_templates(file_, source, AdHoc.section_tag('adhoc_expected'))
        # documentation
        elif _parameters.documentation:
            sys.stdout.write(get_readme(file_, source))
        # install
        if _parameters.install:
            here = os.path.abspath(os.getcwd())
            os.chdir(AdHoc.export_dir)
            os.system(''.join((sys.executable, " setup.py install")))
            os.chdir(here)
            import shutil
            shutil.rmtree(AdHoc.export_dir, True)
        # |:special:|

        # restore for subsequent calls to main
        if not have_adhoc:
            del(AdHoc)
        return 0

    # run doc tests
    if _parameters.test:
        import doctest
        doctest.testmod(verbose = _verbose)
        return 0

    # |:opt:| handle options
    run(_parameters, _pass_opts)

if __name__ == "__main__":
    #sys.argv.insert(1, '--debug') # |:debug:|
    result = main(sys.argv)
    sys.exit(result)

    # |:here:|

# @:adhoc_uncomment:@
# @:adhoc_template:@ -test
# Test template.
# @:adhoc_template:@
# @:adhoc_uncomment:@

if False:
    pass
    # @:adhoc_verbatim:@ # docutils.conf
    # @:adhoc_remove:@
    # @:adhoc_uncomment:@
    # @:adhoc_indent:@ -4
    # @:adhoc_template_v:@ docutils.conf
    # [html4css1 writer]
    # stylesheet: README.css
    # embed-stylesheet: yes
    # language_code: en
    # @:adhoc_template_v:@
    # @:adhoc_indent:@
    # @:adhoc_uncomment:@
    # @:adhoc_remove:@

    # |:info:| The following list is kept in sync with MANIFEST.in.
    # This makes it easier to avoid discrepancies between installation
    # from source distribution vs. installation from compiled script.

    # @:adhoc_include:@ MANIFEST.in
    # @:adhoc_unpack:@ !MANIFEST.in
    RtAdHoc.unpack_(None, file_='MANIFEST.in',
        mtime='2012-10-26T17:21:09', mode=int("100666", 8),
        zipped=True, flat=None, source64=
        'H4sIALIkMGIC/3WSy07DMBBF93xF1khxSys+oBJBYlEWwN4a7Ek6wi95JlXg60lKSZNW'
        '2XhxzrWvNTYF41qLxX73+vJcvX8oCsUd/UP4wpocjuCt2j3tK2WYr5F0MiKwh2hU+r6A'
        '3CTIjNpFA25qbDSrm5YBahYQMqvTWaWLTSy3G0UmzlIXq/jYzJSJob5uomCxU5llRn3f'
        'rz5hDn9KD8zQYPm3iQ9T3Qo5VkPFSAN45AQGtSUj02ZGadMMSKbQ1DF7kNuRtP2cDPTL'
        'er3WC+JBC/rkQJCXIht9hkuBrSafYpYl/6gDsqA9+YymzUzHYRyTR+6vwVLczxPYnedE'
        'vRv/wi8ZvSj5aQIAAA==')
    # @:adhoc_unpack:@
    # @:adhoc_include:@ Makefile
    # @:adhoc_unpack:@ !Makefile
    RtAdHoc.unpack_(None, file_='Makefile',
        mtime='2012-10-17T13:01:02', mode=int("100666", 8),
        zipped=True, flat=None, source64=
        'H4sIALIkMGIC/6VWbW/aSBD+zP6KOUqL3atNXhSdZI4KmjjXqCUgIFIjneTbrBew8Ju8'
        '615a5cff7BqDwSRFOT6sdmeenZl95gW/Aeu9BRFd8XkQcnUgRCapJzLmBxn0wCaV7UMQ'
        'F9tOLrJOmDAadlBGyPh+9nl0601Hd5NLdwq9fcHvPaD+MmF2+oOQwdXn0aU3vveu3LFW'
        'DUv3E3dwNXRtJgT4CctlEAqbJfEcBJd5qi7X7iKuoyCo1Hv1FPuBSn0oDR++piOywmSR'
        '2OL7Qos8IakMqirr/MwOWFK3IGQWxIt5kkVUepqKg/HRbJHSTPAXIDGNuEgp454fMHkQ'
        '0jLupq53OcBl9m2mxSYhNZmC5uiLUVxOTk48ZexXqFNP8igNqeTiKPyZF8QszH1+FPrc'
        'C6I0yeRR4Asv5kJyX4OJ+202GXhXN9MZFhS5/OoObq9vvuryqhw0O+tyG09Gf00GQ+Rm'
        'FzAc3N5cu9PZnvg9umF7sip9KopntRXaXsRt6HoRVdL0Iqik5wCIYbh6PdXrmV7P9Xqx'
        'h9W17bElZysvSvw85F7RXvxYoNw0fEk4qCSkVIr8QUh4+8EPhOy8/bBJzHoOmFi0Kp9l'
        'Grf7yhTYldZMPKPepn5Pv60idF7Ehfw5oNbtUGpoTXkEy2JJlKqR1PoTPrb6pMGWSAH8'
        'cXEBeCI+n9M8lA7QMCQEFwc9bRybSmzphtfKYuuU400+ynK7lFGoBw8OVv5oZ6KYW2Wf'
        'TBWWEBZyGjukgaUmwfoJ7ZaxzZTZhqcnyCKwsjnsKAgJYpxnW/8q2Ea0UiPcShFbjHOT'
        'NPpGQ//+Jo0Qeei167S2u1C6b7ZaCtVEv+oGjkBIs2QBQQyFpouPWJsD4GyZQJOl2mVL'
        'Azeem9016LC6W9jwk5h3NwFun+XAzvtgLtMiww7+h9GFsDKGpC147KmTLZaY1rJnNaCm'
        'xacwXtqoMNVfV05ZH86mcDDYnWFtVq6pK6SR/pDLJIZnS0tlz1Dpw+z1u8AfAwmn5n7B'
        '4dvKAvgNrH+hI7LvHRR20vxB5UFTY2A0w8EX14SCwN4OapcspLFSg4dqE/+FSQMr8kwB'
        '1pGHCV1ZPKJBaFHfz7gQXOh36CC3NpxKZ9UJKJPQw9d/1ORWO+AVd3f6ZSc5B/42jzFq'
        'j7H47x3VjMrBunUMYL4Swbt3G6YVOWYRxbMfD5g5o37zWTiaewNPzpJn3HnCrRP43Ip4'
        'nDvgRpQJuLlycVpiuw1RCBZ8yudznkH/0931tTvp4xUbhtYj/MMRqW+2wTCNzQmaP5va'
        'ibLswOVoOMaB4YBqBH3ZCLkEw8BvFwFNJW2aJhhl3eImZviF1VTfWmCtoKm+coRpHrKp'
        'm6BmU0lfb3NdyXWza8XrLasRUrOKwv/xfqyg+vMT9nqL+t+gblOLX291Kmns08yvGz7W'
        '5n/r1+bDSwwAAA==')
    # @:adhoc_unpack:@
    # @:adhoc_include:@ README.css
    # @:adhoc_unpack:@ !README.css
    RtAdHoc.unpack_(None, file_='README.css',
        mtime='2012-10-10T17:38:17', mode=int("100666", 8),
        zipped=True, flat=None, source64=
        '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')
    # @:adhoc_unpack:@
    #                   README.txt is generated
    #                   adhoc.py is this file
    #                   argparse_local.py is imported
    # @:adhoc_include:@ doc/Makefile
    # @:adhoc_unpack:@ !doc/Makefile
    RtAdHoc.unpack_(None, file_='doc/Makefile',
        mtime='2012-10-20T15:35:57', mode=int("100666", 8),
        zipped=True, flat=None, source64=
        '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'
        'ORHh1PkHUfjTfNMaAAA=')
    # @:adhoc_unpack:@
    # @:adhoc_include:@ doc/_static/adhoc-logo-32.ico
    # @:adhoc_unpack:@ !doc/_static/adhoc-logo-32.ico
    RtAdHoc.unpack_(None, file_='doc/_static/adhoc-logo-32.ico',
        mtime='2012-10-17T12:52:15', mode=int("100666", 8),
        zipped=True, flat=None, source64=
        'H4sIALIkMGIC/62Xe0hbVxzHT5IlsYZpqy4T3HzNYlbrY7Pq3GRJzWNqNiubcyn+k4HQ'
        'gZgOK8xlLSulo9tEqLRULJN2MKxVR0IowXQgPrrB2DRjJeBIMbGdpMQmMcYketX727lx'
        'KdKa5t6bnvBNbm7u/X3O/Z2T3wMhDn7l5iLqHQ3vR0iMEJJg4VNIhnbORwb+LU20o+gA'
        'AFoKh8MHLBaLtru7+3p9ff3vEonkYV5eHuTn5/vKysrut7S0/Nbb29tjs9mUJEkm07Ub'
        'Tw6Ho1qn0xkyMjLWqenGE4fDgaqqKvvo6GgXnsd+ttxQKJSJn/WmUCgEOty9VFNTY5+f'
        'n5die1wmbLvdLi0uLvaw5VI+4HK5kc+UlJQNg8FwBtvl02HPzc1pxWLxOlMmj8uD5vxm'
        'MNYYwVnnBK/KCy65C6bfmoZzknMw9fNUdzw/4OdWYPY2U3ZachqY3jWBV+GNKZfKRYYs'
        'oT7M2bcXOxgMvlJSUrLMlC14QQC3Zbefyd6t8Fj4BuYJnuTr9fobbNb6ROEJ2uyI8LoQ'
        'vxKf72b7/f5ckUhEsNlns4pZZnws34c+glwlC6N8k8nUxubZj2QeYcyOKvRj6If/+fz+'
        'y/3fs+H3vdnHmr+iWfHDFqQCCfuufXxtiSk768UsWFIuseZT2rRtfrT516bWprQBj8dj'
        'xL9adTUhduS/MBLuCfWHblLHxwuO02Y3v9YMXqU3YX6wN3hrtXN1njp2KBxwOONwXHZd'
        'Th0VSxJmUwqcDkzifbAe/U7NQVOgicTuJ7kioQj0xXpwq9xx7U4dnYLOok5Q56gj0kl0'
        'YJFanvJZ4KvAL75jvqfun5PPwfmS89Be3A66Ih1cqbgCDpUjLvee4h405TdF4kIs39kV'
        '9sfXr32zdsev9Xuehy9tchscPHAw7vodSj8ETqVzJwb0h0yBM4E/EmW7lC4ofamU9v7V'
        'Fmoj9xEzRCeOQ5cT5Z8qOsUsZ/EF4GxyEmSQzNz6Z+uTRNh35XchiZ/EOHaavzMbIrmY'
        'hGR/m/8hW/7J10+yqpGMRmN7NP+s31r/lg17+b1lyEzJZMW3Wq2qxzmYgCz/p8x9MPbO'
        'GCs2rts929vbwt01AN4Hx3zv+zZo83EsUbyqYMUfGho6vUcNxiX+JNo8H3gIOvxL1Zdi'
        'xplnSaPRWHFfkBSjBuU/mH3QYpaZN2Lll0eqR3Ch/ALjfEmpoqJieW1trSBeDW42mz+T'
        '5cjgYvlFmDk6A1aZFSalk9DzRg+UiktZ+byysnIZjxK6Pcj4+Hhbenp6mG0PsrtGbG1t'
        'ncX1dS7THmxxcbFarVb/zZadnZ3tGRkZOYvXW5BAD8qfmJhoxfOwCQQCMh6Tyt3l5eX/'
        'DgwMfI175pefVx+MJXS73UXDw8NfdHV1/dTY2HhHLpc7amtr7zc0NEx3dHQYBwcHv1xY'
        'WHgbX8ujbXcSX4rnvYWQFDd9OSsIpToREk4ixKN0FiEOJcRscKL3Re1QNrH9VMzJwU6U'
        'UkyK/R87YiMjvhAAAA==')
    # @:adhoc_unpack:@
    # @:adhoc_include:@ doc/adhoc-logo.svg
    # @:adhoc_unpack:@ !doc/adhoc-logo.svg
    RtAdHoc.unpack_(None, file_='doc/adhoc-logo.svg',
        mtime='2012-10-17T12:44:09', mode=int("100666", 8),
        zipped=True, flat=None, source64=
        'H4sIALIkMGIC/+2cW3MbWXKt3/tX1OG8TMcBwH2/sCX5oSccMRGeF9snzjNFQhLcJMEA'
        'oZbUv97fyg2QFAXqNlK3w9Ht8IioKlTt2jtz5VqZufHkX95eXky/Ljc3q/XV0yO/cEfT'
        '8upsfb66evn06P/957/O29F0sz29Oj+9WF8tnx5drY/+5dkPT/7PfD79vFmebpfn05vV'
        '9tX096tfbs5Or5fTX19tt9cnx8dv3rxZrHYHF+vNy+Mfp/n82Q8/PLn59eUP0zTx3Kub'
        'k/Ozp0e7L1y/3lzYhednx8uL5eXyantz7Bf++Oju8rO7y8/09NWvy7P15eX66sa+eXXz'
        'l3sXb85f3F6t0byJdpHvvR+7cBzCnCvmN++utqdv5+9/lTEe+mpwzh1z7u7Kz7vq5O0F'
        'U/HoYOzs/acz/df8/+0X9gcWN+vXm7PlC765XFwtt8d/+8+/3Z6cu8X59vzebfaz/95z'
        '31uSq9PL5c316dny5nh/3L7/ZnW+ffX0KCRnH18tVy9fbe8+r86fHvF+wT7csx0/zu7u'
        'dHJ7xi1SW8SFnza9tWIX7Qd9cr4+0yieHp2ev1qfzS/WL9fzX8OcKVxoCp9x8ZPz5Ysb'
        'fWk8WZ/S0XRsp27vo5uc/7pavrm78PnpzXidabo+fYmhXKw3T4/+8sL+2514vt6cLzf7'
        'U8X+e+/UmulZbd8N19jde/+Cuuvt+YNnb16dnq/fMHMPT/62Xl8+PYqLHHP54OTZ26dH'
        'JSxKCzH6D05qLL4vcqi1PTzJbL6W48xfX622GOf12w++/nqz0QUXp++WvLL9s3/jm1fr'
        'Ny83mrrt5vXy/sHXq/PlzXuHb29o5+bPn6/fHj5/c3V6PX95sX5+evGRC67Wjz5g3IBh'
        'cf7F6cXN4Qu26/l+lAcvWj//r+XZdn59un312CVvVlcs1nxn/L778sgVe3/wzrdHLnl7'
        'wCB2p949fury9O3qcvXbkhXYr/uL1ZbDm5erK17x+u6r945fLF9sD57YjGEeOPN8vd3K'
        'AN29RR72/tgcc8F9gx4XPbOrntzZAqs0vjhN23dCnrfvdOxof1C2pQOht3x7cHl5LRCy'
        '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'
        'hvZEP+z87If/BprdwG+aZwAA')
    # @:adhoc_unpack:@
    # @:adhoc_include:@ doc/conf.py
    # @:adhoc_unpack:@ !doc/conf.py
    RtAdHoc.unpack_(None, file_='doc/conf.py',
        mtime='2013-08-24T12:03:38', mode=int("100666", 8),
        zipped=True, flat=None, source64=
        'H4sIALIkMGIC/7VabW8bxxH+TvRHLCQERwbk2ZKDIGDjILZjxwbsOIiUJoFhMMvjktzq'
        'eHu53ZPEVP3vfWZmb3nUS6oqadHW5HF3ZuftmWfndKgmn05U4Ra2Wk1VG5aTL+jJ4HBw'
        'qHK1cEW7MVXQwbpKzVtbLrC2WtpV28izpS3NWBWN0cEs1HyLbb5e2+py8ltrizMfdBMU'
        '1p3ooE5MrdQX6ujz6WefTY8fq+PHR8c5azpdW8+iFP41l6agz8PRQl3YsFZhbVTRNg0O'
        'oha2MUVwzVZ5E1RwygZPRwraVjCBfheR37lgsBNqKxeULktVO+/tHDr2LTjXZWu80o1R'
        'dWM8KbEVdloPKboNbmUq07B5dCqR/gzybhWz1udGabUwS92W4e/dYz4IqSjchhwKYa4N'
        '5CzTYAPs8Gt3wZbGrflgYDe1g/f81o+V8wOsfrOEd4KpPDR6NXSN2rhFW5ICl4IlTqOT'
        '48mItcIgDTesTbNz4JjMWyxIpzfpsRVZ0JnXGmKwxeSkl4+WnI8wNaaE5XJ4/Ahp+9nS'
        'OBfGqoVsJ7JyPfcsExs2+gyngkvm3pVtQAqVFk/ICZXoHBx2Z8htBS+F4ePxdUnDLM9G'
        'o8HgXivzR/hvaeeP6m1Yu4o23m8fqzhUk4n6ljPheuQnD/lPjObWtc01v1XGLJCOaoOE'
        '3kDZCZeTOjcNRX2sUFKBfRfdxOtnUnTqqcqO8scZSX+G2Opq2+1PeRNTRlV6Q/kKIWOl'
        'PcQ2qB+foxbNVhUa5W56yQaBSF2qMM6uKHRIQhYqE+05luefZiOFvGTDitYHt0H5G58P'
        'eon7VH3ob4mpmo33BJ1bcwFcMtnHvjUUlFhOsepVMJsaqZiM2U9MZGpK23yQ1s44E+kg'
        's/RMNMF+5dvl0l4qt1QedhSGK58dlg/kySwugcPzxoes22kqwdJrez3ls2xMK7CV8Xbi'
        '7Srt32gfUKXBFaExJqVGPpAfZnhAG221MJe8qctJWy1ds5EU0nOAC1ds3bh/wvZ8ED9g'
        'b5s9W7yGtweFq7eNXa3lIcD4aMyQPFY/uXK50jjiSUEubdLpYhKyMgV9fR0U8qzZHRkm'
        'IrEKwLMmsICLC8PwhH0QdxVlXSGsC3WFoBntzRW2lN4RbCwItc51Y13rlWAXy6DoN65d'
        'raONkEWNKSTFvuspjCcA0J/zX7qT56R5Gr9MrwadQXDp4/xJfpzFjcsWAJ9KzlZF2XLM'
        'dFmv9aO5CfpRU6igUTCDePSejCikhAtbvTLsKcpWsn6/o8y7+szVD2bJgd+HA4ii3Rr4'
        '6AMnVVtTV8DeTjzZm1Q9ReOrTDwBokHoHy6ccnXg0iNhEgwy5wqFp7dXU2UsOXhMMYyN'
        'Fc+5EbgNebhy1WSJyBhpaGNyfEUghPKiWE0Hh7IFTiAfvsTSsUiZLTdpGaUCpYykarQM'
        'yLMMdoPeiC6dR0G8C8I+ea4+WYzVJ7+wV99GJ6B4UQyV3y/2WG+7Dic4AU3FWqqQco0a'
        '1X6zs6vKwU0XZFLp3Bl5ho62X7/mkpLAzDrdAh7MiXbA0ZiT066DowMCZodst9QKvLDR'
        'zVlbT9WvARj364jUU4tkTyDl+jkcxcxYzC6u1IsbCkE2HGVAY+wCUuu6NsCEBQmcLtuq'
        'QExDkYOZgfVMGsotAA/cRNA6OETjn9EqSgpYRNSKaAAZdQrhe3r69KvXO5JqsKadbjbC'
        '+KKxdUzftkKaBBvI/UPfIhRIgjxXnfrpdBQPJMJn0phuOYg3vAEVtCZ3ATZkR3wgUUUu'
        '+HQ04RNM5yiLgRh1G2KLY17EkecyTLTrkDbNRCYd4xWlfRdfNtwJG/p+u+JQwaotqvVS'
        'rQGmJQEqEmiEtN6WJsYX+BsXz+Tx067VSatO1d0dCD5FdzFSr9HpjPlIyobk45wbaiN4'
        'NCNOSWHkPZSWHyNfed8r+ten795GB6gH8hVyAAzfmH7WslyKBX94bcoa1UmgpMD3jdDG'
        'PX4j8L8DNAZvCRH313XYlDNRAy/FsHSYSt6PRjGy0ZOJr01hl7bgYwjnsL+Laipnfrw0'
        'piRtWvYQrLYNYR7O+WoPYJP8c21LTfcFMtPoYi1bKQ/NbYy3f/RZJ+Wp+ldWuLLUNd89'
        'vF2YuW6yKWf3v/8Ls4n8STxzD3Zz2DtAx28+7qVuwiECeRgbedwOdhSVG0HNmNA9ep9Q'
        'ElIOvoyt/it1/mXsel/t++AgHYIKvodaz6QXU4fjXzryUOlzu4rXS03B+CaCp5VO4enU'
        'AIyd0E4Dy7uhp1+k4LBg0CtBcDW823MMw0wulBbeFFxNeCGFHoPWKS7dyt1PI1FlyWxm'
        '7chQikoCfZi1hPmIdtQkGUVB2F2IYWaLWzdBvPoJ9e4uvOItoiLH5xF+pZ519Pnl0edE'
        'vp8cXz45hrAaEFJ6EIVmZWJ2dgpRWnqxdsWErJk8OSY52f3SMZoiDTUhuuCaXxsT/Ehy'
        'FdL+IFt3KAwiaokbLDk94KwOEvqaSBqIoRa75d5x0IF24f2BgL4DabtobDB7gvYWRk+I'
        '8N49QB5IL0cR0Nggw51Eq+wtuLdq6wVTNnSsTBFfwfpNTXkqt0eyICgD/VtGQDV3Ae6i'
        'c7eewkMHWsEX1Y7xCA9KiQU1s6gm8Z95n/+kVngCHhG232tqP12zY6IBPyNcOERQv7Uu'
        'COVRC43AxCoO29qtGo3CJ76Fq55rKCSKKHuwzCb5NBA386ymZjW7hvwi5oGUxe7+NQa7'
        'qf1uDiGNnCIfV6h4hYoFLPsZIzsktNzgy96djjNwVwQNMY1GDOU+E5WyxzuFZOWtKnXS'
        'MOPNSTUcy/R2jLDv91vEN9H1TszCbVAPMyywxXWqshNz935yrfx6B91KW31dEsmuAouz'
        '53bRwjty9tSWSkOMNLmVtiTxib0k+aWtznwc2ghfFZ4rHRUeEufyzS7eLjq8vZjJUhJx'
        '29EPXsQ5oCS8NJcDtqNHxIQpLJ2jQ/fxnuTta+uGGjc1DV+M1It0gc3z/E+o6V+Eb2gC'
        'pL8HvT0xuoGre9RWgKgrPmFWY642HjZyiOhXnpwIgGr1JbnuK7o4KubkDQMDTTEZ9OP1'
        'StoBjiosQm1QcKQk3nbpsvnjD7CtQRVeoI5lRLq0lUWZRybGPb453086B0u8WMIXtW70'
        'GpttgtZuAJIIXgR7k69ydZBfksCDUSeZftzNQ7q++F64JsvkIycCwhLXxBT59kSpS3Lo'
        'yYxW8kLifjSluMlk3+pT8/PDqexgQLhwOQN/EfoODIhtvNY1OpAn8jjMpKr4UUZNNdOf'
        'yReyO+OPtBJUbm/puOMESwS9k3X0uA403jo6wr8s7OgYn0SSQ3l3kmThNTD0Ab5NjEnM'
        'B9nXmzmzoaz7TAKwmQHt28a1ddd1EiLzTInRRKTI1TZdq0Nb4zt2D+PVV8b3MuMPxCIE'
        '1MdC4sZKbknjpKBAC/PqA4oquEcbXQGsPsJIcXgimdRuBwpukSkW/JIH/rfNUKh9Oglr'
        'lKKJFeuhlSI0G40HH/9augcJ1DboC1NKKmAerNDRr1E+ujAcyEkOdtwZjDmWLZVTk6Yk'
        'EF6CFpRIeU1DpPiuAZ5lUkM8o1jrGhnkk0IqVl5xK4TzuwLueOli7yN9QnBNQ0nDMJ/k'
        'Mc7RDmz4A5mEKugAjfE+SaS57V0S26bck/ZNCjGNAngkQdwQkZEvAIg4IxDv7cTF36Wd'
        'fvj4P/XkLr3uaMrX4EM0i/seACIMbRUNegMRPbMn8J6lJDXU6yVdJTGbYWlx1jGiwW+V'
        'yAqVzV7h3F00Sn1IdfNxrI5Gg48PjDcd4NZoX3PsqbnkufADkfk+qNWp+ItwCzsIFRS0'
        'tBLQa1EpkFkrQoxBEM1/BGL3AzD6H+UPvGv26ASNNeO0XnZl76wH1yp1ZVzrE+Q9pMa6'
        '0/+ZKtt54I46e00vMB0cCgaqt/u5hc5ETAxYZ8gBlcP/Uxu0Ffkh64nvZ9puzy3p9rJu'
        '539yoPXczkvbXYbUNy2+VWCV/MJ06fKBgYo0YUBsM3kS541Pd3GV5zUJ8PSi4sZPN961'
        'HI9Vt+D624I4deBJrXqzN4SRmVZa2I1Y6SJQSffp/Yz4UW/xhi6YfIreW4Is6fWFjNVk'
        'N+5kuAcuLXHm021Nd8S4QtrWm5Pn35E+RLeTGgX0ZbaV/a3tC9s3ijlnfMWoRWTVbuam'
        'EVv6L5XWbmNiK2ZlPZGdwmfX1RVp0LjTGbe3dtHbx7jR/+sBHnXTCCEyCR4o8nduF8RS'
        'dzfL3jvBwxjkcz7WkN8X93jztTtsmhfMzdLJFDPeF3Z/RxH/iiJPZJJfmFjfG1QK6l0/'
        'Ps8z6NzdsExSszEzOUtX973j+TuOtxvI/L9P53y4drzdSPymCymr6b2DLs74LWGsCxLV'
        '/YkGi+3e2OxLPuW/sahxji4neciLL/EVnecLpCvyqrjsROGr7Hmqngzk7z+AdgvYSNlG'
        'BLLgBmJ32UBb2rqHj1dTmopNr/BxilSdUNeZqpcbXXj15puX6h1dEd9RK5qo52D88P3X'
        'z3989erlD1/zH+O8m1yqXw1W8s4MaTZM39TB7wecdSR5ql68f/f9m7cvp/yGkjcPcUdR'
        'wyF6oVcH9PRgNFLDwm1qJsswHXYQqT0zanKmDhStHI1ukwmADzdl0tOHy0TOBc135Wti'
        '4w8Pl1yURlc35fLjh0slJLgpVK7F95N5+Dd6n+kIX/+hG0s56Kd4hBYMRbSe0paGnpWt'
        'J/tPJyv6RNeVpiX5ZkJdFE2W4vKyWkwH/wFpPLyL1yUAAA==')
    # @:adhoc_unpack:@
    #                   doc/index.rst is generated
    # @:adhoc_include:@ doc/make.bat
    # @:adhoc_unpack:@ !doc/make.bat
    RtAdHoc.unpack_(None, file_='doc/make.bat',
        mtime='2012-09-18T15:26:21', mode=int("100777", 8),
        zipped=True, flat=None, source64=
        'H4sIALIkMGIC/7VXbU8bORD+TH7FKFKk9gSJkO7DiTanawsITimJINX1QwV1didZN7v2'
        'snZ46a+/8ctmX27jQ0CRIMF+ZuYZe/x4/NfJp7MpTE9Pe73Lk8/wSWYZEzEseYqwlAVc'
        '5QkXDxDLaJOh0ExzKXo9voT+4Gp2dn7x9eOX88nxoA/jMfT78Ka3p1BDbWqsrIeDxYan'
        'ce9tz0zbiePzy/GNGzVjHyYTZzWdza/GBzEMStRgRNF1gahgUEEGMLR254d/XNQMWwgi'
        'ejGdE9nZh9nJZZtmK+YxpEzjw03OcixuFP+JY28HgwZ04MxboYP2TeyAFsIt4mFJaSW1'
        'hATTvDlhRizfIzu3h1Eih7MUmULY0O/3jK0Rrt9rVqxQX//5He4TLOojwBVIgSCX3hog'
        '0VkK7oeCWg9K07az1ADP5p8ntgDU1iDmRWlTGlQoECzDGLiI8WFoYVwYC4y0LHjNi+Ji'
        'laJFlF6YH6SVI7aV061NzqM1Tdcj+6Emwx9KilZKf19NL1ooE9usY3cepvCZG7CgvJA/'
        'KImt9a32tgFrj2mbxnhX2u40PfaYti3mm0UrNSbs6BZi664JmbA5fnX+9+FRbiAiI1O1'
        'tiLH7Heg0+2+p6g1Fltn5Eq34tmh5lKSTEALRUMblkLOVjUcmXKxlHXc3A81Ha4MCxe5'
        'BM6mkKFS5I/Ya6rOVQWPEiYoTmtV5B0Wdxzv7Rdgaepx8YjFMf2NMae6pNWietWYVe5S'
        'LtZRgtHaunPfjDkxwkJQVgagrCRyoXFVcP1Y7S7pE6qSerER1tSPKsBsgSa6ORdUHk0x'
        'BTrtKNgixbi3Z0UARdyWh4gOvLAyYAiMSBwH3Hh7U4nkt9/ekmMoMjp5MLqFkTKg3l6M'
        'aflvDbs7lDkiNlJD3+Fg4VSjJYR1lTbzvT2TTlHIIsU7inxIC8g1jBZw6FfLf3w0wk8V'
        'ILhKMB7CPPEnwlYPMJIwyq/lfbibtleobualfAXIe8iv4+8DBFKo5LE7i5p8BhKpUL8u'
        'lypGIB0n092peAkPpOEQz0zhHQh5vxU90tOIVMQevfrdEeBubpNu5vaeCfA286/OurrJ'
        'huGDu+0WOg+vvV3+5wC7LuMV+BsVtEV0ZqL+I4u1SmQO91wnNqfr3jBJtpedazj/e+IN'
        'nUDO7rbtztjfxIF8HeLVsu3fRjJNKRlS9RUKLBj1P/1GxrdJFEzZMdqny8ZcuglXRz42'
        'tXFd3uua7my/2Rjeai7BXoYmul0ME7LmkinFTeOn4aByfmpodfhdJVFAfl3vskN+fWMT'
        'kl8Hea5k7SZm2qRuVratClByDdYLJNQGcJusWvtspgKkbTvXzdp1egHaFvDsmjaVUusc'
        'O7Tf+g9wNz1cN3Xb3QWYm/kXLXjVpXbwNpMB2hnbIfimzw2QpukXca73zB2saTq81qaR'
        '3rnctssOr7iBvCiBRjPfve5mPpCFb/y7syhfBe0HdKMkZcSe3Sv4bWg9M7oK30YJ5OFf'
        'JN15lM+VwG54yJPzMLy3751unfEuQ1JTvnt2yM32WRSSnBL0ZOoTsvCPrEhmOT1A8R2k'
        'Uq7tA4uJR+dFlS8mtqBEQW50vtF0j9pHWCeDkcMMdfCw+5fZjtvKP+ZCt5WDPH2nCEwt'
        'M8hl9Sj0mSm5KajP25bjvlsGpn3LUKDapLq9r97L7myPzOe/zV7QttwTAAA=')
    # @:adhoc_unpack:@
    # @:adhoc_include:@ doc/z-massage-index.sh
    # @:adhoc_unpack:@ !doc/z-massage-index.sh
    RtAdHoc.unpack_(None, file_='doc/z-massage-index.sh',
        mtime='2013-07-10T13:24:06', mode=int("100666", 8),
        zipped=True, flat=None, source64=
        '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'
        'e7N8EQAA')
    # @:adhoc_unpack:@
    #                   docutils.conf is included above
    #                   namespace_dict.py is imported
    # @:adhoc_include:@ setup.py
    # @:adhoc_unpack:@ !setup.py
    RtAdHoc.unpack_(None, file_='setup.py',
        mtime='2013-08-24T11:47:21', mode=int("100666", 8),
        zipped=True, flat=None, source64=
        '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'
        'Oi/0euz+qev++XuiSt+z6t38D7p16b9oDwAA')
    # @:adhoc_unpack:@
    #                   stringformat_local.py is imported
    #                   use_case_00?_* is imported
    #                   adhoc_test is imported
    #                   dist/adhoc.py is generated

    # |:here:|

# (progn (forward-line 1) (snip-insert-mode "py.t.ide" t) (insert "\n"))
#
# :ide-menu: Emacs IDE Main Menu - Buffer @BUFFER@
# . M-x `eIDE-menu' (eIDE-menu "z")

# :ide: CSCOPE ON
# . (cscope-minor-mode)

# :ide: CSCOPE OFF
# . (cscope-minor-mode (quote ( nil )))

# :ide: TAGS: forced update
# . (compile (concat "cd /home/ws/project/ws-rfid && make -k FORCED=1 tags"))

# :ide: TAGS: update
# . (compile (concat "cd /home/ws/project/ws-rfid && make -k tags"))

# :ide: +-#+
# . Utilities ()

# :ide: TOC: Generate TOC with py-toc.py
# . (progn (save-buffer) (compile (concat "py-toc.py ./" (file-name-nondirectory (buffer-file-name)) " ")))

# :ide: CMD: Fold region with line continuation
# . (shell-command-on-region (region-beginning) (region-end) "fold --spaces -width 79 | sed 's, $,,;1!s,^, ,;$!s,$,\\\\,'" nil nil nil t)

# :ide: CMD: Fold region and replace with line continuation
# . (shell-command-on-region (region-beginning) (region-end) "fold --spaces --width 79 | sed 's, $,,;1!s,^, ,;$!s,$,\\\\,'" t nil nil t)

# :ide: +-#+
# . Fold ()

# :ide: CMD: Remove 8 spaces and add `>>> ' to region
# . (shell-command-on-region (region-beginning) (region-end) "sed 's,^        ,,;/^[ ]*##/d;/^[ ]*#/{;s,^ *# *,,p;d;};/^[ ]*$/!s,^,>>> ,'" nil nil nil t)

# :ide: CMD: Remove 4 spaces and add `>>> ' to region
# . (shell-command-on-region (region-beginning) (region-end) "sed 's,^    ,,;/^[ ]*##/d;/^[ ]*#/{;s,^ *# *,,p;d;};/^[ ]*$/!s,^,>>> ,'" nil nil nil t)

# :ide: +-#+
# . Doctest ()

# :ide: LINT: Check 80 column width ignoring IDE Menus
# . (let ((args " | /srv/ftp/pub/check-80-col.sh -")) (compile (concat "sed 's,^\\(\\|. \\|.. \\|... \\)\\(:ide\\|[.] \\).*,,;s,^ *. (progn (forward-line.*,,' " (buffer-file-name) " " args " | sed 's,^-," (buffer-file-name) ",'")))

# :ide: LINT: Check 80 column width
# . (let ((args "")) (compile (concat "/srv/ftp/pub/check-80-col.sh " (buffer-file-name) " " args)))

# :ide: +-#+
# . Lint Tools ()

# :ide: DELIM:     |: SYM :|         |:tag:|                standard symbol-tag!
# . (symbol-tag-normalize-delimiter (cons (cons nil "|:") (cons ":|" nil)) t)

# :ide: DELIM:     :: SYM ::         ::fillme::             future standard fill-me tag
# . (symbol-tag-normalize-delimiter (cons (cons nil "::") (cons "::" nil)) t)

# :ide: DELIM:     @: SYM :@         @:fillme:@             adhoc tag
# . (symbol-tag-normalize-delimiter (cons (cons nil "@:") (cons ":@" nil)) t)

# :ide: +-#+
# . Delimiters ()

# :ide: COMPILE: Run with --ap-help
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --ap-help")))

# :ide: COMPILE: Run with --help
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --help")))

# :ide: COMPILE: Run with --test
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --test")))

# :ide: COMPILE: Run with --test --verbose
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --test --verbose")))

# :ide: COMPILE: Run with --debug
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --debug")))

# :ide: +-#+
# . Compile with standard arguments ()

# :ide: OCCUR-OUTLINE: Python Source Code
# . (x-symbol-tag-occur-outline "sec" '("||:" ":||") (cons (cons "^\\([ \t\r]*\\(def\\|class\\)[ ]+\\|[A-Za-z_]?\\)" nil) (cons nil "\\([ \t\r]*(\\|[ \t]*=\\)")))

# :ide: MENU-OUTLINE: Python Source Code
# . (x-eIDE-menu-outline "sec" '("|||:" ":|||") (cons (cons "^\\([ \t\r]*\\(def\\|class\\)[ ]+\\|[A-Za-z_]?\\)" nil) (cons nil "\\([ \t\r]*(\\|[ \t]*=\\)")))

# :ide: +-#+
# . Outline ()

# :ide: INFO: SQLAlchemy - SQL Expression Language - Reference
# . (let ((ref-buffer "*sqa-expr-ref*")) (if (not (get-buffer ref-buffer)) (shell-command (concat "w3m -dump -cols " (number-to-string (1- (window-width))) " 'http://www.sqlalchemy.org/docs/05/reference/sqlalchemy/expressions.html'") ref-buffer) (display-buffer ref-buffer t)))

# :ide: INFO: SQLAlchemy - SQL Expression Language - Tutorial
# . (let ((ref-buffer "*sqa-expr-tutor*")) (if (not (get-buffer ref-buffer)) (shell-command (concat "w3m -dump -cols " (number-to-string (1- (window-width))) " 'http://www.sqlalchemy.org/docs/05/sqlexpression.html'") ref-buffer) (display-buffer ref-buffer t)))

# :ide: INFO: SQLAlchemy - Query
# . (let ((ref-buffer "*sqa-query*")) (if (not (get-buffer ref-buffer)) (shell-command (concat "w3m -dump -cols " (number-to-string (1- (window-width))) " 'http://www.sqlalchemy.org/docs/orm/query.html'") ref-buffer) (display-buffer ref-buffer t)))

# :ide: +-#+
# . SQLAlchemy Reference ()

# :ide: INFO: Python - argparse
# . (let ((ref-buffer "*python-argparse*")) (if (not (get-buffer ref-buffer)) (shell-command (concat "w3m -dump -cols " (number-to-string (1- (window-width))) " 'http://docs.python.org/library/argparse.html'") ref-buffer) (display-buffer ref-buffer t)))

# :ide: INFO: Python Documentation
# . (let ((ref-buffer "*w3m*")) (if (get-buffer ref-buffer) (display-buffer ref-buffer t)) (other-window 1) (w3m-goto-url "http://docs.python.org/index.html" nil nil))

# :ide: INFO: Python Reference
# . (let* ((ref-buffer "*python-ref*") (local "/home/ws/project/ws-util/python/reference/PQR2.7.html") (url (or (and (file-exists-p local) local) "'http://rgruet.free.fr/PQR27/PQR2.7.html'"))) (unless (get-buffer ref-buffer) (get-buffer-create ref-buffer) (with-current-buffer ref-buffer (shell-command (concat "snc txt.py.reference 2>/dev/null") ref-buffer) (goto-char (point-min)) (if (eobp) (shell-command (concat "w3m -dump -cols " (number-to-string (1- (window-width))) " " url) ref-buffer)))) (display-buffer ref-buffer t))

# :ide: +-#+
# . Python Reference ()

# :ide: COMPILE: Run with --decompile dist/xx_adhoc.py
# . (progn (save-buffer) (compile (concat "rm -rf __adhoc__; cp -p dist/adhoc.py dist/xx_adhoc.py; python ./" (file-name-nondirectory (buffer-file-name)) " --decompile dist/xx_adhoc.py")))

# :ide: COMPILE: Run with cat dist/adhoc.py | --decompile
# . (progn (save-buffer) (compile (concat "rm -rf __adhoc__; cat dist/adhoc.py | python ./" (file-name-nondirectory (buffer-file-name)) " --decompile")))

# :ide: COMPILE: Run with cat /dev/null | --decompile
# . (progn (save-buffer) (compile (concat "rm -rf __adhoc__; cat /dev/null | python ./" (file-name-nondirectory (buffer-file-name)) " --decompile")))

# :ide: COMPILE: Run with cat /dev/null | --compile
# . (progn (save-buffer) (compile (concat "cat /dev/null | python ./" (file-name-nondirectory (buffer-file-name)) " --compile")))

# :ide: COMPILE: Run with cat /dev/null |
# . (progn (save-buffer) (compile (concat "cat /dev/null | python ./" (file-name-nondirectory (buffer-file-name)) " ")))

# :ide: COMPILE: Run with --help
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --help")))

# :ide: COMPILE: Run with --template doc/index.rst
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --template doc/index.rst")))

# :ide: COMPILE: Run with --template test
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --template test")))

# :ide: COMPILE: Run with --template
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --template")))

# :ide: COMPILE: Run with python3 with --template list
# . (progn (save-buffer) (compile (concat "python3 ./" (file-name-nondirectory (buffer-file-name)) " --template list")))

# :ide: COMPILE: Run with --verbose --implode
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) "  --verbose --implode")))

# :ide: COMPILE: Run with --documentation
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --documentation")))

# :ide: COMPILE: make ftp
# . (progn (save-buffer) (compile (concat "make -k ftp")))

# :ide: COMPILE: Run with --verbose --extract
# . (progn (save-buffer) (shell-command "rm -f README.txt doc/index.rst") (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) "  --verbose --extract")))

# :ide: COMPILE: Run with --verbose --template README.txt
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --verbose --template README.txt")))

# :ide: COMPILE: Run with --template list
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --template list")))

# :ide: COMPILE: Run with --eide #
# . (progn (save-buffer) (shell-command (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --eide '#'") (concat "*templates: " (file-name-nondirectory (buffer-file-name)) "*")))

# :ide: COMPILE: Run with --expected
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --expected")))

# :ide: COMPILE: make doc
# . (progn (save-buffer) (compile (concat "make doc")))

# :ide: COMPILE: Run with --eide
# . (progn (save-buffer) (shell-command (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --eide") (concat "*templates: " (file-name-nondirectory (buffer-file-name)) "*")))

# :ide: COMPILE: Run with python3 with --test
# . (progn (save-buffer) (compile (concat "python3 ./" (file-name-nondirectory (buffer-file-name)) " --test")))

# :ide: COMPILE: Run with python3 w/o args
# . (progn (save-buffer) (compile (concat "python3 ./" (file-name-nondirectory (buffer-file-name)) " ")))

# :ide: COMPILE: Run with --test
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --test")))

# :ide: COMPILE: Run with --verbose
# . (progn (save-buffer) (compile (concat "python ./" (file-name-nondirectory (buffer-file-name)) " --verbose")))

# :ide: +-#+
# . Compile ()

#
# Local Variables:
# mode: python
# comment-start: "#"
# comment-start-skip: "#+"
# comment-column: 0
# truncate-lines: t
# End:
