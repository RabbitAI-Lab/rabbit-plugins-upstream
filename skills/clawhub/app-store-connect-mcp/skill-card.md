## Description:

Provides App Store Connect MCP tools for agents to inspect apps, builds, TestFlight testers, customer reviews, sales and finance reports, team users, and credential health.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, release managers, and support teams use this skill to let an agent work with App Store Connect data, TestFlight workflows, customer reviews, reports, team users, and credential checks through the App Store Connect API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access App Store Connect through a user-provided API key and private key.

Mitigation: Install only when this access is intended, protect the .p8 or PEM value, and use the least-privileged App Store Connect role that supports the intended workflows.

Risk: Write-capable tools can change beta testers, team users, review responses, or beta-review submissions.

Mitigation: Confirm user intent and review inputs before invoking write actions such as deleting testers, inviting users, responding to reviews, or submitting builds for beta review.

## Reference(s):

- [App Store Connect API](https://developer.apple.com/documentation/appstoreconnectapi)
- [App Store Connect API Key Management](https://appstoreconnect.apple.com/access/integrations/api)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [Markdown guidance and structured App Store Connect tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include App Store Connect records and report rows; report output may be limited by the skill's row limit.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
