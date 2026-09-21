## Description:

Guides agents that work with App Store Connect data across apps, builds, TestFlight testers, customer reviews, sales and finance reports, team users, and credential health checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and App Store operations teams use this skill to inspect App Store Connect resources, manage TestFlight testers and builds, respond to customer reviews, retrieve reports, and troubleshoot API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose live account-changing actions when configured with App Store Connect API credentials that have broad permissions.

Mitigation: Use the least-privileged App Store Connect API key available and review the requested action before granting write-capable access.

Risk: Actions such as deleting testers, inviting users, submitting builds, or posting public review responses can affect users or public-facing App Store content.

Mitigation: Require explicit confirmation before executing account-changing or public-facing actions.

Risk: Private key material is required for the MCP connection and could be mishandled if copied into unsafe locations.

Mitigation: Keep the private key local, prefer a file path or protected secret store, and avoid exposing the key in logs or shared prompts.

## Reference(s):

- [App Store Connect API](https://developer.apple.com/documentation/appstoreconnectapi)
- [App Store Connect API Key Management](https://appstoreconnect.apple.com/access/integrations/api)

## Skill Output:

**Output Type(s):** [Text, API Calls, Configuration, Guidance]

**Output Format:** [Markdown or structured text describing App Store Connect data, tool calls, report rows, and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference live App Store Connect account data and account-changing actions when the MCP server is configured with sufficient credentials.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
