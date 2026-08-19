## Description:

Discover, compare, and plan trips from incomplete traveler needs, then revise them when constraints change and save booking-ready day-by-day travel HTML/JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers and travel-planning assistants use this skill to decide where to go, compare destination constraints, build booking-ready day-by-day itinerary artifacts, and revise plans when requirements change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can save travel preferences and trip plans locally, including reusable traveler profiles when the user opts in.

Mitigation: Use the consent-gated profile flow, review any saved profile before reuse, and avoid entering passport numbers, document images, payment details, credentials, exact addresses, or private account context.

Risk: Automatic assistant handoff can start or delegate follow-up planning work after form submission.

Mitigation: Use --assistant none when automatic continuation is not desired, and review generated plans and saved outputs before acting on them.

Risk: Travel facts such as entry rules, fares, timetables, opening hours, and availability can become wrong if not checked live.

Mitigation: Run the documented verification workflow and treat unverified or stale facts as planning assumptions rather than booking-ready conclusions.

## Reference(s):

- [Booking-ready HTML output and safe research](references/booking-html-output.md)
- [Destination decision, research, and explanation](references/decision-and-research.md)
- [Initial intake and preference map](references/initial-intake.md)
- [Reusable traveler profile and local artifact storage](references/profile-and-storage.md)
- [Regional service routing](references/regional-service-routing.md)
- [Incremental replanning](references/replanning.md)
- [Research budget](references/research-budget.md)
- [Parallel verification](references/verification.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, HTML, Shell commands]

**Output Format:** [Markdown guidance plus local JSON and self-contained HTML travel plan files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local loopback intake forms, validation reports, saved profile data when the user opts in, and booking-ready trip deliverables.]

## Skill Version(s):

2.3.0 (source: server release metadata and plugin manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
