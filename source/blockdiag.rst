#################################
Block Diagrams with ``blockdiag``
#################################

Inline:

.. blockdiag::

    blockdiag {
       orientation=portrait;
       node_width = 233;
       node_height = 89;
       default_fontsize = 20;

       p1 [ label="Process 1", numbered = 42 ];
       l1 [ label="Lock ADO A", shape = cloud, textcolor = white, color = "#11557C"];
       m1 [ label="Make the change" ];
       u1 [ label="Unlock the item" ];
       p2 [ label="Process 2" ];
       w1 [ label="Wait for lock" ];
       l2 [ label="Lock ADO A" ];
       r1 [ label="Rollback or fail" ];

       p1 -> l1 -> m1 -> u1;

       p2 -> w1;
       w1 -> l2, l1;
       l2 -> r1;
    }


*****************************
Directory Structure
*****************************

Using external file (:file:`/include/directories.diag`):

.. blockdiag:: /include/directories.diag
   :alt: Server directories
   :caption: Server directories
   :desctable:
