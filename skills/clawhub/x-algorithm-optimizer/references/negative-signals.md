# Negative Signals and Suppression: what quietly kills reach

> Source: `home-mixer/filters/`, `visibility-filtering/rules/registry.rs`,
> `agatha/scalding/labels/`, `grox/flows/`, `media-model-proxy/`,
> `pnsfwmedia/`. 2026-08 snapshot.
>
> **Purpose of this file:** so honest creators do not *accidentally* trip
> classifiers and lose reach they earned. It is a map of the tripwires, not a
> guide to evading enforcement. Content that genuinely violates policy is
> supposed to be suppressed, and nothing here helps with that.

Three layers remove or throttle a post, in order:

1. **Pre-scoring filters:** hard drops before ranking.
2. **Ranking penalties:** the negative-signal weights plus the offset collapse
   (see [scoring-weights.md](scoring-weights.md)).
3. **Visibility filtering (VF):** post and account labels that drop a post,
   often **only for out-of-network viewers**. This is the "your followers still
   see it but strangers never do" mechanism.

## Layer 1: pre-scoring filters (hard drops)

Your post is removed outright, before it is even scored, if any of these hold.
They run in this order in `phoenix_candidate_pipeline.rs`:

| Trigger | Filter |
|---|---|
| Older than **48 hours**, or creation time unreadable | `AgeFilter` |
| It is your own post (in your own feed) | `SelfTweetFilter` |
| It is an OON **retweet or reply**, or a reply whose parent is missing | `OONRetweetReplyFilter` |
| SimClusters-sourced, OON, author flagged NSFW | `OONNsfwSimclustersFilter` |
| Viewer muted or blocked you, or you blocked them (either direction, including quoted/retweeted authors) | `AuthorSocialgraphFilter` |
| Post matches the viewer's muted keywords | `MutedKeywordFilter` |
| Subscriber-only content the viewer cannot access | `IneligibleSubscriptionFilter` |
| Duplicate, already-seen, or already-served | dedup and seen filters |
| For brand-new/resurrected viewers only: OON post below an engagement threshold | `NewUserMinEngagementFilter` (off by default) |

**Creator takeaways:** post **originals** (OON replies and retweets are dropped
for stranger reach), publish while fresh, and do not repeat yourself into the
seen filters.

## Layer 3: visibility-filtering labels

VF returns ALLOW, INTERSTITIAL (blur behind a tap), or DROP per post and viewer.
The first rule that says DROP wins and evaluation stops. Nearly all rules exempt
the author viewing their own post, which is exactly why suppression is invisible
to the person being suppressed: you always see your own post looking normal.

### Drops that apply to everyone (in-network and OON)
Suspended, deactivated, erased, or protected author; viewer blocks or mutes
author; and the safety labels `PDNA`, `BOUNCE`, `SPAM`,
`FOSNR_HATEFUL_CONDUCT`, `FOSNR_VIOLENT_SPEECH`, `FOSNR_ABUSE`,
`FOSNR_CIVIC_INTEGRITY`, legal takedowns matching the viewer's country, and
nullcast (ads-only) posts.

### Interstitial (blurred, not dropped)
`NSFW_HIGH_PRECISION`, `GORE_AND_VIOLENCE_HIGH_PRECISION`, `NSFW_CARD_IMAGE`,
and NSFW-flagged author with media. Shown behind a tap-through unless the viewer
opted into sensitive media. Also age-gated: dropped for logged-out or under-18
viewers, and for viewers with no stated age in a list of 16 countries.

### The "shadowban" set: DROP for OON only, ALLOW for followers
These fire **only** for recommended (stranger) distribution. Your followers see
the post normally; it simply never reaches anyone who does not follow you. This
is the precise mechanism people call shadowbanning:

- **Tweet and media labels:** `NSFW_HIGH_RECALL`, `NSFW_HIGH_PRECISION`,
  `GORE_AND_VIOLENCE_HIGH_PRECISION`, `NSFW_CARD_IMAGE`, `NSFW_TEXT`,
  `DO_NOT_AMPLIFY`, `MALICIOUS_URL`, `SPAM_HIGH_RECALL`, `FOSNR_ABUSE_INSULTS`,
  DMCA media, and geo-restricted media.
