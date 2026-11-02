## Description:

Discover GCP-hosted AI agent and MCP-relevant assets, emit canonical agent-bom inventory JSON, and scan it without giving agent-bom long-lived GCP credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and cloud engineers use this skill to inventory operator-approved GCP projects for Vertex AI, Cloud Run, Cloud Functions, GKE, and related agent infrastructure, then save a canonical inventory for optional scanning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GCP discovery accesses project and resource data using the operator's credentials.

Mitigation: Use read-only credentials scoped to approved projects, and never paste or display credential secrets.

Risk: Credential handling and redaction in the discovery adapter and its dependencies could not be verified because the adapter is not bundled.

Mitigation: Obtain and review the adapter and its dependencies before running the skill.

Risk: The generated inventory may contain sensitive infrastructure details.

Mitigation: Inspect the inventory before sharing it.

## Reference(s):

- [agent-bom project repository](https://github.com/koda-ai-studio/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions]

**Output Format:** [Canonical JSON inventory file with shell-command and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes inventory to an operator-selected path; optional scanning is user-directed.]

## Skill Version(s):

0.112.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
