==================================================
Stan whines about zero register (mostly in RISC-V)
==================================================

As if stuff written here wasn't esoteric enough, this rant is about
an amateur's understanding of assembly programming. Viewer discretion
is advised.

.. contents

But what is zero register? (or, the strawman, maybe)
====================================================

The weird part of zero register talk is that CPU instruction sets
with those tend to have some differences in what exactly a zero
register is. So, AArch64 ISA (what a name, by the way) has some
instructions having access to a zero while others use a similar
encoding for stack pointer, while PowerPC has certain memory
operations treating one of the registers as zero while others
treat it as a regular register.

This is confusing, but whoever came up with such schemes has clearly
realized that. It's not really different from having a weird encoding
for operations involving zero, and an extra register that's usable
for some other things. Not the worst thing in the world, has advantages,
has disadvantages.

What is specifically befuddling to me is the real deal zero register.
Here's how I define that one:

- It's an entry in general registers bank present in all instructions.
- It can be "written to", and the results are ignored.
- And of course, it always reads as zero.

This seems to be, at a glance, what RISC-V and MIPS instruction sets use.

Zero register advocacy
======================

There is one (1) advantage of a zero register presence that I am aware of,
namely that it allows the CPU designers to remove certain operations in favor
of more complex operations that are already implemented anyway doing their
job. A standard example is replacing a register-to-register move by an
addition involving a zero, assuming you have a separate destination operand.

Strawland
=========

To be completely fair to zero register, it makes sense if you are making
a really, really tiny processor, that lacks all sort of instruction
transformation madness that most processors a typical coder recognizes
as such have deployed.
So, to reiterate, it's an okay design trick if you're trying to fit
a 32-bit CPU into least transistors possible or something. In that sense,
it's a bit like a branch delay slot.

Both RISC-V and MIPS claim they are not exclusively
targeting such environments. Well, MIPS is mostly historical now, but some
people are trying to push RISC-V as the challenger to ARM of all things.
So, if you have aspirations for your core to be performant,
I should present the case that a zero register is a waste of opcode space,
and RISC-V is just full of examples why.

Stan's arguments against zero register
======================================

Immediates
----------

Do you have variation opcodes with constant arguments? Do these arguments
include zero? If they do, that's a natural way of encoding operations
involving a zero argument, if you absolutely have to.

RISC-V has immediate encoding for most of its baseline instructions, by the way,
and recommended way to encode a register-register move is with one of those.
But it still has a zero register.

Discarded data operation results
--------------------------------

There are two ways this can go.

- Your CPU has a flags register that your instruction updates. You save
  yourself from having an equivalent compare opcode, sure. I don't think
  that's a lot, but it's something.

- Or, your instruction doesn't affect the flags register. Maybe your CPU
  doesn't even have a flags register. In which case, you can now encode a NOP
  with every instruction that normally writes to GPR. Go you.

It may interest you that RISC-V doesn't have a flags register. It uses
compare-and-branch instructions instead, where zero register is somewhat
useful as an argument.

A special case is when you discard a load operation result. Which is...
a rather esoteric thing, unless you're doing complex decoding and interpreting
it as a prefetch, I guess?

The power of zero in core data operations
-----------------------------------------

Here's a table that I believe makes my statement pretty clear. It doesn't
get into details and a lot of operations have variations that aren't elaborated
upon here, but that, in my opinion, would just strengthen my case that the zero
value is actually not that useful. I've included some further stuff involving
parameter symmetry to showcase how it could be abused to encode more ops in less bits.
(There's no 0 @ 0 consideration since it's rather obvious except for division.)

============== ============ ==================== ================= ===========================
Operation      Symmetrical? A @ 0                0 @ A             A @ A                      
-------------- ------------ -------------------- ----------------- ---------------------------
Addition       yes          copy                 copy              potentially useful (A << 1)
Subtraction    no           copy                 useful (negation) zero
Multiplication yes          zero                 zero              useful
Division       no           NaN or runtime error zero              one
Bit OR         yes          copy                 copy              copy
Bit AND        yes          zero                 zero              copy
Bit NAND       no           copy                 zero              zero
Bit XOR/EOR    yes          copy                 copy              zero
Bitshifts      no           copy                 zero              something unusual
============== ============ ==================== ================= ===========================

So for the purpose of those core data manipulation operations,
operations involving zero register have, like, three types
of useful results total. And if you have three-argument operands
everywhere, then copying and zeroing are already possible to handle
with bit functions. Zero turns out to be most useful in case of
being the first argument of subtraction, which is usually comparable
to the compare-and-branch case discussed earlier.

To be fair, it's entirely possible that your simple CPU implements some more complex
operations. For instance, you could compute a shift as a combined shift-add with a zero add.
(Same about adding, but that usually has an immediate mode for shift amount.)
This is not the case with RISC-V. It has separate shift and add instructions.

Adressing a'la mode
-------------------

Here's where I think the zero register really comes from, although it's all speculation.

#. Someone comes up with the RISC philosophy of having simple instructions
   instead of complex ones.
#. This turns out to be somewhat successful for data processing operations,
   but in comparison to established CISC processors, loads and stores are
   problematically slow.
#. Load and store operations also happen to have two register arguments.
   Most RISC operations have three.
#. It turns out that performance improves if you can do more complex stuff with
   registers to compute addresses, but that makes the whole RISC setup sound pick
   and choosey.
#. Someone decides that having a mode involving (possibly scaled) register sum
   and a zero register is a decent compromise, and tries to justify it after the fact.

This is based upon the whole PowerPC thing where zero register is normal sometimes.

RISC-V doesn't do this, to my knowledge. It has a single mode, but one
with immediate offsets. The zero register can instead be used as a base for such an
immediate offset, which is useful, unless your system uses address space layout
randomization and doesn't want you to have any hardcoded addresses. Most operating systems
want ASLR nowadays, though you can disable it if you're feeling like voiding warranties.
Microcontrollers that don't run operating systems are a bit more likely to make use of it.

Conclusion
==========

The RISC-V implementation of zero register turns out to be useless for vast majority
of its data manipulation opcodes. The load/store usage of such seems to be limited
to microcontroller context where "zero page" is not affected by ASLR. The major
exceptions in the set of expectedly common instructions are some uses with subtraction
and the compare-and-branch opcode, which could probably be handled well in other ways.

Zero register in general may not be particularly hard to include in a processor,
but the rewards are pretty close to zero unless you're really thin on decode space.
Even then, there are alternative tricks that you can use and keep that register
number for actual variables. Try it, please.
