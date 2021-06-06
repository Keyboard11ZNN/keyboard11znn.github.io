===========================================================
Stan whines about widget support for controllers on Android
===========================================================

.. contents

I've been recently gifted an Android variant of Razer Kishi,
a gamepad-esque contraption that can wrap around a modern smartphone,
with a rubbery tape in the middle to adjust for different widths (or heights, when phone is held vertically).
I don't imagine everyone potentially interested
has one already, so here are some thoughts related to trying it out.

Nitpicking on Kishi itself
==========================

Kishi is pretty good. It is not my dream product, but it absolutely delivers on its promise.
I have tried a few platformers, some of which I found absolutely unplayable on a touch screen
given my skills, and the improvement is pretty much what you imagine. The speaker chamber also works.

Things to keep in mind for clones and sequels
---------------------------------------------

There are a few caveats to be aware of that could probably be improved in some sort of Kishi 2:

- The relatively big one is that I need to remove the case from my phone to attach the Kishi,
  and I don't think this is particularly case or phone specific. The USB-C plug is just that short.
  I imagine that many people don't use cases at all, but for me one feels nevessary at least
  when not having the controller on it (we'll get to details later), and the company behind it does suggest to take it off
  while in use to preserve power, as there's no off switch.

- For a somewhat premium product, it does have a lot of frugal properties
  (though it's not that expensive that's unjustifiable given the tape and whatnot):

  - As I just said, there's no off switch.

  - There's an outside USB-C port, but it only does power passthrough.

  - There are also no other ports. Console controllers have almost standardized audio jack connection by now.
    I know Razer helpfully suggests Bluetooth headphones from them and others work fine, but I don't like wireless,
    and the wired connection is a part of appeal of Kishi to me.

  - Speaking of console controllers, Kishi cannot be used as a wireless pad, and less understandably cannot be used as
    a separate wired one.

- I have no idea what the designers were thinking when they laid out non-gameplay buttons (start/select equivalents).

Like I said, nitpicks. There's room to improve, but at what it attempts to do, it's pretty good.

Alternative design ideas, or what you should consider doing instead of cloning Kishi
------------------------------------------------------------------------------------

Holding this device in my hands next to a variety of other gamey things made me sure that I'm actually not a huge
fan of the now standard controller and handheld layout. To be clear, I'm not saying it's a travesty or something,
but I'd rather have more buttons for other fingers and less for thumb than otherwise. If you're making a whole
screened device by yourself, you could even arrange the buttons so that they are there without taking away
the easily marketable screen space by focusing on the back and sides.

If you are NOT making a screened device, then, regardless of whether you try out a less thumb-focused layout or not,
I would suggest taking more looks on the "gaming clip" pads. Now, these existed in a huge variety before Kishi, too.
But I'm talking inspiration here, not necessarily cloning another product. One thing that I'm thinking about is situating
the controller behind the phone instead of below it. I'm imagining something like that all the time when holding my smartphone
by its flipped cover.

Less about more Kishi, more about less touch screen
===================================================

I hate touch screens. If you don't, good for you. In my case, my fingers apparently move a little less precisely
than an average person's or something, so tactile feedback is helpful, but mostly for games. What is REALLY annoying ***ALL THE TIME***
is the interaction between eyes watching the screen, fingers touching the screen, and rest of hand holding it.

Imagine if your mouse cursor was almost always extending to the bottom of the screen, and you are supposed to scroll through big pages by dragging with this huge cursor,
and holding the mouse on the sides too tightly would click, and not necessarily where you point at. That's pretty much how touch screen UIs on phones feel to me.
(That's why the case is such a big deal, by the way -- it eliminates most margin touches by holding.)

This has lead me in the past to curious situations where I would intentionally use the web browser on my original Nintendo 3DS
in spite of it being slow and clunky and having a by-then-modern Android smartphone in the pocket, because it could be controlled with buttons.
Which leads to an interesting question. How do some prominent applications on Android handle gamepads?

You might think they simply won't, but there's a small caveat in that there's a version of Android intended for running on TVs, or running
on devices exclusively connected to TVs. These have their own design guidelines, which involves apps being usable, when possible, with equivalents
of a D-Pad, a confirm button, and a back button. Kishi can seemingly fit into APIs for these, but how well it can do?

(Also, there's accessibility stuff, but I don't even know if there's a connection there.)

I didn't look much at everything, but... here's what I did get.

- Understandably a lot of stuff just ignores everything, or everything but the back button.

- Social media apps *try* to implement something, but it's usually limited to switching big tabs, which renders likes of Facebook unusable.

  - But, Twitter can scroll through tweets, which is appreciated!

- VLC for Android is a particularly weird and interesting case. It has a "mobile device" mode and a separate "TV" mode that you can manually switch in settings.
  The regular mode is a bit like Facebook in that it tries to do something with gamepad inputs, and you can occasionally make it do something, but making
  it do something you want seems harder. The TV mode, on the other hand, seems to work perfectly with the gamepad, but not so much without it, plus it makes
  really bad use of the screen.

  - The TV mode seems to follow Google's developer guidelines about making stuff bigger than on the phones, which given that the phones guidelines are to make stuff
    bigger than on desktop PCs makes me wonder if there's a next step in this evolution.

- Firefox ignores the gamepad completely.

- The Blink browsers I tested, Chrome, Samsung thing and Vivaldi, share the same behaviour. You cannot use the gamepad inputs anywhere near to exclusively.
  Links on pages seem to never work. But, you can scroll the page most of the time with them, which is nice.

  - Reminder: when Vivaldi says they make their stuff separate from Chrome "unlike other browsers", stuff like this is not covered.
    That's not to say they're lying, but they're probably focused on cutting out Google tracking stuff and not, like, rethinking everything.

  - Is there no Chrome for TVs, or is it completely separate?

Well, it's not good, but, you know. It's not like spatial navigation is that easy to implement. It's not like someone is doing it on HTML on Android.

Oh wait, there's Gmail.

Gmail is a bit tricky to assess since I scrolled through my mails instead of YouTube and Wikipedia, but it seems to have working spatial navigation for Links
in marketing, although a bit hard to use since it's not particularly well visible which is highlighted.

Which leads me to non-rhetorical questions.
Does Gmail contain this feature all by itself, while Chrome wasn't blessed with?
Does it use some toolkit that comes with it? 
Does the SYSTEM come with it but nobody else enables it?

Since Google is gonna Google, Gmail application is not open source and I can't just check, but I guess that will just leave me bewlidered.
