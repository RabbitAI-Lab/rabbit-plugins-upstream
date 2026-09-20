## Description:

agent-bom-scan builds a dependency bill of materials, checks supported lockfiles against a curated OSV-verified advisory database, and emits provenance-stamped vulnerability findings for authorized projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to audit authorized project dependencies for known vulnerabilities, generate BOMs, and produce machine-readable findings for supply-chain review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install instructions rely on an unpinned ClawHub installer, which creates supply-chain review risk.

Mitigation: Install in a restricted, non-privileged environment and prefer a pinned, verified ClawHub installer when available.

Risk: Online scan failures can make vulnerability coverage incomplete while leaving only offline findings available.

Mitigation: Treat online errors as incomplete results, review the failure, and rerun or investigate before using the scan as clearance.

Risk: Generated reports and feedback logs can disclose dependency details.

Mitigation: Protect `bom.json`, `findings.json`, `bom_report.md`, and `feedback.jsonl` as sensitive project artifacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/agent-bom-scan)
- [Triage and interpretation](references/triage.md)
- [Online mode protocol](references/online_protocol.md)
- [Advisory database format](references/advisories_format.md)
- [OSV querybatch endpoint](https://api.osv.dev/v1/querybatch)
- [OSV query endpoint](https://api.osv.dev/v1/query)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Key=value command summaries, JSON BOM and findings files, Markdown reports, and concise triage guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline by default; explicit online mode sends package name, version, and ecosystem to OSV.dev.]

## Skill Version(s):

2.0.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
