---
name: x-algorithm-optimizer
description: >-
  Optimize posts for X's (Twitter's) For You feed algorithm, based on X's
  open-sourced ranking code. Use when the user wants to write, draft, review, or
  improve a post/tweet/thread for reach, engagement, or virality on X, for
  example "write a tweet about...", "make this post go viral", "why isn't my post
  getting reach", "optimize my thread for the algorithm", "review my tweet before
  I post". Grounds advice in the actual scoring weights, filters, and
  distribution mechanics rather than generic social-media tips.
license: MIT
---

# X Algorithm Optimizer

Help the user create posts for X's **For You** feed that the ranking algorithm
will distribute widely, grounded in X's open-sourced algorithm code rather than
folk wisdom. Every recommendation here traces to a specific mechanism in that
code (see `references/`).

## The one-paragraph model of the algorithm

X predicts, for each post, the probability a viewer will take each of about 30
actions, then scores the post as a **weighted sum** of those probabilities. The
weights are wildly asymmetric: a copy-link share is worth about **40 times a
like**, a reply about 10 times, and a single report cancels roughly 468 likes.
A net-negative post does not just rank low, it collapses to near zero and sinks.
High score alone is not enough. The post must also survive hard filters (a
48-hour age limit, originals-only for stranger reach) and visibility labels that
can silently drop a post to strangers while your followers still see it.
Reaching **followers** is easy. Reaching **strangers** (out-of-network) is the
real game, gated by ML retrieval that finds posts whose embedding matches a
viewer's engagement history. Note the model never reads your raw text: it sees a
semantic embedding of the post, its engagement counts, and graph and context
features.

## Two laws to optimize toward

1. **Optimize for "send to a friend," not "like."** Copy-link share (20),
   reply (5), quote (5), and DM share (5) dominate the like (0.5). Write content
   people forward and respond to.
2. **Avoiding negatives beats chasing positives.** One report (−234) or mute
   (−58.8) outweighs dozens of positives, and the offset transform then
   collapses the whole post. Rage-bait and engagement-bait are mathematically
   negative-EV.

## Workflow

Work through these steps. Pull exact numbers, thresholds, and label names from
`references/` as needed. Do not rely on memory for specifics; cite them so the
user can trust and audit the advice.

### Step 1: understand the situation
Ask for (or infer from context) what you need:
- **Follower count** (determines cold-start eligibility, the at-most-1,000 boost).
- **Niche or topic**, and **account age**.
- **Goal:** reach strangers, deepen with followers, drive replies, drive clicks,
  or grow followers.
- **The draft**, if they have one, or the idea if they do not.

If the user just wants a post written and gives a topic, proceed with sensible
defaults and note the assumptions. Do not over-interrogate.

Then pick the matching playbook in
[references/account-playbooks.md](references/account-playbooks.md).

### Step 2: draft or revise for the weight table
Structure the post to earn **high-value actions** (see
[references/scoring-weights.md](references/scoring-weights.md)):
- A **hook** that beats the first-two-seconds scroll test (scrolling past costs
  −0.02 and, at scale, feeds negative signals).
- A **reason to reply**, such as a genuine question, a take worth answering, or a
  useful prompt. Reply is worth 5.0. This is not cheap "comment below" bait,
  which risks negatives.
- A **reason to forward**: reference-worthy utility, the clearest explanation of
  something, content a viewer sends a friend. Copy-link is 20, DM is 5.
- **Dwell** for longer content, since threads accumulate weighted dwell time.
- Deprioritize chasing likes as a goal. They are the weakest positive at 0.5.

Name explicitly which high-value action this post is engineered to earn. For
concrete weak-to-strong rewrites to pattern-match against, see
[references/examples.md](references/examples.md). Before relying on any popular
X-growth tactic, check it against [references/myths.md](references/myths.md).
Much common advice (hashtags, engagement-bait, post-volume, chasing likes) is
contradicted by the actual ranking code.

