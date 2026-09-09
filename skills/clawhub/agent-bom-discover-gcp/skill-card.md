## Description:

Discover GCP-hosted AI agent and MCP-relevant assets from the operator's environment, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived GCP credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud security engineers use this skill to discover Vertex AI, Cloud Run, Cloud Functions, GKE, and related GCP assets as canonical agent-bom inventory, then optionally scan that inventory for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may use local GCP authentication context, including Application Default Credentials or configured credential files, for read-only inventory discovery.

Mitigation: Use narrowly scoped read-only ADC, workload identity, or short-lived service account credentials, and do not paste service account keys or token values into chat.

Risk: Generated inventory JSON can contain cloud resource details that may be sensitive outside the operator's environment.

Mitigation: Write inventory only to an operator-selected path and review the JSON before sharing, scanning, or exporting it.

Risk: Running discovery against broad projects can expose more resource metadata than intended.

Mitigation: Limit use to operator-approved GCP projects and credentials with the minimum read-only permissions needed for the inventory task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-discover-gcp)
- [agent-bom repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)
- [Cloud Resource Manager API endpoint](https://cloudresourcemanager.googleapis.com)
- [Vertex AI API endpoint](https://aiplatform.googleapis.com)
- [Cloud Run API endpoint](https://run.googleapis.com)
- [Cloud Functions API endpoint](https://cloudfunctions.googleapis.com)
- [Google Kubernetes Engine API endpoint](https://container.googleapis.com)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with bash commands; generated artifacts are JSON inventory and findings files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default workflow is discover-only and writes inventory to an operator-selected path.]

## Skill Version(s):

0.103.2 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
