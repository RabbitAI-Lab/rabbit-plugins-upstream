## Description:

Manage connectors and integrations using the Cargo CLI. Use when the user wants to list, create, update, or remove connectors, discover available integrations, or understand what connector actions are available for use in workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Cargo connector instances, discover available integrations and actions, and prepare connector configuration for workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connector changes can affect active plays, tools, or models that depend on a connector.

Mitigation: Before removing or updating a connector, verify the connector UUID and review usage counts such as playsCount, toolsCount, and modelsCount.

Risk: Credential-based connector setup can expose live API keys through shell history, logs, or process listings.

Mitigation: Use safer authentication flows where available and avoid pasting live API keys directly into command lines.

Risk: Using the wrong integration or action slug can produce incorrect workflow configuration.

Mitigation: Run the Cargo CLI discovery commands for integrations, actions, schemas, and autocomplete values before preparing connector or workflow configuration.

## Reference(s):

- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [Connector examples](references/examples/connectors.md)
- [Integration examples](references/examples/integrations.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Cargo CLI command examples and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON response shapes, connector identifiers, integration slugs, action slugs, and configuration guidance.]

## Skill Version(s):

1.2.1 (source: frontmatter, skill-metadata.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
