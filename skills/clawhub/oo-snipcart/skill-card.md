## Description:

Snipcart (snipcart.com). Use this skill for Snipcart requests such as reading, creating, and updating data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Snipcart connector schemas and run customer or order actions through an OOMOL-connected account. It supports listing and retrieving Snipcart records and includes confirmation guidance for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow documents remote installer commands that execute downloaded scripts.

Mitigation: Use a verified official package when available, or download, inspect, and verify the installer before execution.

Risk: The skill can operate on live Snipcart data through a broadly framed connector.

Mitigation: Inspect the live action schema and confirm the exact action and payload before any create, update, or destructive operation.

Risk: The get_order action is tagged as write even though its description says it retrieves an order.

Mitigation: Treat the action as potentially state-changing until the connector schema and behavior are confirmed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-snipcart)
- [Snipcart Homepage](https://snipcart.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, OOMOL authentication, and a connected Snipcart account.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
