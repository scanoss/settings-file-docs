Settings File: Your Control Center
================================

One file to rule them all - your settings file is where you:

.. tip::
   * Tell scanners which files to examine (and which to skip)
   * Configure how deeply to analyze your code
   * Customize outputs to match your needs

Think of it as your scanning command center, where each option helps craft the perfect scan for your project.

------------------


BOM Operations
=================

Tell your scanner what you know to improve matching results and control your software component inventory

Two Types of Operations
---------------------

1. **Component Hints**
   Tell your scanner what components you recognize:
   *"Hey, this folder is jQuery 3.2.1 - use this to identify related files!"*

2. **Result Cleanup**
   Clean up and standardize results:
   *"Replace all jQuery 3.2.1 with 3.5.0"* or *"Remove test files"*



Your First BOM Operation
-----------------------

Let's start with a simple example - removing test files from your results:

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

What this does:
- Looks for any files in paths containing "test/"
- Removes them from your results
- For example, it will remove "test/unit/mytest.js" but keep "src/main.js"

Common Use Cases
--------------

1. Updating Component Versions
   Let's say you want to standardize on a specific version of jQuery:

   .. code-block:: json

      {
        "bom": {
          "replace": [
            {
              "purl": "pkg:github/jquery/jquery@3.2.1",
              "replace_with": "pkg:github/jquery/jquery@3.5.0"
            }
          ]
        }
      }

2. Providing Better Scan Context
   If you know certain files are from a specific component:

   .. code-block:: json

      {
        "bom": {
          "include": [
            {
              "path": "lib/jquery/",
              "purl": "pkg:github/jquery/jquery@3.5.0"
            }
          ]
        }
      }

3. Cleaning Up Results
   Remove all test and example files:

   .. code-block:: json

      {
        "bom": {
          "remove": [
            {
              "path": "test/"
            },
            {
              "path": "examples/"
            }
          ]
        }
      }



Technical Reference
-----------------

 :doc:`Component Matcher <bom/rule_base>`
    Defines the core matching properties (path and purl) that all operations use to identify components.


**Available Operations**

   :doc:`Include <bom/rule_include>`
        Define components to include in scanning using the base matching criteria.

   :doc:`Exclude <bom/rule_exclude>`
        Define components to exclude from scanning using the base matching criteria.

   :doc:`Remove <bom/rule_remove>`
        Remove components from scan results using the base matching criteria.

   :doc:`Replace <bom/rule_replace>`
        Replace matched components with alternative definitions using the base matching criteria.

.. note::
    Each operation inherits the same path and purl matching behavior, while implementing its own specific action. See each operation’s reference for detailed usage examples.

--------------------------

SKIP Operations
==============
Tell the scanner what to skip and when - save time by scanning only what matters.

.. code-block:: json

  {
    "settings": {
      "skip": {
        "patterns": {
          "scanning": [
            "# Common files to skip",
            "node_modules/",
            "dist/",
            "build/"
          ]
        }
      }
    }
  }

Want more control? Check our detailed guides:
:doc:`Skip by pattern <skip_patterns>` | :doc:`Skip by size <skip_sizes>` | :doc:`Advanced examples <skip_examples>`