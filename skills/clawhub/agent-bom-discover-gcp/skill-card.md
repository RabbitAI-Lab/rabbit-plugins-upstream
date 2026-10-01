## Description:

Guides discovery of GCP-hosted AI and workload assets into agent-bom inventory JSON, with optional local scanning for findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inventory AI agents and related services in approved GCP projects, then optionally scan the resulting inventory for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inventory may expose sensitive cloud metadata even after credential values are redacted.

Mitigation: Confirm the project, region, credential scope, and output path; use only approved projects and existing read-only credentials, and control access to the inventory file.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-gcp)
- [agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery writes inventory JSON to an operator-selected path; an optional scan writes findings JSON.]

## Skill Version(s):

0.107.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
