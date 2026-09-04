## Description:

Provides App Store Connect MCP tools for managing apps, TestFlight builds and testers, customer reviews, sales and finance reports, team users, and connector health checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and App Store operations teams use this skill to inspect and manage App Store Connect resources, including apps, TestFlight workflows, customer reviews, sales reports, team users, and credential health checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact App Store Connect account and release actions without documented confirmation safeguards.

Mitigation: Use a least-privilege App Store Connect API key and require explicit user confirmation before invitations, deletions, build submissions, beta group changes, or public review responses.

## Reference(s):

- [App Store Connect API Documentation](https://developer.apple.com/documentation/appstoreconnectapi)
- [App Store Connect API Key Setup](https://appstoreconnect.apple.com/access/integrations/api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text guidance for MCP tool usage, setup, and App Store Connect operations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide MCP actions that read account data or perform write operations in App Store Connect.]

## Skill Version(s):

0.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
