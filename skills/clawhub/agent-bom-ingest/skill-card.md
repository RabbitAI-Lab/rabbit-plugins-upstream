## Description:

Validates and ingests operator-pushed agent-bom inventory JSON from AWS, Azure, GCP, Snowflake, CMDB, or endpoint collectors for local findings, graph, policy, provenance, and auditor-ready exports without direct cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and engineers use this skill when they already have canonical inventory JSON and need to validate, scan, graph, or export local agent-bom findings without granting direct cloud credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inventory files can contain sensitive infrastructure details.

Mitigation: Review inventory content before scanning and rely on schema validation plus redaction before display or export.

Risk: Optional push behavior can send results to an operator-provided control plane.

Mitigation: Set AGENT_BOM_PUSH_URL and AGENT_BOM_API_KEY only for an operator-owned destination and never expose token values in chat or output.

Risk: Malformed or incomplete inventory can misrepresent provenance, permissions, or credential posture.

Mitigation: Stop and ask the operator to regenerate canonical inventory when required trust fields are missing instead of scanning a best-effort summary.

## Reference(s):

- [agent-bom repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI project](https://pypi.org/project/agent-bom/)
- [OSV vulnerability API](https://api.osv.dev/v1)
- [GitHub Advisory API](https://api.github.com/advisories)
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-ingest)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide JSON, SARIF, HTML, Markdown, CycloneDX, or SPDX exports through the agent-bom CLI.]

## Skill Version(s):

0.103.2 (source: artifact/SKILL.md frontmatter and evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
