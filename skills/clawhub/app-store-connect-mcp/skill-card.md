## Description:

App Store Connect MCP helps agents work with App Store Connect data, including apps, builds, TestFlight testers, customer reviews, sales and finance reports, team users, and credential health checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, release managers, and App Store operations teams use this skill to let an agent inspect and manage App Store Connect apps, TestFlight workflows, customer reviews, sales reports, finance reports, team users, and connector health.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose high-impact App Store Connect account and public-response actions, including inviting users, deleting testers, changing beta groups, replying to reviews, and submitting builds.

Mitigation: Use the least-privileged Apple API key possible and require explicit human review before any account, TestFlight, review-response, or build-submission action.

Risk: The skill depends on App Store Connect API credentials, including a private key path or PEM value.

Mitigation: Keep the private key local, avoid sharing it in prompts or logs, and rotate or revoke the key if credential exposure is suspected.

## Reference(s):

- [App Store Connect API Documentation](https://developer.apple.com/documentation/appstoreconnectapi)
- [App Store Connect API Key Management](https://appstoreconnect.apple.com/access/integrations/api)
- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/app-store-connect-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown or plain text guidance with App Store Connect tool results and configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize App Store Connect API data and propose account, TestFlight, review-response, sales, finance, or team-user actions depending on granted credentials.]

## Skill Version(s):

1.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
