# Image briefs

## Sources

SKILL.md Workflow step 5 is the picture policy: user pictures first, then the library question, then generation or labeled frames. When you generate, use one request per distinct scene with a full text prompt; you may pass pictures from this Skill's library or pictures already made for this deck as `--reference` style inputs so the series keeps one look. Never pass third-party or source photos, screenshots, or photos of real people as inputs.

Every prompt should end with: "Photorealistic, restrained corporate documentary photography, deep navy and white accents, natural daylight. No text, logos, signage, watermarks, readable screens, or identifiable landmarks."

| Slot | Frame | Brief |
| --- | --- | --- |
| Cover banner (`.cover-art`) | very wide, about 4.5:1 crop of a 16:9 image | Contemporary low-rise office campus or glass facade with a calm courtyard; keep the subject in the middle band so a wide crop works. |
| Introduction (`.art`) | about 5:4 | Three or four colleagues working over paper plans at a clear desk; faces and hands grouped centrally. |
| Foundation banner (`.wide-art`) | about 3.6:1 | A bright open office with a small group collaborating; people in the middle third. |
| Workflow portrait (`.art`) | tall, about 5:6 | Two or three people in candid discussion, framed so a vertical centre crop keeps both faces. |
| Pilot scope (`.art`) | about 16:9 | An empty, sunlit meeting room or office entrance seen through glass; no people needed. |
| Team portraits (`.portrait`) | square, circular crop | Head-and-shoulders portrait, facing camera, softly blurred bright office background. Use one image per person or a 2x2 grid with white gutters cropped into four squares. Fictional people only. |

Generate each picture at the aspect that `style-kit.json` lists for its slot (16:9 for the cover, introduction, foundation, workflow and pilot scope photos; 1:1 for team portraits); the Frame column describes the visible crop, so keep the subject inside it. For a new slot with no listed aspect, default to landscape 1536x1024 (square 1024x1024 for portraits). Convert to WebP (quality about 88, long edge at most 1920 px), set it on the image node (the build inlines it), and keep the deck under 20 MB. Each semantic page needs a different picture.
