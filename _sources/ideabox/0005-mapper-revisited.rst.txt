=====================================================
Things that can be done with an NES mapper, revisited
=====================================================

I've had some enlightening discussions about capabilities of NES
on the NESDEV forums, which has been a cool stretch for my brain.
I find it fitting to summarize resultant findings here, given my
previous ramblings being published close enough.

As always, if someone doesn't care for making new circuits for
old consoles, it's their loss, I guess.

.. contents

Things that should work as expected
===================================

Bigger tile mode, column shifting, palette tile binding or tile row binding,
those would work pretty much as expected.

Background size adjustment would require a bit more of mess, but is doable.

Muxing the bus
==============

It turns out ROM and RAM chips of classic bus kind have actually
kinda slowed down since SNES era, and the ones are close remain
significantly more expensive (since everything moved to more involved
buses). Combined with a variety of possible timing misalignmments,
this makes a single bus design unviable, although some elements could be
approximated; it would take relatively complex circuitry, though.

Secondary background generator extensions
=========================================

A secondary background generator could be adjusted so that it could
show secondary objects merely by tweaking the secondary background tiles a bit more.

Ease of access
==============

A major point to consider is whether a particular design isn't too much
for the NES CPU to handle, unless you add on another CPU, which makes
the considerations significantly less interesting. A nice way of doing
that would be to summarize some of the various properties into overall
indices which could be bound to tile numbers or a reduced count of secondary
property numbers, or both which could be combined together.
I do not have the optimal count of such.

CPU tweaks
==========

While NES CPU lacks the wires which are present in some other members of
6502 family and allow opcode substitution, a slightly dumber technique
is available which also allows it, and so much more. Specifically, you need
to assign more than eight bits of data for eight bits which CPU will read.
I'm not sure about the exact perfect amount and haven't ruled out it being fractional.
The biggest source of acceleration would be injection of "immediates" from cartridge
RAM into the opcode stream.
This could just accelerate arithmetic on RAM values, but it would be most
powerful when abused for address arithmetic.

This trick is not specific to NES
CPU, for the record, and could easily be applied on anything else which
tends to execute code from ROM.

