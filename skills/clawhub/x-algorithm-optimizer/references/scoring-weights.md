# Scoring Weights: how a post's rank is computed

> Source: X's open-source For You algorithm, `home-mixer/params/param.rs`,
> `home-mixer/params/config.rs`, and `home-mixer/scorers/ranking_scorer.rs`.
> Values are the production-synced defaults as of the 2026-08 repository
> snapshot. X periodically rewrites these defaults via cron to track live
> production, so treat exact numbers as a snapshot and re-derive from a fresh
> clone if precision matters.

## The formula

The Phoenix ranking model predicts a probability `P(action)` for roughly 30
possible viewer actions on your post. `RankingScorer` collapses those
probabilities into one number:

```
weighted_score = Σ ( weight_i × P(action_i) )      # over all action heads
final_score    = offset( weighted_score )          # see "the offset" below
                 × author_diversity_multiplier      # repeat-author decay
                 × oon_multiplier                    # 0.75 if out-of-network
                 ( with a cold-start lift applied first, if eligible )
```

The code computes the positive terms and negative terms into two running sums
(`compute_weighted_parts` in `ranking_scorer.rs`), subtracts, applies the
offset, then multiplies by the diversity and out-of-network factors. See
[distribution-mechanics.md](distribution-mechanics.md) for those multipliers.

## The weight table (this is the core secret)

The weights are extremely asymmetric. This table *is* the algorithm's value
system. Memorize the ordering, not the decimals.

| Action | Weight | Plain meaning |
|---|---:|---|
| **Share via copy link** | **+20.0** | Someone copies your link to share off-platform. The single most valuable signal. |
| **Reply** | **+5.0** | Someone writes a reply. Gets a further +15.0 if you and the viewer follow each other (see below). |
| **Quote** | **+5.0** | Someone quote-posts you. |
| **Share via DM** | **+5.0** | Someone sends your post to a friend in DMs. |
| **Follow author** | **+4.0** | The post converts a viewer into a follower. |
| **Share (generic)** | +2.0 | Generic share action. |
| **Retweet** | +1.0 | A plain repost. |
| **Favorite (like)** | **+0.5** | A like. Worth 1/40th of a copy-link share. |
| Click | +0.4 | Any click into the post. |
| Open link | +0.2 | Opens an external link. |
| Photo expand | +0.05 | |
| Video open | +0.05 | |
| Video quality view (VQV) | +0.05 | Only counts if the video is at least 10 seconds long. |
| Quoted click | +0.05 | |
| Continuous dwell time | +0.004 / unit | Time actually spent on the post. Compounds on longer content. |
| Post unexplored (novelty) | +0.02 | Small novelty term, in-network only by default. |
| Profile click, quoted VQV, binary dwell | 0.0 | Present in the model but zero-weighted by default. |

### Negative signals (these dominate everything)

| Action | Weight | Break-even |
|---|---:|---|
| **Report** | **−234.0** | One report cancels about 468 likes, 47 replies, or 12 copy-link shares. |
| **Mute author** | **−58.8** | One mute cancels about 118 likes. |
| **Not interested** | **−43.2** | Tapping "not interested" on your post. |
| **Block author** | **−31.2** | |
| Not dwelled | −0.02 | Scrolling straight past your post without stopping. |

The comment at `param.rs:279` notes these weights blend two things: how much an
action is valued, and how rare it is across the network. Negative feedback is
rare, which is part of why each instance carries such a large magnitude.

## The offset transform (why a bad post collapses, not just drops)

After summing, `offset_score` reshapes the result (`ranking_scorer.rs`,
`NEGATIVE_SCORES_OFFSET = 0.001` from `config.rs`):

- If the post's combined score is **positive**, it simply gets `+0.001`.
- If the combined score is **negative**, it is remapped into a tiny band near
  zero: `(combined + negative_sum) / total_sum × 0.001`.

The practical effect: any post whose negative terms outweigh its positive terms
does not merely rank a little lower, it collapses to a near-zero score and sinks
to the bottom of the candidate pool. Net-negative content is effectively removed
from contention, not gently demoted. This is the math behind "one report can
tank a post."

## The two laws that fall out of the numbers

**Law 1: optimize for "send to a friend," not "like."**
Copy-link share (20), DM share (5), reply (5), and quote (5) dwarf the like
(0.5). The algorithm rewards content people forward and respond to, not content
they passively approve of. A post that earns 10 likes and 0 shares scores about
5.0. A post that earns 1 like and 1 copy-link share scores about 20.5.

**Law 2: avoiding negatives beats chasing positives.**
A single report (−234) erases the weighted value of 468 likes, and the offset
transform then collapses the whole post. Rage-bait and engagement-bait are
mathematically negative-EV: the mutes, reports, and "not interested" taps from
annoyed viewers outweigh the engagement from fans. The safest high-scoring
content is broadly inoffensive but specifically compelling to its audience.

## Worked examples

Assume the model predicts these probabilities for two drafts (illustrative):

**Draft A, a hot take designed for likes**
- P(favorite)=0.20, P(reply)=0.02, P(copy_link_share)=0.001,
  P(not_interested)=0.03, P(mute)=0.005
- combined ≈ 0.5·0.20 + 5·0.02 + 20·0.001 − 43.2·0.03 − 58.8·0.005
  ≈ 0.10 + 0.10 + 0.02 − 1.30 − 0.29 = **−1.37**
- Net negative, so the offset collapses it to near zero. Suppressed.

**Draft B, a genuinely useful thread opener**
- P(favorite)=0.08, P(reply)=0.06, P(copy_link_share)=0.02, P(dm_share)=0.03,
  P(not_interested)=0.002
- combined ≈ 0.5·0.08 + 5·0.06 + 20·0.02 + 5·0.03 − 43.2·0.002
  ≈ 0.04 + 0.30 + 0.40 + 0.15 − 0.086 = **+0.80**. Strong.

Draft A "feels" more engaging but loses, because it provokes negative feedback
and earns no forwarding. The skill optimizes toward Draft B.

## The bidirectional-follow boost

If the viewer and the author **mutually follow** each other, an *original* post
(not a reply, not a retweet) gets **+15.0** added to its reply weight
(`BidirectionalFollowReplyWeightBoost`, applied in `reply_weight_for`). There is
also a dwell-weight boost slot for mutuals, set to 0.0 by default. Mutual-follow
relationships massively amplify ranking, so building genuine two-way connections
with your audience is directly rewarded. The boost applies only to original
posts; replies and retweets do not receive it (confirmed by the test
`bidirectional_weight_boosts_only_mutual_original_posts`).

## Caveat: an alternate scoring mode exists

The code has a second scoring regime, **dwell-regret** (`ValueModelMode`,
`DwellRegretWeights` in `ranking_scorer.rs`), which gates positive engagements
through a learned model with even larger negative constants (report −60000,
mute −15000, not-interested −10000). It is **not** the default. `ValueModelMode`
defaults to `"weighted"`, the mode described above, but X can switch users onto
dwell-regret through an experiment. The optimization direction is the same in
both modes (forward-worthy content, avoid negatives). Only the exact arithmetic
differs. Optimize for the signals, not the decimals.
