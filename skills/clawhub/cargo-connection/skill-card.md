## Description:

Cargo Connection helps agents authenticate Cargo connectors, inspect integration capabilities, and resolve connector UUIDs and action slugs for workflow nodes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Cargo connector setup, audit authenticated connector usage, discover supported integrations and actions, and prepare connector configuration for Cargo workflow nodes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or uses @cargo-ai/cli@latest, which may change behavior across releases.

Mitigation: Pin the Cargo CLI version for production or shared agent environments.

Risk: Connector commands can involve API tokens, connector credentials, and sensitive connector configuration.

Mitigation: Avoid pasting real tokens or API keys into command lines or chat, keep connector JSON out of public logs, and rotate any exposed credentials.

Risk: Connector list and get responses may expose workspace configuration for non-credit connectors.

Mitigation: Treat connector JSON as sensitive operational data and limit transcript sharing to the minimum fields needed.

Risk: The security verdict recommends review before production use.

Mitigation: Review the skill before installing it in production or shared agent environments.

## Reference(s):

- [Cargo Connection on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-connection)
- [Cargo Skills Repository](https://github.com/getcargohq/cargo-skills)
- [Connector Examples](references/examples/connectors.md)
- [Integration Examples](references/examples/integrations.md)
- [Response Shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON and may include connector configuration; review outputs before sharing logs or transcripts.]

## Skill Version(s):

1.5.0 (source: frontmatter, skill-metadata.json, server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
