==========================================
Things that can be done with an NES mapper
==========================================

.. contents

The Nintendo Entertainment System, its Japanese predecessor Famicom,
and a bunch of clones of these video game machines have a cartridge
setup featuring two completely separate adressed data buses. This
design is found quite often in arcade machine cartridges, but not
so much in home hardware (excluding Neo Geo if you count it). It is
unclear whether this was simply meant to skip copying data to RAM
connected to the secondary bus, as was the case in arcade machines,
or were the designers already envisioning what actually happened:
game developers started putting some pretty crazy circuitry inside
the carts. While other systems had cartridges with enhancement chips,
on the NES a comparatively big portion of the library has something
more complicated than a simple bank mapper, even if it's a simple
IRQ generator. Regardless, the name "mapper" stuck.

The point of this page is to explore what could be done with this
system. I probably won't be able to make my own overpowered cartridge,
but I've spent way too much time at night thinking about the possiblities
to do nothing with them.

Context (basics)
----------------

The NES has two "big" buses connected to the cartridge. The CPU
bus has 16 address wires and 8 data wires, except the top address
wire is weird, but it can be worked around if necessary. Additionally,
there's a read-or-write wire. The PPU (graphics chip) bus has 14 address
wires, 8 data wires and the direction wire, plus extra two wires that
allow you to activate one of two on-board PPU RAM slots which are kilobyte
long.

There are some differences between systems. Famicoms and derived clones
include two wires that allow you to mix in some sound (although reliability
of this approach on clones is expectedly iffy).
NES replaced those with some DRM chip wires and ten "extension" wires,
which in early systems connected to an extension slot, but no official
hardware for that thing ended up being released. It appears that the NES
was designed during the short time Nintendo thought they could transition
Famicom software to FDS format, which didn't end up happening, and thus
international audio circuitry was moved to slot that was abandoned.

Most home cartridge systems ended up with some sort of address mapping
circuitry on cartridges, but the PPU bus being connected to the cartridge
presented some unique possibilities.

Historical use of PPU bus
-------------------------

Before the circuitry madness started, there were, generally speaking,
two standard ways to design NES cartridges. Either you connected
extra RAM for texture access to the system and treated the whole thing
like any other cartridge console at the time, or you plugged in a separate
chip with patterns burnt in and didn't touch them; in either case, you then
plugged on-board RAM into where PPU wanted tilemaps. The latter point
was rarely touched upon, for one reason or another.

The major step forward was putting a slot mapper on PPU side (controlled
by CPU regardless). This allowed modifying the pattern availability to PPU
really fast. (Note that NES had a DMA, but only for sprite definiition table.)
In combination with either carefully written code or an IRQ generator on
CPU side, it was, in fact, possible to switch the banks mid-frame. Fun fact about
IRQ generators: the PPU bus access allowed realively easy scanline counting.

Because PPU accessed the memory in a very predictable pattern, a few games
went a bit further. A relatively simple trick involved pattern which switched
the bank mapping when accessed, eliminating the IRQ overhead for predictable
cases. However, further trickery was developed, such as shadow tilemaps
with bank information and in case of one chip from Nintendo, higher precision
background color information. (The PPU used 8x8 background tiles, but palettes
for tiles were selected in 16x16 tile clusters, and they were easier to manipulate
in 32x32 clusters; however, it then proceeded to re-read those for each and every
tile, which I can't decide what to think of). Distinguishing whether patterns were
requested for background or sprites by timing measurement was also implemented.

Things that can be done with PPU bus
------------------------------------

Well, you can just send arbitrary 256x240 2bpp bitmaps onto the screen directly
from the cartridge, if you want to, and throw in a Core i7 for game logic, but...
you know. Overkill.

Things that could have been done with PPU bus
---------------------------------------------

If your point would be to make something that could realistically be done in the
eighties, relax, because there are a lot of possibilities that weren't touched
yet remain completely viable.

* The column offset mode available on SNES and Mega Drive is backportable
  without any particular issue, and in fact with a possibility of removing
  the border column problems present in those. Further trickery is possible by
  changing those offsets mid-frame, which could maybe be automated.

* Background tiles can be given arbitrary vertical size and multiplied
  horizontal size.

* Palette indices can be given to individual rows of patterns. This would
  be easier to use by the game code as per-tile description rather than
  secondary palette background map getting more detailed than regular
  tilemap itself, I think?

* A secondary background pattern can be injected into empty background
  data. This is not a full secondary background, but it would have its uses.
  Think of it as tile animation parallax trick taken up to eleven. You could
  maaaaaybe add more sprites this way, but that stretches even my believability.

* The background maps themselves could be given less annoying dimensions.

The NES specific CPU bus tricks
-------------------------------

The regular math acceleration tricks, bank mapping and auto-increment registers
are there. Unfortunately opcode injection doesn't seem particularly viable.
There are a few ingenious uses of the standards in connection to audio subsystem
(although on Japanese systems you can just mix in your stuff),
but the PPU connection remains the source of most possible hackery.

* You can DMA or maybe even bank swap pattern and background definition data without
  involvement of system hardware. Note that this can't be done with sprite definitions
  or palettes, even though the latter hypothetically lay in PPU bus space.

* Text blitter! That is more due to the pattern format being complex, but it's a possibility.
  You could also blit other stuff, I guess.

* Sprite definitions transform, linked with bank mapping to achieve arbitrary
  sprite banking.

The most general trick
----------------------

While in the eighties, CPU bus and PPU bus chips were separate, you may consider actually
merging them and demultiplexing if your current circuitry is fast enough as a cost saving
measure. Instant bus shift is just a bonus.

Extra notes on Neo Geo
----------------------

Very few of the ideas here seem applicable to Neo Geo. You may wonder why. Well, basically,
Neo Geo has a dedicated foreground tilemap that doesn't really link to the cartridge at all,
and everything else is done with sprites. This means there's little to do with background
definitions, although you could still implement a sprite definition transform connected to
bank mapping or pipe data to audio bus.
