## Description:

Validate and ingest operator-pushed agent-bom inventory JSON from AWS, Azure, GCP, Snowflake, CMDB, or endpoint collectors for local findings, graph, policy, provenance, or auditor-ready exports without giving agent-bom direct cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, security engineers, platform engineers, and auditors use this skill to validate canonical inventory JSON, run local agent-bom scans, and produce findings or exports for review and automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on a locally installed agent-bom CLI.

Mitigation: Confirm the CLI source and version are trusted before installing or running it.

Risk: Inventory files can contain sensitive operational details.

Mitigation: Review inventory content before scanning or exporting and rely on the skill's redaction guidance before display or sharing.

Risk: Optional push and advisory lookups can send data to operator-provided or public endpoints.

Mitigation: Enable network push or enrichment only when the destination, authentication method, and data sharing are acceptable for the environment.

Risk: API tokens or URL credentials could be exposed if handled carelessly.

Mitigation: Use environment variables for optional credentials and do not print raw tokens, URL credentials, private keys, or environment variable values.

## Reference(s):

- [agent-bom GitHub repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)
- [OSV API](https://api.osv.dev/v1)
- [GitHub Advisory API](https://api.github.com/advisories)
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-ingest)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and export-format recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers local validation, local scanning, optional push behavior, and JSON, SARIF, HTML, Markdown, CycloneDX, or SPDX export choices.]

## Skill Version(s):

0.102.0 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
