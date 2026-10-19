## Description:

Compares an Agent's installed Rotifer Genes with Arena rankings and recommends stronger replacements for user approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and Agent operators use /evolve to assess local Rotifer capabilities, compare Arena candidates, and approve or roll back Gene upgrades. They can also create and run local Agents built from Genes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running an Agent can execute an unpinned npm fallback when the Rotifer CLI is absent.

Mitigation: Before using /evolve run-agent, install and review a pinned @rotifer/playground CLI version.

Risk: Upgrading can replace project Genes with unsigned third-party code that changes Agent behavior.

Mitigation: Inspect the publisher, safety results, and source before approving each replacement; use rollback if needed.

## Reference(s):

- [Rotifer documentation](https://rotifer.dev/docs)
- [Rotifer protocol specification](https://github.com/rotifer-protocol/rotifer-spec)
- [Rotifer MCP server source](https://github.com/rotifer-protocol/rotifer-mcp-server)
- [Rotifer playground repository](https://github.com/rotifer-protocol/rotifer-playground)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files]

**Output Format:** [Markdown recommendations and local Gene or Agent files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Gene replacements require user approval; running an Agent executes Gene code.]

## Skill Version(s):

2.4.9 (source: ClawHub release metadata; artifact metadata lists 2.4.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
