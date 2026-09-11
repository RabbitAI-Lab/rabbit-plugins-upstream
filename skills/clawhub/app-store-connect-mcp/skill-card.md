## Description:

Enables an agent to connect to App Store Connect for apps, builds, TestFlight testers, customer reviews, sales and finance reports, team users, and credential health checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and app teams use this skill to let an agent inspect and manage App Store Connect resources, including TestFlight workflows, reviews, reports, and team users. It is intended for users who can supply appropriate App Store Connect API credentials and review write actions before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use App Store Connect credentials for sensitive account, tester, review, and financial workflows.

Mitigation: Use the least-privileged API key that supports the intended workflows and keep the private key only in the MCP host configuration.

Risk: Write-capable workflows can invite users, delete testers, submit builds, or respond to reviews.

Mitigation: Require explicit user confirmation before executing App Store Connect write actions.

## Reference(s):

- [App Store Connect API Documentation](https://developer.apple.com/documentation/appstoreconnectapi)
- [App Store Connect API Key Setup](https://appstoreconnect.apple.com/access/integrations/api)
- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/app-store-connect-mcp)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration instructions]

**Output Format:** [Markdown with tool names, workflow steps, and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce App Store Connect data summaries and parsed sales or finance report rows through MCP tool use.]

## Skill Version(s):

0.4.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
