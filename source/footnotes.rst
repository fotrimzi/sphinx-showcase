#########
Footnotes
#########

Here is an explicitly numbered footnote (1) [1]_.

Since Sphinx 1.3.3 [#]_ , footnotes must be done like this:

.. code-block:: rest

   Text [#]_ 
   
   .. rubric:: Footnotes
   
   .. [#] Text of footnote

The ``[*]`` form no longer seems to work, even though mentioned `here
<http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#footnotes>`_.

Footnotes can be put anywhere in the rst file but it is best to place them at
the very bottom of the file.

Here is a long named footnote [#long]_. It should not roll off the page or onto
the next page.

.. rubric:: Footnotes

.. [1] This is the first explicitly numbered footnote. All others are auto-numbered.
.. [#] Released 2nd December 2015
.. [#long] A long footnote to check that it does not overlap onto the next page, which 
   can be adjusted with the ``interfootnotelinepenalty`` parameter, currently at a value of
   10000. A long footnote to check that it does not overlap onto the next page, which 
   can be adjusted with the ``interfootnotelinepenalty`` parameter, currently at a value of
   10000. A long footnote to check that it does not overlap onto the next page, which 
   can be adjusted with the ``interfootnotelinepenalty`` parameter, currently at a value of
   10000. A long footnote to check that it does not overlap onto the next page, which 
   can be adjusted with the ``interfootnotelinepenalty`` parameter, currently at a value of
   10000. A long footnote to check that it does not overlap onto the next page, which 
   can be adjusted with the ``interfootnotelinepenalty`` parameter, currently at a value of
   10000. 
