SCANOSS Settings Documentation
==============================


This documentation will help you better understand the concept of the SCANOSS Settings file, as well as how to implement it when using SCANOSS clients and services.

.. note::
   This feature is available for all SCANOSS clients and integrations.


What is the SCANOSS Settings file?
==================================


In the context of using SCANOSS for declared or undeclared component detection, the settings file is a feature to configure the SCANOSS clients and services.

As a way of illustrating the feature, we will take the example of the SCANOSS GitHub Actions integration.

After triggering the Action (in this case, through a pull request), we will get in return a summary of all undeclared components found in our code:

.. image:: screenshot.png


We can see that the action detected 2 undeclared components: "pkg:github/kingventrix007/kickstart" and "pkg:github/zephyrproject-rtos/zephyr-testing". One reason to use the settings file would be to exclude certain components from the scan results, that's the use case we are going to follow for this example.

To implement the settings file in this case, we will create a file named "scanoss.json" in the root directory of our project and inside there we will paste the package url of each component we want to exclude from following scans. 

The format of the "scanoss.json" file goes like this:

.. code-block:: json

    {
        "bom": {
            "exclude": [
                {
                    "purl": "pkg:github/kingventrix007/kickstart"
                },
                {
                    "purl": "pkg:github/zephyrproject-rtos/zephyr-testing"
                }
            ]
        }
    }


After you trigger the action again with this configuration in place, the previously detected components will no longer appear as undeclared in your results.

While this example demonstrates excluding components from scan results, the SCANOSS Settings file supports various other use cases, such as:
- Preventing false positive matches
- Customizing scanning behavior for specific components
- Managing component detection rules across your project



SCANOSS Settings Rules
=====================

The SCANOSS settings file provides two types of rules: Result Manipulation Rules that work on scan results, and Scanning Rules that are sent to the scanning engine.


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