## Description:

Travel Buddy helps agents discover, compare, and plan trips from incomplete traveler needs, then revise constraints and save booking-ready day-by-day HTML/JSON deliverables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and their assisting agents use Travel Buddy to choose feasible destinations, plan itineraries, verify current travel facts, manage opt-in local profiles, and produce booking-ready trip deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store local trip and profile files and use live web research, which may expose sensitive travel preferences if users enter unnecessary personal data.

Mitigation: Use a dedicated local workspace, review profile fields before reuse, and avoid entering passport numbers, payment details, credentials, exact addresses, or private account data.

Risk: Optional automatic assistant handoff can start a continuation task when the user only wants intake data collected.

Mitigation: Run the intake workflow with --assistant none when automatic Codex or Claude continuation is not desired.

## Reference(s):

- [Travel Buddy README](README.md)
- [Travel Buddy README (Chinese)](README_CN.md)
- [Booking-ready HTML output and safe research](references/booking-html-output.md)
- [Initial intake and preference map](references/initial-intake.md)
- [Regional service routing](references/regional-service-routing.md)
- [Reusable traveler profile and local artifact storage](references/profile-and-storage.md)
- [Research budget](references/research-budget.md)
- [Parallel verification](references/verification.md)
- [Destination decision, research, and explanation](references/decision-and-research.md)
- [Incremental replanning](references/replanning.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with generated JSON and self-contained HTML travel deliverables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local traveler profiles, trip JSON, verification reports, and final HTML files in a user-selected workspace.]

## Skill Version(s):

2.2.0 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
