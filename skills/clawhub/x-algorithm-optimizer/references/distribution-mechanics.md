# Distribution Mechanics: how a post reaches people

> Source: `home-mixer/sources/`, `home-mixer/models/candidate.rs`,
> `home-mixer/util/phoenix_request.rs`, `home-mixer/scorers/ranking_scorer.rs`,
> `home-mixer/scorers/author_cold_start.rs`, `home-mixer/params/config.rs`,
> `vm-ranker/dpp.rs`, `thunder/`, `simclusters/`, `phoenix/`. 2026-08 snapshot.

There are two audiences for any post: **in-network** (your followers) and
**out-of-network / OON** (everyone else, reached through ML retrieval).
Reaching followers is easy. Reaching strangers is where the algorithm gates
hard, and nearly every mechanic below is about OON reach.

Feed sizing constants for context (`config.rs`): the pipeline scores up to
**2,800** candidates (`PHOENIX_CLIENT_MAX_CANDIDATES`), selects the top **50**
(`TOP_K_CANDIDATES_TO_SELECT`), and the final For You response is about **35**
posts (`RESULT_SIZE`) plus feed modules. So on the order of a thousand
candidates compete for a few dozen slots per refresh.

## 1. Exactly what the model sees (and does not)

The per-candidate message sent to the ranking model is `TweetInfo`, built in
`home-mixer/models/candidate.rs::as_tweet_info`. There is **no raw post text,
no raw media, and no hashtag field**. The complete per-post feature set is:

- **Identity and graph:** `tweet_id`, `author_id`, the quoted / reply / retweet
  tweet and author IDs, `is_author_followed_by_user`, and `is_following_user`
  (does the author follow the viewer back). Note `is_following_user` is only
  populated when the post is **not** a retweet, so the mutual-follow signal is
  carried on originals and replies, not reposts.
- **Semantic IDs:** `semantic_ids`, discrete tokens from a multimodal embedding
  of the post, hydrated by `semantic_id_hydrator.rs`. This is the model's *only*
  view of your content. Text and media are compressed into this embedding
  upstream.
- **Engagement counts (bucketed):** `fav_count`, `retweet_count`, `quote_count`,
  `reply_count`, `view_count`, `bookmark_count`. These are direct inputs, so
  early engagement literally becomes a feature the model reads for every later
  viewer. Bookmark count is an input even though bookmark has no ranking weight,
  which means bookmarks quietly signal quality to the model.
- **Bool flags:** `has_media`, `is_retweet`, `is_quote`, `is_reply`.
- **Media and language:** `min_video_duration_ms`, `language_code`.

The viewer side (`build_user_context` in `phoenix_request.rs`) is where heavy
personalization lives. The model also receives, per request: user age bracket
and exact age, declared and inferred gender (plus an inferred-gender
confidence), user state, followed Grok topics, followed starter packs,
latitude/longitude, DMA (media market) code, installed apps, timezone, device
network type, and country. This is why the *same* post ranks very differently
for two viewers: geography, topic-follows, and demographics all condition the
prediction.

**Consequences for a creator:**
1. **Consistency wins.** Posting in a coherent niche gives you a clean,
   recognizable embedding neighborhood, so the two-tower model can retrieve you
   to the exact users who engage with that neighborhood.
2. **Early velocity compounds.** Because engagement counts are inputs, the first
   30 to 60 minutes of engagement shape how the model scores you for everyone
   after (a rich-get-richer effect).
3. **Wording tricks do not fool the ranker,** but they do change your embedding
   and they drive the human actions the model predicts. Write for humans; the
   embedding follows.

## 2. Retrieval: how you become a candidate at all

### Thunder (in-network / followers), `thunder/`
- Serves recent posts from accounts the viewer follows, sorted purely by
  **recency**, with no ML ranking. Posts are held in memory only inside a
  retention window; once a post ages past it, it is evicted and no longer
  served.
- Per-author caps: 50 original posts, 30 replies, 100 videos. The following
  list is capped at 10,000 accounts. `ThunderMaxResults` is 1,200.
- **Takeaway:** for followers, posting recently gets you in, but you compete
  against your own recent posts (the per-author caps) and everything ages out
  of the window.

### Phoenix retrieval (two-tower), the main OON discovery path
- A candidate tower embeds every post from its post and author multimodal
  embeddings and L2-normalizes it. The viewer's engagement-history sequence
  builds a user vector. The nearest posts by dot product are retrieved, up to
  1,000 (`PhoenixMaxResults`).
- **Takeaway:** you become retrievable to a stranger when your content's
  embedding sits near what that person has historically engaged with, even with
  zero follow relationship. This is the single biggest OON growth lever, and it
  is driven by niche consistency.

### SimClusters, engagement-neighborhood retrieval
- For each post the viewer recently engaged with, it does a nearest-neighbor
  lookup. Your post enters a cluster based on **who favorited it** (log-fav
  weighted). Constraints: cosine similarity at least 0.5, **post age under 48
  hours**, up to 800 results.
- **Takeaway:** getting favorited early by a *coherent* audience places you in a
  clean cluster and makes you retrievable here. Scattered likes from an
  incoherent audience muddy your cluster.

### Indexing (phoenix-rankall)
- Nearly everything is indexed. There is no rich safety filter at admission,
  only hard blacklists and zero-ID drops. **Suppression happens at scoring and
  serving, not at admission.** See [negative-signals.md](negative-signals.md).

