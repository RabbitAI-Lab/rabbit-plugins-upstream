## Description:

Discovers AWS-hosted AI agent and related workload assets and writes canonical agent-bom inventory JSON for optional local scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud security teams use this skill to inventory AWS agent and workload assets with operator-approved read-only credentials, then optionally scan or export the inventory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inventory discovery exposes AWS resource details to the agent and the chosen local output file.

Mitigation: Use an operator-approved read-only role or short-lived profile and choose and protect the inventory output path.

Risk: Optional scans or exports may send inventory to a destination beyond the initial discovery workflow.

Mitigation: Review and explicitly approve any scan or export destination before running it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-aws)
- [agent-bom project homepage (listed in skill metadata; source provenance unavailable)](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions and shell commands; canonical inventory JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes inventory to an operator-selected path; local scanning and export require explicit approval.]

## Skill Version(s):

0.109.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
