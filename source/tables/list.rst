###########
List Tables
###########

The following uses a list table with various ways of specifying columns widths.
Since Sphinx 1.6, there are more ways to specify column alignments and
widths.

Default with table parameter:

``:widths: 1 2``

.. note::

   Can't be used together with ``tabularcolumns``.

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

Default with:

``.. tabularcolumns:: |\Yc{0.1}|\Yr{0.2}|``

.. note::

   Sphinx 1.6.5 only

.. .. tabularcolumns:: |X[c,1]|X[2]|

.. .. tabularcolumns:: |\Yc{0.33}|\Yr{0.67}|

.. list-table::
   :header-rows: 1

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