### Step 3: negative-signal and suppression audit
Run the checklist in
[references/negative-signals.md](references/negative-signals.md). Confirm the
post will not:
- Provoke mute, report, or "not interested" from any audience segment.
- Trip a visibility label (NSFW, gore, spam, `DO_NOT_AMPLIFY`, `MALICIOUS_URL`).
  Vet links, media, avatar, and banner, since some labels are account-level.
- Read as an engagement-bait or spam pattern (`SPAM_HIGH_RECALL`,
  coordinated-spam detection).
- Damage the account's blocks-and-reports-relative-to-likes ratio, the agatha
  chain that silently caps stranger-reach.

Flag that going viral *increases* scrutiny: Grox re-scans posts with an LLM at
128 and again at 1,024 favorites, so clearly-viral content must be clearly clean.

### Step 4: distribution tactics
From [references/distribution-mechanics.md](references/distribution-mechanics.md):
- **Original, fresh, and niche-consistent.** A post lives about 48 hours,
  front-loaded. Originals reach strangers; replies and retweets carry a 0.75
  out-of-network handicap and are cold-start-ineligible.
- **Cold-start:** if the account has at most 1,000 followers, every fresh
  original gets a roughly slot-15 injection, so lean into consistent originals.
- **One strong post per session** (author-diversity decay: 2nd post ×0.625, 3rd
  ×0.44).
- **Differentiate on trends,** because the DPP rerank drops near-duplicate
  embeddings from adjacent slots.
- **Build mutual follows** for the +15 reply weight, which also flips
  out-of-network into in-network reach.
- **Timing:** post when the coherent audience is active, so early velocity, which
  compounds through the engagement-count features, lands inside the window.

### Step 5: (optional) score the draft
Run the heuristic critic for a concrete before/after and a flagged report:

```bash
python scripts/post_critic.py "your draft text here"
# or pipe a file:            python scripts/post_critic.py < draft.txt
# or compare variants:       python scripts/post_critic.py --compare "draft A" "draft B"
```

It estimates the post's action profile, computes the weighted score with the
real weight table, and flags hook strength, reply and forward potential, and
negative-signal risk. It is a heuristic writing aid, **not** a simulator of X's
ML model. Present it as directional, and explain *why* each flag fired using the
references.

## Output style

- Give the **revised post** (or new draft) first, then a short, specific
  rationale tied to mechanisms. For example: "opens with a question, targeting
  reply weight 5.0; no external link, avoiding MALICIOUS_URL risk and the low
  0.2 link value."
- Offer one or two variants when useful, such as a reply-optimized version and a
  forward-optimized version.
- Be honest about tradeoffs and uncertainty. The weights are a dated snapshot,
  and the model is more complex than any checklist.

## Scope and ethics

This skill optimizes **genuine, policy-compliant content** for legitimate reach.
It does **not** help with spam or engagement farming, coordinated inauthentic
behavior, buying or faking engagement, ban evasion, or evading safety labels on
content that genuinely violates policy. The suppression mechanics in
`references/negative-signals.md` are documented so honest creators avoid
*accidentally* tripping classifiers, not to help anyone evade enforcement. If a
request is for one of the excluded uses, decline and offer the legitimate
alternative: make the content actually better.

## Reference index

- [references/scoring-weights.md](references/scoring-weights.md): the weight
  table, the score formula, the offset transform, worked examples, and the
  bidirectional-follow boost.
- [references/distribution-mechanics.md](references/distribution-mechanics.md):
  exactly what the model sees, retrieval paths, the out-of-network discount,
  cold-start, diversity decay, DPP, and timing.
- [references/negative-signals.md](references/negative-signals.md): filters,
  visibility labels, the OON-only "shadowban" set, the agatha reputation chain,
  and Grox.
- [references/account-playbooks.md](references/account-playbooks.md): strategy by
  account size and content format.
- [references/examples.md](references/examples.md): worked weak-to-strong post
  rewrites with the mechanism behind each.
- [references/myths.md](references/myths.md): popular X-growth advice the ranking
  code confirms or refutes, with citations.

> Grounded in X's open-source For You algorithm (2026-08 snapshot). Weights are
> production-synced defaults that X periodically updates, so re-derive from a
> fresh clone of the algorithm repo if you need current exact values.
