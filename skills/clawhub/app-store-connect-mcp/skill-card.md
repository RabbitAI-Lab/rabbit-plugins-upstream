## Description:

This skill helps an agent work with App Store Connect apps, builds, TestFlight testers, customer reviews, sales and finance reports, team users, and credential health checks through the App Store Connect API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and app operations teams use this skill to inspect and manage App Store Connect resources, including apps, builds, TestFlight testers, reviews, reports, and team users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent using this skill can access App Store Connect through Apple API credentials.

Mitigation: Install it only for workflows that require App Store Connect access and use a least-privilege Apple API key.

Risk: Write-capable workflows can invite users or testers, delete testers, submit builds, or post review responses.

Mitigation: Confirm important write actions before allowing the agent to execute them.

## Reference(s):

- [App Store Connect API Documentation](https://developer.apple.com/documentation/appstoreconnectapi)
- [App Store Connect API Key Setup](https://appstoreconnect.apple.com/access/integrations/api)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown and structured tool-call results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include App Store Connect data summaries, setup guidance, and proposed write actions for user confirmation.]

## Skill Version(s):

0.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
