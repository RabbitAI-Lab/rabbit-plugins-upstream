## Description:

Helps agents inspect App Store Connect apps, builds, reviews, sales reports, and team users, and request confirmed account changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and App Store Connect team members use this skill to review apps, TestFlight activity, customer feedback, sales and finance reports, and team access, and to approve account changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An overprivileged API key can expose business and account data or authorize unintended changes.

Mitigation: Use the least-privileged App Store Connect API key needed for the task and review confirmation previews before approving writes.

Risk: Disclosure of the App Store Connect private key could compromise account access.

Mitigation: Keep the .p8 private key local and do not share it with other users or services.

## Reference(s):

- [App Store Connect API documentation](https://developer.apple.com/documentation/appstoreconnectapi)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/app-store-connect-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration guidance]

**Output Format:** [Text and structured App Store Connect results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sales and finance reports are returned as parsed rows; write actions require user confirmation.]

## Skill Version(s):

1.2.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
