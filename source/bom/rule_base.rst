Common Properties
~~~~~~~~~~~~~~~
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


Path Matching
~~~~~~~~~~~~
The path property uses two matching modes based on the trailing slash:

.. list-table::
   :header-rows: 1

   * - Mode
     - Description
   * - Exact
     - Must match the complete path exactly
   * - StartsWith
     - Matches any path that starts with src/lib


.. note::
   The presence of a trailing slash (/) in the path pattern automatically enables startsWith matching behavior:

   * ``src/lib`` requires an exact match with the full path
   * ``src/lib/`` matches any path that begins with "src/lib/"

   This provides a simple way to toggle between exact and prefix matching without additional configuration.

.. warning::
   Be cautious with trailing slashes as they significantly change matching behavior:

   * ``test/`` will match:
     - test/file.js
     - test/subfolder/file.js
     - test/anything/here.txt

   * ``test`` will only match:
     - test

Examples
^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Rule Path
     - Input Path
     - Matches?
     - Explanation
   * - src/file1.c
     - src/file1.c
     - ✅ YES
     - Exact path match
   * - src/file1.c
     - src/file1.cpp
     - ❌ NO
     - Different extension
   * - src/lib/
     - src/lib/file1.c
     - ✅ YES
     - Path starts with src/lib/
   * - src/lib
     - src/lib/file1.c
     - ❌ NO
     - No trailing slash, requires exact match of "src/lib"




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
