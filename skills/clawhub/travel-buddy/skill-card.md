## Description:

Travel Buddy helps agents discover, compare, plan, and revise trips from incomplete traveler needs using local intake forms, live research expectations, and saved booking-ready HTML and JSON deliverables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT

## Use Case:

External users and travel-planning agents use this skill to turn incomplete trip preferences into destination shortlists, booking-ready itineraries, and dependency-aware replans. It is intended for advice, comparison, verification, and local deliverable generation, not for bookings or purchases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some validation and test paths can read local plan files beyond the active trip workspace.

Mitigation: Run validators only on trusted plan JSON and review the skill before installation until path scoping is corrected.

Risk: The skill creates local travel workspaces, serves temporary loopback forms, makes travel-research web requests, and saves trip/profile data locally.

Mitigation: Use the profile workflow only with explicit consent, avoid document numbers, payment details, passwords, and precise home addresses, and review saved local files before sharing them.

Risk: Travel facts such as fares, entry rules, opening hours, weather, and availability can change or remain unverified.

Mitigation: Require source dates and verification status in plans, and recheck critical facts directly before booking or traveling.

Risk: Explicit assistant modes can launch additional planning tasks if used intentionally.

Mitigation: Use the default automatic mode for ordinary assisted runs, and choose explicit assistant modes only when a separate planner is intended.

## Reference(s):

- [Travel Buddy ClawHub Page](https://clawhub.ai/dong845/skills/travel-buddy)
- [README](README.md)
- [Initial Intake](references/initial-intake.md)
- [Decision and Research](references/decision-and-research.md)
- [Research Budget](references/research-budget.md)
- [Verification](references/verification.md)
- [Profile and Storage](references/profile-and-storage.md)
- [Regional Service Routing](references/regional-service-routing.md)
- [Replanning](references/replanning.md)
- [Booking HTML Output](references/booking-html-output.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Code, Files]

**Output Format:** [Markdown guidance with inline shell commands and local HTML/JSON deliverables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a local Travel Buddy workspace, serve temporary loopback intake forms, run validation scripts, and save trip plans locally.]

## Skill Version(s):

2.5.0 (source: server release metadata and plugin metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
