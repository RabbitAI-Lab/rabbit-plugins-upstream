# Image plan

The product is never a photo. Board, burn-up, roadmap, triage, threads,
heatmap, command palette, capacity, velocity and audit log are all HTML, CSS and
SVG rendered from data. Photography appears only where a real developer-tool
site uses it: customer portraits, a customer story, the team, and small avatars
inside the product UI.

## Art direction (append to every prompt)

> Candid documentary photography for a software company website, 35mm lens at
> eye level, soft late-morning daylight from large windows, warm sand, oatmeal
> and muted sage-mint palette with natural oak and pale plaster, gentle
> contrast, natural skin tones, faint film grain, calm and approachable mood, no
> screens facing the camera, no readable text, no logos.

The palette deliberately repeats the site tokens (sand, mint, oak) so photos
sit inside the page instead of on top of it. All portraits share the same light
and the same waist-up framing with the head in the upper third.

## Slots

| id | Role | Aspect / size | Crop focus (`object-position`) | Used in |
| --- | --- | --- | --- | --- |
| `quote-rhea` | Customer portrait | 2:3, 900w; shown 4:5 | `42% 16%` (face left of center) | Quote carousel slide 1 |
| `quote-jonas` | Customer portrait | 2:3, 900w; shown 4:5 | `50% 14%` | Quote carousel slide 2 |
| `quote-amara` | Customer portrait | 2:3, 900w; shown 4:5 | `55% 12%` | Quote carousel slide 3 |
| `quote-kenji` | Customer portrait | 2:3, 900w; shown 4:5 | `58% 12%` | Quote carousel slide 4 |
| `qf-rhea`, `qf-jonas`, `qf-amara`, `qf-kenji` | Face thumbnails | 112px square, cropped from the portrait masters (440px square around the face) | centered face | Carousel thumbnails, sign-up quote |
| `story-vantri` | Customer story / editorial | 3:2, 1600w | `62% 40%` (presenter and wall) | Home story card; cloned at runtime into the story route hero (16:8) |
| `team-tracklane` | Team | 3:2, 1600w; shown 16:8.4 | `50% 46%` | About route |
| `avatars` (source only) | Contact sheet, 3x3 | 1:1, 1024w | n/a | Cropped into 9 avatars, not shipped |
| `av-lucia` ... `av-amaya` | Product UI avatars | 112px square | centered face | Board cards, thread, project lead, sales contact |

Avatar crops (from the 1254px master, 294px squares centred on each face):
Lucía (top left), Tobi (top center), Mara (top right), Daniel (middle left),
Noor (middle center), Felix (middle right), Ingrid (bottom left), Owen (bottom
center), Amaya (bottom right). Use `cwebp -crop x y w h -resize 112 112`.

## Exact prompts

**quote-rhea** (portrait): Environmental portrait of a woman in her mid-thirties
of South Asian descent who leads a platform engineering team, shoulder-length
dark hair, wearing a rust-colored fine knit sweater, standing beside a pale
plaster wall next to a tall fiddle-leaf fig, arms loosely folded, warm genuine
half smile, looking just past the camera, waist-up framing with her head in the
upper third, shallow depth of field with a quiet open-plan office softly blurred
behind her.

**quote-jonas** (portrait): Environmental portrait of a man in his early forties
of Northern European descent who is an engineering manager, short beard with
grey flecks, wearing a navy overshirt over a white t-shirt, seated on a low oak
bench in a sunlit studio office with shelves of books and trailing plants
blurred behind him, forearms resting on his knees, calm friendly expression
looking toward the camera, waist-up framing with his head in the upper third.

**quote-amara** (portrait): Environmental portrait of a woman in her late
twenties of West African descent who is a product lead, natural coily hair tied
up, small gold hoop earrings, wearing an oatmeal linen shirt, leaning against a
deep windowsill in a bright studio with a sage-green painted wall and a board of
blank pastel sticky notes softly blurred behind her, laughing lightly and
looking slightly off camera, waist-up framing with her head in the upper third.

**quote-kenji** (portrait): Environmental portrait of a man in his early
thirties of Japanese descent who is a staff engineer, short black hair, round
tortoiseshell glasses, wearing a moss-green crewneck sweatshirt, standing in a
quiet corridor of a warm minimalist office with oak slat walls and a tall window
casting soft side light, hands in pockets, thoughtful relaxed smile, looking at
the camera, waist-up framing with his head in the upper third.

**story-vantri** (landscape): A product team of five people in a weekly planning
session around a long oak table in a sunlit loft office, one person standing at
a wall of blank pastel sticky notes arranged in neat columns while pointing at a
column, the others seated with closed laptops, paper notebooks and coffee cups,
plants and tall steel-frame windows, candid moment mid-conversation, wide shot
at eye level, nobody looking at the camera.

**team-tracklane** (landscape): Relaxed group photo of the eight-person team of
a small software company gathered on and around a long wooden bench in their
bright studio office, mixed ages, genders and backgrounds, casual clothing in
muted earth and sage tones, most smiling at the camera, natural light from tall
windows on the left, potted plants and a pale plaster wall behind, wide framing
with generous space above their heads.

**avatars** (square): A contact sheet of nine head-and-shoulders portraits
arranged in a precise 3 by 3 grid of equal square cells separated by thin,
perfectly straight off-white gutters, each cell showing a different adult
(varied ages, genders and ethnicities) centered and facing the camera with a
relaxed friendly expression, every person against the same plain warm
sand-beige studio backdrop, identical soft daylight and identical framing in
every cell, no borders, no numbers, no captions.

## Rules when adapting

- Keep the slot list short (6 to 8 generations). Regenerate anything with text,
  logos, visible screens, extra fingers, uncanny faces or a mis-placed head.
- Laptops in photos stay closed; screens are never the subject.
- `<img>` gets meaningful alt text, `width`/`height`, `loading="lazy"` below the
  fold and `decoding="async"`. Avatars are CSS background classes with
  `role="img"` and an `aria-label` where they carry meaning.
- Reference each file once in the source (CSS class or one `<img>`) so inlined
  demos do not duplicate data.
- Images were generated for this Skill; replace them with the user's own
  photography when available, keeping the same roles and crops.
