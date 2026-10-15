## Description:

Helps operators discover GCP-hosted AI agents and related workloads, produce agent-bom inventory JSON, and optionally scan that inventory for findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inventory AI-related resources in approved GCP projects and optionally scan the resulting inventory for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Discovery uses local GCP credentials to read inventory from selected projects.

Mitigation: Use scoped, read-only credentials and confirm approved projects before running discovery; never paste credentials into chat.

Risk: Generated inventory may contain sensitive details about cloud resources.

Mitigation: Choose and review the output path, and inspect inventory before sharing it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-gcp)
- [agent-bom project (skill metadata; not verified release provenance)](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON files]

**Output Format:** [Markdown guidance and shell commands; canonical inventory JSON and optional scan findings JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery writes to an operator-selected path; scanning is optional and requires operator approval.]

## Skill Version(s):

0.108.4 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
