######
Tables
######

*****
Plain
*****

+----------+----------+
| Header A | Header B |
+==========+==========+
| Data A1  | Data B1  |
+----------+----------+
| Data A2  | Data B2  |
+----------+----------+
| Data A3  | Data B3  |
+----------+----------+

*********
Directive
*********

Use this if you need a caption or reference.

.. _table1:

.. table:: Table with ``table`` directive

   +----------+----------+
   | Header 1 | Header 2 |
   +==========+==========+
   | Data A1  | Data B1  |
   +----------+----------+
   | Data A2  | Data B2  |
   +----------+----------+
   | Data A3  | Data B3  |
   +----------+----------+

******************
``tabularcolumns``
******************

(Works only in PDF outputs.)

.. tabularcolumns:: |c|r|

.. table:: Table ``tabularcolumns``

   +---------------------+--------------------------+
   | Header 1 (Centered) | Header 2 (Right aligned) |
   +=====================+==========================+
   | Data A1             | Data B1                  |
   +---------------------+--------------------------+
   | Data A2             | Data B2                  |
   +---------------------+--------------------------+
   | Data A3             | Data B3                  |
   +---------------------+--------------------------+

***********
List Tables
***********

.. list-table::
   :header-rows: 1
   :widths: 1 2

   * - Header A1 (Centre, 1/3)
     - Header B1 (Right, 2/3)

   * - DATA A1
     - DATA B1

   * - DATA A2
     - DATA B2

   * - DATA A3
     - DATA B3

   * - DATA A4
     - DATA B4

*********************
Tables from CSV files
*********************

======
Inline
======

.. csv-table:: Inline CSV
   :header-rows: 1

   Header A1,Header B1
   DATA A1,DATA B1
   DATA A2,DATA B2
   DATA A3,DATA B3

========
External
========

.. csv-table:: Long CSV Table
   :header-rows: 2
   :delim: tab
   :file: include/long-table.tsv
