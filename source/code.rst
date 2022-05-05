###########
Code Blocks
###########

Code blocks can be rendered using any of the following.

**************
``code-block``
**************

.. code-block:: rst

   .. code-block:: <language>

      THE CODE

``<language>`` can be any of those recognised by `pygments <http://pygments.org>`_ or
the word ``none`` if none.

.. seealso::

   Pygments supported languages at http://pygments.org/languages/

******************
``parsed-literal``
******************

.. code-block:: rst

   .. parsed-literal::

      THE (INTERPRETED) CODE

``parsed-literal`` has the advantage of being able to interpret the code
contents as latex or replacement tags (e.g. ``|project|``).

********
``samp``
********

.. code-block:: rst

   :samp:`Some Code ({emphasised})`

``samp`` is useful for inline code highlighting where certain parts can be
emphasised (with italics) by including them in curly braces.

************************
Standard Code Formatting
************************

.. code-block:: rst

   ``Some Inline Code``

This is the simplest way to render code-like inline content.

********
Examples
********

================================
Interpreted (``parsed-literal``)
================================

.. |token| replace:: my replacement text

.. parsed-literal::

   This uses a replacement text: |token|


.. code-block:: none

   This uses a replacement text:

These two should have similar backgrounds, borders and widths, heights and
margins, even though they are created with different directives.


==========
C Programs
==========

Hello World
===========

.. code-block:: c

   #include<stdio.h>

   main()
   {
       printf("Hello World");
   }

*******************
Code Block Captions
*******************

The ``caption`` option to the ``code-block`` directive is now (as of Sphinx
1.5.5) working well, with the exception that the gaps between the caption and
the code block are not well spaced. This makes it hard to see what caption goes
with what block where there are a series of code blocks, as in the following
example.


.. code-block:: none
   :caption: First caption for first block

   First block

.. code-block:: none
   :caption: Second caption for second block

   Second block

.. code-block:: none
   :caption: Third caption for third block

   Third block

.. code-block:: none
   :caption: Fourth much longer and extended caption for fourth block to see how wrapping works and that captions are left-aligned properly with a ragged-right justification.

   Fourth block
