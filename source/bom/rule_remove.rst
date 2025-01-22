Remove Rule
===========

The remove rule allows you to filter out specific components from your scan results. When a component matches the rule criteria, it will be replaced with a "non-match" result in the final output.

This rule follows the core matching system described in :doc:`Rule Matching <rule_base>`, using the same path and PURL matching behavior.

Properties
=========

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Property
     - Type
     - Description
   * - path
     - string
     - File path pattern for matching (inherited from base rules)
   * - purl
     - string
     - Package URL for component matching (inherited from base rules)
   * - start_line
     - number
     - Starting line number for filtering (scanoss.java only)
   * - end_line
     - number
     - Ending line number for filtering (scanoss.java only)

Line Number Matching (scanoss.java only)
=============================================

When using scanoss.java, the remove rule extends the base matching system with line-range filtering capabilities:

* If ``start_line`` and ``end_line`` are specified, the rule will match components whose local line numbers overlap with the specified range
* Line matching is based on the component's local line numbers, not the OSS file line numbers
* A match occurs when there is any overlap between the specified line range and the component's lines

Example
==================

Here's an example that demonstrates removing test files and specific line ranges:

.. code-block:: json

   {
     "bom": {
       "remove": [
         {
           "path": "test/",
           "purl": "pkg:github/example/lib@1.0.0"
         },
         {
           "path": "src/main.java",
           "start_line": 100,
           "end_line": 150
         }
       ]
     }
   }

This configuration:

1. Removes any component that matches both:
   * Path starting with "test/"
   * PURL "pkg:github/example/lib@1.0.0"

2. In scanoss.java scans, also removes matches in src/main.java between lines 100-150

.. note::
   When a match occurs, the component is replaced with a non-match result that maintains the file structure. The output will look like this:

   .. code-block:: json

      {
        "src/main.java": [
          {
            "id": "none",
            "server": {
              "kb_version": {
                "daily": "25.01.13",
                "monthly": "24.12"
              },
              "version": "5.4.9"
            }
          }
        ]
      }

   This format preserves the file entry while indicating the content was filtered out.

.. warning::
   Line number filtering is only available when using scanoss.java. Other scanners will ignore the start_line and end_line properties.