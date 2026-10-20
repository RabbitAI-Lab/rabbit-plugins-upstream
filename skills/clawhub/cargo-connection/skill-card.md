## Description:

Helps agents connect Cargo to external services, manage authenticated connectors, discover integrations and actions, and find identifiers needed for workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to find supported Cargo integrations, authenticate and manage connectors, and identify connector and action IDs for workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unpinned CLI installation may introduce unreviewed changes.

Mitigation: Pin and vet the @cargo-ai/cli version before installing in a production workspace.

Risk: API tokens entered as command-line arguments may be exposed.

Mitigation: Prefer hosted or OAuth sign-in, or use a safer secret input method.

Risk: Connector updates or removals may affect the wrong workspace or disrupt dependent workflows, tools, and models.

Mitigation: Verify the active workspace and connector identity, then check dependencies before changing or removing a connector.

## Reference(s):

- [Cargo Connection on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-connection)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Connector examples](references/examples/connectors.md)
- [Integration examples](references/examples/integrations.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Text]

**Output Format:** [Markdown with CLI examples and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector and action identifiers can be used in Cargo workflows.]

## Skill Version(s):

1.6.0 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
