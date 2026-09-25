## Description:

Provides an MCP connector for App Store Connect covering apps, TestFlight, customer reviews, sales and finance reports, team users, and credential health checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and app operations teams use this skill to inspect and manage App Store Connect data, including apps, TestFlight testers and builds, customer reviews, sales reports, and team users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access App Store Connect data through the user's API key.

Mitigation: Install only for workflows that require App Store Connect access, use the least-privileged Apple API role that supports the workflow, and protect the .p8 private key.

Risk: Approved write operations can change testers, review responses, beta review submissions, or team invitations.

Mitigation: Review confirmation previews carefully before approving any write operation; the skill documents confirmation-required responses and single-use confirmation tokens.

## Reference(s):

- [App Store Connect API Documentation](https://developer.apple.com/documentation/appstoreconnectapi)
- [App Store Connect API Key Setup](https://appstoreconnect.apple.com/access/integrations/api)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/app-store-connect-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown and structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write operations require explicit confirmation before execution.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
