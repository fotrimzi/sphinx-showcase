###############################
Examples for use in ``RefCard``
###############################

**************
Explicit/drawn
**************

.. text output can't handle this

.. +-----------------------------+
.. | Future Prices               |
.. +=======+============+========+
.. | DEC02 | 16-12-2002 | 98.595 |
.. +-------+------------+--------+
.. | MAR03 | 17-03-2003 | 96.645 |
.. +-------+------------+--------+

************************
List, CSV, CSV with file
************************

.. list-table:: Table Title
   :header-rows: 1

   *   - Header Column 1
       - Header Column 2
       - Header Column 3

   *   - Data Column 1
       - Data Column 2
       - Data Column 3

.. csv-table:: Zero Rates from Swap rates
   :header-rows: 1

   TENOR,DAYS,:math:`Z_j`
   1Y,367,1.7053%
   2Y,731,2.4095%
