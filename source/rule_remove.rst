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
4. Package PURL with Version Match

Remove by Multiple Properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

5. Path and PURL: Remove files that match both path and package URL criteria

Special Cases
^^^^^^^^^^^^^

6. Line Range Filtering (scanoss.java only): Remove files within specific line ranges of a file using start_line and end_line


-------------


1. Example Exact Path Match
~~~~~~~~~~~~~~~~~~~

This filter type performs a case-sensitive comparison between the specified path and the file paths in the scan results.
The filter applies regardless of whether the match type is 'file', 'snippet' or 'none'.

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

The path property have an implicit startsWith behavior - meaning they will match any path that begins with the specified pattern.


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
   The startsWith behavior in path matching may have unintended consequences. Consider these scenarios:

   * **Partial Path Matches**: A path pattern like ``test`` will match multiple unrelated paths:

     - ``test/file.js``
     - ``test_utils/file.js``
     - ``testing/main.cpp``

   * **File Extension Issues**: A path pattern may match files with different extensions:

     - Pattern ``main.c`` would match ``main.cpp``
     - Pattern ``script.py`` would match ``script.pyc``

   Should we implemente a pattern matching system similar to .gitignore rules to avoid these issues? or?.



-------------------------------

3. Example Package URL Match
~~~~~~~~~~~~~~~~~~~~~~~~

This filter type removes files from the scan results if any of their PURLs match the specified package URL in the remove rule. The matching is done against all PURLs associated with a component, and if any match is found, the entire file entry is removed from the results.

**Settings** :download:`📥 <_static/filename/rule_remove/3_package_url_match/scanoss.json>`

.. literalinclude:: _static/filename/rule_remove/3_package_url_match/scanoss.json
   :language: json
   :linenos:


**Raw Scan Results** :download:`📥 <_static/filename/rule_remove/3_package_url_match/result.json>`

.. literalinclude:: _static/filename/rule_remove/3_package_url_match/result.json
   :language: json
   :linenos:

**Expected Output** :download:`📥 <_static/filename/rule_remove/3_package_url_match/expected.json>`

.. literalinclude:: _static/filename/rule_remove/3_package_url_match/expected.json
   :language: json
   :linenos:

.. note::
   This example demonstrates PURL-based filtering:

   * Files removed (contain ``pkg:npm/scanoss``):

     - ``src/test_main.cpp``
     - ``src/helper.cpp``

   * Files retained (no matching PURL):

     - ``src/utils.cpp``

   The removal occurs when any PURL in a file's list matches the specified package URL in the rule.

-------------------------------

4. Example PURL Version Match
~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates how PURL matching works with specific versions.

**Settings** :download:`📥 <_static/filename/rule_remove/4_purl_version_match/scanoss.json>`

.. literalinclude:: _static/filename/rule_remove/4_purl_version_match/scanoss.json
   :language: json
   :linenos:


**Raw Scan Results** :download:`📥 <_static/filename/rule_remove/4_purl_version_match/result.json>`

.. literalinclude:: _static/filename/rule_remove/4_purl_version_match/result.json
   :language: json
   :linenos:

**Expected Output** :download:`📥 <_static/filename/rule_remove/4_purl_version_match/expected.json>`

.. literalinclude:: _static/filename/rule_remove/4_purl_version_match/result.json
   :language: json
   :linenos:

.. note::
   This example demonstrates version-specific PURL matching:

   * Files removed (exact version match ``pkg:npm/lodash@4.17.21``):

     - ``src/utils/helper.js``

   * Files retained (different or no version):

     - ``src/lib/functions.js`` (version 4.17.20)

   The version must match exactly for the rule to apply. Removing a specific version will not affect files with different versions or no version specified.


.. warning::
 TBD: What happens with multiple purls? The version only is associated to the first purl.
 How we should handle the purl and version with multiple?¿ Maybe consider only the first purl?


-------------------------------

5. Example Path and PURL Match
~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates how to remove files that match multiple criteria simultaneously. The rule will only apply when all specified conditions are met - in this case, both the path and PURL must match for a file to be removed from the results.

**Settings** :download:`📥 <_static/filename/rule_remove/5_path_and_purl_match/scanoss.json>`

.. literalinclude:: _static/filename/rule_remove/5_path_and_purl_match/scanoss.json
   :language: json
   :linenos:


**Raw Scan Results** :download:`📥 <_static/filename/rule_remove/5_path_and_purl_match/result.json>`

.. literalinclude:: _static/filename/rule_remove/5_path_and_purl_match/result.json
   :language: json
   :linenos:

**Expected Output** :download:`📥 <_static/filename/rule_remove/5_path_and_purl_match/expected.json>`

.. literalinclude:: _static/filename/rule_remove/5_path_and_purl_match/expected.json
   :language: json
   :linenos:


.. note::
   This example demonstrates multi-criteria filtering:

   * Files removed (matches both conditions):

     - ``src/test/main.cpp`` (matches path "src/test" and PURL "pkg:npm/scanoss")

   * Files retained (matches only one condition):

     - ``src/test/utils.cpp`` (matches only path)
     - ``src/lib/helper.cpp`` (matches only PURL)

   Files must match all conditions specified in the rule to be removed from the results.


-------------------------------


Multiple Rules Behavior
~~~~~~~~~~~~~~~~~~~~~

The remove rules are applied independently and their order in the settings file does not affect the final result. Here are some important considerations:

**Common Scenarios**

1. Multiple Path Rules

   Consider having these two rules in your configuration:

   .. code-block:: json

      [
        {"path": "test"},
        {"path": "src/test"}
      ]

   The rules will be processed as follows:

   * Rule 1 (``test``):

     - Matches any file path starting with "test"
     - Includes paths like ``test/file.js``, ``testing/main.cpp``

   * Rule 2 (``src/test``):

     - Matches any file path starting with "src/test"
     - Includes paths like ``src/test/file.js``, ``src/testing/main.cpp``

   Both rules work independently, meaning:

   * Files matching either rule will be removed
   * Order of rules doesn't matter
   * The more specific path (``src/test``) doesn't override the general one (``test``)


2. Mixed Property Rules

   Consider having these two rules in your configuration:

   .. code-block:: json

      [
        {"path": "test"},
        {"path": "test", "purl": "pkg:npm/example"}
      ]

   The rules will be processed as follows:

   * Rule 1 (``path`` only):

     - Removes all files with path starting with "test"
     - This includes all possible matches of Rule 2

   * Rule 2 (``path`` and ``purl``):

     - Would remove files that match both path "test" and PURL "pkg:npm/example"
     - However, these files were already removed by Rule 1

   Therefore, the second rule becomes redundant as all potential matches were already handled by the first rule's broader scope.


.. warning::
   When using multiple rules, consider:

   * The cumulative effect of all rules
   * Potential unintended matches from broad path patterns

.. tip::
   To maintain clarity:

   * Group related rules together in the settings file
   * Avoid redundant rules that don't add filtering value