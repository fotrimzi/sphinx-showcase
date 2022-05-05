############
``graphviz``
############

******
Inline
******

.. graphviz::

   digraph {
      rankdir=LR;

      node [shape=box fontsize=9];

      one [label="One"];
      two  [label="Two"];
      tre  [label="Three"];

      one -> two -> tre;
   }


********
External
********

.. graphviz:: _img/graph.dot
   :caption: Graph caption
