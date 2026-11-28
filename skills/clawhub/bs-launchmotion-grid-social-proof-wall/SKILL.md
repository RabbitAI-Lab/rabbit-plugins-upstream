---
name: bs-launchmotion-grid-social-proof-wall
description: "Turn real social posts about your product into a 3D social-proof wall: your agent finds TikTok, Instagram, YouTube Shorts, X and Threads posts that mention the product (or uses the links you give), records each post as it plays, and lays 6-14 of them out whole in two drifting rows under one headline on a black stage. Delivers an editable HyperFrames scene and a 5.5-second MP4 in 1080p or 4K."
---

# Social Proof Wall

Real posts about the product, recorded from the platforms themselves, shown whole in a slowly turning 3D wall under one headline in the user's language. One editable HyperFrames project, 5.5 s by default, 1920×1080 canvas, renders at 1080p (default) or 4K, 30 fps, black background with a fine grid by default.

## 1. Ask where the posts come from

Always ask the user to choose before doing anything else, unless they already said:

1. **"I'll send the post links."** The user pastes links to their posts (TikTok, Instagram Reels or posts, YouTube Shorts, X, Threads, LinkedIn). Use exactly those.
2. **"Find them for me."** The user gives the product name (and, if the name is common, one or two words that tell it apart, such as its domain or category). You search the platforms and pick the posts.

Also ask for the headline (or offer one, see section 4) and confirm 1080p or 4K.

## 2. Set up once

```bash
npm install --prefix <this skill>/scripts
```

This installs `playwright-core`. Recording drives an installed Google Chrome headlessly (set `CHROME_PATH` if Chrome is somewhere else); Chrome is needed because the platforms serve H.264 video that bare Chromium cannot play. FFmpeg and the HyperFrames CLI are also required.

## 3. Find and record the posts

### Option 2: search

```bash
node scripts/find-posts.mjs --product "Kite" [--keywords "AI notes app"] --out posts.json
```

It searches each platform (DuckDuckGo `site:` queries plus YouTube Shorts search) and prints candidates with `platform`, `url`, `title`, `snippet` and `mentions`. Search results are only candidates:

- Drop posts about a different product with the same name, posts in a language the user did not ask for, and duplicates of the same video.
- Prefer creators talking about the product over the product's own account; one or two official posts are fine.
- If a browser tool or web search is available to you, use it to add more posts (for example the platform's own search) when fewer than 8 good ones turn up.
- Show the user the short list (author, platform, one line each) before recording, and let them remove any.

### Probe, then record

For each post, look at it first and pick the second where the product is on screen:

```bash
node scripts/record-post.mjs --url "<post url>" --out tiles/01.mp4 --probe
# writes tiles/01.probe.jpg: one frame per second, labelled 0s, 1s, 2s ...
node scripts/record-post.mjs --url "<post url>" --out tiles/01.mp4 --start 4 --seconds 6
```

- Read each probe sheet. Choose `--start` where the product, its site or its name is visible; avoid frames that are only a face if a product frame exists nearby.
- `--seconds` must be at least the wall length plus 0.5 s (6 s for the default 5.5 s wall).
- Video posts become an MP4 of the post area (video, author, counts, caption), stepped frame by frame so playback speed is exact. Posts with no video (text or image posts) become a still PNG with the same name. Both work on the wall.
- Name tiles in the order you want them on the wall (`01`, `02`, ...). The first half fills the top row.
- Exit code 2 means the post was unavailable or could not be found on the page; drop it. Sign-in walls, cookie banners, onboarding tips and play badges are removed automatically, but check the probe sheet: if a tile still shows a sign-in prompt or a blank player, drop it.
- Posts are recorded in the platforms' dark theme to sit on the black wall; add `--scheme light` when you build a white wall.
- Recordings have no sound. Run up to six recordings at the same time.

Aim for 8–12 tiles (minimum 3, maximum about 14). Mix platforms and orientations; landscape and square posts sit next to vertical ones at their own shape and are never cropped.

## 4. Build the wall

```bash
node scripts/build-wall.mjs --tiles ./tiles --out ./wall --title "Creators can't stop talking about [[Kite]]"
npx hyperframes preview ./wall
npx hyperframes render ./wall --output ./wall.mp4 --fps 30 --quality high --resolution 1080p
# 4K: --resolution 4k
```

- **Headline.** Write it in the language the user is writing to you in, unless they ask for another one (a film for an English-speaking audience usually wants English). One line: at most about 44 characters in Latin scripts, about 20 in Chinese, Japanese or Korean. Wrap the product name in `[[ ]]` to color it with the theme accent. English examples: `Creators can't stop talking about [[Kite]]`, `The internet is talking about [[Kite]]`; for a user writing in Chinese, write the same idea in Chinese. Smiley Sans covers Latin and Chinese; for Japanese or Korean add `--font` with a font that covers it, or use `--font inter` and let the system font fill in. `--title ""` removes the headline and gives the wall the full frame.
- **Background.** `--bg black` (default), `--bg white`, or `--bg "#RRGGBB"` for a brand-dark or brand-light stage. `--grid off` removes the fine grid. Keep the background calm: black, white or a very dark or very light brand tone, never a saturated color.
- **Accent.** `--theme blue` (default), `--theme mono`, `--theme orange`, or `--accent "#RRGGBB"`. It only colors the `[[ ]]` words.
- **Font.** Headlines use Smiley Sans (Deyi Hei). `--font inter` uses Inter; `--font path/to/font.woff2` (or .ttf/.otf) uses the user's own headline font.
- **Length and layout.** `--seconds 5.5` (default; 4–8 works), `--rows auto|1|2|3` (auto: up to 5 tiles in one row, up to 14 in two, more in three), `--order 03.mp4,01.mp4,...` to reorder without renaming.

The camera and timing are fixed: the wall turns from 18° to 12° while drifting in, and the tiles rise in one after another in the first second.

## 5. Use it in a LaunchMotion film

The rendered `wall.mp4` is a scene like any other LaunchMotion scene. Join it with the others using the full library's `assemble.mjs`, usually right after the product beats and before the closing call to action.

## Resolution

Before rendering, ask the user whether they want 1080p or 4K. If they do not say, render 1080p. For 4K add `--resolution 4k` (3840×2160): the scene and its timing stay the same, Chrome renders it at twice the pixel density, and the render takes longer. Post recordings are captured at twice the screen density, so tiles stay sharp in 4K.

## Rules

- Only use public posts, and only what they show. Never edit a post's text, numbers or captions, and never present a post about another product as one about the user's product.
- Remind the user that the posts belong to their creators: for a public ad, they should have the creators' permission or use the wall only where sharing posts is allowed.
- Show every post whole; do not crop tiles to fill gaps.

## Check

Look at the first, middle and last frames of the render. Every tile should be the post itself (no sign-in prompt, cookie banner or blank player), the headline should be on one line, and nothing should be cut off at the frame edges. Replace or drop any bad tile, rebuild and render again.
