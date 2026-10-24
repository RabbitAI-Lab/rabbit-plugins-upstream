## Description:

Connects an agent to App Store Connect to inspect apps, TestFlight builds and testers, customer reviews, sales reports, and team users, and to perform authorized management actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and App Store Connect team members use this skill to review app operations, TestFlight activity, customer feedback, sales data, and team access, and to request approved changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: App Store Connect API credentials can expose sensitive account data and permit changes.

Mitigation: Use a least-privileged API key and protect the .p8 private key.

Risk: Inviting users, deleting testers, changing group membership, replying to reviews, and submitting builds can change live account state.

Mitigation: Review the proposed action and its target before confirming each write.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/app-store-connect-mcp)
- [App Store Connect API documentation](https://developer.apple.com/documentation/appstoreconnectapi)
- [App Store Connect API key setup](https://appstoreconnect.apple.com/access/integrations/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Tabular data, Guidance]

**Output Format:** [Natural-language summaries and structured App Store Connect results, including report rows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Management actions require user confirmation.]

## Skill Version(s):

1.3.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
