####################
Custom Class Options
####################

As of Sphinx 1.6, table customisation can be done with files in ``_templates``.
This avoids the need for the ``ac_table.py``, which was preventing regular updates
of Sphinx.

The options are given via the table directive's
``:class:`` argument and are shown as follows:


.. ``rwshade``
..   Data row alternate shading ON (default: OFF)

``small``
   Small table text size (default: normal)

``data``
   A synonym for ``small`` (for backward compatibility with data-team tables).

.. .. table:: Plain Drawn Table with ``table`` Directive and ``class`` options: ``rwshade``
..    :class: rwshade

..    +----------+----------+
..    | Header 1 | Header 2 |
..    +==========+==========+
..    | Data A1  | Data B1  |
..    +----------+----------+
..    | Data A2  | Data B2  |
..    +----------+----------+
..    | Data A3  | Data B3  |
..    +----------+----------+
..    | Data A4  | Data B4  |
..    +----------+----------+
..    | Data A5  | Data B5  |
..    +----------+----------+
..    | Data A6  | Data B6  |
..    +----------+----------+

.. table:: Plain Drawn Table with ``table`` Directive and ``:class: small``
   :class: small

   +----------+----------+
   | Header 1 | Header 2 |
   +==========+==========+
   | Data A1  | Data B1  |
   +----------+----------+
   | Data A2  | Data B2  |
   +----------+----------+
   | Data A3  | Data B3  |
   +----------+----------+


.. list-table:: List Table with ``tabularcolumns`` and ``:class: small``
   :header-rows: 1
   :class: small

   * - Header A1
     - Header B1

   * - DATA A1
     - DATA B1

   * - DATA A2
     - DATA B2

   * - DATA A3
     - DATA B3

   * - DATA A4
     - DATA B4
