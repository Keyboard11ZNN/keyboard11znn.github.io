========================================================================
A calling convention concept for functions with C++-like exception model
========================================================================

.. contents

Motivation
----------

With C++'s biggest advantage compared to competing programming languages
being its high performance, the two features that lower that performance
are understandably controversial, namely RTTI and exceptions. The exceptions
are the less nuanced part of this setup, mostly because they rely upon RTTI,
but for other reasons as well.

The most controversial, as of late, part of the exception conundrum involves
calling conventions. The most direct approach is to embed the return value
in the processor state at every return of a function, and this is the approach
proposed by Herb Sutter. However, Bjarne Stroustrup recently claimed that
this approach was tested in the past and lead to unsatisfactory results
when it came to performance of code which did not stumble upon an exception.

Current practice
----------------

The most heavy-handed convention involves heavy use of C-style stack state
saving functions.

There are two more advanced techniques available for use. On Windows, Microsoft
came up with something called Structural Exception Handling, and on Linux
and friends, something called DWARF-2 Unwinding Tables is present. These
should, theoretically, allow the non-throwing performance of code to reach
the equivalent of little-to-no error checking. However, this doesn't seem to
work very well.

The explanation documents for DWARF-2 Unwinding Tables include a very
peculiar example, where an exception is thrown through a function that
doesn't do anything with it. Given that RAII is a thing now, it looks
like it was not taken into account during DWARF-2 and SEH dessign, resulting
in, effectively, rethrows when a destructor is encountered.

Enter Stan's Dumb Idea
----------------------

Let's have the exception marker without the exception marker. Let's embed it
in the execution state.

This is superficially similar to Unwinding Tables, to the best of my
understanding, but is way dumber in the setup.

#. Find a sequence of bytes which will never appear in compiled code.
   Something involving defined illegal opcodes is ideal.
#. Compile the code mostly as if a marker convention was in place.
   Separate the blocks used exclusively in exception-thrown path
   to avoid them polluting cache while no exception is thrown.
#. After our function, or multiple functions, embed our special not-code
   sequence, and follow it with a differential pointer to the special jump
   table.
#. The special jump table should contain differential pointers to return
   addresses coupled with differential pointers to corresponding exception
   path blocks.

When an exception is thrown, instead of returning directly from function,
we scan the executable code itself and switch the return pointer so that
it goes to the exception path (while the marker convention would contain
a conditional jump at the return point).

This scheme has one obvious disadvantage compared to other setups I can think
of, in that the code page must be readable by the code unless processor has
special support for the type of operation presented here. In fact, I came
up with the whole concept while considering such processor support first,
but that would obviously be useless for milliards of machines deployed today,
while doing in the wizard as shown here wouldn't. However, setting code to
unreadable executable is, from what I hear, a pretty rare setup - I've heard
of hackers stumbling upon it on Wii U and being very surprised.

