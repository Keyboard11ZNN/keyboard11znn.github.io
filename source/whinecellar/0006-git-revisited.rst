===========================
Stan whines about Git again
===========================

For the past year or so, I've been using Git daily. Remember when I wrote
that could lead to reevaluation of some of my comments? Let's see if that
checks out.

.. contents

Expectations vs. reality
========================

It turns out Git can handle non-text stuff relatively okay. It understandably needs
some help with merging it, and yes, you can set it up so that this happens automatically.
This does not really help with chicken and egg problem, but it's something.

The Windows-related conundrums should really be evaluated separately. Interestingly,
I've tried to avoid using Windows at work when possible due to, uhm, corporate systems
slowing down absolutely everything, so the part where Git works better on Linux
may have been an advantage. Usage of filesystem as database has... disadvantages,
but things could be worse. The tool separation? That part causes real problems.
Most often, a separate tool updates and I don't realize that affects Git in some
(presumably negative) way. SSH is somewhat stable; GPG loves to change key formats
for unknown reasons.

Rebases are as annoying as I expected them to. When your boss doesn't use them, everything
is fine. When your boss uses them, things go awry. Thankfully, the part about your boss
wanting you to rebase stuff can be relatively painless thanks to temporary branches.

New stuff
=========

Well.

Merging conundrums
------------------

This has as much to do with Git as with indentation in general, but some relatively trivial
merges fail because of the two being involved. Throw an automatic linting tool which likes
to align stuff into the mix and this stops being theoretical. Granted, that's also on the tool,
but it's annoying and makes me wish for binary source code again.

Worktrees and submodules
------------------------

This is a legitimate bug brought out of design scope extension. Basically, two of major powerful
Git features happen to be incompatible with each other, and no one cares. No one cares, because
top Git users don't really use worktrees, which is at least in part because they're incompatible
with submodules. Chicken, anyone?

However, submodules are not that big of a deal, because of...

Customizations specific to huge users
-------------------------------------

The really huge players in the development league deploy their own "enhancements" to submodule
system. Most notably, Google has came up with some "gclient" thing, which... I do not exactly
understand what is it that it does differently than submodules would. This would be a good moment
to attack Google for doing such things, since they really like customizing everything, but
in this case, they're not alone. What is particularly apathy inducing is that maybe some of those
customizations just smooth things out and stock Git is enough to handle related projects,
but good luck figuring out which ones are those and which ones are more complex without wasting
loads of time.

Summary
=======

No. Just no.
