## Description:

Danube helps agents discover and run organizational and catalog tools through MCP or REST using a Danube API key, with user confirmation before consequential actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Danube to find, inspect, and invoke tools available to their organization, including connected services, workflows, and account-management capabilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Danube API key can grant broad access to connected tools, credentials, wallets, workflows, and skills.

Mitigation: Limit key permissions where possible, keep the key secret, and grant access only to services needed for the task.

Risk: An action that writes, sends, spends, or deletes may not trigger a platform confirmation prompt.

Mitigation: Independently review the exact tool and inputs and obtain the user's explicit approval before consequential actions.

Risk: The skill directs agents to save reusable service parameter defaults after a successful call without asking first.

Mitigation: Review proposed persistent defaults with the user before saving them; never store secrets as defaults.

## Reference(s):

- [ClawHub Danube release](https://clawhub.ai/preston-thiele/skills/danube)
- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [REST API reference](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline JSON and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool results may include data from connected services; consequential actions require user review.]

## Skill Version(s):

8.1.24 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
