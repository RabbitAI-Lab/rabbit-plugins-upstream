## Description:

Discovers AI and workload assets in Google Cloud Platform projects, writes a canonical agent-bom inventory, and can scan that inventory when requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud security engineers can inventory Vertex AI, Cloud Run, Cloud Functions, GKE, and related workloads in operator-approved GCP projects. They can then optionally scan the generated inventory for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses local GCP credential sources, and scanner coverage was partial because one referenced local path could not be resolved.

Mitigation: Use only operator-approved projects with read-only credentials. Keep credentials in the operator environment; do not paste or display credential values.

## Reference(s):

- [agent-bom project](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown instructions and JSON inventory, with optional JSON scan findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes inventory JSON to an operator-selected path; scanning is opt-in.]

## Skill Version(s):

0.115.5 (source: skill frontmatter, server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
