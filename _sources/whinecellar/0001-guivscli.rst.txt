=============================
Stan whines about GUI vs. CLI
=============================

.. contents

There's a bit of a consensus dichotomy between Graphical User Interface
programs and Command Line Interface programs that doesn't seem to me
like it has a good reason to exist. Usually, GUI programs allow less
sophisticated manipulation of the program, while CLI implies sophistication
overload.

However, this is not the fundamental difference between the two. Nor is
presence of mouse controls, nor even the presence of graphics - the term
TUI exists for a good reason, and I would guess it is way closer to GUI
than CLI not in the name only.

What really made GUI take off is the guiding hand it offers in telling
you what the possibilities of the program are in the first place, without
the need to explicitly say much.

Consider a graphical program launcher, a Start menu if you, like me, come
from a Windows background, but I am aware there are many equivalents that work
just like it. There's a list of programs. They may come in folders, but
that's not really important, one could do something similar with shells.
This program is here, and this one, and this one, and maybe you need to scroll
a bit to see them all, but one is given just enough information to launch
every single one of them.

On the other hand, the equivalent usable on the shell is naming the program.
If you're a shell guru, you probably can figure out what is installed by
echo-ing $PATH and doing a bunch of ls-es. Except, that implies you know
echo and ls are installed, and shell behaves normally and uses $PATH, etc..
If you come with little knowledge, CLI is as unfriendly as possible without
being actively hostile.

It is relatively likely that your terminal does something about unfound
programs, actually, and asks you if you didn't mean something similar.
The problem is that this work isn't done yet. Programs have options
that can behave in various ways. Even assuming you didn't stumble upon
one of the exceptional programs that does arguments in a completely different
way than everyone else - for instance, tar and 7z use unescaped command words
that would typically indicate a file - if you are not aware of the standards
in the first place, they don't help.

Meanwhile, the graphical 7-zip shows you a set of buttons. Of course, you can
suppose that some button is hidden until you spin the mouse cursor in a
special way, but you can similarly imagine a CLI program which wants its
arguments in as Caesar-encoded Roman numerals.

There are several things that the GUI programs typically cannot do. To stick
with 7-zip example, it offers less complex control over compression options
when compared to its CLI sibling. But does it have to? No! Someone just decided
that everyone interested will be capable of using the CLI version, which
is plain untrue.

Of course, CLI is perfect for certain purposes, such as writing shell scripts.
This doesn't mean we can get everyone on the command line train. For regular
invocation of programs, it's an insanely cranky tool, and should never be
an only option.

