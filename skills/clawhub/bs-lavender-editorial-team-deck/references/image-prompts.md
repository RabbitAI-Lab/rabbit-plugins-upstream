# Imagery

## Sources

Follow SKILL.md Workflow step 5 for picture sources, the library question and tools. Only this Skill's library pictures or pictures already made for this deck may be passed as references; never pass third-party, source, or reference-template images, screenshots, or photos of real people. Every pictorial slot gets its own picture with a full text prompt; never show the same photo on two pages. Generate each picture at the aspect that `style-kit.json` lists for its slot (`images[].aspect`); the ratios in the table below are defaults for new slots with no listed aspect.

## Look

Original grayscale editorial photography: soft window light, plain light-grey seamless backdrops or quiet unbranded studios, plain dark clothing, natural confident posture, fine grain. No text, lettering, logos, watermarks, or recognizable real people.

## Slots and framing

| Slot | Layout | Framing |
|---|---|---|
| Cover team photo | `cover-right`, about 653px x 562px | 3:2 or 16:9 group of three to five, centered, heads in the upper third |
| Overview photo | `wide-portraits`, panoramic band | 16:9 working session across a table, faces on a horizontal line at mid height |
| Lead portrait | `lead-photo`, full bleed | 3:2 close-up, subject in the right half, empty backdrop on the left for the title |
| Role portraits | `role-card`, tall columns | 3:4 waist-up portrait, head in the upper quarter, plain backdrop |
| Contact portrait | `close-photo`, tall window | 3:4 waist-up, relaxed, facing slightly toward the title |

## Prompt pattern

"An original black-and-white editorial photograph of [fictional subject and role], [pose and expression], [framing from the table above], plain light-grey seamless backdrop, soft window light from the left, fine film grain, magazine quality, [ratio] composition. No text, no lettering, no logos, no watermark."

Convert results to WebP (quality about 88, long edge at most 1920px), embed them with meaningful alt text, and keep the deck under 20 MB.
