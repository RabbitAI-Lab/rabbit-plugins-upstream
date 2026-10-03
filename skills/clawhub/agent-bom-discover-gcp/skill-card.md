## Description:

Discovers GCP-hosted AI agent and MCP-related resources in approved projects and produces canonical agent-bom inventory JSON for optional scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inventory AI and workload assets in approved GCP projects, then optionally scan the resulting inventory for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Existing Google Cloud credentials could expose inventory from an unintended project.

Mitigation: Use least-privilege read-only credentials and verify the approved project before discovery.

Risk: Generated inventory can contain sensitive resource metadata or be written to the wrong location.

Mitigation: Confirm the output path and review the inventory for sensitive metadata before sharing it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-discover-gcp)
- [Project homepage (listed in skill metadata; import provenance unavailable)](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON inventory files, Optional JSON findings]

**Output Format:** [Markdown guidance with shell commands; canonical JSON inventory and optional JSON scan findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery only by default; inventory is saved to an operator-selected path and credentials are redacted.]

## Skill Version(s):

0.107.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
