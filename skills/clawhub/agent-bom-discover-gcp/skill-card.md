## Description:

Discovers GCP-hosted AI agent and MCP-relevant assets in approved projects and produces canonical agent-bom inventory JSON for optional scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inventory AI agents and related workloads in approved GCP projects, then optionally scan the inventory with agent-bom.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Existing GCP authentication can expose inventory from unintended projects.

Mitigation: Use scoped read-only credentials and confirm the approved project before discovery.

Risk: Generated inventory may contain sensitive resource details if shared.

Mitigation: Confirm the output path and review the sanitized inventory before sharing it outside the environment.

## Reference(s):

- [agent-bom project](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Canonical JSON inventory file and Markdown guidance; optional JSON scan findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inventory is schema-validated and sanitizes credential-like values; scanning requires operator approval.]

## Skill Version(s):

0.106.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
