## Description:

Discover, compare, and plan trips from incomplete traveler needs, then revise them when constraints change using local intake forms, opt-in traveler profiles, live research, and booking-ready HTML/JSON deliverables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use Travel Buddy to choose destinations, compare feasible options, collect consented travel preferences, and produce fact-checked trip plans. It is suited for travel inspiration, itinerary construction, and dependency-aware replanning when dates, constraints, or requirements change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores opt-in traveler profiles and generated plan files locally, which can include sensitive travel preferences.

Mitigation: Create reusable profiles only after explicit consent, avoid storing passport numbers, document images, payment data, credentials, exact home addresses, and private account context, and delete only the named local profile after confirming the path.

Risk: Loopback intake forms are intended for local use and could receive a submission from another local process while open.

Mitigation: Use the intake form only during the active workflow, rely on the short-lived random-port and single-submission behavior described by the artifact, and review saved profile or trip data before using it.

Risk: Travel facts such as fares, availability, entry rules, opening hours, and weather can become stale or be checked incompletely.

Mitigation: Require live-source research with source dates for volatile facts, run the five-domain verification before final delivery, and label unverified outputs as not fact-checked instead of booking-ready.

Risk: The workflow may start a new Codex or Claude task after trip form submission.

Mitigation: Use the documented assistant selection controls, including --assistant none, when automatic continuation is not desired.

Risk: Booking links and provider labels can be misleading if they are not checked against the destination they actually open.

Mitigation: Validate generated HTML, run link-target checks when network access is available, and have the user review booking links manually; the skill does not book, pay, log in, or change accounts.

## Reference(s):

- [Server-resolved GitHub source repository](https://github.com/dong845/travel-buddy)
- [ClawHub skill page](https://clawhub.ai/dong845/skills/travel-buddy)
- [Booking-ready HTML output and safe research](references/booking-html-output.md)
- [Destination decision, research, and explanation](references/decision-and-research.md)
- [Initial intake and preference map](references/initial-intake.md)
- [Reusable traveler profile and local artifact storage](references/profile-and-storage.md)
- [Regional service routing](references/regional-service-routing.md)
- [Research budget](references/research-budget.md)
- [Parallel verification](references/verification.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, shell commands, JSON plan files, and self-contained HTML travel pages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-first workflow; reusable profiles are opt-in and booking-ready plans should be verified before use.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