- **Account labels:** `NSFW_HIGH_RECALL`, `NSFW_HIGH_PRECISION`,
  `NSFW_NEAR_PERFECT`, `NSFW_AVATAR_IMAGE`, `NSFW_BANNER_IMAGE`,
  `SPAM_HIGH_RECALL`, `COMPROMISED`, `READ_ONLY`,
  `IMPERSONATION_HIGH_PRECISION`, `ABUSIVE_HIGH_RECALL`, `DO_NOT_AMPLIFY`.

A few of these (`ABUSIVE_HIGH_RECALL`, account-level `DO_NOT_AMPLIFY`,
`FOSNR_ABUSE_INSULTS`) additionally allow existing followers, so their
suppression is specifically a reach-to-strangers penalty. Note that a couple of
harsh-sounding labels, `EGREGIOUS_NSFW` and `RECOMMENDATIONS_BLACKLIST`, are
**not** wired to drop in this code.

**Creator takeaways:**
- A `MALICIOUS_URL` label drops you OON, so vet every link and shortener you post.
- A NSFW avatar or banner can suppress *all* your posts to strangers even when
  the posts themselves are clean, because those are account-level labels.
- `DO_NOT_AMPLIFY` and `SPAM_HIGH_RECALL` are account-level, so one bad pattern
  can throttle your whole account's stranger-reach while your follower feed looks
  untouched. You may never notice.

## The account-reputation chain (agatha): the slow killer

`agatha/scalding/labels/` computes smoothed ratios per account, where the
denominator is **out-of-network favorites only**. The formula (from
`RateBasedLabels.scala`, smoothing constant 0.1) is roughly
`score = (interactions + 0.1) / (interactions + oon_favs + small_term)`, so a
higher ratio is worse:

- **BlocksPerFav:** distinct users who blocked you, divided by OON favs.
- **ReportsPerFav:** distinct abuse reports, over a 180-day window.
- **SpamReportsPerFav:** distinct legitimate spam tattles.

High ratios feed the NSFW, spam, and abusive user models, which produce the
account-level labels in the OON-only drop set above. The causal chain:

```
audience reacts badly (blocks / reports / spam-flags relative to likes)
    -> agatha ratio rises
    -> NSFW / spam / abusive-high-recall account label
    -> silent OON-only drop (followers still see you; strangers do not)
```

**Creator takeaway:** the ratio is *relative to your likes*. A post that earns
lots of likes and a few blocks is fine. A post that earns few likes and some
blocks is dangerous. This is the mathematical reason rage-bait backfires: it
inflates the numerator faster than the denominator.

## Grox: the LLM re-scan that scales WITH virality

`grox/flows/ptos/` runs LLM classifiers (Grok/Gemma) over posts for
AdultContent, ViolentMedia, Spam, IllegalAndRegulatedBehaviors, HateOrAbuse,
ViolentSpeech, SuicideOrSelfHarm, and ChildSafety. Verdicts are written back to
the safety stores that become the `SPAM`, `NSFW_*`, `FOSNR_*`, and
`DO_NOT_AMPLIFY` labels the VF rules read.

Escalation is **fav-gated** (`ptos/constants.py`): at **128 favorites** a post
gets a deluxe re-check, and at **1,024 favorites** it is re-checked by a stronger
internal model. High-fav posts with media get an injected adult-content recheck.

**Creator takeaway:** going viral triggers *more* scrutiny, not less. A post
that skated by at 50 favorites can be relabeled and suppressed at 128. Borderline
content is riskiest precisely when it is working, so keep clearly-viral content
clearly clean.

## The single defensive checklist

Before posting, confirm none of these apply:
1. Any audience segment likely to **mute, report, or tap "not interested"**?
   (Those weights are −58.8, −234, and −43.2, and a net-negative post collapses.)
2. Links vetted, with no shortener or domain that could read as `MALICIOUS_URL`?
3. Media clean, and avatar and banner clean (they carry account-level NSFW
   labels)?
4. Not an engagement-bait or spam pattern (follow-for-follow, "reply GO", mass
   identical replies), which risk `SPAM_HIGH_RECALL` and coordinated-spam
   detection?
5. If it is likely to exceed 128 favorites, is it clean enough to survive an LLM
   re-scan?
6. Are your blocks-and-reports-relative-to-likes ratios staying healthy across
   recent posts?
