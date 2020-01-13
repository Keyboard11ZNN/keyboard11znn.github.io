===========================================================
Quick and dirty indented language lossless alpha-conversion
===========================================================

.. contents

Motivation
----------

The source specification of computer programs and other things
is, for historical reasons, typically composed of text files.
However, in accordance with modern understanding of code being tidy,
those text files tend to follow multiple rigid structures, which
lowers their information density when compared to storage length. One such
structure is indentation.

Indentation is very useful for viewer of the code, but it comes with
a lot of drawbacks when one considers its direct storage in text files.
The most basic one is that, naturally, it wastes space. This can be partially
mitagated with compression algorithms, but if it wasn't the case those
could do a better job on the rest of the code.

Idea
----

A very simple encoding could be made which would allow lossless compression
of a typical source code file, that would at the same time preserve most
of its non-indentation properties so that dictionary algorithms could
keep doing their jobs. Additionally, this could improve performance of some
diff utilities.

Amongst 128 standard US-ASCII characters, the first 32 are control codes.
Out of these 32, maybe 5 are commonly seen within source code. The rest
could be used to implement the indentation encoding, with one reserved
to preserve their actual occurences if they happened to happen. In fact, this
is such a huge collection of control codes that the indentation encoding
would barely take half of them, and the occasionally used high bytes are
completely absent from our discussion so far; further encoding improvements
are certainly possible; this is an undercooked idea though, so we're going
to focus on indentation encoding.

The indentation in most languages tends to follow a stack-like structure.
A stack of indentation strings seems like a natural pick. It could be
pushed at a start of indentation block, and popped at the end of one.

Most programs tend to follow a simple scheme of indentation levels,
each denoted with a tab character or a constant length space string.
However, there are some exceptions in various styles, and some
ocassional oddities which could use a more varied string, like
blocks of C++ one-line comments. Encoding most used schemes with a single
control code while allowing encoding new ones seems like a fine decision.

There doesn't seem to be a logical reason to allow manipulating
the indentation stack in the middle of a line.

C, C++ and similar languages could achieve further compression by combining
pushing and popping from indentation stack with embedded parentheses, braces,
and maybe brackets.

Python and similar languages could achieve further compression by combining
popping several layers from the stack in a lesser count of control codes.

Problems
--------

While this could be easily implemented as a compression layer in 7-zip style
archive, implementation in version control systems is likely to be hard
due to their embedded difference utilities not expecting the control codes,
especially used in the way presented here.

