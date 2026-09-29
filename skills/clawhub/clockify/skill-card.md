## Description:

Helps agents track time and manage Clockify projects, clients, tasks, and workspaces through a Maton-managed connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and teams use this skill to inspect time entries and manage projects, clients, tasks, and workspaces in a connected Clockify account. With explicit approval, they can also set up hosted functions and triggers for ongoing automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes or deletions may affect the wrong Clockify account or resource.

Mitigation: Confirm the connected account, target resource, and intended effect with the user before each write or deletion.

Risk: Functions, triggers, and destinations may continue acting or forwarding event data after setup.

Mitigation: Obtain explicit approval for each automation and third-party destination, including what data is sent and how often; remove it when no longer needed.

Risk: A long-lived API key can be exposed when used outside the OAuth-backed CLI.

Mitigation: Prefer OAuth through the CLI and keep any API key out of logs, commands, and persisted files.

## Reference(s):

- [Clockify skill release](https://clawhub.ai/byungkyu/skills/clockify)
- [Maton homepage](https://maton.ai)
- [Clockify API documentation](https://docs.clockify.me/)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include requested Clockify records or instructions for approved changes and automation.]

## Skill Version(s):

1.2.4 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
