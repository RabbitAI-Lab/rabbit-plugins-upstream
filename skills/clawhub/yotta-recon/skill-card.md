## Description:

Yuanxi (yotta-recon) is a zero-dependency network reconnaissance skill that helps agents perform authorized port scanning, service identification, and version fingerprinting for security testing and asset inventory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Security engineers, developers, and authorized asset owners use this skill to inventory exposed services and collect version fingerprints before security testing or remediation planning. It is intended for explicitly authorized targets, including owned assets, test environments, CTF labs, and approved assessments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthorized scanning can create legal and operational risk.

Mitigation: Run check-scope first, provide a scope file when possible, and scan only targets the user explicitly owns or is authorized to test.

Risk: Network probing can burden fragile services or look like hostile scanning.

Mitigation: Use limited target ranges and tune --top, --ports, --concurrency, --timeout, and --rate to keep scans narrow and controlled.

Risk: Version fingerprints and known-risk hints can be incomplete, spoofed, or affected by downstream patching.

Mitigation: Treat findings as leads for manual verification; do not treat a risk hint as proof of exploitability.

Risk: Broad multi-agent installation increases supply-chain and operator-error exposure.

Mitigation: Install only where needed and pin the npm version for reproducible deployments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-recon)
- [Scope Guard authorization discipline](references/scope-guard.md)
- [Service and version fingerprints](references/service-fingerprints.md)
- [Protocol probe behavior](references/protocol-probes.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Plain text tables, JSON output, and Markdown reports with command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include scan_id, timestamp, target, authorization source, service fingerprints, version hints, risk levels, and truncated banners.]

## Skill Version(s):

0.1.6 (source: server release metadata; artifact frontmatter and package.json remain 0.1.5 per release changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
