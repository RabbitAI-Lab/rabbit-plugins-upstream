## Description:

Lets an agent discover and call paid APIs through the user's taskfuel.ai account, charging each call to a prepaid balance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taskfuel.ai](https://clawhub.ai/user/taskfuel.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can find and purchase search, market data, enrichment, and other API capabilities through a connected taskfuel.ai account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill suggests piping a remote installer directly into a shell.

Mitigation: Review the installer and use a safer verified installation method before connecting an account.

Risk: The agent can spend prepaid funds on small API calls without asking each time.

Mitigation: Set an explicit task budget and require confirmation before the first paid call in each session.

Risk: Paid requests can disclose task data to external API providers.

Mitigation: Review request contents and provider suitability before sending sensitive information.

## Reference(s):

- [Taskfuel skill on ClawHub](https://clawhub.ai/taskfuel.ai/skills/taskfuel)
- [Taskfuel publisher on ClawHub](https://clawhub.ai/user/taskfuel.ai)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text and Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API results vary by provider and endpoint; paid calls draw from the user's prepaid balance.]

## Skill Version(s):

0.5.1 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
