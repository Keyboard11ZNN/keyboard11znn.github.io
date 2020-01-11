===============================================================
How to accelerate C++ compilation without killing preprocessing
===============================================================

.. contents

Motivation
----------

The C++ language is notorious for its long compilation times.
There are two issues at hand that seem to be the primary culprits
in the eyes of internet. Firstly, C++ uses header files, a technology
inherited from C, which amongst its many drawbacks requires the files
to be processed from scratch in every module; secondly, it uses
templates, which need to be instantiated for every type instantiation
in every module.

Currently deployed countermeasures
----------------------------------

The template issue can now be handled in some cases by specifically
mentioning certain templates being explicitly constructed elsewhere,
and then explicitly constructing these templates elsewhere. This requires
further programming prowess compared to just using the templates,
but is a relatively clean solution.

The overall speed of compilation issue is handled by the following
things, which aren't satisfactory in my humble opinion:

- throwing raw power at the problem with a compilation server farm.
  (Google is known to do this.)
- combining separate C++ object files into larger object files.
  This is a huge hack that happens to work sometimes, but explicitly
  prevents certain C++ functionality from being used. It also requires
  smart grouping of concatenated modules to acquire any speed gains;
  the only time saved is on the parts they all use.
- using a common header as a starting state for compilation of all objects.
  This is, actually, less of a hack than the previous take, or at least
  it can be in certain implementations, however its utility is limited.
  The precompiled header, as it is often called, should only cover stable
  elements of the codebase such as unmodified dependences of the project
  and some very well regarded base code, or else it will cause spontaneous
  recompilations of everything.

The ISO C++ committee has decided to come up with a module system,
a C++ take on a modern declaration importing. This is likely to result
in some speed-up regarding repeated parsing of header files, but unlikely
to help with template instantiation compared to status quo.

Existing work and the anti-axiom
--------------------------------

C++ compilation can be sped up in a quite different fashion, if one is ready
to abandon certain assumptions about how C++ build systems work.

If you're using something like GNU Make or Ninja to build a C++ program,
the process is lead exclusively by the timestamps of the involved files.
This is inefficient; imagine if you rename some variables; there's no
need to redo the register allocation in the program, is there. Some existing
build systems took notice and started using filename hashes instead, which
is a good move. Further improvements can be acquired by splitting off
the preprocessing step; renaming internal variables without saving debug
info will still rebuild an object file, but adding a comment will stop that
half-way through.

Today, I present to you the concept of Futomake. Futomake takes the idea
of reusing previous work and takes it up to eleven. However, this requires
further cooperation of the compiler and the build system than typically seen
today. In result, you get equivalent of precompiled headers just working
automatically, and further boost to unity builds, server farms, and modules.
I think.

Futomake core concepts
----------------------

Futomake is based on the idea that the compiler can turn back at the build
system and tell it that actually, it didn't do its full job, but the build
system can finish it by invoking it again in certain ways, possibly more
than one time. This could be actually implemented by compiler taking over the
building wholesale, or by standardizing a way for the hypothetical Futomake
to talk with hypothetical C++ compiler. The other important part is that
Futomake uses hashes to recognize the work that is already done. In fact,
some extra savings are possible by using hashes in places of things other
than timestamps.

The resultant setup is completely compatible with the current source code
relying on preprocessor; this includes, for lack of a better term,
preprocessor "hacks".

A part of the speedup is something we could call "context" and "relevant
context", which is where a technique similar to dependency information
generation comes into play. Namely, the first run of compiler over a chunk
of code can tell us what external entities are relevant to it.

This can involve basically everything; templates, functions, and preprocessor.
I'm going to show you a preprocessor example since a lot of people think
it must be slow, and it's arguably the simplest thing here nonetheless.

A preprocessor example
----------------------

Consider we have two files, a common header and the object file.

The object file, "main.cpp", looks like this::

   #include "header.hpp"
   int main() {
      return 1;
   }


The header file, "header.hpp", looks like this::

   #include <library1.hpp>
   #include <library2.hpp>

At this point, things get a little bit more interesting. "library1.hpp" is::

   #ifndef L1
   #define L1
   int l1();
   #endif //L1

The "library2.hpp", on the other hand, features some preprocessor driven
functionality::

   #ifndef L2
   #define L2
   #ifdef L2_INCLUDE64
   long long l2_64();
   #endif //defined L2_INCLUDE64
   int l2();
   #endif //L2

So Futomake tells preprocessor something along the lines of:

   Hey, preprocessor, preprocess me that "main.cpp"

Then preprocessor replies:

   No can do, but I'll tell you how to.
   Get an initial context of "__FILE__ is main.cpp, __LINE__ is 1..."
   and tell me to preprocess "main.cpp" with that.

So Futomake does just that, and the reply is:

   No can do, but I'll tell you how to.
   First, I preprocessed an empty beginning of the file for you.
   Turns out I did not need __FILE__, __LINE__ or __GNUC__.
   The result is that empty file here.
   The next thing you must do is to preprocess "header.hpp" with context "...",
   then preprocess "main.cpp" from line 2 with context "header.hpp end but...",
   then concatenate these three parts.

This keeps happening inside "header.hpp". The important change is that
preprocessor lists out the tokens it stumbled upon, so that Futomake
knows to rerun it if they change. Which is not really present here since we
start with an include as we often do.

Now, let's consider how stuff... changes if we change stuff in "main.cpp".

If you make the main function do something else, no defines change.
So Futomake, upon a rerun, can skip the repreprocessing of the header.
If it's really smart it can even skip directly to the main function itself,
and if there's something below main maybe it can reuse old preprocessing
for that as well.

If you add a "#define L2_INCLUDE64" at the top, "header.hpp" and "library2.hpp"
will need (maybe partial) reprocessing. That's kind of intended.
But "library1.hpp" won't, since it doesn't include that token, so its inclusion
has the same relevant context; so Futomake will pick the result of the old run.

If Futomake's cache is shared between object files, we just got prepreprocessed
files for free.

Regarding not-preprocessing
---------------------------

The post-preprocessing parser could stop at least at the end of every function.
If it could stop more often, that's great. Combined with extraction of relevant
contexts, this could really speed stuff up.

Global optimization wouldn't gain much from this, but it's often done on the
whole program anyway. Sometimes it could be avoided altogether, especially
if the "concatenation" seen in preprocessor example was replaced with a more
shuffle-friendly process.

Final note
----------

Futomake is obviously a pun on Make programs and sushi.

If it's not clear from being in The Ideabox, I did not code an implementation
of Futomake (yet?). I find the concept easy to understand, but I don't deny
C++ compilers are complicated as is.

