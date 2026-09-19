## Description:

Agent BOM Compliance generates CycloneDX 1.5 SBOMs and JSON compliance findings for agent projects using an offline Python rule engine for secrets, dependency pinning, egress drift, model provenance, license presence, and audit trails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to inspect agent project trees before release or CI promotion, producing SBOM, scan, report, trend, and audit JSON outputs that support remediation decisions. It provides a verifiable compliance signal, not a certification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanning an untrusted repository can follow symlinked files outside the selected directory and include local file-derived data in outputs.

Mitigation: Run the skill in a sandboxed or least-privilege account and avoid scanning repositories you do not trust until symlink handling is fixed.

Risk: The audit ledger is local and configurable through AGENT_BOM_AUDIT.

Mitigation: Point AGENT_BOM_AUDIT only to a path you control, keep ledger permissions restricted, and anchor head hashes in CI artifacts when stronger tamper evidence is needed.

Risk: The skill provides a compliance signal but does not certify SOC 2, ISO 27001, CMMC, or similar programs.

Mitigation: Use the JSON findings, SBOM, and audit trail as review inputs alongside accredited audits and organizational controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/agent-bom-compliance)
- [Operations guide](artifact/docs/operations.md)
- [Integration guide](artifact/docs/integration.md)
- [Standards evidence](artifact/docs/evidence.md)
- [Manifest](artifact/manifest.json)
- [Changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON outputs with Markdown and shell-command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent_bom.*.v1 JSON contracts, CycloneDX 1.5 SBOM JSON, report sidecar files, and hash-chained audit JSONL entries.]

## Skill Version(s):

2.0.1 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
