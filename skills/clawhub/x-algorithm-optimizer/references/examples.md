# Before / After: worked rewrites

> Concrete transformations showing the principles applied. Each pairs a weak
> draft with a stronger rewrite and names the mechanism that makes the
> difference. Use these as patterns, not templates. The point is the reasoning.

---

### 1. Like-bait → forwardable

**Before:** *"AI is changing everything. Like if you agree! 🚀"*
- Targets only the like (0.5). "Like if you agree" is engagement-bait →
  `not_interested`/`mute` risk and `SPAM_HIGH_RECALL`. No reason to reply or
  forward. Vague, so it doesn't land in a clean embedding neighborhood.

**After:** *"The one AI workflow that actually saved me time this year: draft
in bullet points, let the model expand, then cut 30%. The expand-then-cut order
is the whole trick. What's your current writing loop?"*
- Concrete + reference-worthy → targets copy-link share (20) and DM share (5).
- Ends on a genuine question → reply (5).
- Specific topic → clean embedding cluster → better out-of-network retrieval.
- No bait, no negative-signal risk.

---

### 2. Hot-take rage-bait → substantive stance

**Before:** *"Unpopular opinion: everyone using [framework] is just too lazy to
learn real engineering. Cope."*
- "Unpopular opinion" + "cope" = rage markers. Provokes block/mute/report
  (−31.2 / −58.8 / −234) and inflates the agatha blocks-per-fav ratio → account
  label → silent out-of-network throttle. Net-negative EV.

**After:** *"[Framework] optimizes for shipping speed at the cost of runtime
control. That's the right trade for 90% of apps and the wrong one for the other
10%. Here's how I decide which project I'm on 👇"*
- Same strong opinion, but defensible and useful → invites quote (5) and reply
  (5) instead of blocks.
- Thread lead-in → dwell time + follow.
- Doesn't spike the reputation ratios that cap reach.

---

### 3. Link dump → value-in-post

**Before:** *"Great read on scaling Postgres 👇 https://example.com/blog/post"*
- Almost all value is behind the link. Link-open is only +0.2; click +0.4.
  Nothing to reply to or forward. If the domain is ever flagged, `MALICIOUS_URL`
  drops it out-of-network.

**After:** *"Scaling Postgres, the 3 changes that mattered most for us: (1)
connection pooling before read replicas, (2) partition the biggest table early,
(3) `pg_stat_statements` is non-negotiable. Full write-up in replies. Which one bit
you hardest?"*
- The post itself is the value → forwardable (copy-link 20, DM 5).
- Link moved to a reply, so the main post keeps attention and dwell.
- Question → reply (5).

---

### 4. Hashtag spray → clean

**Before:** *"New blog post! #tech #ai #ml #coding #dev #startup #productivity"*
- 6 hashtags: no ranking benefit (no hashtag feature exists in the model),
  reads as spammy, weakens the hook, nudges `not_interested`.

**After:** *"Spent the weekend making our build 4× faster. The surprise: 80% of
the win was one cache config nobody had touched in two years. Write-up soon —
what's the most embarrassing quick-win you've shipped?"*
- Zero hashtags. The topic words do the discovery work via the embedding.
- Story + vulnerability + question → reply and forward.

---

### 5. Reach-farming reply → original post

**Before (as a reply under a 500k account):** *"So true! 💯 Follow me for more
takes like this!"*
- Replies are out-of-network-discounted (×0.75) and cold-start-ineligible.
  "Follow me for more" is bait. Adds nothing → no forward, no genuine reply.

**After (as your own original):** *"Watched a 500k account explain [topic] today
and realized the thing they skipped: [specific insight]. Here's the part that
actually matters in practice…"*
- Original → eligible for cold-start boost (if <1k followers) and full
  (undiscounted) ranking.
- Builds on the idea with a specific insight → quote/forward-worthy.

---

### 6. "Comment below" bait → real question

**Before:** *"What do you think? Comment below!! 👇👇"*
- Generic bait, no substance to react to. The empty prompt reads as
  engagement-bait, not conversation.

**After:** *"If you could delete one meeting from every week permanently, which
one — and what would you do with the hour?"*
- A specific, low-effort-to-answer, genuinely interesting question → high reply
  probability (5) without any bait pattern.
- Universally relatable → wide embedding reach, broad reply base.

---

## The transformation checklist these share

Every "after" does some subset of:
1. **Moves value into the post** so it's forwardable (chase the 20, not the 0.5).
2. **Ends on a specific, answerable question** (chase the 5).
3. **Holds a defensible stance** instead of a provocative one (avoid −234/−58.8).
4. **Is a self-contained original** (reach vehicle + cold-start eligibility).
5. **Is specific to one niche** (clean embedding → better retrieval).
6. **Drops the bait and the hashtag spray** (no spam-classifier or negative-feedback risk).
