Settings File: Your Control Centre
================================
The settings file is your central configuration hub that puts you in control of how your code is scanned and analyzed. Think of it as your project's command centre - one file that coordinates all aspects of your scanning process.

What Can You Do With It?
-----------------------
.. tip::
   The settings file lets you:

   * Define Your Scope
     Control exactly which files get scanned and which don't, saving time and processing power.

   * Set Scanning Depth
     Choose how thoroughly you want to analyze your code, from quick scans to deep dives.

   * Configure Detection Rules
     Fine-tune how components are identified in your codebase.

   * Customize Output Format
     Get results that match your needs, whether it's detailed reports or focused summaries.

   * Manage Component Information
     Control how your software components are identified and represented.

How It Helps
-----------
* **Efficiency**: Skip unnecessary files and focus on what matters
* **Accuracy**: Guide the scanner to make better decisions
* **Flexibility**: Adapt the scanning process to your specific needs
* **Consistency**: Maintain standardized scanning across your projects

The settings file is your single source of truth for scanner configuration, ensuring that your scans are reproducible and aligned with your project's requirements.


------------------


BOM Operations
=================
Tell your scanner what you know to improve matching results and control your software component inventory.
BOM operations are powerful tools that help you guide the scanning process and manage your results effectively.

Two Types of Operations
---------------------

1. **Component Hints**
   Help the scanner make better matching decisions by providing context:

   * Positive hints (Include): *"Hey, this folder might be jQuery 3.2.1!"*
   * Negative hints (Exclude): *"This folder definitely isn't jQuery"*

   These hints influence how the scanner matches components in your codebase, helping it make more accurate decisions based on your knowledge of the project.

2. **Result Cleanup**
   Modify your results to better reflect your project's reality:

   * Version updates (Replace): *"Update any jQuery 3.2.1 to show as 3.5.0"*
   * Non-match marking (Remove): *"Mark test files as not being part of any component"*

   These operations help you maintain clean, accurate component information that matches your project's actual state.

When to Use Each Type
--------------------
* Use **Component Hints** when you want to:
   * Guide the scanner with your knowledge of the codebase
   * Help avoid false matches
   * Improve overall matching accuracy

* Use **Result Cleanup** when you need to:
   * Standardize component versions
   * Mark non-component files appropriately
   * Keep your results focused on relevant components


-------------------------

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

**What this does:**

- Looks for any files in paths containing "test/"
- Marks them as "non-match" in your results
- For example, "test/unit/mytest.js" will be marked as non-match, while "src/main.js" remains unchanged

--------------------


Common BOM Operations Use Cases
-------------------------------

Replace Operation: Version Standardization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


**Use Case**: When you need to update or standardize component versions across your project.

**Example**: Standardizing jQuery version across your codebase

.. code-block:: json

   {
     "bom": {
       "replace": [
         {
           "purl": "pkg:github/jquery/jquery",
           "replace_with": "pkg:github/jquery/jquery@3.5.0"
         }
       ]
     }
   }

**What it does**:

* Finds all instances of jQuery
* Replaces them with jQuery 3.5.0 in your results
* Helps maintain consistent versions across your project


Remove Operation: Setting Files as Non-Match
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Use Case**: When you have files that shouldn't be identified as part of any component.

**Example**: Marking test files as non-matches

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

**What it does**:

* Identifies files in specified paths (like "test/" or "examples/")
* Marks these files as "non-match" in your results
* Ensures these files aren't identified as being part of any component
* For example, all files under "test/" will be marked as not belonging to any package

Include Operation: Component Hints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Use Case**: When you want to provide hints about which components might be in specific locations.

**Example**: Suggesting jQuery's location to the scanner

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

**What it does**:

* Hints to the scanner "This path might contain this component"
* Provides additional context for the scanner's matching process
* Helps the scanner make better-informed decisions during matching
* For example, suggesting "lib/jquery might be jQuery 3.5.0" gives the scanner helpful context for those files


Exclude Operation: Negative Component Hints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Use Case**: When you want to hint that certain components are not present in specific locations.

**Example**: Hinting that certain files are not third-party libraries

.. code-block:: json

   {
     "bom": {
       "exclude": [
         {
           "path": "vendor/",
           "purl": "pkg:github/thirdparty/*"
         }
       ]
     }
   }

**What it does**:

* Hints to the scanner "This component is not in this path"
* Provides negative matching context to the scanner
* Helps the scanner make better decisions by knowing what not to match
* For example, telling it "vendor/ does not contain thirdparty components" helps avoid false matches

Technical Reference
-----------------

   :doc:`Rule Matching <bom/rule_base>`
        Core matching system using paths and package URLs that powers all component rules.

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
Tell the scanner what to skip

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