## 3. The multipliers applied after scoring

### Out-of-network discount, ×0.75
Every OON post's final score is multiplied by **0.75** (`OonWeightFactor`,
confirmed by the test `applies_oon_discount_to_out_of_network`). Two important
extensions:
- In-network **replies and retweets** are *also* discounted 0.75 by default
  (`EnableOonRescoreForInNetworkRepliesRetweets`). Only original in-network
  posts escape the discount.
- Topic-request OON uses ×0.5 (`TopicOonWeightFactor`).
- **New-viewer crush:** for a brand-new viewer account (younger than the
  configured age threshold, with at least `NEW_USER_MIN_FOLLOWING = 5` follows),
  the OON factor collapses to `NEW_USER_OON_WEIGHT_FACTOR = 0.00001`. New users
  see almost exclusively in-network content. This is about the *viewer* being
  new, not the author.
- **Takeaway:** original posts are your reach vehicle. A reply or retweet starts
  at a 25% handicap for stranger reach.

### Author-diversity decay
The k-th post from the same author already ranked above in a viewer's slate is
multiplied by `(1 − 0.25)·0.5^k + 0.25` (`AuthorDiversityDecay = 0.5`,
`AuthorDiversityFloor = 0.25`):
- 1st post ×1.0, 2nd ×0.625, 3rd ×0.4375, asymptote ×0.25.
- **Takeaway:** one strong post per session beats five mediocre ones. Flooding
  the timeline actively demotes your own later posts.

### Cold-start boost (the small-creator on-ramp)
`author_cold_start.rs`. One post per eligible feed load is lifted to the score
of roughly **slot 15 to 16** if ALL of these hold:
- author has **at most 1,000 followers** (`ColdStartFollowerCap`),
- the post is an **original** (not a reply, not a retweet),
- the post has **under 1,000 impressions** (`ColdStartImpressionThreshold`, read
  from `view_count`),
- the post is currently ranked within the top 85% of the nonzero-scored slate
  (`LowImpressionsMaxPositionRatio = 0.85`),
- in the treatment arm, the post is **under 24 hours old**
  (`ColdStartMaxPostAgeSecs = 86400`).

The target score is drawn randomly from the score sitting at rank 15 to 16
(`ColdStartSlotMin`/`Max`), and only the single best-eligible under-exposed post
is lifted per request.
- **Takeaway:** if you are under 1,000 followers, every fresh original gets one
  guaranteed injection near slot 15 into feeds where it is retrieved. This is the
  biggest structural gift for new accounts, and it applies only to original
  posts under 24 hours old. Post originals, consistently, while you are small.

## 4. DPP diversity rerank (vm-ranker), theta = 0.65

The final rerank (`vm-ranker/dpp.rs`) greedily builds the slate from the top
**150** candidates (`VMRankerDppMaxSelectedRank`), trading each candidate's
**score** against its **redundancy** to already-selected posts. The kernel is
`K[i][j] = qf_i · qf_j · cos(embedding_i, embedding_j)`, where
`qf_i = exp(alpha · q_i)`, `q_i` is the score normalized by the pool's max
score, and `alpha = theta / (2(1 − theta))` (about 0.93 at theta 0.65). The
similarity is cosine over the same multimodal embeddings used in retrieval,
stored as f16 vectors. Greedy selection stops at `top_k` or when the marginal
gain falls below 1e-6 (near-duplicate exhaustion).

Behavior (from the tests in `dpp.rs`): among near-identical embeddings only the
single highest scorer survives, and an orthogonal (differentiated) candidate is
promoted even at a lower raw score.
- **Takeaway:** during a trend, do not post the same take as everyone else. Your
  embedding collides with higher-scored posts and you are dropped from adjacent
  slots. Post the orthogonal angle. Distinctiveness is rewarded at rerank,
  independent of your own score.

## 5. Timing and freshness: the 48-hour game

- Hard `AgeFilter`: posts older than **48 hours are removed** from the feed
  entirely (`MAX_POST_AGE = 48h`). The filter also drops a post if its creation
  time cannot be read.
- SimClusters excludes posts older than 48 hours from retrieval.
- Post age is a direct model feature, and cold-start requires under 24 hours.
- Served-post dedup excludes your last 100 served posts for 10 minutes.
- **Takeaway:** a post has roughly a 48-hour life, front-loaded into the first
  hours. Post when your coherent audience is active, so early engagement
  velocity (which compounds via the engagement-count features) lands inside the
  window.

## Note: scoring is skipped on cached posts

`PhoenixScorer` does not re-score posts served from the request cache
(`has_cached_posts`), and there is a kill-switch decider for the ranker. A
separate new-user history threshold can route accounts with short engagement
histories to a different model cluster. These are serving details, but they
explain why the same post can score slightly differently across refreshes.

## Priority order of levers (highest ROI first)

1. **Provoke high-value actions** (reply, quote, copy-link and DM share). See
   [scoring-weights.md](scoring-weights.md).
2. **Never trip negative signals or suppression labels.** See
   [negative-signals.md](negative-signals.md).
3. **Post original, fresh, niche-consistent content** (retrieval and cold-start).
4. **One strong post per session** (diversity decay).
5. **Differentiate from the current trend wave** (DPP).
6. **Build mutual-follow relationships** (+15 reply boost, easy OON-to-in-network
   flips).
