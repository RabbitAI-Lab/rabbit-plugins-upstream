## Description:

Discovers GCP-hosted AI agent and MCP-relevant assets and produces canonical agent-bom inventory JSON for optional scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators inventory AI and workload assets in approved GCP projects, then optionally request agent-bom findings from the saved inventory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Existing GCP authentication can access resources beyond the intended inventory scope.

Mitigation: Use read-only credentials limited to operator-approved projects.

Risk: Inventory may be written to an unintended location or shared without review.

Mitigation: Verify the operator-selected output path and review inventory before sharing it.

Risk: The workflow depends on separately installed agent-bom tooling.

Mitigation: Review the agent-bom package or source before installing or running it.

## Reference(s):

- [agent-bom project homepage (skill metadata)](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON inventory, JSON findings on request]

**Output Format:** [Markdown guidance and shell commands; canonical JSON inventory and optional JSON findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is schema-validated and credential material is redacted; scanning requires an explicit request.]

## Skill Version(s):

0.108.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
