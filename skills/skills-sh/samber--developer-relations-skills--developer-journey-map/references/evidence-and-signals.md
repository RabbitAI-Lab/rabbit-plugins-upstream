# Evidence, signals and owners per stage

What to look for, what to count, and who usually owns it. Adapt the owner column to the actual org - the point of the column is that it names someone, not that it matches this table.

## Contents

- [Per-stage table](#per-stage-table)
- [Buyer-lane signal families](#buyer-lane-signal-families)
- [The friction log protocol](#the-friction-log-protocol)
- [The exit interview protocol](#the-exit-interview-protocol)
- [Support-signal mining](#support-signal-mining)
- [What each surface can physically report](#what-each-surface-can-physically-report)
- [Signal hygiene](#signal-hygiene)

## Per-stage table

Stage names below use the unsourced discover → advocate spine; map them onto whichever model the skill selected.

| Stage      | Evidence to gather                                                                                                                                                | Candidate signals (pick one)                                                       | Usual owner                     |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------- |
| Discover   | where inbound actually comes from; search queries that reach the docs; which communities mention the product; self-reported "how did you hear about us" free text | new self-reported first touches per month, by source                               | marketing or DevRel             |
| Evaluate   | friction log of a first read; docs searches returning nothing; comparison questions in community threads; competitor pages developers land on next                | docs sessions reaching a decision page; repo clones; trial starts                  | docs owner or product marketing |
| Try        | cold-run of the quickstart on a clean machine; step-level drop-off; time from signup to first result; the errors that appear in the first hour                    | median time to first success, and share of starters reaching it                    | developer experience or docs    |
| Adopt      | interviews about what got the product into a real project; the approval steps inside the user's own company; incident and limits questions                        | share of first-success users still active at 30 days; workloads in production      | product                         |
| Contribute | first-PR experience walkthrough; setup failures on machines the maintainers never tested; time to first review response                                           | first-time contributors per quarter; share who return for a second contribution    | maintainers                     |
| Advocate   | who already talks about the product unprompted; which of them got any support for it                                                                              | unprompted public mentions by named practitioners; talks or posts by non-employees | community or DevRel             |

Two stages have published evidence about what developers actually do there; use it to aim the questions rather than to fill the cells.

- **Evaluate.** Larios Vargas et al. (ESEC/FSE 2020, DOI 10.1145/3368089.3409711; 16 interviews, 115 survey respondents) ranked what developers say drives library selection: maturity/stability 62%, usability 55%, documentation 51%, license 45%, active maintenance 44%, security 39%, popularity 30% rated "highly influential". Same study, one interviewee: _"Checking security vulnerabilities is important, but I do not check it up-front."_ Read the ranking as a checklist of what an evaluation-stage surface has to answer, and read the quote as the reason to cross-check any self-report against behaviour.
- **Contribute.** GitHub's Open Source Guides report that contributors who received code review within 48 hours had a much higher rate of return and repeat contribution, and that "it only takes one negative experience to make someone not want to come back". Time-to-first-review is therefore the contribution stage's default signal, and the stage's exit event is the merge, not the submission.

Buyer lane, when the developer is not the buyer:

| Buyer stage         | Evidence                                                                                   | Candidate signal                              | Usual owner                       |
| ------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------- | --------------------------------- |
| Technical approval  | security questionnaires received; the questions that stall; architecture review objections | evaluations that clear security review        | security or solutions engineering |
| Commercial approval | licensing and dependency-policy blockers; procurement timelines                            | days from first approver contact to signature | sales or finance                  |

## Buyer-lane signal families

The developer lane counts people; the buyer lane counts accounts. Roll individual usage up to an account before reading anything in this lane - email domain, workspace or organisation object, licence or API key, or self-reported company. Each is imperfect; a lane with no rollup cannot be read at all, because forty signups from one company look like forty leads.

Three families, in increasing order of buying intent:

| Family           | What it looks like                                                                                                                                                     | Where it sits on the map                                                                      |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Depth            | production environment, sustained volume, wired into CI or a deployment pipeline, retention over weeks rather than a spike                                             | the developer lane's adoption/production stage, read at account level                         |
| Spread           | a second and third active developer in the same account, a shared workspace, invites sent, several repos or services                                                   | the entry trigger for the buyer lane - one developer is evaluation, three is a decision       |
| Boundary contact | someone opened an SSO or RBAC page, asked an audit or compliance question, hit a rate or seat limit, requested a security questionnaire, or looked at enterprise terms | the strongest and rarest signal, and the cleanest exit event for the buyer lane's first stage |

Boundary contact is the one worth instrumenting first: it is the only signal that maps directly onto the paid boundary, and it is cheap to capture because it is a page view or a support request the product already sees.

Record the champion explicitly as a row participant, not as a persona note. The champion argues the case when nobody from the vendor is in the room, so the artefact they carry - an internal one-pager, a re-runnable benchmark, a reference architecture, pre-answered licence and data-handling questions - is the buyer lane's real touchpoint. A pack nobody opens is evidence the champion does not exist yet, which is itself a finding about the stage.

## The friction log protocol

Google's DevRel practice popularised this artefact (Aja Hammerly, "An introduction to friction logging", developerrelations.com, 8 July 2018), and it remains the cheapest high-quality evidence for a journey map.

- Header: your name, platform, language, browser, date, product version.
- Scenario: one realistic use case in under two sentences, familiar enough that nobody asks "why would someone do that?".
- Body: a running log of actions and reactions. Record the search terms you used, which result you clicked and its URL, the commands and code you pasted verbatim, and your emotional reactions ("now I'm frustrated", "copied this from the docs without reading the prose").
- Convention: green for delight, yellow for friction, red for blocking.
- Unlike a bug report, minimal reproduction steps are not the goal - the narrative is.

Whoever is newest to the product is the best logger, because veterans route around rough spots without noticing.

## The exit interview protocol

Recruiting people who abandoned the journey is hard and worth the effort; they are the only witnesses to the stages that leak silently.

1. Open by removing the sales frame: you are not trying to win them back, only to understand the experience.
2. "Walk me through your experience with the product, from first contact to today."
3. "Was there a specific moment when you decided to stop?"
4. "What are you using instead, and what made it a better fit?"
5. "If you could change one thing, what would it be?"

Tag each answer with the stage it belongs to before analysing. Three abandonment interviews usually relocate the team's assumed leak by at least one stage.

## Support-signal mining

- Pull the last quarter of tickets, issues and community questions.
- Tag each by the stage the asker was in, not by product area.
- Count clusters, then check the biggest cluster against the friction log - a cluster can mean high friction or simply high traffic at that stage.
- Watch for the inverse signal: a stage with almost no questions and low conversion is a stage where people leave without speaking.

## What each surface can physically report

Before promising a signal, check the surface can produce it and check what it silently distorts. Three corrections change a developer journey map's numbers more than anything else.

**Analytics blocking.** Plausible Analytics measured its own proxied script against a third-party analytics script on a site carrying Hacker News and Reddit traffic (August 2021) and found **58% of that tech audience blocked the third-party script**. The breakdown: 82.3% on Linux, 88.3% on Firefox, 68.2% on desktop versus 49.9% on mobile.

A docs-site session count is therefore roughly measuring the non-developer half of a developer audience, and the blocking rate varies by page: an install page loses far more than a pricing page. Consequences for the map:

- never write an absolute traffic number in a cell
- compare step-to-step ratios inside one source
- fix it in cost order: first-party or proxied script, then server/CDN log analysis, then a product-side event for anything past signup

**Retention windows.** Three sources expire on their own schedule and cannot be backfilled:

- repository traffic endpoints keep **14 days** and need write access to that repository
- npm download data 18 months
- PyPI time series 180 days
- chat venues cap history by plan

Any signal drawn from those has to be snapshotted into your own store from the day it is defined, or next quarter's re-read has no baseline to compare against.

**Referrer loss.** Aggregators, chat clients, privacy browsers and slide links strip referrers, and roughly 70% of AI-assistant-driven traffic arrives with no referrer at all. A large "direct" bucket on the discovery stage is the normal case, not an instrumentation bug - label the stage inferred and move on rather than chasing it.

Two registry footnotes worth knowing before a download count becomes a signal: npm counts HTTP 200 responses for tarballs, including build servers and mirrors, so it is a request count and not a person count; PyPI excludes known mirrors by default. The two are not comparable, and neither is a user count.

## Signal hygiene

- **One signal per stage.** More turns the map into a dashboard and hides the decision.
- **Reject monotonic counters.** Total stars, cumulative signups and all-time downloads only go up and cannot fall when the journey breaks. Convert to a rate or a period delta.
- **Apply the "so what" test.** If the number moved 20% next month, would anyone act? If not, it is decoration.
- **Apply the ownership test.** Can the named owner plausibly move it within the review period?
- **Pair an incentivised volume metric with a quality counter-metric.** Rewarding signups produces throwaway accounts; pair it with 30-day retention of the same cohort. Rewarding closed issues produces premature closes; pair it with reopen rate.
- **Respect the small-N floor.** Below roughly 30 events in a period, publish the raw list with dates rather than a percentage.
- **State the attribution bias.** Self-reported attribution over-counts memorable touches and under-counts docs and search; tagged links under-count everything not clicked from a taggable surface and inflate "direct". Pick one, state its bias, hold it constant across quarters.
