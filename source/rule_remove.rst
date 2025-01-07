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

.. note::
 Files with match type 'none' are always kept in the results, regardless of the filter settings. This is a global behavior that applies to all remove rules.


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


1. Exact Path Match
~~~~~~~~~~~~~~~~~~~

This filter type performs a case-sensitive comparison between the specified path and the file paths in the scan results.
The filter applies regardless of whether the match type is 'file' or 'snippet'.

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
   :emphasize-lines: 3-12

**Note:** The file sdk/include/api/grpc.h is kept because does not have a match #TODO

-------------------------------

2. StartsWith Path Match
~~~~~~~~~~~~~~~~~~~~~~~~

This filter removes files where the path starts with the specified string.
This is similar to a directory match but more flexible as it can match any path prefix, not just complete directory names.

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

Key Behaviors:
^^^^^^^^^^^^^

StartsWith Matching:
* Matches any file path that starts with "src/test"
* Removes "src/test/helper.cpp" and "src/test_main.cpp"
*Does NOT remove "src/testing/mock.cpp" (different path)
*Does NOT remove "src/test-config.h" (has id: "none")


**Case Sensitivity:**
The matching is case-sensitive "src/test" would not match "src/TEST/file.cpp"


**Partial Path Matching**
Matches both directory and file paths "src/test" matches both "src/test/helper.cpp" (directory) and "src/test_main.cpp" (filename starting with test)


**Non-Match Preservation**
Files with "id": "none" are preserved even if their paths match
