===========
Sphinx hack
===========

The Sphinx software, which I'm using to process this website, is supposed
to be used to write software manuals. This is mostly a superset of what one
needs to write something more freeform, but there's a few exceptions. Mostly,
displaying stuff newest-up for the re-visitors.

I've repeatedly read the Sphinx documentation's chapter on constructing
a "todo" extension, and after an interval of wrestling with Python I got the
following piece of... spaghetti? Maybe it's more of a cheesey lasagne.

.. literalinclude:: ../_ext/k11specials.py
   :language: python3

