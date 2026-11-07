# Newsletter curators

Read this when the goal is editorial mentions in third-party developer newsletters, between announcements or around one. This file holds the per-newsletter routes for every skill in the collection. Growing a newsletter of your own is a different job: samber/developer-relations-skills@devrel-newsletter-growth.

## Contents

1. How curators find links
2. Content first, then three levers
3. Linkable content
4. Routes and rules per newsletter
5. Relationship upkeep
6. Templates
7. Tracking mentions
8. Limits

## 1. How curators find links

A practitioner newsletter is one person's or one small team's weekly judgement. Curators describe the same sources over and over:

- Feeds: RSS from engineering blogs, release announcements, other newsletters.
- Aggregators and communities: Hacker News, Reddit, language and ecosystem forums.
- Package-registry monitors for updates to popular packages.
- Reader submissions. At Cooperpress (JavaScript Weekly, Golang Weekly, Node Weekly and others), Peter Cooper put submissions at "perhaps about a third" of what runs, and any reader can send one as a reply to the issue email.

Two consequences:

- Being findable where the curator already looks does most of the work. A post with no feed, on a gated page, or mirrored only on a third-party platform is invisible to most of these sources.
- Some newsletters take no submissions at all. Hacker Newsletter curates only from Hacker News, and This Week in Rust takes project updates only from r/rust, so the route in is posting there. Vote solicitation is banned on Hacker News.

## 2. Content first, then three levers

Run these in order:

1. **Linkable content** is the precondition. A tip with nothing worth linking burns the curator's attention, and no relationship rescues it.
2. **Pick the levers** below for each piece.
3. **Mention tracking** runs on every piece, because it decides which newsletters stay on the map.

Ranked by mentions earned per hour, once a linkable piece exists:

| Lever                          | Effort                      | Value                                                                       |
| ------------------------------ | --------------------------- | --------------------------------------------------------------------------- |
| Tips by each curator's route   | `++` minutes per curator    | `++` the main route at Cooperpress, Console.dev and Changelog News          |
| Presence where curators source | `+` an hour per piece       | `++` the only route into Hacker Newsletter and This Week in Rust's projects |
| Relationship upkeep            | `-` a standing weekly habit | `-` thin evidence that familiarity alone earns a mention                    |

- effort: relationship upkeep > presence where curators source > tips
- value: tips == presence where curators source > relationship upkeep
- efficiency: tips > presence where curators source > relationship upkeep

Tips and presence tie on value because each is the only way into a different set of newsletters. Curators publish rules, not etiquette for pitches or follow-ups, and a reliable source who follows the rules gets picked.

The order starves relationship upkeep. Promote it when the media map shows one niche newsletter reaching most of the target developers and its curator is a peer in the same community. There, reading, replying and showing up is community participation the work needs anyway.

Re-rank against what you know: a founder already known to a curator moves tips first even for a smaller piece, and a team with unique data spends more on content, because a benchmark travels further than any tip.

## 3. Linkable content

Curators link pages, not companies. What they pick:

- Tutorials, walkthroughs and deep dives that explain something differently from the official docs.
- Benchmarks and survey data with methodology a reader can check.
- A release write-up that explains what changed and why it matters. This Week in Rust requires project items to be "more informative than just a changelog".
- Engineering case studies with a named engineer's byline in a personal register. Pointer's curator states a preference for personal blogs over corporate marketing.

What readers click once an item is included: curated learning repositories, survey data, tutorials and case studies topped JavaScript Weekly's most-clicked links of 2018.

What gets rejected, across the published rules:

- Paywalled or email-gated pages, including members-only blog platforms.
- Press releases and commercial announcements with no technical substance.
- Rants. This Week in Rust asks for a post explaining how to make the thing better instead.
- LLM-written articles. This Week in Rust refuses them outright.
- Duplicates of an item already covered.

Newsletters disagree on type, so match the piece to the newsletter before sending. This Week in Rust wants tutorials; Changelog News rejects tutorials and wants news.

Publish the piece on your own domain with an RSS feed and a canonical URL. A mirror elsewhere can point back to it, never replace it.

## 4. Routes and rules per newsletter

Check each newsletter's current page before sending. Routes close and change without notice.

