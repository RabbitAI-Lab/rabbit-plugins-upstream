## Description:

Discover GCP-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived GCP credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud platform operators use the skill to inventory approved GCP projects and workloads, including Vertex AI, Cloud Run, Cloud Functions, and GKE, as canonical agent-bom JSON. They can request an optional scan of that inventory for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The partial scan flags local GCP credential-file references and an unresolved adapter path; it does not establish credential exposure or malicious intent.

Mitigation: Review the skill and referenced adapter before installing, use operator-approved read-only credentials, and do not paste credential values into chat.

## Reference(s):

- [Agent BOM project](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands, Guidance]

**Output Format:** [Canonical agent-bom inventory JSON with shell commands and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discovery writes an operator-selected JSON file; scanning is optional and performed only when requested.]

## Skill Version(s):

0.115.4 (source: skill frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
