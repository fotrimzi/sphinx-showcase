##############
Spell Checking
##############

``aspell`` is used in ``SGML`` mode to spell check the single HTML output file.

Tags to ignore are listed in the ``.aspell.conf`` file, part of the ``ac-doc`` package.

This section tests each filter.

Only these 4 words should appear in the spell check output (:file:`_logs/spell-check.txt`):

#. Curageously
#. Hipnotised
#. Nethertheless
#. Inconsequenshal

This item will not fail, because it is part of a URL link (HTML anchor).

#. `blahdeblah <http://www.asset-control.com>`_

.. note::

   Anchors (``<a>``) were included in the aspell skip list due to the large
   number of auto-generated links to C-API and FE functions.

The remaining items below are also exempt from checking.

*******
``pre``
*******

``supercalifragilisticexpialidocious``

********
``code``
********

.. code-block:: none

   idontbelieveitsoyoushouldnteither


********
``href``
********

`Link to address <http://www.asset-control.com>`_