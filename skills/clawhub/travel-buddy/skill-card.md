## Description:

Discover, compare, and plan trips from incomplete traveler needs, then revise them when constraints change.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and assistants use this skill to choose feasible destinations, compare trade-offs, build booking-ready itineraries, and replan when dates, constraints, or preferences change. It emphasizes live verification of volatile travel facts, local-first profile storage, and self-contained plan deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local travel profiles, drafts, plans, logs, and final HTML may contain personal travel preferences, itinerary details, or other sensitive context.

Mitigation: Install only if comfortable with local workspace storage, keep the workspace in a trusted location, and review or delete saved files when they are no longer needed.

Risk: Automatic continuation can start a separate planning run when the user does not want that behavior.

Mitigation: Use `--assistant none` when automatic continuation is not desired.

Risk: Travel intake could invite users to overshare sensitive data that is unnecessary for planning.

Mitigation: Do not enter passport numbers, document images, payment details, credentials, exact home addresses, or private account information.

## Reference(s):

- [Travel Buddy on ClawHub](https://clawhub.ai/dong845/skills/travel-buddy)
- [Booking-ready HTML output and safe research](references/booking-html-output.md)
- [Destination decision, research, and explanation](references/decision-and-research.md)
- [Initial intake and preference map](references/initial-intake.md)
- [Reusable traveler profile and local artifact storage](references/profile-and-storage.md)
- [Regional service routing](references/regional-service-routing.md)
- [Incremental replanning](references/replanning.md)
- [Research budget](references/research-budget.md)
- [Parallel verification](references/verification.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, HTML, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, plus local JSON and self-contained HTML travel deliverables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save local profiles, drafts, plans, logs, verification reports, and final HTML under a Travel Buddy workspace.]

## Skill Version(s):

2.4.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
