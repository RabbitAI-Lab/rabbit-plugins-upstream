## Description:

Discovers GCP-hosted AI agent and workload assets using operator-controlled read-only credentials and produces sanitized agent-bom inventory JSON for optional scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inventory Vertex AI, Cloud Run, Cloud Functions, GKE, and related agent infrastructure in approved GCP projects, then optionally scan the resulting inventory for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Discovery accesses local GCP credentials and inventories cloud resources.

Mitigation: Use only approved projects and scoped, least-privilege read-only credentials; never paste or print credentials.

Risk: Generated inventory may reveal sensitive cloud configuration when shared.

Mitigation: Review the sanitized inventory JSON before sharing or scanning it, and write it only to an operator-selected path.

Risk: The example discovery command relies on an external agent-bom installation and project source.

Mitigation: Verify the referenced agent-bom dependency and source before running the example command.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-discover-gcp)
- [agent-bom project homepage (listed in skill metadata; import provenance unavailable)](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON inventory, JSON findings]

**Output Format:** [Markdown instructions and schema-validated JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes sanitized inventory to an operator-selected path; produces JSON scan findings only when requested.]

## Skill Version(s):

0.108.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
