########################
Graphs with ``graphviz``
########################

***********************************
Simple Directed Graph (``digraph``)
***********************************

.. graphviz::

   digraph {
      rankdir=LR;

      node [shape=box fontsize=9];

      basic [label="Basic"];
      norm  [label="Normalized"];
      cons  [label="Consolidated"];

      basic -> norm -> cons;
   }


***********************************
External Graph with Embedded Images
***********************************

.. graphviz:: four-eyes-1.dot
   :caption: The Four-eyes Roles
