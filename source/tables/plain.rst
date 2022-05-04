##################
Plain Drawn Tables
##################

Such tables are 'drawn' as boxes, like this:

.. code-block:: rst

   +----------+----------+
   | Header A | Header B |
   +==========+==========+
   | Data A1  | Data B1  |
   +----------+----------+
   | Data A2  | Data B2  |
   +----------+----------+
   | Data A3  | Data B3  |
   +----------+----------+


And look like this:

+----------+----------+
| Header A | Header B |
+==========+==========+
| Data A1  | Data B1  |
+----------+----------+
| Data A2  | Data B2  |
+----------+----------+
| Data A3  | Data B3  |
+----------+----------+

========================
With ``table`` Directive
========================

Using the ``table::`` directive with a drawn box allows it to be given a title
and to be linked via a ``:ref:`` reference.

The table below is preceded by the string ``.. _table1:`` and can now be
referenced as ``:ref:`table1``` and linked to as :ref:`table1`.

.. _table1:

.. table:: Plain Drawn Table with ``table`` directive

   +----------+----------+
   | Header 1 | Header 2 |
   +==========+==========+
   | Data A1  | Data B1  |
   +----------+----------+
   | Data A2  | Data B2  |
   +----------+----------+
   | Data A3  | Data B3  |
   +----------+----------+

=======================
With ``tabularcolumns``
=======================

Table widths and column alignments can be controlled with the
``tabularcolumns`` directive. This example table is preceded by the text:

``.. tabularcolumns:: |\Yc|\Yr|``

.. .. tabularcolumns:: |\Yc{0.3}|\Yr{0.3}|

.. table:: Plain Drawn Table with ``table`` directive and ``tabularcolumns`` to control alignment

   +---------------------+--------------------------+
   | Header 1 (Centered) | Header 2 (Right aligned) |
   +=====================+==========================+
   | Data A1             | Data B1                  |
   +---------------------+--------------------------+
   | Data A2             | Data B2                  |
   +---------------------+--------------------------+
   | Data A3             | Data B3                  |
   +---------------------+--------------------------+
