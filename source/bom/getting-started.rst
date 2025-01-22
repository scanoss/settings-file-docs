BOM Operations
=============

Tell your scanner what you know with commands to control your software component inventory

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

Next Steps
---------
Once you're comfortable with these basics, check out the Technical Reference


:doc:`Remove <rule_remove>`
    Remove specific components or files from scan results based on various criteria.

:doc:`Replace <rule_replace>`
    Replace identified components with alternative component definitions.

:doc:`Include <rule_include>`
    Define components to be included in the scanning process.

:doc:`Exclude <rule_exclude>`
    Define components to be excluded from the scanning process.