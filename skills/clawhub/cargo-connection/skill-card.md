## Description:

Cargo Connection helps agents manage Cargo connector authentication, discover integrations and actions, and resolve connector UUIDs and action slugs for workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Cargo users and workflow builders use this skill to connect external systems to Cargo, inspect available integrations and actions, and retrieve connector and action identifiers needed in Cargo workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connector commands can handle sensitive credentials or change authenticated external-service connections.

Mitigation: Install only if you use Cargo and trust the @cargo-ai/cli package; avoid putting secrets directly in shell commands when possible and confirm the active workspace with cargo-ai whoami before write operations.

Risk: Removing or changing a connector can disrupt Cargo plays, tools, or workflows that depend on it.

Mitigation: Check dependent plays, tools, and connector usage counts before removing a connector or changing its configuration.

Risk: Incorrect connector UUIDs, action slugs, or autocomplete values can cause workflow failures or empty action results.

Mitigation: Resolve actions and connector identifiers with the Cargo CLI discovery commands, and use connector autocomplete for fields that require dynamic values.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cargo-ai/skills/cargo-connection)
- [Cargo Skills Homepage](https://github.com/getcargohq/cargo-skills)
- [Connector Examples](references/examples/connectors.md)
- [Integration Examples](references/examples/integrations.md)
- [Response Shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Cargo CLI and an authenticated Cargo workspace for command execution.]

## Skill Version(s):

1.4.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
