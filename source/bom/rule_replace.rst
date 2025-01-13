Replace Rule
============

The replace rule allows you to substitute matched components with alternative definitions in your scan results. This is particularly useful for standardizing component versions or updating license information.

This rule follows the core matching system described in :doc:`Rule Matching <rule_base>`, using the same path and PURL matching behavior.

Properties
============

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
   * - replace_with
     - string
     - Package URL to use as replacement
   * - license
     - string
     - License identifier to apply to the replaced component

Component Creation Behavior
============

When replacing components, the system handles two special cases:

1. New Component Creation
   If the ``replace_with`` PURL doesn't exist in the current scan results:

   * A minimal component will be created using the replacement PURL
   * The new component includes:

     - Package URL name and version from ``replace_with``
     - License if specified in the rule
     - Other context-specific properties (TBD)


2. Existing Component Reference
   If the ``replace_with`` PURL exists in the current scan results:

   * The replacement will use information from the existing component
   * Component properties will be copied from the matching component
   * Additional properties may be updated based on the rule (TBD)

Example
============

Here's an example that demonstrates replacing component versions and licenses:

.. code-block:: json

   {
     "bom": {
       "replace": [
         {
           "path": "lib/jquery/",
           "purl": "pkg:github/jquery/jquery@3.2.1",
           "replace_with": "pkg:github/jquery/jquery@3.5.0",
           "license": "MIT"
         }
       ]
     }
   }

This configuration:

1. Matches components that:

   * Have a path starting with "lib/jquery/"
   * Use PURL "pkg:github/jquery/jquery@3.2.1"

2. Replaces matches with:

   * Updated PURL "pkg:github/jquery/jquery@3.5.0"
   * MIT license

.. note::

   When the replacement PURL doesn't exist in scan results, a new minimal component is created. This ensures continuity while maintaining accurate component tracking.


Advanced Usage
============

You can use replace rules to:

1. Standardize Component Versions

   * Update all instances of a component to a specific version
   * Ensure consistency across your project

2. Update License Information

   * Correct or update license information for specific components
   * Apply standard licenses to matched components

3. Component Migration

   * Move from one package ecosystem to another
