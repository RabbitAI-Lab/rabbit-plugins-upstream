# Image briefs

## Sources

Follow SKILL.md Workflow step 5 for picture sources, the library question and tools. Only this Skill's library pictures or pictures already made for this deck may be passed as references; never pass reference slides, third-party or source images, screenshots, someone else's artwork, or photos of real people. Write a full text prompt for every picture, one distinct scene per semantic slide. Generate each picture at the aspect that `style-kit.json` lists for its slot (`images[].aspect`); the sizes in the aspect table below are defaults for new slots with no listed aspect.

## Marker illustration (default for most pages)

Append this style block to every scene description:

> Hand-drawn editorial illustration in loose black ink marker lines with flat mint green fills (hex #3eaf9d) used sparingly on clothing and a few objects, everything else left as warm off-white paper (hex #f1f0ec). Friendly cartoon people with simple round faces, dot eyes, rounded bodies, natural diverse looks. Clean plain off-white background that fills the entire canvas edge to edge, no border, no frame, no shadow, no texture, no text, no letters, no numbers, no logos.

Scene ideas: neighbors building something at a shared table (cover), a person looking into an empty room with a toolbox (manifesto portrait), two people showing a finished object (split), a host at a planning board (timeline sketch), a calm doorway welcome (challenge page), a seated circle with tools on the floor (roles), a small group waving and holding the result (closing).

For an accent page, ask for "a flat mint green (hex #3eaf9d) background filling the whole canvas" instead of off-white.

## Aspect ratio per layout

| Layout | Slot | Generate |
| --- | --- | --- |
| Cover | `.cover-art`, top band, right-aligned | landscape 1536x1024, figures in the lower two thirds |
| Manifesto | `.intro-art`, full-height right window | portrait 1024x1536, empty paper at the top |
| Split, challenge, closing | `.split-art`, `.challenge-art`, `.closing-art` | landscape 1536x1024 |
| Strategy (accent) | `.strategy-art` | landscape 1536x1024 on mint |
| Timeline, roles | `.timeline-sketch`, `.gathering-art` | landscape 1536x1024, wide and low |

## Photo band

> A candid editorial photograph of adult hands working together around a plain wooden worktable with simple hand tools, offcuts, paper sketches and a half-built shelf. Warm natural daylight, understated mint accents, realistic anatomy and materials. Wide horizontal composition with useful detail through the middle band. No faces in focus, no logos, no readable text, no watermarks.

Use it only for `.photo-band` (full-bleed lower half of an accent page). Keep headings and labels outside the image.

## Embedding

Convert to WebP (quality about 88 for illustrations, 90 to 95 for photos, long edge at most 1920 px) and inline as a data URI so the deck stays offline. If an illustration's paper color differs slightly from `--paper`, shift the flat background to the exact slide color so no rectangle edge shows. Keep the complete deck under 20 MB. Speaker notes may say an image is illustrative; never imply it documents a real event.
