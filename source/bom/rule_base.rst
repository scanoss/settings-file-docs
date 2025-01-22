SCANOSS Rule Matching Guide
~~~~~~~~~~~~~~~


Common Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SCANOSS rules have two properties in common that determine matching behavior:

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


The path property uses two matching modes controlled by a single character - the trailing slash (/):

.. list-table::
   :header-rows: 1

   * - Mode
     - Example
     - Description
   * - Exact Match
     - ``src/lib``
     - | Must match the complete path exactly
       | Will ONLY match "src/lib", nothing more or less
   * - StartsWith Match
     - ``src/lib/``
     - | Matches any path that begins with "src/lib/"
       | Can have any number of subdirectories or files after it

.. note::
   The trailing slash (/) acts as a simple switch between the two modes:

   * Without slash (``src/lib``):
     - Requires exact match of the entire path
     - Example: "src/lib/file.txt" would NOT match
     - Example: Only "src/lib" would match

   * With slash (``src/lib/``):
     - Matches any path that starts with the pattern
     - Example: "src/lib/file.txt" would match
     - Example: "src/lib/subfolder/file.txt" would match
     - Example: "src/lib/deep/nested/file.txt" would match

Examples
^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Rule Path
     - Match Mode
     - Input Path
     - Matches?
     - Explanation
   * - src/lib
     - Exact
     - src/lib
     - ✅ YES
     - Exact match - paths are identical
   * - src/lib
     - Exact
     - src/lib/file.txt
     - ❌ NO
     - Exact match required, but input has extra content
   * - src/lib/
     - StartsWith
     - src/lib/file.txt
     - ✅ YES
     - Input starts with "src/lib/"
   * - src/lib/
     - StartsWith
     - src/lib/subfolder/file.txt
     - ✅ YES
     - Input starts with "src/lib/"
   * - src/lib/
     - StartsWith
     - src/libs/file.txt
     - ❌ NO
     - Input does not start with "src/lib/"
   * - src/lib/
     - StartsWith
     - src/lib
     - ❌ NO
     - Input is shorter than the required prefix

.. warning::
   Common pitfalls to avoid:

   * Not having a trailing slash when you want to match subdirectories
   * Having a trailing slash when you only want to match one specific path
   * Forgetting that exact matches (no slash) will reject anything longer than the pattern

Purl Matching
~~~~~~~~~~~~~~


The PURL property uses two matching modes based on the version specification:

.. list-table::
  :header-rows: 1

  * - Mode
    - Description
  * - Basic
    - Matches the base PURL without version constraints
  * - Version-specific
    - Must match both the PURL and specified version


.. note::
  The presence of a version (@version) in the PURL automatically enables version-specific matching behavior:

  * ``pkg:github/scanoss/wfp`` matches any version of the component
  * ``pkg:github/scanoss/wfp@1.4.2`` requires exact version match

  This provides a simple way to toggle between basic and version-specific matching without additional configuration.

.. warning::
    ⚠️ Components can have multiple Package URLs (PURLs) associated with them. The version shown in the component details corresponds to the first PURL.


Examples
^^^^^^^^^


.. list-table::
  :header-rows: 1

  * - Rule PURL
    - Scan Result PURLs
    - Version
    - Matches?
  * - pkg:github/scanoss/wfp
    - | pkg:github/scanoss/wfp
      | pkg:npm/@scanoss/wfp
    - 1.4.2
    - ✅ YES
  * - pkg:github/scanoss/wfp@1.4.2
    - | pkg:github/scanoss/wfp
      | pkg:github/scanoss/engine
    - 1.4.2
    - ✅ YES
  * - pkg:github/scanoss/wfp
    - | pkg:npm/@scanoss/wfp
      | pkg:github/scanoss/engine
    - 1.4.2
    - ❌ NO


Combined Path and Purl Matching
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
   Combined matching requires BOTH conditions to be satisfied:

   * Path must match according to path matching rules
   * PURL must match according to PURL matching rules
   * Version must match if specified in PURL

   If either condition fails, the entire rule fails to match.


