# Account Playbooks: strategy by situation

> Derived from [scoring-weights.md](scoring-weights.md),
> [distribution-mechanics.md](distribution-mechanics.md), and
> [negative-signals.md](negative-signals.md). Match the user's situation to a
> playbook, then draft against it.

## A. Cold-start account (≤ 1,000 followers)

You have one structural superpower: the **cold-start boost** injects one fresh
original post near slot 15 per eligible feed load, as long as you're under
1,000 followers, the post is an original under 24h with < 1,000 impressions.

Playbook:
- **Post originals only for growth.** Replies and retweets are cold-start-
  ineligible AND OON-discounted. Save replies for relationship-building with
  specific accounts, not reach.
- **Pick one niche and stay in it.** Consistency builds a clean embedding
  neighborhood so two-tower retrieval delivers you to the right strangers. Every
  off-topic post muddies your cluster and wastes retrieval.
- **Optimize each post for one reply-worthy idea.** Reply weight (5.0) is your
  most reachable high-value action at low follower counts.
- **One quality post > many posts.** Diversity decay means your 3rd post today
  scores ×0.44. Cadence: 1–2 excellent originals/day beats 10.
- **Convert engagers to mutual follows.** Mutual follow = +15 reply weight and
  flips your OON 0.75 handicap into easy in-network reach.
- **Watch your blocks/reports-vs-likes ratio from day one.** The agatha
  denominator is OON favs, and small accounts have thin denominators, so a
  couple of reports hurt disproportionately.

## B. Growth account (1k–50k)

You've lost the cold-start boost; now it's pure content-quality + velocity.
- **Front-load engagement velocity.** Engagement counts are model inputs;
  the first hour shapes scoring for everyone after. Post at your audience's
  peak, and seed genuine early replies (ask a real question in the post).
- **Engineer forwarding, not liking.** The gap between copy-link share (20) and
  like (0.5) is your whole opportunity. Make posts people *send* someone:
  genuinely useful, reference-worthy, "this explains the thing you asked about."
- **Threads for dwell.** Continuous dwell time is weighted (0.004/unit) and
  compounds on longer content that holds attention. A strong thread earns dwell
  that single posts can't.
- **Differentiate on trends (DPP).** When jumping a trend, take the orthogonal
  angle, since near-duplicate embeddings get dropped from adjacent slots.

## C. Established account (50k+)

Your risk shifts from "getting seen" to "not getting throttled."
- **Protect account reputation.** At scale, one pattern that spikes
  blocks/reports-per-fav can apply an account-level `DO_NOT_AMPLIFY` /
  `SPAM_HIGH_RECALL` / abusive label that silently caps *all* your OON reach.
- **Clean at virality.** Grox re-scans at 128 and 1,024 favs. Anything that
  could read as borderline is riskiest exactly when it's taking off.
- **Still one strong post per slate.** Diversity decay applies at every size.
- **Mutual-follow core.** A large mutual-follow base is a durable ranking
  asset (+15 reply weight, in-network reach that skips the OON discount).

## D. By content format

| Format | Algorithm reality | Move |
|---|---|---|
| Single text post | Cheap, but no dwell accumulation | Make it forwardable or reply-provoking |
| Thread | Earns dwell time (0.004/unit), holds attention | Strong hook first post; each post must pull the next |
| Video | VQV only counts if **≥ 10s**; video open +0.05 | Make videos ≥10s; hook in first 2s to beat scroll-past (−0.02) |
| Image post | has_media is a feature; clean media only | Ensure media can't read as NSFW/gore to the classifiers |
| Reply | OON-discounted, cold-start-ineligible | Use for relationships, not reach |
| Quote | +5.0, and original | Great for reach if you add real value over the quoted post |
| Link post | Link opens are low value (0.2) and `MALICIOUS_URL` risk | Vet the domain; put the value in the post, not behind the link |

## E. The universal draft checklist

For any post, run these in order:
1. **Hook** survives the first-2-seconds scroll test (avoid the −0.02
   not-dwelled penalty).
2. **One high-value action** the post is designed to earn: a reply (a real
   question / a take worth answering), a forward (useful/reference-worthy), or a
   quote (add-able). Name it explicitly.
3. **Negative-signal audit.** See the checklist in
   [negative-signals.md](negative-signals.md). Would any segment mute/report it?
4. **Original + fresh + on-niche.**
5. **Differentiated** from the current wave if trend-jacking.
6. **Cadence.** Is this the one post for this session, or are you diluting
   yourself via diversity decay?
