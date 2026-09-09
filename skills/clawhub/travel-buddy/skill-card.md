## Description:

Travel Buddy helps agents discover, compare, plan, verify, and replan trips from incomplete traveler needs, producing booking-ready local HTML and JSON deliverables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel-planning agents use this skill to turn partial trip requirements into destination shortlists, verified itineraries, booking-review links, and dependency-aware replans without making purchases or account changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved profiles and trip workspaces can contain personal travel preferences and itinerary details.

Mitigation: Use the local consent-gated workspace, avoid passport numbers, document images, payment details, passwords, account credentials, and exact home addresses, and review or delete saved profiles when no longer needed.

Risk: Travel plans depend on volatile fares, timetables, operating hours, entry rules, weather, safety notices, and availability.

Mitigation: Verify current facts with live or official sources, label estimates and researched-current facts, and keep booking links browse-only for user review.

Risk: Optional background assistant handoff can start a separate planner if deliberately forced.

Mitigation: Use --assistant codex or --assistant claude only when a separate background planner is intended; otherwise continue in the active session.

## Reference(s):

- [Travel Buddy on ClawHub](https://clawhub.ai/dong845/skills/travel-buddy)
- [Initial intake and preference map](references/initial-intake.md)
- [Destination decision, research, and explanation](references/decision-and-research.md)
- [Research budget](references/research-budget.md)
- [Parallel verification](references/verification.md)
- [Booking-ready HTML output and safe research](references/booking-html-output.md)
- [Reusable traveler profile and local artifact storage](references/profile-and-storage.md)
- [Regional service routing](references/regional-service-routing.md)
- [Incremental replanning](references/replanning.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance plus generated JSON and self-contained HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save local traveler profiles, plan JSON, discovery JSON, verification reports, and self-contained HTML under a user-selected Travel Buddy workspace.]

## Skill Version(s):

2.6.0 (source: server release metadata and plugin manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
