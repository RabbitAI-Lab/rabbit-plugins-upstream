## Description:

Yuanxi yotta-recon is a cross-agent network reconnaissance skill for zero-dependency port scanning, service identification, and version fingerprinting with built-in Scope Guard authorization discipline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, security engineers, and asset owners use this skill to inventory authorized targets, identify open ports and common service versions, and produce reconnaissance findings before security testing or exposure review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network reconnaissance outside an authorized scope can create legal or operational risk.

Mitigation: Use only on systems the user owns or is explicitly authorized to test; prefer a scope file and run check-scope before scanning.

Risk: Reconnaissance reports and captured banners may expose sensitive asset information.

Mitigation: Treat generated reports, JSON output, and banners as sensitive data and limit storage or sharing to the authorized engagement context.

Risk: Version fingerprint risk hints can be incomplete or misleading if services are patched, backported, or spoofed.

Mitigation: Manually verify any risk hint before treating it as a confirmed vulnerability or recommending remediation.

## Reference(s):

- [Scope Guard](references/scope-guard.md)
- [Service Fingerprints](references/service-fingerprints.md)
- [Protocol Probes](references/protocol-probes.md)
- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-recon)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Text tables, JSON, Markdown reports, and concise command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include scan IDs, timestamps, target summaries, authorization source, service fingerprints, banners, and risk hints that require human verification.]

## Skill Version(s):

0.1.5 (source: server release, frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
