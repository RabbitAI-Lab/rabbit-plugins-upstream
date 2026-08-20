# Myth-Busting: common X advice the code contradicts

> Each entry cites the mechanism in X's open-source algorithm that confirms or
> refutes it. This is the skill's biggest edge over generic "grow on X" advice:
> most of that advice is folklore the actual ranking code disproves.

### Myth: "Hashtags boost your reach."
**False.** The per-candidate features the ranking model receives (`TweetInfo`,
built in `home-mixer/models/candidate.rs`) contain **no hashtag signal** at all.
The model conditions on a semantic embedding, engagement-count buckets, graph
relationship, post age, and media flags. Hashtags only matter insofar as they
shift your text embedding. Meanwhile 3+ hashtags correlate with spam patterns
and weaken the human hook. Use 0–1, for genuine discoverability only.

### Myth: "Ask for likes/retweets, engagement bait works."
**False and actively harmful.** "Like if you agree / RT to win / follow for
follow / comment GO" patterns are exactly what the spam classifiers target
(`SPAM_HIGH_RECALL` → out-of-network drop) and they provoke `not_interested`
(−43.2) and `mute` (−58.8). You trade a few cheap likes (0.5 each) for
negative signals worth ~100× more each.

### Myth: "Post as often as possible to maximize reach."
**False.** Author-diversity decay multiplies your k-th post in a viewer's slate
by `(1−0.25)·0.5^k + 0.25`: 2nd post ×0.625, 3rd ×0.44, floor ×0.25
(`ranking_scorer.rs`). Flooding demotes *your own* later posts. One strong
original per session beats ten.

### Myth: "Likes are the metric that drives distribution."
**False.** Favorite weight is **0.5**, the lowest positive. Copy-link share is
**20**, reply/quote/DM-share **5**, follow **4** (`param.rs`). The algorithm
rewards forwarding and conversation, not approval.

### Myth: "Controversy and ratio-bait drive reach."
**False over any horizon beyond one post.** agatha computes
blocks-per-favorite, reports-per-favorite, and spam-reports-per-favorite where
the denominator is *out-of-network favorites*. High ratios apply account-level
labels (`ABUSIVE_HIGH_RECALL`, `DO_NOT_AMPLIFY`, spam) that silently cap your
stranger-reach. One report is −234. Controversy inflates the numerator faster
than the likes inflate the denominator.

### Myth: "The algorithm hates external links, never post them."
**Nuanced, not a blanket ban.** There is no flat link penalty; link-open is a
positive action (+0.2) and click is +0.4. The real issues are: (1) a
`MALICIOUS_URL` label drops you out-of-network, so a sketchy domain/shortener
hurts; (2) links are low-value actions and pull attention off-platform, costing
dwell. Verdict: links are fine. Vet the domain, and put the value in the post
itself rather than behind the link.

### Myth: "Video always gets boosted."
**Nuanced.** Video-open and video-quality-view are only **+0.05** each, and VQV
requires the video to be **≥ 10 seconds** (`MinVideoDurationMs`). Video isn't
inherently boosted; it just adds low-weight actions plus dwell-time potential.
A great text thread can out-dwell a weak video.

### Myth: "New accounts can't get any reach."
**False. New accounts have a structural on-ramp.** The cold-start boost injects
one fresh (<24h) **original** post from a ≤1,000-follower account near slot 15
per eligible feed load (`author_cold_start.rs`). The catch: it must be an
original (not a reply/retweet) and you must not sabotage it with negative
signals. (Note the separate fact that new *viewers* see mostly in-network
content, which is about who's watching, not who's posting.)

### Myth: "Reply under big accounts to ride their reach."
**Nuanced.** Replies are out-of-network-discounted (×0.75) and are
**cold-start-ineligible**. Replying gets you visibility to that thread's
in-network audience, which is a real relationship and visibility play, but it is
not an algorithmic out-of-network reach vehicle. For reach, post originals.

### Myth: "The algorithm reads my post and judges its quality."
**False.** The model never sees your raw text. It sees an embedding plus
engagement counts and graph/context features (`candidate.rs`,
`phoenix_request.rs`). It infers quality *indirectly* from the human actions it
predicts, not from comprehension. This is why early engagement from a coherent
audience matters so much: it's the signal the system actually reads.

### Myth: "Delete and repost underperformers to get a second shot."
**Weak/false.** Previously-seen and previously-served posts are filtered
(`PreviouslySeenPostsFilter`, served-dedup of your last 100 for 10 min), and
reposting identical content lands in the same embedding neighborhood with the
same weak predicted-action profile. Rework the content, don't recycle it.

### Myth: "Editing a post kills its reach."
**Mostly false.** `DropStaleTweetsRule` drops the *superseded* (old) edit
version, not your current one. Editing doesn't penalize the live post; it just
retires the stale copy.

---

**The through-line:** almost every piece of popular X-growth advice optimizes
for *likes and volume*. The code optimizes for *forwarding, conversation, and
not annoying people*. When folklore and the weight table disagree, trust the
weight table.
