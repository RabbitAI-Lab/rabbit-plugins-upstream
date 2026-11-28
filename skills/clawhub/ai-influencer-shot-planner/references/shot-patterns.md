# Shot patterns

Five formats. Each one is short on purpose: a format earns a repeat by being
cheap to make and easy to recognise in the feed.

Every pattern shares three beats. **Hook** in the first second, **turn** at the
cut, **payoff** before the loop. If a shot does not do one of those, cut it.

Character sheet tokens are written as `<CS>` below — copy the real sheet in, verbatim.

---

## 1. Outfit change — 3 shots, 8s

The strongest format for a character who sells style. One locked camera, three
wardrobes, three hard cuts. The face must not move; only the clothes change. This
is exactly the `Elevator outfit change` template's shape.

| # | Sec | Framing | Action | Camera |
|---|---|---|---|---|
| 1 | 3 | Medium, eye level, mirrored interior | Stands, adjusts a sleeve, looks off-frame | Locked |
| 2 | 3 | Identical | Same pose, second outfit, meets the lens | Locked |
| 3 | 2 | Identical | Third outfit, steps toward the door | Locked |

Image prompt, shot 1:

```
<CS>, wearing a bronze sequin slip gown, standing inside a mirrored elevator
at night, warm overhead light from above the door, 35mm, medium shot at eye
level, realistic fabric sheen and skin texture, no text, no watermark
```

Shot 2 and 3: copy it and change **only** the wardrobe clause and the action.

Motion prompt, all three:

```
She holds her pose and makes one small adjustment; camera locked; the elevator
light and framing stay fixed across the cut
```

Why it works: the cut does the storytelling, so the model only has to keep a
still person still.

---

## 2. Café or bar reveal — 2 shots, 6–8s

Cheap, calm, and it reads as "a real person's afternoon" rather than an ad.

| # | Sec | Framing | Action | Camera |
|---|---|---|---|---|
| 1 | 4 | Close, shallow depth | Hands wrap a cup, face out of focus | Locked, then rack focus |
| 2 | 3 | Medium | Looks up and holds the lens for half a beat | Slow push in |

Image prompt, shot 1:

```
<CS>, hands around a white espresso cup on a marble café table, face out of
focus behind steam, late afternoon window light from the left, 50mm at f/2,
shallow depth of field, realistic skin texture, no text, no watermark
```

Motion prompt, shot 1: `Focus pulls from the cup to her eyes; camera locked; the window light does not change`

---

## 3. Street walk — 1–2 shots, 5–8s

The format to use when the character's presence matters more than the story.
One shot is enough; two if you want a wider establishing beat.

| # | Sec | Framing | Action | Camera |
|---|---|---|---|---|
| 1 | 6 | Full, slight low angle | Walks toward lens, coat moving, passes the camera | Handheld drift |

Image prompt:

```
<CS>, full body, walking toward the camera on a narrow city street in early
morning, low sun behind her rimming the coat, 35mm, slight low angle,
realistic motion blur on the coat hem, no text, no watermark
```

Motion prompt: `She walks forward at an even pace and exits past the lens; camera drifts with a slight handheld sway; street and light stay fixed`

---

## 4. Get ready with me — 3 shots, 8–12s

Best format when the post needs to mention a product without looking like an ad.
Keep hands and face doing different things in each shot so the cuts read as time
passing.

| # | Sec | Framing | Action | Camera |
|---|---|---|---|---|
| 1 | 3 | Close on hands | Picks up a bottle, unscrews the cap | Locked |
| 2 | 4 | Medium, mirror | Applies it, checks the reflection | Locked |
| 3 | 3 | Close, eye level | Looks at the lens, small nod | Locked |

Image prompt, shot 2:

```
<CS>, seated at a dressing table facing a round mirror, applying serum with
two fingers, warm side light from a window on the right, 50mm at f/2, medium
shot from behind her shoulder, realistic skin texture, no text, no watermark
```

Motion prompt: `She applies the serum in one slow stroke and glances at the mirror; camera locked; mirror reflection and light stay fixed`

---

## 5. First bite — 2 shots, 6s

Reaction format. The trick is that shot 1 never shows the face; the payoff is
entirely in shot 2.

| # | Sec | Framing | Action | Camera |
|---|---|---|---|---|
| 1 | 3 | Close on hands and plate | Lifts a fork, food in frame | Locked |
| 2 | 3 | Close on face | Bites, eyes widen slightly, nods | Locked |

Image prompt, shot 2:

```
<CS>, close-up at eye level in a small restaurant at lunch, fork near her
mouth, warm side light from a window on the left, 85mm at f/1.8, realistic
skin and lip texture, no text, no watermark
```

Motion prompt: `She takes one bite, chews once and gives a small nod; camera locked; the plate and window light stay fixed`

---

## Cutting a plan down

When the rendered output must be shorter, cut a whole shot — never seconds from
every shot. Three 3-second shots cut to two 3-second shots still reads as one
scene; three 2-second shots reads as a slideshow.

When it must be longer, add a shot that shows the same place from a new angle
rather than extending an existing one. A longer hold on one shot shows the model's
weaknesses; a new angle hides them and keeps the cut rhythm.
