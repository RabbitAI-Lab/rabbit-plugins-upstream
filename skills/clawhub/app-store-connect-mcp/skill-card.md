## Description:

Provides MCP tools for agents to inspect and manage App Store Connect apps, TestFlight builds and testers, customer reviews, sales and finance reports, and team users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and App Store operators use this skill to let agents retrieve App Store Connect data and perform TestFlight, review-response, reporting, and team-user workflows through the App Store Connect API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform account-changing or public-facing App Store Connect actions such as invitations, tester deletion, build submission, and review responses.

Mitigation: Require explicit human confirmation before executing invitations, deletions, build submissions, or review responses.

Risk: The skill requires App Store Connect API credentials and a private .p8 key or PEM value.

Mitigation: Use a least-privileged API key, store the private key securely, and avoid exposing the key in prompts, logs, or shared configuration.

Risk: The skill is intended for real App Store Connect accounts and may affect production app operations.

Mitigation: Install it only for accounts the user intends agents to manage and review requested changes before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/app-store-connect-mcp)
- [App Store Connect API documentation](https://developer.apple.com/documentation/appstoreconnectapi)
- [App Store Connect API key setup](https://appstoreconnect.apple.com/access/integrations/api)

## Skill Output:

**Output Type(s):** [text, API calls, configuration, guidance]

**Output Format:** [Markdown guidance with MCP tool-call instructions and structured App Store Connect API or report results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sales and finance reports may be returned as parsed row objects and truncated by the configured row limit.]

## Skill Version(s):

0.2.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
