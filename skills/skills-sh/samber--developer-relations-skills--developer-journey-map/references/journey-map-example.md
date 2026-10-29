# Worked example and row quality

A fictional but realistic map, followed by weak-versus-strong versions of each column.

- **Product:** a hosted queue service with an SDK, sold self-serve with an enterprise tier.
- **Segment:** a backend engineer at a 50-500 person company.
- **End state:** production usage.

## Contents

- [The map](#the-map)
- [Buyer lane](#buyer-lane)
- [Moments](#moments)
- [Leak diagnosis](#leak-diagnosis)
- [Weak vs strong rows](#weak-vs-strong-rows)

## The map

Stage model: API and platform five-stage arc, chosen because the end state is production usage and the team already counts first API calls.

| Stage       | Developer's job                                       | Entry trigger            | Exit event                                                     | Touchpoints                                         | Owner                | Friction evidence                                                                                               | Signal                                                                    |
| ----------- | ----------------------------------------------------- | ------------------------ | -------------------------------------------------------------- | --------------------------------------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Awareness   | "find something better than the queue we hand-rolled" | search or peer mention   | lands on docs or repo                                          | search results, community threads, comparison posts | growth marketing     | 41 of 78 signup surveys last quarter said "colleague" - inferred, self-reported                                 | 78 self-reported first touches/quarter (inferred)                         |
| Onboarding  | "prove it works from my laptop"                       | opens the quickstart     | first successful publish + consume from local code             | quickstart, SDK install, dashboard, API keys        | developer experience | friction log 2026-08-14: key creation buried two clicks past a plan chooser; 11 min of 19 min run spent on auth | median 19 min to first success; 34% of quickstart starters reach it       |
| Integration | "wire it into our service behind a feature flag"      | first success reached    | SDK called from a service repo on a shared branch              | SDK reference, error docs, support                  | product              | 23 of 61 tickets last quarter were retry/idempotency semantics, all from this stage                             | 46% of first-success users make a call from a non-local IP within 30 days |
| Production  | "own this on call"                                    | staging traffic observed | sustained traffic for 14 days plus an alerting rule configured | runbooks, status page, limits docs, support         | product              | 3 of 3 exit interviews cited no documented failure semantics as the blocker                                     | 22% of integrating accounts reach 14-day sustained traffic                |
| Advocacy    | "tell people it saved us"                             | six months in production | public talk, post or unprompted recommendation                 | community, conference CFPs, changelog               | DevRel               | none gathered yet                                                                                               | 4 unprompted public mentions last quarter (raw list, below small-N floor) |

## Buyer lane

Present: the enterprise tier requires a security review. Two stages, both owned outside DevRel.

| Buyer stage         | Exit event                                  | Owner                 | Signal                                                          |
| ------------------- | ------------------------------------------- | --------------------- | --------------------------------------------------------------- |
| Technical approval  | security questionnaire returned and cleared | solutions engineering | 6 of 9 questionnaires cleared last quarter                      |
| Commercial approval | contract signed                             | sales                 | median 38 days from first approver contact (n=9, raw list kept) |

## Moments

- **First success**: first message published and consumed from local code. Median 19 minutes today.
- **Moment of truth**: the decision to put it behind a feature flag in a real service - this is where the team stops evaluating and starts depending.
- **Abandonment point**: inside onboarding, at API-key creation, earlier than the team assumed. The assumption before the map was that people churned during integration.

## Leak diagnosis

Onboarding. 34% of quickstart starters reach first success, the lowest owned conversion on the map, and it is the earliest stage with both a measured rate and an owner able to change it (developer experience owns the quickstart and the key-creation flow). Integration converts worse in absolute terms at 46%, but it sits downstream, so fixing onboarding raises its input volume before its rate is worth touching.

Handoff:

- developer experience owns the fix
- the signal to watch is share of quickstart starters reaching first success
- re-read the map in 90 days

Gaps: the awareness row is inferred from a self-report survey with a 12% response rate. Advocacy is below the small-N floor and stays a raw list until it is not.

## Weak vs strong rows

**Exit event**

- Weak: "developer understands the value proposition." Cannot be observed, counted or owned, so no one can be accountable for it.
- Strong: "first message published and consumed from local code." One event, already logged, unambiguous.

**Owner**

- Weak: "DevRel" in every row. Means nobody negotiated the map with the teams that own the surfaces.
- Strong: "developer experience" for onboarding, "product" for integration and production, "sales" for commercial approval - and the map notes that no one owns awareness, which is itself the finding.

**Friction evidence**

- Weak: "developers find auth confusing." A hypothesis wearing an evidence costume.
- Strong: "friction log 2026-08-14: key creation buried two clicks past a plan chooser; 11 of 19 minutes spent on auth." Cited, dated, reproducible.

**Signal**

- Weak: "total signups: 4,300." Monotonic, cannot fall when the stage breaks, and covers three stages at once.
- Strong: "34% of quickstart starters reach first success." A rate, scoped to one stage, movable by the named owner.

**Developer's job**

- Weak: "user enters the consideration phase." Describes the vendor's funnel, not a person's task.
- Strong: "prove it works from my laptop before I bring it to the team." A sentence a developer would recognise as their own.

**Leak diagnosis**

- Weak: "our 34% quickstart conversion is below the 40-60% industry benchmark, so onboarding is broken." The benchmark does not exist. Every number in circulation for this stage is one company's anecdote, measured against a different audience, a different product maturity and a different definition of "started". A map that argues from a borrowed rate cannot be checked, and it hides the only comparison that means anything.
- Strong: "34% of quickstart starters reach first success, down from 41% in the May map, and it is the earliest measured stage with an owner who can change it." Compared against itself, over a stated period, with the owner named in the same sentence.

**Why the stage leaks (B=MAP)**

- Weak: "developers aren't motivated to finish onboarding - we should add a value-prop banner above the quickstart." Reaches for motivation because copy is cheaper to write than steps are to remove. The friction log already said 11 of 19 minutes went to authentication, which is an ability problem, and no banner shortens it.
- Strong: "ability. The Ability Chain's weakest link here is time: key creation costs 11 of the run's 19 minutes because it sits two clicks past a plan chooser. Removing the plan chooser from the first-key path is the test." Names the branch, names the scarce resource, and proposes something falsifiable.

**Buyer lane**

- Weak: a lane with one row reading "enterprise deals - sales owns it", drawn from a list of individual signups. Forty developers from one company read as forty leads, so nothing in the lane can be counted.
- Strong: usage rolled up to an account by email domain, with three signals named:
  - depth (14-day sustained traffic)
  - spread (three active developers in one workspace)
  - boundary contact (someone opened the SSO page)

  Boundary contact is used as the lane's entry trigger, because it is the only one that maps onto the paid boundary.

- Also weak, in the other direction: an empty buyer lane on a self-serve product. Write "none - the developer decides and pays" explicitly, so the next reader knows it was decided rather than forgotten.
