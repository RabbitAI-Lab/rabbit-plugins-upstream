## Description:

Cargo Connection helps agents manage Cargo CLI connectors and integrations, including authentication, connector discovery, integration catalog browsing, and resolution of connector UUIDs and action slugs for workflow nodes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to discover Cargo integrations, create and audit authenticated connectors, and gather the connector UUIDs and action slugs needed for workflow nodes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connector create, update, and remove commands can change authenticated external-system connections in the active Cargo workspace.

Mitigation: Confirm the active workspace with cargo-ai whoami before write operations and review connector UUIDs, playsCount, and toolsCount before updates or deletion.

Risk: Connector configuration values and API tokens may include secrets.

Mitigation: Treat connector config values and login tokens as secrets, avoid exposing them in prompts or logs, and prefer Cargo-supported OAuth or token handling.

Risk: Using the wrong integration action or autocomplete value can produce invalid workflow node configuration.

Mitigation: Resolve actionSlug values with integration get, inspect jsonSchema and uiSchema, and fetch required autocomplete values before writing workflow configuration.

## Reference(s):

- [Cargo Skills Repository](https://github.com/getcargohq/cargo-skills)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)
- [Connector examples](references/examples/connectors.md)
- [Integration examples](references/examples/integrations.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON on stdout and non-zero failures return JSON with an errorMessage field.]

## Skill Version(s):

1.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
