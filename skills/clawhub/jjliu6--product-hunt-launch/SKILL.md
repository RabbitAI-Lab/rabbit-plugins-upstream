---
name: product-hunt-launch
version: 1.0.0
description: Helps quickly prepare a Product Hunt launch submission — name, tagline, description, topics/tags, gallery/thumbnail/video guidance, makers/shoutouts/pricing, maker's first comment, and launch timing. Use this skill whenever the user mentions Product Hunt, "PH launch", launching a new product, wants to submit/post something on Product Hunt, asks "is this suitable for Product Hunt", or wants to fill out a Product Hunt form — even if they don't spell out every field they need. Also trigger for Chinese phrasing like "上product hunt", "发布产品", "product hunt 提交/上线". The user wants this to be FAST and low-effort each time — don't over-interview, just gather the essentials and generate a ready-to-paste draft.
---

# Product Hunt Launch Helper

Goal: turn "I have a product to launch" into a ready-to-paste Product Hunt
submission — every field filled in, final draft, not a template with
blanks — in one pass with minimal back-and-forth.

The user who set this skill up explicitly wants speed over process ("不管太多"
— don't overthink it). Don't run a long interview and don't hand back a
form with placeholders for the user to fill in themselves — that defeats
the point. If you already know enough about the product (from this
conversation, a repo, a live site you can look at), go find the remaining
details yourself before asking the user anything.

## Step 0 — Look before you ask

Before questioning the user, check what you can already establish:

- Is there a live URL in the conversation? If so, treat it as the primary
  source of truth — read the page (and a `/demo` or similar page if one
  exists) rather than guessing at what the product does.
- Is there context on how it was built (mentioned frameworks, hosting,
  deploy platform, this being a Claude Code / Cowork project, etc.)? That
  feeds the Shoutouts field later — don't make the user re-list what you
  already watched them build.
- What's genuinely different about this product, not just what it does?
  A generic feature list undersells everything — the whole submission
  should be built around whatever specific hook makes this one worth
  clicking on (an unusual mechanic, a constraint nobody else has, multi-
  language support, zero-install, a surprising performance number,
  whatever it actually is). Find that hook before writing anything, and
  make sure it shows up in the tagline, description, and first comment —
  not just once, buried in one field.

Only ask the user for what you genuinely can't infer.

## Step 1 — Gather the essentials (one shot, not a multi-turn interview)

If not already known or inferable from Step 0, ask for these in a single
message:

1. Product name (≤40 characters)
2. Live URL
3. Pricing (free / freemium / paid / one-time)
4. Who's making the launch — just you, or are there collaborators to tag
   as co-makers?

Do NOT ask about images, video, or topics up front — those are handled in
Step 3, since the user usually needs to go produce or point you at those
assets rather than answer a question about them on the spot.

## Step 2 — Generate every field, ready to paste

Produce all of the following together, as final copy — not a fill-in-the-
blank template:

### Name
The product name as given, ≤40 characters.

### Tagline
- **Hard limit: 60 characters.** Count it and state the count for each option.
- One punchy line built around the hook from Step 0, not a feature list or
  generic category description.
- Give 2-3 alternatives so the user can pick.

### Description
- **Target: ≤260 characters** (Product Hunt's field technically allows more,
  and you'll see ~500 cited elsewhere, but shorter descriptions perform
  better and 260 is the safer real limit to write to).
- What it is, who it's for, why it's different, in plain language — no
  "revolutionary"/"game-changing" filler. If there's room, one line on the
  practical specifics (time to use it, install needed or not, languages
  supported) goes further than another adjective.
- Give 1-2 alternatives.

### Topics/tags
Suggest up to 3. Don't just reach for the closest generic Product Hunt
topic (e.g. defaulting to "Artificial Intelligence" or "Productivity" for
everything) — if the product has a specific category, tell the user to
search Product Hunt's actual topic list for that narrower match first
(e.g. "Icebreaker", "Events", "Team Building" instead of just "Games"),
since specific tags reach a more relevant, more likely-to-upvote audience.

### Makers & Shoutouts
- **Makers**: the user, plus anyone they mentioned as a collaborator.
- **Shoutouts (≤3)**: tools/platforms that genuinely helped build or ship
  it — inferred from Step 0 context (e.g. the build tool, hosting/deploy
  platform, an AI coding assistant used). Don't invent these; only include
  what you actually have evidence for, and ask if you're not sure.

### Pricing
State plainly (Free / Freemium / Paid / One-time), as given in Step 1.

### Maker's first comment
This is the single most-read piece of content on launch day — present in
~70% of Product of the Day/Week/Month winners. Draft it in the user's
voice, first person, as the actual maker (not marketing copy). A pattern
that works well: open with a direct, personal greeting ("Hey Product Hunt
👋, I'm [name].") then:

1. Why you built it — the real reason, personal not corporate ("most
   icebreakers are kind of painful" beats "we identified a market gap")
2. What it does and who it's for, in plain language
3. A short checkmark-style list (✅) of the 3-4 things that actually make
   it worth trying — pull these straight from the genuine differentiators
   you found in Step 0, not a generic feature dump
4. Pricing/offer if relevant (e.g. a launch-day discount or free tier)
5. Close with a genuine, specific question inviting discussion — not
   "What do you think?" but something concrete tied to an actual open
   decision, e.g. "Would love feedback: what would make this land even
   better in a big room?"

## Step 3 — Media guidance (offer to actually help produce it, not just spec it)

Don't just hand over a spec sheet — actively help where you can:

- **Gallery images**: 1270×760px, minimum 2 (ideally 3-5), each under 3MB.
  The **first image is the social preview card** — shared on Twitter/
  LinkedIn/Slack — so it needs to work as a standalone visual, not just a
  cropped screenshot. If the product has a demo/walkthrough page or the
  user can share screenshots, suggest a concrete shot sequence that tells
  the story in order (e.g. entry/join step → core interaction → the most
  dramatic/rewarding moment, placed first since it's the social card →
  any admin/host/behind-the-scenes view). Offer to actually generate or
  crop the images yourself if given screenshots or a style direction —
  don't just describe the spec and stop.
- **Thumbnail**: 240×240px square — the small icon shown in feeds and
  rankings. Should be a clean mark that reads at small size and hints at
  what the product does in one glance. Offer to produce this too.
- **Video (optional but strongly recommended)**: must be a **public
  YouTube URL** — Product Hunt does not accept direct uploads or private/
  unlisted links. If the product already has some kind of auto-demo,
  scripted walkthrough, or recording flow, point out that recording that
  is nearly free effort and converts well — no need to storyboard a new
  video from scratch. If the user has a local file, remind them it needs
  to go to YouTube (public) first, and offer to help write the video's
  title/description.
- **GIFs**: allowed in the gallery, but don't autoplay in the PH feed
  (only on the product page) — the first static gallery image still has
  to carry the "wow" on its own.

## Step 4 — Timing

Default recommendation: **12:01 AM PT on a Tuesday, Wednesday, or
Thursday** (avoid Monday — most crowded — and Friday — lowest traffic;
launching right at 12:01 AM PT gives the full 24-hour voting window PH's
daily ranking is based on).

But also check for a better option: does the user have a recurring event,
meetup, newsletter, or audience touchpoint where they'll have real,
engaged people on hand around a specific date? Launch-day comments from
genuine users beat any "optimal day" formula, since Product Hunt momentum
compounds from real early engagement. If such a touchpoint exists, suggest
aligning the launch to it even if it falls outside the Tue/Wed/Thu rule,
and explain the trade-off so the user can decide.

If the user gives a target date, convert it to confirm which PT-day it
falls on and flag it if it's a Mon/Fri.

## Step 5 — Final pre-submit checklist

Close with a short checklist the user can tick through before hitting submit:

- [ ] Name ≤40 chars
- [ ] Tagline ≤60 chars, benefit-led (not feature list)
- [ ] Description ≤260 chars
- [ ] ≤3 topics, as specific as Product Hunt's list allows
- [ ] Makers tagged; Shoutouts (≤3) credited
- [ ] Pricing set
- [ ] ≥2 gallery images at 1270×760px, first one works as a standalone social card
- [ ] Thumbnail at 240×240px
- [ ] Video is a *public* YouTube link (if using one)
- [ ] Maker's first comment drafted and ready to post the moment it's live
- [ ] Launch date/time set — either the Tue/Wed/Thu 12:01 AM PT default, or
      aligned to a real audience touchpoint

## Notes

- Keep the tone of generated copy matching how the user actually talks
  about their product elsewhere in the conversation — don't default to
  generic startup-marketing voice.
- If the user only wants one piece (e.g. "just write me a tagline"), don't
  force the full workflow — give just that, but mention the rest is
  available if useful.
- This skill is meant to be reused for every future launch, not just the
  current product — keep the approach (look before you ask, ground
  everything in the product's real hook, offer to actually produce assets
  not just spec them) the same each time so it stays fast without going
  generic.
