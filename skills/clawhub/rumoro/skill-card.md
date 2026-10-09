## Description:

Helps agents track social mentions, triage conversations, configure alerts, and review analytics through Rumoro.

This skill is ready for commercial/non-commercial use.

## Publisher:

[markolo10](https://clawhub.ai/user/markolo10)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, support, and research teams use this skill to monitor brands and competitors, find relevant posts, review trends, and manage alerts in their Rumoro workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A write key permits changes to the Rumoro workspace.

Mitigation: Use a read key for search and analytics; grant write access only when changes are needed.

Risk: Alerts can send mention data to external destinations.

Mitigation: Review webhook, email, Slack, and Telegram destinations before sending data.

Risk: Deletes, member removal, key revocation, secret rotation, and merges can disrupt workspace operations.

Mitigation: Confirm these actions with the user before proceeding.

## Reference(s):

- [Rumoro OpenClaw integration guide](https://docs.rumoro.dev/integrations/openclaw)
- [Rumoro API reference](https://api.rumoro.dev/v1/openapi.json)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline commands and structured results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize mentions and analytics or propose changes to workspace settings and alerts.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
