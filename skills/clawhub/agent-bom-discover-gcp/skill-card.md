## Description:

Discover GCP-hosted AI and workload assets and create canonical agent-bom inventory for optional scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and cloud security teams use this skill to inventory operator-approved GCP projects for Vertex AI, Cloud Run, Cloud Functions, GKE, and related workloads. It writes canonical JSON locally for review and optional scanning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GCP discovery reads operator credential configuration and queries approved projects, so overly broad credentials or project selection can expose more infrastructure inventory than intended.

Mitigation: Use read-only credentials scoped to operator-approved projects and do not share credential values in chat.

Risk: The generated inventory may contain sensitive infrastructure details if it is stored or shared carelessly.

Mitigation: Write only to an operator-selected path, protect the inventory, and review redaction before sharing or uploading it.

## Reference(s):

- [agent-bom project repository](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-gcp)

## Skill Output:

**Output Type(s):** [Files, JSON, Guidance]

**Output Format:** [Canonical JSON inventory file with concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes to an operator-selected path; scanning is optional and requires an explicit request.]

## Skill Version(s):

0.111.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
