## Description:

Check vulnerabilities in a specified package/version, repository, container image, or SBOM, or inspect a specified CVE.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use the skill to assess vulnerabilities in a named package, repository, container image, or SBOM, look up a specified advisory, and produce scan findings, remediation or compliance guidance, and SBOM outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online vulnerability lookups share package names, versions, and advisory identifiers with providers; image and repository scans contact the specified registry or host.

Mitigation: Confirm authorization before querying private identifiers. Use offline mode when network lookups are not authorized and report the resulting coverage gaps.

Risk: Local configuration or SBOM inputs may contain sensitive information, and benign configuration values may remain in memory during processing.

Mitigation: Read only specifically authorized inputs, do not print or upload configuration contents, and do not use discovered cloud credentials.

Risk: The scanner is an external runtime whose behavior, redaction, and referenced tests were not verified in this review.

Mitigation: Pin the external scanner to a reviewed release and treat the review as covering the instruction bundle only.

## Reference(s):

- [Agent BOM source repository](https://github.com/koda-ai-studio/agent-bom)
- [Agent BOM on PyPI](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)
- [Credential redaction source](https://github.com/koda-ai-studio/agent-bom/blob/main/src/agent_bom/security.py)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, JSON, Markdown, Files]

**Output Format:** [Text findings and guidance, JSON or SARIF scan results, Markdown or HTML reports, and CycloneDX or SPDX SBOM files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output depends on the specified target and requested format; offline scans may have reduced advisory coverage.]

## Skill Version(s):

0.112.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
