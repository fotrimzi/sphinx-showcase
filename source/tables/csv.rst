##########
CSV Tables
##########

=====
Short
=====

.. .. tabularcolumns:: |J|J|

.. csv-table:: Short, Plain CSV Table
   :header-rows: 1

   Header A1,Header B1
   DATA A1, DATA B1
   DATA A2, DATA B2
   DATA A3, DATA B3

==========================
Short with Formatted Items
==========================

.. csv-table:: Short CSV table with formatted caption & header (**BOLD**, *ITALIC*, ``CODE``)
   :header-rows: 2

   **Bold Header** *Italic Col* ``Code 1``,**Header** *Col* ``2``
   Header A1,Header B1
   ``CODE``, DATA B1
   DATA A2, DATA B2
   DATA A3, DATA B3

==============
From File
==============

.. csv-table:: Default long (102 row) double-header-row CSV Table
   :header-rows: 2
   :delim: tab
   :file: long-table.tsv

.. csv-table:: Long (102 row) double-header-row CSV Table with ``class: data``
   :header-rows: 2
   :class: data
   :delim: tab
   :file: long-table.tsv

.. csv-table:: Long (102 row) CSV Table with ``class: small``
   :header-rows: 2
   :class: small
   :delim: tab
   :file: long-table.tsv
