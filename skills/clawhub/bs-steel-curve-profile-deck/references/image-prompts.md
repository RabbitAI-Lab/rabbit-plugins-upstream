# Image prompts

## Picture policy

SKILL.md Workflow step 5 is the only picture policy: user pictures first, then the library question, then generation with the tools it names. When you generate, write a full text prompt for every picture, one request per scene, at the `aspect` that `style-kit.json` and the compose report list for the slot (landscape 3:2 or 16:9 is only the default for a new slot with no listed aspect). One or two pictures from this Skill's library or pictures already made for this deck may be passed as style references so the series keeps one look. Never pass third-party, source, or reference-template images, screenshots, or photos of real people as inputs.

Each semantic page needs its own picture; never repeat one photo on two pages. Keep the finished deck under 20 MB.

## Shared style line

Append to every prompt: "Photorealistic editorial photograph, bright daylight, steel-blue (#456b83), white, and pale ice-blue palette, clean modern architecture, calm premium mood. No text, no signs, no logos, no readable screens."

## Scene briefs by slot

- Cover (`.cover-art`, tall crop on the right): a contemporary glass-fronted building at street level or seen from below, a few people entering, lots of sky.
- Introduction (`.intro-art`, portrait crop): two colleagues at a bright desk, close framing, faces in the center third.
- Foundation (`.arch-left`, wide crop): a small team planning around a shared table, subjects centered low in the frame.
- Reach (`.arch-right`): an interior with few people, such as a lounge, lobby, or floor plate, with generous empty foreground.
- Workflow (`.bleed-left`, tall crop): people walking through a workspace, subjects in the center third so a dark card can overlap the lower left.
- Team (`.team-art.a` / `.b`): two different on-site roles, for example a facilities walk-through and a reception welcome; keep subjects centered.
- Closing (`.closing-art`): a relaxed meeting or handshake moment, subject on the left half.

Avoid uniforms with badges, brand colors of real companies, identifiable landmarks, and real people.
