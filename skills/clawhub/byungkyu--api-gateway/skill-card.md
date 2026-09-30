## Description:

Helps agents use Maton to call APIs for connected third-party apps and manage approved event automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users with a Maton account can ask an agent to read from or act on connected services, such as mail, CRM, and spreadsheets. With explicit approval, the agent can also configure event triggers and hosted automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to connected apps may expose sensitive data or change records.

Mitigation: Keep OAuth scopes narrow, prefer read-only calls, and confirm each write or send action with the user.

Risk: Webhook destinations and event handlers can forward data or run code on future events.

Mitigation: Require approval for each trigger, destination, and handler; review external URLs and handler code, and delete unused automations.

Risk: API keys and hosted functions can grant persistent access to connected services.

Mitigation: Prefer device login over raw API keys; review function permissions and network access before deployment, and remove unused functions and connections.

## Reference(s):

- [ClawHub API Gateway release](https://clawhub.ai/byungkyu/skills/api-gateway)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with CLI examples and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions on connected services require a Maton account and network access.]

## Skill Version(s):

1.2.24 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