| Newsletter                       | Route                                                                        | Rules worth knowing                                                                                                   |
| -------------------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Cooperpress titles               | Reply to any issue email                                                     | No published criteria; submissions worked weekly and the curator says he replies; sponsored items labelled            |
| This Week in Rust                | Pull request to the draft issue; project and tooling updates only via r/rust | Human-written articles only; link text equals page title, canonical URL, no tracking parameters                       |
| Console.dev                      | Email on its selection-criteria page                                         | Tools only, developer as primary user, self-service signup; a separate betas list takes only pre-1.0 or beta releases |
| Changelog News                   | Submission form                                                              | Own work encouraged; no tutorials, no commercial products; notifies only if published                                 |
| TLDR                             | A submissions address circulates, unconfirmed on TLDR's own pages            | Practical over breaking news; primary sources preferred                                                               |
| CNCF newsletter                  | marketing@cncf.io; KubeWeekly ended as a weekly and its old form may be dead | Of interest beyond one commercial platform, within the last month, not gated                                          |
| Hacker Newsletter                | None                                                                         | Curated only from Hacker News                                                                                         |
| Others with no published process | The editor's public contact, if one exists                                   | Assume the common rules: useful, ungated, recent, not a press release                                                 |

Send within a day of publishing, before the newsletter's weekly cut-off. CNCF takes nothing older than a month, and Cooperpress works submissions at weekends.

## 5. Relationship upkeep

Curators reward reliability, not familiarity. Keep the habit small and useful to them:

1. Read the last five issues in the public archive before the first tip, a self-set minimum that shows what the curator actually picks. Then subscribe.
2. Reply to an issue now and then with something useful to them: a correction, or a link that fits their beat and has nothing to do with you.
3. Share issues that featured anyone's good work, and credit the curator by name when you do.
4. Meet them where they already go: conferences they speak at, communities they post in. Expect nothing from it directly.
5. Send a coverage-gap note only to a newsletter that covered you before, after several substantive releases it missed. Cooper described these notes from already-covered projects as useful corrections. Never send one to a curator who has never covered you.

Never chase. Changelog News notifies only on publication, so silence there is a no. Cooperpress works weekly and says it replies, so wait one full cycle before reading silence as an answer.

## 6. Templates

Tip, sent as a reply to the latest issue or by the newsletter's route:

```
Subject: <what it is> - <the one fact a reader cares about>

<One sentence: what the piece shows, with the number or decision in it.>
Link: <ungated canonical URL>
Disclosure: I maintain <project>. / I work on <project> at <company>.
```

Coverage-gap note, once, to a newsletter that covered you before:

```
Since your mention of <project> in issue <N>, we shipped:
- <release>: <what changed, one line, link>
- <release>: <what changed, one line, link>
No reply needed. Thanks for the newsletter.
```

Thank-you, after a mention, with no new ask:

```
Thanks for including <piece> in issue <N>. <One line on what it changed, e.g. questions it brought in.>
```

Run every tip through your preferred humanizer skill before sending, as with any pitch in the main workflow. Never use it to pass off an LLM-written article as human-written.

## 7. Tracking mentions

Find the mention first, then measure the page, not the link:

- Detect mentions: subscribe to every newsletter on the map, search their public archives monthly, and watch This Week in Rust's public draft pull requests.
- Expect no usable UTM parameters on editorial links. Some curators forbid them, as This Week in Rust's style guide does, and others rewrite links. UTMs belong to paid slots.
- Expect most clicks to arrive with no referrer, because mail apps and RSS readers rarely send one. They show up as direct traffic.
- Record daily unique visitors on the linked page before sending, then read the lift against that baseline.
- Segment by referrer domain where one is present, and count unexplained direct lift on that page as probable newsletter traffic.
- Judge by what follows the visit: installs, signups, stars, issues opened. One practitioner's published log of a niche mention, a single case, shows tens to low hundreds of visits, not thousands.
- Log every tip and mention in the media map's pitch tracker: newsletter, issue, piece, route, outcome. Review it quarterly and drop newsletters that never pick or never convert.

## 8. Limits

- Send one tip per curator per real piece. Repeated tips for minor releases teach the curator to skip you.
- Never offer payment, a gift or reciprocity for an editorial pick. A sponsored slot is a separate purchase with its own label. Changelog News routes commercial products to sponsorship, and Console.dev holds advertisers to its editorial criteria.
- Disclose your affiliation in every self-submission, even where no rule asks for it.
- Never ask users or friends to submit your work for you without the same disclosure.
- Never ask anyone to upvote the piece on an aggregator a newsletter curates from.
- Accept no as the answer. Curator independence is what makes the mention worth having.
