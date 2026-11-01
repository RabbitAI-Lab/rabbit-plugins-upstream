# Developer journey stage models

Five stage vocabularies are in circulation. Pick one, keep its published names, and do not blend two - blended models produce stages with no agreed definition and two competing terminal states.

## Contents

- [The five models](#the-five-models)
- [Choosing between them](#choosing-between-them)
- [The unsourced default](#the-unsourced-default)
- [Why the tails disagree](#why-the-tails-disagree)
- [What the map has to add](#what-the-map-has-to-add)

## The five models

### 1. Revell's six-stage developer journey

Initial awareness → deep awareness → evaluation and validation → commitment → standardization → community and advocacy.

Matthew Revell, developerrelations.com, 16 June 2016, published alongside the CORE situational-analysis framework. The only published model with an explicit enterprise standardisation stage, where a tool stops being one team's choice and becomes an organisation's default.

Strong when: the product is a commercial developer platform sold into companies, and the interesting question is why teams adopt it but the organisation never standardises on it.

### 2. AAARRRP

Awareness → acquisition → activation → retention → referral → revenue → product.

Phil Leggetter, 2016, `leggetter.co.uk/aaarrrp/`, adapted from Dave McClure's AARRR "pirate metrics" with a seventh element for developer products: users and the DevRel team help define and build the product.

Strong when: the map has to line up with a company-wide funnel other teams already use, or the conversation ends in a revenue question. Weak when the desired end state is contribution rather than purchase - it has no vocabulary for that.

### 3. Orbit levels

Explorer → participant → contributor → advocate.

Orbit Model, developed by developer advocates from 2014, published on GitHub November 2019; no longer under active development, so cite it as a stable framework rather than a maintained product. Its two axes - love (depth of engagement with the mission) and reach (sphere of influence) - combine into "gravity".

Strong when: the journey is community-shaped and depth of relationship matters more than a purchase. Weak as a whole-journey model for a commercial product, because it says nothing about evaluation or production use.

### 4. API and platform five-stage arc

Awareness → onboarding → integration → production → advocacy.

Carried by the `gtm-developer-ecosystem` skill (beingsmit/technical-product-gtm). Its stages are useful; its published numbers are one company's anecdotes and must never be quoted as benchmarks.

Strong when: the product is an API or SDK and the real conversion is "running in production", which the commercial models tend to hide inside retention.

### 5. OSS contributor funnel

Land → find work → set up → change → submit → survive review → return.

Consolidated from GitHub's Open Source Guides and the newcomer-barriers research literature. Two steps leak hardest and leak silently: local setup, and waiting for review. GitHub's Open Source Guides report that contributors who received code review within 48 hours had a much higher rate of return and repeat contribution, and that "it only takes one negative experience to make someone not want to come back".

Strong when: the desired end state is contribution. Use it as the whole model for an OSS project, or as an expansion of a single "contribute" stage inside another model.

## Choosing between them

| If the end state is…                 | Use                    | Terminal stage  |
| ------------------------------------ | ---------------------- | --------------- |
| an organisation defaults to the tool | Revell six-stage       | standardization |
| paid conversion and expansion        | AAARRRP                | revenue         |
| deep community relationships         | Orbit levels           | advocate        |
| workloads running in production      | API five-stage arc     | production      |
| sustained outside contribution       | OSS contributor funnel | return          |

That table deletes rather than ranks: a model whose terminal stage is not the funded end state leaves the menu. The ranked comparison of what survives lives in the skill's step 1; the effort notes below only feed it.

Secondary criteria, in order:

1. **Observability.** Prefer the model whose stage boundaries you can already see in data you hold. This is the effort axis, and it decides the ranking in step 1.
2. **Ownership.** Prefer boundaries that fall on team lines, so each stage gets one accountable owner instead of a committee.
3. **Continuity.** If a previous map exists, keep its model unless it broke - comparability against your own history is worth more than a better-fitting vocabulary.

Effort to stand each one up, in orders of magnitude - evidence needed before a boundary can be counted:

| Model                  | Effort              | What makes it cost that                                                                          |
| ---------------------- | ------------------- | ------------------------------------------------------------------------------------------------ |
| API five-stage arc     | an hour to a day    | first call, integration and production usually already sit in product telemetry                  |
| OSS contributor funnel | a few days          | the repository holds first PR, review latency and return; recruiting abandoners is the slow part |
| AAARRRP                | a week to a quarter | mostly coordination: its stages must reconcile with a company-wide funnel another team owns      |
| Revell six-stage       | a quarter           | the standardisation boundary needs account rollup and buyer-side interviews almost nobody holds  |
| Unsourced default      | near-zero           | nothing to reconcile - and it buys no comparability, which is why cheapest is not first          |

## The unsourced default

Discover → try → adopt → contribute → advocate is the shorthand many teams start from. It is a merge of models 3, 4 and 5 rather than a framework anyone published. It works as a working spine for a first map, and it is honest to use - as long as nobody presents it as a framework, and as long as the "adopt" stage gets split once it becomes clear it hides both integration and production.

## Why the tails disagree

The models agree on the start and diverge after adoption because they were built for different desired outcomes:

- Revell ends where an organisation commits.
- AAARRRP ends at money plus product feedback.
- Orbit and the contributor funnel end where an individual takes on work for the project.

A map keeping all three tails has three terminal stages and therefore no priority order. Choose the tail that matches what funds the program, and demote the others to optional branches drawn under the main line.

## What the map has to add

Stage owners, and the exit event that proves a developer left one stage for the next, come from the map rather than from a stage model: the models stop at vocabulary. Revell's guide closed by promising per-stage measurement in a future guide that never followed, which is a fair summary of the field's state - the journey vocabulary is settled, per-stage measurement is not. Those columns are the map's real work and have to be derived per product.
