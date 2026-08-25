## Description:

Discover GCP-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived GCP credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud security operators use this skill to inventory Vertex AI, Cloud Run, Cloud Functions, GKE, and related agentic GCP infrastructure as canonical agent-bom inventory. It supports discover-only workflows and optional local scans when the operator asks for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the operator's local GCP authentication context to inventory cloud resources.

Mitigation: Use read-only, narrowly scoped, short-lived, ADC, workload-identity, or scoped service account credentials, and do not paste service account JSON or credential values into chat.

Risk: Generated inventory can describe sensitive cloud resources.

Mitigation: Write inventory only to an operator-selected path and review handling of the resulting JSON before sharing or exporting it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-gcp)
- [agent-bom source repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, json]

**Output Format:** [Markdown guidance with bash commands and JSON inventory or findings files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default workflow writes schema-valid inventory to an operator-selected path; scan findings are produced only when requested.]

## Skill Version(s):

0.102.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
