# Skill routing reference

Read this before routing any task that could plausibly match two skills. Every disambiguation below comes from the siblings' own declared scopes, not from inference.

## Table of Contents

- [Boundary forks](#boundary-forks)
- [Do-not-route signals](#do-not-route-signals)
- [Host auto-selection](#host-auto-selection)
- [Ordered chains](#ordered-chains)
- [Coverage gaps](#coverage-gaps)
- [Sibling-collection recommendations](#sibling-collection-recommendations)

## Boundary forks

### Docs authoring - five skills, five jobs

Ask what the reader is trying to do, not what the page will be called.

| Reader's state                                             | Route to                                                           | Never route to                                                     |
| ---------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| Has never run the thing; needs one verified success fast   | `samber/developer-relations-skills@developer-quickstart-guide`     | `samber/developer-relations-skills@developer-tutorial`             |
| Wants to learn a concept by building something             | `samber/developer-relations-skills@developer-tutorial`             | `samber/developer-relations-skills@developer-quickstart-guide`     |
| Already competent; needs one specific task done            | `samber/developer-relations-skills@developer-how-to-guide`         | `samber/developer-relations-skills@developer-tutorial`             |
| Landed on the repository and is deciding whether to bother | `samber/developer-relations-skills@readme-optimization`            | `samber/developer-relations-skills@developer-quickstart-guide`     |
| Pasted an error string into a search box                   | `samber/developer-relations-skills@developer-troubleshooting-docs` | `samber/developer-relations-skills@developer-docs-structure-audit` |
| A coding agent, not a human, reading unattended            | `samber/developer-relations-skills@coding-agent-docs-optimization` | `samber/developer-relations-skills@developer-docs-structure-audit` |

Conflating a tutorial with a how-to guide fails both readers: the learner gets an unexplained recipe, the working developer gets a lecture. Route a how-to guide to `samber/developer-relations-skills@developer-how-to-guide`, never to the nearest neighbour. A breaking-change upgrade is a how-to with its own ordering rules and stays with `samber/developer-relations-skills@version-migration-guide`.

`samber/developer-relations-skills@developer-docs-structure-audit` operates on the whole docs set, never on one page. When the user asks "where should this page live", that is a structure question. When they ask "how do I write this page", route by reader state above.

`samber/developer-relations-skills@docs-code-sample-standards` owns the policy every sample obeys and the audit of an existing corpus. A single snippet inside one page being written belongs to whichever authoring skill owns that page. The portfolio of sample repos itself - which exist, who owns them, when they retire - belongs to `samber/developer-platform-skills@sample-app-strategy`.

`samber/developer-relations-skills@docs-localization-strategy` decides whether a language gets translated docs, which pages, and how translations stay current. Translating one file on request needs no skill. hreflang, canonicals and indexing of translated pages stay with `samber/developer-relations-skills@docs-seo`.

`samber/developer-relations-skills@docs-versioning-strategy` decides which versions keep docs and in what state, whether to run a version switcher, latest-only docs, per-major archives or version badges, how doc fixes get backported, which banners old pages carry, and when a docs version retires. The supported-versions table it maps from belongs to `samber/developer-relations-skills@oss-release-policy`. Canonical, noindex, sitemap and redirect mechanics for the version tree, including old docs outranking current, stay with `samber/developer-relations-skills@docs-seo`. Old-version AI answers stay with `samber/developer-relations-skills@developer-docs-ai-visibility`. The upgrade guide itself stays with `samber/developer-relations-skills@version-migration-guide`.

`samber/developer-relations-skills@developer-keyword-research` decides which pages to write from what developers actually search - error strings, task queries, integration intents - and never writes them. On-page and docs-site SEO stays with `samber/developer-relations-skills@docs-seo`.

`samber/developer-relations-skills@developer-docs-ai-visibility` owns how AI assistants and AI search cite the docs: which pipeline (training recall, search retrieval, live fetch) produced a wrong or old-version answer, the version signals and corrections that fix it, and a repeated prompt panel measuring version-correct answers. Crawl policy, canonicals and version-tree posture stay with `samber/developer-relations-skills@docs-seo`; machine-readable surfaces and unattended agent integration stay with `samber/developer-relations-skills@coding-agent-docs-optimization`; referral channel setup stays with `samber/developer-relations-skills@devrel-analytics`.

### Release communication - changelog vs migration guide

- `samber/developer-relations-skills@changelog-writing` - one release, everything that shipped, one line of action per breaking entry.
- `samber/developer-relations-skills@version-migration-guide` - one breaking change set, blast-radius ordering, before/after code, deprecation timeline, verified by upgrading a real project.

A major version usually needs both, in that order. A patch release needs only the first. Neither owns the versioning policy itself. A project's release contract - scheme, breaking-change definition, supported versions, backports, cadence, deprecation windows - belongs to `samber/developer-relations-skills@oss-release-policy`, written once and applied by both. A hosted API's version scheme belongs to `samber/developer-platform-skills@api-versioning-policy`.

### Security reports - the routing entry vs the pipeline

- `samber/developer-relations-skills@oss-issue-triage` - keeps security reports out of the public tracker: the chooser entry and the rule that a misfiled report is an emergency.
- `samber/developer-relations-skills@oss-security-disclosure` - everything behind that entry: SECURITY.md, private reporting, triage and scoring, embargo, CVE and advisory, patched release, downstream notice.

A security fix release still gets its notes from `samber/developer-relations-skills@changelog-writing`, after the advisory is public. Which lines receive the fix comes from the supported-versions table `samber/developer-relations-skills@oss-release-policy` writes. Shipping the patched package to its registry belongs to `samber/developer-platform-skills@sdk-package-publishing`.

### Measurement - four skills, four layers

- `samber/developer-relations-skills@devrel-metrics` - which numbers deserve a target, the attribution rule, and what gets cut. The framework layer.
- `samber/developer-relations-skills@devrel-analytics` - how those numbers get collected: event taxonomy, identity spine, link tagging, surface register. The instrumentation layer.
- `samber/developer-relations-skills@developer-community-health` - the community venue only: activity, responsiveness, contributor funnel, sentiment.
- `samber/developer-relations-skills@developer-survey-design` - asking developers directly: a recurring survey, its sample, its privacy handling, and what its published percentages may claim.

- "Our numbers disagree between tools" routes to `samber/developer-relations-skills@devrel-analytics`.
- "Leadership isn't convinced" routes to `samber/developer-relations-skills@devrel-metrics`.
- "Is our Discord dying" routes to `samber/developer-relations-skills@developer-community-health`.
- "We want to run a State of X survey and publish the numbers" routes to `samber/developer-relations-skills@developer-survey-design`; community-health supplies the sentiment items if the survey carries them.
- "Feature requests pile up in Discord and product never sees them" routes to `samber/developer-relations-skills@developer-feedback-loop` - it carries requests to a product decision and back; community health only measures the venue.
- Feature requests filed as code-host issues split in two: labels, response targets and staleness stay with `samber/developer-relations-skills@oss-issue-triage`; the product decision and the public reply go to `samber/developer-relations-skills@developer-feedback-loop`. Publishing the roadmap those decisions feed belongs to `samber/developer-platform-skills@public-roadmap-strategy`.
- "We lose developers somewhere between trial and production" routes to `samber/developer-relations-skills@developer-journey-map` - it names the leaking stage; `samber/developer-relations-skills@devrel-metrics` sets targets once the leak is known.
- "How do we compare to a competitor" routes to `samber/developer-relations-skills@devrel-competitor-analysis` - it looks outward; the other four look inward.

### Open source visibility - launch, distribution, transparency

- `samber/developer-relations-skills@oss-launch` - the launch window itself: readiness gate, positioning, channel sequencing, run of show, trending mechanics.
- `samber/developer-relations-skills@oss-distribution-strategy` - everything after that window: registry presence, curated lists, downstream packaging, release cadence as a visibility beat.
- `samber/developer-relations-skills@build-in-public` - the ongoing personal or company transparency practice, independent of any launch.
- `samber/developer-relations-skills@producthunt-playbook` - Product Hunt as a platform, launch or relaunch: whether a devtool belongs there, self-hunting, account and supporter eligibility, featuring vs points, maker comment, vote-solicitation and AI-comment rules, the two-month relaunch gap, product forum and Product Page afterwards.
- `samber/developer-relations-skills@hackernews-playbook` - Hacker News as a platform, launch or not: Show HN eligibility and the new-account block, title and first comment, thread conduct and staff disclosure, Who is hiring, flags, reposts and the second-chance pool.

"Adoption flattened after launch" is distribution, not a second launch. "What should I post every week" is build-in-public. "Which channels, in what order, on launch day" is oss-launch; "our Product Hunt listing, our launch was not featured, our points dropped, can we relaunch" is producthunt-playbook; "our Show HN text, our account can't post Show HN, our thread is on fire, our HN post died" is hackernews-playbook. `samber/developer-relations-skills@tech-press-relations` handles journalists, embargoes and third-party newsletter curators for any of the three; it never owns the announcement post itself.

### Maintainer load - the person vs the project

- `samber/developer-relations-skills@oss-maintainer-sustainability` - the maintainer's own capacity: time budget, published limits, maintenance-only mode, recruiting help, stepping down, handover or archive.
- `samber/developer-relations-skills@oss-governance` - the project's rules: decision rights, trust ladder, credential inventory, emeritus.
- `samber/developer-relations-skills@oss-issue-triage` - the queue's system: labels, response targets, staleness policy.

"I'm burned out and want to stop" routes to maintainer sustainability, which hands the ladder to governance and the queue design to triage. "We need a GOVERNANCE.md" never routes there. "I want to earn a living from it" routes to `samber/developer-relations-skills@oss-monetization`, unless the honest goal is fewer hours, which stays with maintainer sustainability.

### Sponsorship - who is paying whom

- `samber/developer-relations-skills@oss-monetization` - the maintainers of one project choose what to sell: paid add-on, support, content, hosting or a license move.
- `samber/developer-relations-skills@oss-sponsors-fundraising` - the maintainer wants sponsorship or grant money in.
- `samber/developer-relations-skills@oss-sponsors-brand-strategy` - the company decides which projects to fund.
- `samber/developer-relations-skills@developer-event-sponsorship` - the company buys conference, meetup or hackathon sponsorship.

Read the question's subject. "Which tier should we pick on this maintainer's page" is the company side, not the maintainer side. "Should I sell a Pro version" is monetization, not sponsorship; "set up GitHub Sponsors tiers" is sponsorship.

### Community - four skills on one timeline

1. `samber/developer-relations-skills@developer-community-launch` - before anything exists: should it exist, where, seeded how, and when to fold it back.
2. `samber/developer-relations-skills@developer-community-moderation` - the rules and the enforcement machinery, written before the first incident.
3. `samber/developer-relations-skills@developer-community-health` - measurement, once there is enough activity to have a baseline.
4. `samber/developer-relations-skills@developer-champions` - recognition and obligations for the top members, once a reliable top exists.

Recurring question sessions sit beside this timeline, not on it: `samber/developer-relations-skills@developer-office-hours-program` designs office hours or a standing AMA at any stage - format, time-zone slot, engineer rotation, scope card, write-up loop. "Our office hours get three people" routes there, not to community health; the requests those sessions surface route on to `samber/developer-relations-skills@developer-feedback-loop`.

A community that has not run 90 days has no health baseline; route measurement asks there to "not now" with that unblocking condition. `samber/developer-relations-skills@oss-contributor-onboarding` is the code-contribution equivalent of a community funnel and belongs to the open-source block, not here.

### Strategy - five skills that all sound like "what should we do"

- `samber/developer-relations-skills@devrel-strategy` - the DevRel program's own charter: driver, goals, pillars, staffing sequence, refused list.
- `samber/developer-relations-skills@devrel-team-structure` - where DevRel reports and how the team is shaped. Org design only.
- `samber/developer-relations-skills@devrel-budget-allocation` - the money split across pillars, with thresholds and a cut list.
- `samber/developer-relations-skills@developer-first-gtm` - how developer adoption becomes revenue. A company-level motion, not a DevRel charter.
- `samber/developer-relations-skills@devtools-business-model` - what is sold and how it makes money at all.

Chain them rather than choosing between them when the user is genuinely at zero: model → GTM → strategy → team → budget.

Three related, narrower skills: `samber/developer-relations-skills@devtools-pricing-strategy` sets the value metric and price points inside the business model; `samber/developer-relations-skills@open-source-company-strategy` decides which assets stay open; `samber/developer-relations-skills@oss-license-strategy` picks the license text for one project.

`samber/developer-relations-skills@oss-monetization` is the maintainer-scale counterpart of `devtools-business-model`: one project, its own maintainers, no outside funding, with hours and contributor trust as constraints. A funded company choosing its revenue model stays with `devtools-business-model`.

Two more sound like strategy and are not interchangeable with the five above:

- `samber/developer-relations-skills@developer-ecosystem-strategy` - whether and how far the product opens into a platform others build on. The revenue model stays with `samber/developer-relations-skills@devtools-business-model`; running the marketplace belongs to `samber/developer-platform-skills@connector-marketplace-strategy`.
- `samber/developer-relations-skills@open-standards-strategy` - how to engage one named standard or protocol: ignore, consume, certify, extend, contribute, co-found or drive. Governing your own project stays with `samber/developer-relations-skills@oss-governance`.

### Speaking and media - sequence, not competition

`samber/developer-relations-skills@conference-cfp-submission` (get accepted) → `samber/developer-relations-skills@tech-talk-outline` (structure the talk) → `samber/developer-relations-skills@developer-live-demo-design` (make the demo survive). None of them writes slides or coaches delivery.

- `samber/developer-relations-skills@tech-podcast-interview-prep` is for being someone else's guest.
- `samber/developer-relations-skills@technical-video-script` is for your own recorded video.
- `samber/developer-relations-skills@engineering-blog-post` is the written form.
- `samber/developer-relations-skills@devto-playbook` publishes that written form on dev.to - organization account, canonical cross-posting, tag rules, AI disclosure, cadence - and never drafts it.
- `samber/developer-relations-skills@developer-case-study` is the customer's story rather than yours.
- `samber/developer-relations-skills@devrel-content-calendar` plans the quarter these pieces land in and never writes them.
- `samber/developer-relations-skills@devrel-newsletter-program` designs a standing newsletter as a programme - whether to run one, cadence, template, owner, sunset - and never writes an issue. Release notes stay with `samber/developer-relations-skills@changelog-writing`; the quarter's slot plan stays with the calendar.
- `samber/developer-relations-skills@devrel-newsletter-issue` writes, edits or reviews one issue against that programme's template - item write-ups, own releases, sponsor slot, email-safe code, plain-text part, pre-send check, corrections. It starts once the items are chosen; a launch announcement, transactional or internal staff email is not an issue.
- `samber/developer-relations-skills@devrel-newsletter-deliverability` keeps that newsletter's opt-in mail in the inbox - authentication and the sending subdomain, Gmail, Yahoo and Outlook bulk-sender rules, one-click unsubscribe, warm-up after a platform move or a silent stretch, bounce handling, spam-folder diagnosis. Consent and who may be mailed stay with the list-growth side; cold outbound sales email is out of this collection entirely.
- `samber/developer-relations-skills@devrel-newsletter-growth` grows and keeps that newsletter's list - signup surfaces, consent when adding subscribers, item pitches and swaps with other newsletters, churn reading, per-source metrics. Cadence stays with the programme skill; a release pitched to reporters, with no newsletter of your own to grow, stays with `samber/developer-relations-skills@tech-press-relations`.
- `samber/developer-relations-skills@devrel-newsletter-sourcing` picks one issue's items against that charter - intake channels, the window since the last issue, primary-source and duplicate gates, the thin-issue call - and never writes the copy. A topic that needs its own post goes back to the calendar.
- `samber/developer-relations-skills@devrel-newsletter-sponsorship` sells sponsor slots in a newsletter you publish - sellability gate, acceptance policy, slots and caps, a rate card priced from human clicks, the ad label, booking terms, the sponsor report. Whether the newsletter carries ads at all stays with the programme charter; buying a slot in someone else's newsletter is not this skill; sponsor tiers that fund a project stay with `samber/developer-relations-skills@oss-sponsors-fundraising`.

### Events - speak, sponsor, or run it yourself

- `samber/developer-relations-skills@conference-cfp-submission`, `samber/developer-relations-skills@tech-talk-outline`, `samber/developer-relations-skills@developer-live-demo-design` - you are on someone else's stage.
- `samber/developer-relations-skills@developer-event-sponsorship` - you are paying to appear at someone else's event.
- `samber/developer-relations-skills@developer-meetup-program` - you run a small recurring local group yourself: format, cadence, speaker pipeline, venue sponsor, health.
- `samber/developer-relations-skills@devrel-webinar-program` - you run a recurring online technical webinar series yourself: format mix, seasons, topic backlog, speakers, replay, and the lead-handoff contract with sales. A Q&A-only series goes to the office-hours skill instead; platform, streaming and moderation mechanics go to `samber/dev-event-organizer-skills@virtual-event-production`.

Ask who owns the event before routing. A conference or hackathon you organize is not `samber/developer-relations-skills@developer-meetup-program` - that is organizer work and belongs to `samber/dev-event-organizer-skills` (see below).

### Employer brand - the strategy, the surfaces, the other side of the table

- `samber/developer-relations-skills@tech-employer-branding` - why engineers should want to work here, and which channels carry that claim: the EVP, the verification-surface audit, the ranked channel bets, the hiring measurement baseline. Strategy altitude; it produces no artefact.
- `samber/developer-relations-skills@engineering-blog-post` - one post the plan commissions.
- `samber/developer-relations-skills@github-profile-optimization` - the code-host profile the plan audits as one verification surface.
- `samber/developer-relations-skills@devrel-career` - the candidate reading those same surfaces from the other side of the table.

Ask who is hiring whom.

- "How do we attract senior engineers" is the strategy skill.
- "Write the post" and "fix the profile" are the execution skills - and a plan that skips straight to them has no EVP behind it.
- Hiring for DevRel roles specifically - role definitions, job postings, interview loops, scorecards - is none of the four; route to `samber/developer-relations-skills@devrel-hiring`.

### Profile surfaces

`samber/developer-relations-skills@readme-optimization` owns one repository's README. `samber/developer-relations-skills@github-profile-optimization` owns the personal or organization profile page and which repositories get pinned. When both are in play, fix the pinned repositories' READMEs first - the profile sends traffic into them. The repository's GitHub surfaces beyond the page - Discussions, release notifications, topics, star policy - belong to `samber/developer-platform-skills@github-engagement-playbook`.

### Education - the program vs the credential

`samber/developer-relations-skills@developer-education-strategy` decides whether to invest in structured education and which rung - curated path, curriculum with labs, badge, certification. `samber/developer-relations-skills@developer-certification-program` designs the credential once one is on the table, mostly for freelancers and IT services firms selling consulting: the outside consumer gate, tier, exam format, proctoring and identity, renewal tied to product versions, fees, verification, the expert directory, revocation and retirement, plus the prep course hosted on a MOOC or edtech platform and the training and exam-delivery partners. A prep course for one credential stays here; a curriculum or academy beyond it is education strategy. Run education strategy first when no curriculum exists yet; go straight to the certification skill when the ask is about an exam, a badge or its renewal.

## Do-not-route signals

- Debugging a live production incident → not `samber/developer-relations-skills@developer-troubleshooting-docs`; that skill writes the page afterwards.
- Reviewing the product's own source code or error strings → outside the collection.
- Triaging one specific issue → not `samber/developer-relations-skills@oss-issue-triage`; that skill designs the system.
- Tracking a rival vendor's DevRel motion → not `samber/developer-relations-skills@devrel-radar`, which builds a personal watch list of sources; route to `samber/developer-relations-skills@devrel-competitor-analysis`.
- Reporting a vulnerability in someone else's project, or patching CVEs in the user's own dependencies → not `samber/developer-relations-skills@oss-security-disclosure`, which is maintainer-side only; outside the collection.
- Configuring the user's own Dependabot or Renovate, or pinning someone else's package → not `samber/developer-relations-skills@oss-release-policy`, which writes the maintainer's contract; outside the collection.
- Legal sign-off on a license, CLA, trademark or contract → every relevant skill is a decision framework and says so.
- Recruiting or interviewing DevRel staff → route to `samber/developer-relations-skills@devrel-hiring`, not `samber/developer-relations-skills@devrel-career` (candidate side only) or `samber/developer-relations-skills@tech-employer-branding` (engineering employer brand, not a role's interview loop).
- Writing courses or lesson content → `samber/developer-relations-skills@developer-education-strategy` stops at the operating model.
- Writing exam items, running exam delivery, or preparing as a candidate for someone else's exam → not `samber/developer-relations-skills@developer-certification-program`, which designs the issuer's program; outside the collection.
- Certifying a partner's connector or integration rather than a person → not `samber/developer-relations-skills@developer-certification-program`; recommend `samber/developer-platform-skills@connector-certification-program`. Admitting a partner's app to a marketplace → `samber/developer-platform-skills@app-marketplace-review`.
- Building the slides, editing the video, running the camera → outside the collection.
- Drafting a dev.to article → not `samber/developer-relations-skills@devto-playbook`, which only covers publishing and engaging there; route to `samber/developer-relations-skills@engineering-blog-post`. Administering a self-hosted Forem instance → outside the collection.
- Product-user onboarding (in-app) → not `samber/developer-relations-skills@oss-contributor-onboarding`, which is about code contribution.
- Reading or tracking Product Hunt launches, topics or leaderboards through its API → not `samber/developer-relations-skills@producthunt-playbook`, which covers how to take part on the site; outside the collection.
- Fetching, summarizing or monitoring Hacker News stories through its API → not `samber/developer-relations-skills@hackernews-playbook`, which covers how to take part on the site; outside the collection.
- Brand or marketing-page share in AI answers, or the docs site's own AI assistant → not `samber/developer-relations-skills@developer-docs-ai-visibility`, which covers third-party assistants citing the docs; outside the collection.

## Host auto-selection

Some harnesses select a skill by matching the request against every installed skill's `description`, before this kickoff runs - triggering a sibling directly, or the kickoff and a sibling together.

- A sibling triggered directly, without the kickoff, is not a bypass to correct: each sibling's `description` triggers standalone, and the kickoff exists for ambiguous or multi-skill requests only.
- When both fire on the same request, treat the kickoff's decision as confirming what the harness already started, never a second dispatch that re-runs or contradicts a sibling in progress.

Pattern from `penpot/penpot-ai-kit@penpot-router`: a router degrading to a confirmation role once a host has already auto-selected by description.

## Ordered chains

Offer a chain only when the task genuinely decomposes. Every chain below is in dependency order, not efficiency order: a later link consumes what the earlier one produces and cannot run before it, so ranking a chain adds nothing. Common ones:

- **First DevRel hire, nothing exists:** `samber/developer-relations-skills@developer-segmentation` → `samber/developer-relations-skills@devrel-strategy` → `samber/developer-relations-skills@devrel-metrics` → `samber/developer-relations-skills@devrel-content-calendar`.
- **Open-sourcing a project:** `samber/developer-relations-skills@oss-license-strategy` → `samber/developer-relations-skills@readme-optimization` → `samber/developer-relations-skills@oss-contributor-onboarding` → `samber/developer-relations-skills@oss-launch` → `samber/developer-relations-skills@oss-distribution-strategy`.
- **Docs overhaul:** `samber/developer-relations-skills@developer-docs-structure-audit` → `samber/developer-relations-skills@developer-quickstart-guide` → `samber/developer-relations-skills@developer-how-to-guide` → `samber/developer-relations-skills@docs-code-sample-standards` → `samber/developer-relations-skills@docs-seo`.
- **Major version release:** `samber/developer-relations-skills@version-migration-guide` → `samber/developer-relations-skills@changelog-writing` → `samber/developer-relations-skills@engineering-blog-post`.
- **Conference season:** `samber/developer-relations-skills@conference-cfp-submission` → `samber/developer-relations-skills@tech-talk-outline` → `samber/developer-relations-skills@developer-live-demo-design`.
- **Community from zero:** `samber/developer-relations-skills@developer-community-launch` → `samber/developer-relations-skills@developer-community-moderation` → `samber/developer-relations-skills@developer-community-health` → `samber/developer-relations-skills@developer-champions`.
- **Proving the program:** `samber/developer-relations-skills@devrel-metrics` → `samber/developer-relations-skills@devrel-analytics` → `samber/developer-relations-skills@devrel-budget-allocation`.
- **Maintainer sustainability money:** `samber/developer-relations-skills@oss-sponsors-fundraising` → `samber/developer-relations-skills@build-in-public`.

Each link hands the next one a named artifact. If you cannot say what gets handed over, there is no chain - route to one skill instead.

## Coverage gaps

State these plainly as gaps. Do not route to a neighbour.

- The exec-facing DevRel report narrative and budget defense.
- A trademark _usage and enforcement_ policy aimed at third parties. Who holds the mark, the domains and the registry accounts belongs to `samber/developer-relations-skills@oss-governance`; clearing a name before launch belongs to `samber/developer-relations-skills@oss-launch`; registering it before selling belongs to `samber/developer-relations-skills@oss-monetization`. Monetizing one open-source project is _not_ a gap - `samber/developer-relations-skills@oss-monetization` owns it - nor are maintainer burnout (`samber/developer-relations-skills@oss-maintainer-sustainability`) or succession and bus-factor planning (`samber/developer-relations-skills@oss-governance`: contributor absence factor, trust ladder, inactivity rule, emeritus).
- Organizing your own conference or hackathon, conference booth operations, post-event follow-up.
- Student and campus programs. A developer newsletter is _not_ a gap at programme level - `samber/developer-relations-skills@devrel-newsletter-program` owns it; writing one issue is not a gap either - `samber/developer-relations-skills@devrel-newsletter-issue` owns it; finding each issue's items belongs to `samber/developer-relations-skills@devrel-newsletter-sourcing`; inbox placement belongs to `samber/developer-relations-skills@devrel-newsletter-deliverability`; list growth belongs to `samber/developer-relations-skills@devrel-newsletter-growth`; selling its sponsor slots belongs to `samber/developer-relations-skills@devrel-newsletter-sponsorship`.
- Choosing a docs platform, and monitoring brand mentions across developer channels or brand share in AI answers. Docs cited at the right version in AI answers is _not_ a gap - `samber/developer-relations-skills@developer-docs-ai-visibility` owns it.
- Per-community playbooks for Reddit, Lobsters, X or LinkedIn. Hacker News is _not_ a gap - `samber/developer-relations-skills@hackernews-playbook` owns it.
- Producing any final asset: slides, video files, rendered graphics, published pages.
- Legal advice of any kind.

## Sibling-collection recommendations

Same owner, separate collections. Recommend installing one; never depend on it.

| Signal in the task                                                                                                                                                                                                                   | Belongs to                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| Public API surface design, versioning policy, error shape, rate limits, idempotency                                                                                                                                                  | `samber/developer-platform-skills`                              |
| Endpoint-level reference completeness, undocumented operations, spec-to-docs drift                                                                                                                                                   | `samber/developer-platform-skills@api-reference-quality`        |
| A hosted API's version scheme, breaking-change definition, deprecation notice windows, sunset signalling                                                                                                                             | `samber/developer-platform-skills@api-versioning-policy`        |
| Breaking-change CI gate on spec diffs (oasdiff, graphql-inspector, buf), an API changelog or change feed generated from the contract                                                                                                 | `samber/developer-platform-skills@api-changelog-automation`     |
| Which deployed integrations still call a deprecated API surface or old SDK, who owns them, chasing them before a sunset, brownouts, sunset readiness | `samber/developer-platform-skills@integration-health-monitoring` |
| Webhooks, sandbox and test mode, integration observability, API status communication                                                                                                                                                 | `samber/developer-platform-skills`                              |
| SDK portfolio decisions, developer portal design, OAuth for third-party apps                                                                                                                                                         | `samber/developer-platform-skills`                              |
| Building your own connector marketplace, app review, listing standards, marketplace economics                                                                                                                                        | `samber/developer-platform-skills`                              |
| Which sample repos, reference apps and templates exist, who owns them, when they retire                                                                                                                                              | `samber/developer-platform-skills@sample-app-strategy`          |
| Publishing SDK packages or CLI binaries (npm, PyPI, Maven, NuGet, Go, crates.io, pub.dev, RubyGems, Packagist, Hex, SwiftPM, CocoaPods, Homebrew, winget, Scoop), CI auto-publishing, trusted publishing, rolling back a bad version | `samber/developer-platform-skills@sdk-package-publishing`       |
| The public CLI wrapping the API: commands, `--json` and exit codes, CLI login, agent-safe use                                                                                                                                        | `samber/developer-platform-skills@cli-interface-design`         |
| Shipping an Agent Skill (SKILL.md) inside an SDK or CLI repo, versioned with each release                                                                                                                                            | `samber/developer-platform-skills@agent-skill-offering`         |
| Opening the product to AI agents beyond docs: which agent classes reach signup, app and API, agent identity and delegated auth, agents provisioning resources, counting agent usage | `samber/developer-platform-skills@agent-integration-surfaces` |
| Building, adopting or publishing the product's own Terraform/OpenTofu provider                                                                                                                                                       | `samber/developer-platform-skills@terraform-provider-offering`  |
| Whether to ship an official VS Code or JetBrains extension, Open VSX and marketplace publishing, extension telemetry and deprecation                                                                                                 | `samber/developer-platform-skills@ide-extension-offering`       |
| Whether and how to publish the roadmap, commitment wording, voting boards                                                                                                                                                            | `samber/developer-platform-skills@public-roadmap-strategy`      |
| Flat GitHub stars after launch, Discussions, release notifications, topics, star-buying asks                                                                                                                                         | `samber/developer-platform-skills@github-engagement-playbook`     |
| A vendor's product tag on Stack Overflow, staff answering, self-promotion flags, unanswered backlog                                                                                                                                  | `samber/developer-platform-skills@stackoverflow-playbook`       |
| Your product's own Zapier integration: triggers, Platform CLI code, app-directory review and beta, Zap templates, partner tier, versions                                                                                             | `samber/developer-platform-skills@zapier-integration-playbook`              |
| Your product's own Slack app on the Slack Marketplace: submission, scope justifications, a returned review, listed vs unlisted, delisting warnings | `samber/developer-platform-skills@slack-app-directory-playbook` |
| Organizing your own conference, meetup logistics at production scale, hackathon operations                                                                                                                                           | `samber/dev-event-organizer-skills`                             |
| Selling sponsorship as the organizer, prospectus, pricing, fulfillment                                                                                                                                                               | `samber/dev-event-organizer-skills`                             |
| Running a CFP as the organizer, talk selection, speaker sourcing, hospitality and coaching                                                                                                                                           | `samber/dev-event-organizer-skills`                             |
| Venue, ticketing, schedule design, run of show, attendee experience                                                                                                                                                                  | `samber/dev-event-organizer-skills`                             |
| Registration forecast, headcount for catering or hotel block, when registration hits its cap                                                                                                                                         | `samber/dev-event-organizer-skills@event-registration-forecast` |
| Virtual event platform, remote-speaker setup, live chat and Q&A moderation staffing                                                                                                                                                  | `samber/dev-event-organizer-skills@virtual-event-production`    |

The line for events runs through who is paying: this collection covers the speaker and the sponsor; the event collection covers the organizer. The line for platforms runs through who builds the surface: this collection covers documenting and evangelizing it; the platform collection covers designing it.

Say it as a recommendation: "This is organizer-side work - `samber/dev-event-organizer-skills` covers it; this collection stops at the sponsor and speaker side." Then stop. Do not improvise the sibling's advice.
