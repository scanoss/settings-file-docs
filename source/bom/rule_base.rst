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

   * - Path Pattern
     - Mode
     - Description
   * - src/file1.c
     - Exact
     - Must match the complete path exactly
   * - src/lib/
     - StartsWith
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

Path Matching Examples
^^^^^^^^^^^^^^^^^^^^

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
   * - src/lib/
     - src/lib/file1.c
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