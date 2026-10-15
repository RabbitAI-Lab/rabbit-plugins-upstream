## Description:

Helps agents access App Store Connect apps, TestFlight builds and testers, customer reviews, sales and finance reports, and team users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

App developers and team members use this skill to inspect app and TestFlight status, manage testers and users, respond to reviews, and retrieve sales and finance reports through App Store Connect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to App Store Connect credentials may expose account data or permit privileged changes.

Mitigation: Use the least-privileged Apple API key needed for the workflow and protect the .p8 private key.

Risk: Tester changes, review responses, beta submissions, and team invitations can alter live account state.

Mitigation: Review action previews and approve only intended changes before execution.

## Reference(s):

- [App Store Connect API documentation](https://developer.apple.com/documentation/appstoreconnectapi)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/app-store-connect-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Agent responses with App Store Connect data and action previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sales and finance reports include parsed rows; finance totals are separate summary data.]

## Skill Version(s):

1.3.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
