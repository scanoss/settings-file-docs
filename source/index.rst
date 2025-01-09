============================
SCANOSS Rules - Getting Started
============================

What are SCANOSS Rules?
----------------------
SCANOSS rules help you filter and modify your scan results. Think of them as search filters that help you find and process specific files or components in your codebase.

When Do You Need Rules?
----------------------
Common scenarios where rules are helpful:

* Excluding test files from your results
* Removing specific versions of components
* Focusing on specific parts of your codebase
* Cleaning up scan results

Your First Rule
--------------
Let's start with a simple example. Imagine you want to exclude all test files from your scan results:

.. code-block:: json

   {
     "bom": {
       "remove": [
         {
           "path": "test/"
         }
       ]
     }
   }

This rule tells SCANOSS: "Remove any file that has a path starting with 'test/'"

How it Works
~~~~~~~~~~~
When you apply this rule:

* ✅ ``test/unit/file1.c`` will be removed
* ✅ ``test/integration/tests.cpp`` will be removed
* ❌ ``src/main.c`` will stay (doesn't start with "test/")

Building More Complex Rules
-------------------------

Example 1: Excluding a Specific Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Let's say you want to exclude a specific version of a component:

.. code-block:: json

   {
     "bom": {
       "remove": [
         {
           "purl": "pkg:github/scanoss/wfp@1.4.2"
         }
       ]
     }
   }

This will remove any file that matches WFP version 1.4.2.

Example 2: Combining Criteria
~~~~~~~~~~~~~~~~~~~~~~~~~~
You can combine path and component criteria:

.. code-block:: json

   {
     "bom": {
       "remove": [
         {
           "path": "src/lib/",
           "purl": "pkg:github/scanoss/wfp"
         }
       ]
     }
   }

This rule means: "Remove WFP components, but only in the src/lib/ directory"

Tips and Best Practices
---------------------

1. Path Matching
~~~~~~~~~~~~~~
* Use a trailing slash (``src/lib/``) to match all files in a directory
* Without a trailing slash (``src/lib``), only exact matches count

.. code-block:: json

   // With trailing slash: matches all files in directory
   {"path": "src/lib/"}  // Matches: src/lib/file1.c, src/lib/utils/helper.c
   // Without trailing slash: matches exact path only
   {"path": "src/lib"}   // Only matches the exact path "src/lib"

2. Version Matching
~~~~~~~~~~~~~~~~
* Be specific with versions when needed
* Remember that versions can appear in two places:
   * In the PURL: ``pkg:github/scanoss/wfp@1.4.2``
   * In the component's version field

.. code-block:: json

   // Version specific
   {"purl": "pkg:github/scanoss/wfp@1.4.2"}  // Only matches version 1.4.2
   // Any version
   {"purl": "pkg:github/scanoss/wfp"}        // Matches any version

3. Rule Ordering
~~~~~~~~~~~~~
Rules are applied in order of specificity:

1. Most specific (path + PURL + version) first
2. Medium specific (PURL + version or path + PURL) next
3. Least specific (just path or just PURL) last

Common Patterns
-------------

Excluding Test Files
~~~~~~~~~~~~~~~~~~
.. code-block:: json

   {
     "bom": {
       "remove": [
         {"path": "test/"},
         {"path": "tests/"},
         {"path": "src/test/"}
       ]
     }
   }

Excluding Development Files
~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: json

   {
     "bom": {
       "remove": [
         {"path": "dev/"},
         {"path": "examples/"},
         {"path": "docs/"}
       ]
     }
   }

Focusing on Specific Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: json

   {
     "bom": {
       "remove": [
         {
           "purl": "pkg:github/scanoss/wfp",
           "path": "src/core/"
         }
       ]
     }
   }

Next Steps
---------
* Check our `Technical Reference <link-to-technical-doc>`_ for detailed documentation
* Try creating rules for your specific use cases
* Experiment with combining different criteria
* Remember to validate your rules with test cases

Troubleshooting
-------------

Common issues and solutions:

**Rule not matching?**
   * Check for trailing slashes in paths
   * Verify version numbers
   * Make sure PURLs match exactly

**Multiple rules needed?**
   * Start with the most specific rules
   * Test each rule individually
   * Combine rules as needed

**Not sure which rule to use?**
   * Start simple
   * Add criteria one at a time
   * Test with sample data




SCANOSS Settings Rules
=====================

The SCANOSS settings file provides two types of rules: Result Manipulation Rules that work on scan results, and Scanning Rules that are sent to the scanning engine.



======================
SCANOSS Rules Documentation
======================

Introduction
------------
SCANOSS rules are powerful filters that allow you to control how scan results are processed. They provide a flexible way to match and manipulate files and components in your scan results based on specific criteria.

A rule defines:

* What to match (using paths and package URLs)
* How to match it (exact or pattern matching)
* What to do with the matches (remove, replace, etc.)

Rules can be as simple as matching a single file path or as complex as combining multiple criteria like paths, package URLs, and versions.

.. contents:: Table of Contents
   :depth: 2
   :local:

Base Rules
----------

Common Properties
~~~~~~~~~~~~~~~
SCANOSS rules have two base properties that determine matching behavior:

.. list-table::
   :header-rows: 1

   * - Property
     - Type
     - Description
   * - path
     - string
     - File path pattern for matching
   * - purl
     - string
     - Package URL for component matching

Path Matching
~~~~~~~~~~~~
The path property uses two matching modes based on the trailing slash:

.. list-table::
   :header-rows: 1

   * - Path Pattern
     - Mode
     - Description
   * - src/file1.c
     - Exact
     - Must match the complete path exactly
   * - src/lib/
     - StartsWith
     - Matches any path that starts with src/lib

Path Matching Examples
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Rule Path
     - Input Path
     - Scan Result PURLs
     - Matches?
     - Explanation
   * - src/file1.c
     - src/file1.c
     - ["pkg:github/scanoss/wfp", "pkg:npm/@scanoss/wfp"]
     - ✅ YES
     - Exact path match
   * - src/file1.c
     - src/file1.cpp
     - ["pkg:github/scanoss/wfp"]
     - ❌ NO
     - Different extension
   * - src/lib/
     - src/lib/file1.c
     - ["pkg:github/scanoss/wfp", "pkg:github/scanoss/engine"]
     - ✅ YES
     - Path starts with src/lib/
   * - src/lib/
     - src/lib/file1.c
     - ["pkg:github/scanoss/wfp"]
     - ❌ NO
     - No trailing slash, requires exact match

PURL Matching
~~~~~~~~~~~~

Basic PURL Matching
^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Rule PURL
     - File Path
     - Scan Result PURLs
     - Version
     - Matches?
     - Explanation
   * - pkg:github/scanoss/wfp
     - src/file1.c
     - ["pkg:github/scanoss/wfp", "pkg:npm/@scanoss/wfp"]
     - -
     - ✅ YES
     - PURL found in list
   * - pkg:github/scanoss/wfp@1.4.2
     - src/file2.c
     - ["pkg:github/scanoss/wfp", "pkg:github/scanoss/engine"]
     - 1.4.2
     - ✅ YES
     - Base PURL matches + version matches
   * - pkg:github/scanoss/wfp
     - src/file3.c
     - ["pkg:npm/@scanoss/wfp", "pkg:github/scanoss/engine"]
     - -
     - ❌ NO
     - PURL not in list

PURL Version Matching
^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Rule PURL
     - File Path
     - Scan Result PURLs
     - Component Version
     - Matches?
     - Explanation
   * - pkg:github/scanoss/wfp@1.4.2
     - src/file1.c
     - ["pkg:github/scanoss/wfp", "pkg:npm/@scanoss/wfp"]
     - 1.4.2
     - ✅ YES
     - Version matches
   * - pkg:github/scanoss/wfp@1.4.2
     - src/file2.c
     - ["pkg:github/scanoss/wfp@1.4.1"]
     - 1.4.2
     - ❌ NO
     - PURL version mismatch
   * - pkg:github/scanoss/wfp@1.4.2
     - src/file3.c
     - ["pkg:github/scanoss/wfp"]
     - 1.4.1
     - ❌ NO
     - Component version mismatch

Combined Path and PURL Matching
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Rule
     - File Path
     - Scan Result PURLs
     - Version
     - Matches?
     - Explanation
   * - {"path": "src/lib/", "purl": "pkg:github/scanoss/wfp"}
     - src/lib/file1.c
     - ["pkg:github/scanoss/wfp", "pkg:npm/@scanoss/wfp"]
     - -
     - ✅ YES
     - Path and PURL match
   * - {"path": "src/lib/", "purl": "pkg:github/scanoss/wfp@1.4.2"}
     - src/lib/file2.c
     - ["pkg:github/scanoss/wfp"]
     - 1.4.2
     - ✅ YES
     - Path, PURL, and version match
   * - {"path": "src/lib/", "purl": "pkg:github/scanoss/wfp@1.4.2"}
     - src/lib/file3.c
     - ["pkg:github/scanoss/wfp"]
     - 1.4.1
     - ❌ NO
     - Version mismatch

Rule Applications
---------------

Remove Rules
~~~~~~~~~~
Remove rules extend base rules with additional properties for line-specific matching:

.. list-table::
   :header-rows: 1

   * - Property
     - Type
     - Description
   * - start_line
     - number
     - Starting line for matching (scanoss.java only)
   * - end_line
     - number
     - Ending line for matching (scanoss.java only)

Example remove rule:

.. code-block:: json

   {
     "path": "src/lib/file1.c",
     "purl": "pkg:github/scanoss/wfp",
     "start_line": 10,
     "end_line": 20
   }

Result Manipulation Rules
-----------------------

These rules are applied after scanning to modify the results:

:doc:`Remove <rule_remove>`
    Remove specific components or files from scan results based on various criteria.

:doc:`Replace <rule_replace>`
    Replace identified components with alternative component definitions.

Scanning Engine Rules
-------------------

These rules are sent to the scanning engine to control the scanning process:

:doc:`Include <rule_include>`
    Define components to be included in the scanning process.

:doc:`Exclude <rule_exclude>`
    Define components to be excluded from the scanning process.