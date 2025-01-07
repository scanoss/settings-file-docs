===========
Remove Rule
===========

The remove rule allows you to filter out specific files from your scan results. Rules can be combined and are applied independently of their order in the settings file.

Rule Properties
===============

- **path:** Filter by file path (string)
- **purl:** Filter by package URL (string)
- **start_line:** Filter by starting line number (number, only available in scanoss.java)
- **end_line:** Filter by ending line number (number, only available in scanoss.java)


-------------------


Remove by Path
^^^^^^^^^^^^^^
1. Exact Path Match : Remove results from a specific file path
2. StartsWith Path Match:  Remove all results from files that starts with the specified path

Remove by PURL
^^^^^^^^^^^^^^

3. Package URL Match: Remove all files that match the specified package URL

Remove by Multiple Properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

4. Path and PURL: Remove files that match both path and package URL criteria

Special Cases
^^^^^^^^^^^^^

5. Line Range Filtering (scanoss.java only): Remove files within specific line ranges of a file using start_line and end_line


-------------


1. Example Exact Path Match
~~~~~~~~~~~~~~~~~~~

This filter type performs a case-sensitive comparison between the specified path and the file paths in the scan results.
The filter applies regardless of whether the match type is 'file', 'snippet' or 'none'.

.. warning::
 Do we actually want to remove the key from the result? Or would be better to replace the component for a match type none?

**Settings** :download:`📥 <_static/filename/rule_remove/1_exact_path_match/scanoss.json>`

.. literalinclude:: _static/filename/rule_remove/1_exact_path_match/scanoss.json
   :language: json
   :linenos:


**Raw Scan Results** :download:`📥 <_static/filename/rule_remove/1_exact_path_match/result.json>`

.. literalinclude:: _static/filename/rule_remove/1_exact_path_match/result.json
   :language: json
   :linenos:

**Expected Output** :download:`📥 <_static/filename/rule_remove/1_exact_path_match/expected.json>`

.. literalinclude:: _static/filename/rule_remove/1_exact_path_match/expected.json
   :language: json
   :linenos:


.. warning::
 TBD: Do the file needs to be removed completly? Or we can assign a non match id?



-------------------------------

2. Example StartsWith Path Match
~~~~~~~~~~~~~~~~~~~~~~~~

This filter removes files where the path starts with the specified string.
The path rules have an implicit startsWith behavior - meaning they will match any path that begins with the specified pattern.


**Settings** :download:`📥 <_static/filename/rule_remove/2_starts_with_path_match/scanoss.json>`

.. literalinclude:: _static/filename/rule_remove/2_starts_with_path_match/scanoss.json
   :language: json
   :linenos:


**Raw Scan Results** :download:`📥 <_static/filename/rule_remove/2_starts_with_path_match/result.json>`

.. literalinclude:: _static/filename/rule_remove/2_starts_with_path_match/result.json
   :language: json
   :linenos:

**Expected Output** :download:`📥 <_static/filename/rule_remove/2_starts_with_path_match/expected.json>`

.. literalinclude:: _static/filename/rule_remove/2_starts_with_path_match/expected.json
   :language: json
   :linenos:


.. warning::
    The implicit startsWith behavior in path matching can potentially remove more files than intended.
    For example, a path pattern of "test" would match both "test/file.js" AND "test_utils/file.js".
    Another case will be the path pattern "main.c" and will remove the file main.cpp.
    A system like .gitignore should be considered


