## Description:

Query OneHome (CoreLogic) from a shell with @fetchproxy/cli to resolve consumer scope, search shared listings, and read listing details through authenticated GraphQL and REST calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access authorized OneHome real-estate share data from scripts or shell sessions when the MCP server is not installed or desired.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles private OneHome magic-link tokens, bearer authorization headers, session tokens, terminal output, and temporary JSON files that could expose account access if mishandled.

Mitigation: Use the skill only on trusted machines, treat tokens and generated files like passwords, remove temporary files after use, and disable the capture profile when finished.

Risk: The workflow relies on an authorized OneHome share and on trusting the fpx CLI and browser extension with the active session.

Mitigation: Install and run the skill only when authorized to access the OneHome share and when the fpx CLI and browser extension are trusted for that session.

## Reference(s):

- [OneHome GraphQL + REST operations for fpx](references/graphql-operations.md)
- [OneHome fpx Skill Page](https://clawhub.ai/chrischall/skills/onehome-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, JSON examples, GraphQL queries, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes setup steps, token handling guidance, GraphQL and REST request examples, and troubleshooting notes.]

## Skill Version(s):

0.13.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
