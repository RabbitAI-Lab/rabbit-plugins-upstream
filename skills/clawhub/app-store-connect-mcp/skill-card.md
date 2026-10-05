## Description:

Helps agents manage App Store Connect apps, TestFlight testers and builds, customer reviews, sales reports, and team users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and app managers use this skill to inspect their App Store Connect accounts, manage TestFlight participation, respond to customer reviews, retrieve sales and finance reports, and administer team access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An overprivileged or exposed Apple API key could grant access to sensitive App Store Connect data and actions.

Mitigation: Use the least-privileged key that supports the task and keep the .p8 private key protected.

Risk: Invitations, tester removals, review responses, beta review submissions, and team-user changes can affect live accounts.

Mitigation: Review each confirmation preview carefully and approve only the intended change.

## Reference(s):

- [App Store Connect API documentation](https://developer.apple.com/documentation/appstoreconnectapi)
- [App Store Connect API key setup](https://appstoreconnect.apple.com/access/integrations/api)

## Skill Output:

**Output Type(s):** [Text, Guidance, Structured data]

**Output Format:** [Markdown and structured App Store Connect results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sales and finance reports are returned as parsed rows; write actions require user confirmation.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
