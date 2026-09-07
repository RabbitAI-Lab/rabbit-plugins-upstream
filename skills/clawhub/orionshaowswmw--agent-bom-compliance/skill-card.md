## Description:

Offline SBOM and verifiable compliance scanner for agent projects that generates CycloneDX 1.5 JSON SBOMs, audits project trees with a curated rules engine, emits explicit control references, records a hash-chained audit trail, and trends findings across runs without network or telemetry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to generate SBOMs, scan agent project trees for offline supply-chain and compliance signals, and produce JSON evidence for CI gates or review workflows. It is a verifiable-compliance signal, not a certification for SOC 2, ISO 27001, CMMC, or other audited frameworks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project symlink files may cause traversal to read files outside the selected target directory.

Mitigation: Run the skill only on trusted project directories, avoid privileged execution, or update traversal to skip symlink files and verify resolved paths remain under the target root before opening.

Risk: Audit-chain records are keyless and can be truncated or extended by an attacker with local write access.

Mitigation: Anchor the latest audit hash outside the local ledger, such as in CI artifacts or another protected record, after each gating run.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/agent-bom-compliance)
- [Operations Guide](docs/operations.md)
- [Standards Evidence](docs/evidence.md)
- [Integration Guide](docs/integration.md)
- [Manifest](manifest.json)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Configuration, Guidance]

**Output Format:** [JSON command output and generated JSON files, with Markdown documentation for operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stdlib-only Python commands produce schema-tagged JSON for doctor, sbom, scan, report, trend, and audit workflows.]

## Skill Version(s):

2.0.1 (source: frontmatter, changelog, manifest, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