Examples
^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 25 15 25 10 10 15

   * - **Rule**
     - **File Path**
     - **Scan Result PURLs**
     - **Version**
     - **Matches?**
     - **Explanation**
   * - | path: "src/lib/"
       | purl: "pkg:github/scanoss/wfp"
     - src/lib/file1.c
     - | pkg:github/scanoss/wfp
       | pkg:npm/@scanoss/wfp
     - \-
     - ✅ YES
     - | ✓ Path starts with "src/lib/"
       | ✓ PURL found in list
   * - | path: "src/lib/"
       | purl: "pkg:github/scanoss/wfp@1.4.2"
     - src/lib/file2.c
     - | pkg:github/scanoss/wfp
     - 1.4.2
     - ✅ YES
     - | ✓ Path starts with "src/lib/"
       | ✓ PURL and version match
   * - | path: "src/lib/"
       | purl: "pkg:github/scanoss/wfp@1.4.2"
     - src/lib/file3.c
     - | pkg:github/scanoss/wfp
     - 1.4.1
     - ❌ NO
     - | ✓ Path starts with "src/lib/"
       | ✗ Version mismatch (1.4.1 ≠ 1.4.2)
   * - | path: "src/lib/exact"
       | purl: "pkg:github/scanoss/wfp"
     - src/lib/different
     - | pkg:github/scanoss/wfp
     - \-
     - ❌ NO
     - | ✗ Path doesn't match exactly
       | ✓ PURL matches
   * - | path: "test/"
       | purl: "pkg:github/scanoss/wfp"
     - src/lib/file1.c
     - | pkg:github/scanoss/wfp
     - \-
     - ❌ NO
     - | ✗ Path doesn't start with "test/"
       | ✓ PURL matches
   * - | path: "src/lib/"
       | purl: "pkg:github/scanoss/wfp"
     - src/lib/file1.c
     - | pkg:npm/@scanoss/wfp
       | pkg:github/scanoss/engine
     - \-
     - ❌ NO
     - | ✓ Path starts with "src/lib/"
       | ✗ Required PURL not found
   * - | path: "src/lib"
       | purl: "pkg:github/scanoss/wfp@1.4.2"
     - src/lib
     - | pkg:github/scanoss/wfp
     - 1.4.2
     - ✅ YES
     - | ✓ Path matches exactly
       | ✓ PURL and version match
   * - | path: "src/lib/"
       | purl: "pkg:github/scanoss/wfp"
     - src/lib/subdir/file.c
     - | pkg:github/scanoss/wfp
     - \-
     - ✅ YES
     - | ✓ Path starts with "src/lib/"
       | ✓ PURL matches (any depth)
   * - | path: "src/lib/"
       | purl: "pkg:github/scanoss/wfp@2.0.0"
     - src/lib/file.c
     - | pkg:github/scanoss/wfp@1.0.0
     - 2.0.0
     - ❌ NO
     - | ✓ Path starts with "src/lib/"
       | ✗ PURL version mismatch

.. warning::

   * Path matches but PURL doesn't:

     - The file is in the right location but wrong component
     - Results in NO MATCH

   * PURL matches but path doesn't:

     - Right component but wrong location
     - Results in NO MATCH

   * Both match but version wrong:

     - Right component and location but wrong version
     - Results in NO MATCH


Rule Priority
~~~~~~~~~~~~
SCANOSS sorts all rules based on a priority system before applying them. This ensures a deterministic order of evaluation, with more specific rules being checked before general ones:

.. list-table::
   :header-rows: 1

   * - Priority Level
     - Rule Properties
     - Score
     - Description
   * - Highest
     - PURL + Path
     - 4
     - Rules with both PURL and path are checked first
   * - Medium
     - PURL only
     - 2
     - Rules with only PURL are checked second
   * - Low
     - Path only
     - 1
     - Rules with only path are checked last
   * - None
     - No properties
     - 0
     - Rules with neither property are ignored


When Rules Have Equal Priority
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If two rules have the same priority score, additional criteria are used:

1. For rules with paths:

   * The rule with the longer path takes precedence
   * Example: ``src/lib/utils/`` takes precedence over ``src/lib/``

2. If no other criteria distinguish the rules:

   * The rules are considered equal
   * The first matching rule will be applied

.. warning::
   Be careful when defining multiple rules that could match the same files:

   * More specific rules (longer paths) take precedence over general rules
   * Rules with both PURL and path always take precedence
   * Rules with neither property will never be applied

