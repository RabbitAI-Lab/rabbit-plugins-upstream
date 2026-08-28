## Description:

Yuanxi yotta-recon gives agents a zero-dependency network reconnaissance workflow for authorized port scanning, service identification, version fingerprinting, asset inventory, and Markdown or JSON reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, security testers, and asset owners use this skill to let an agent check authorization, scan authorized targets, identify open ports and common services, and produce audit-friendly reconnaissance output before deeper security testing or inventory work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthorized or overly broad scanning can create legal and operational risk.

Mitigation: Use scope files where possible, scan only targets the user controls or has permission to test, run check-scope before scan, and do not bypass DENY results.

Risk: Network reconnaissance can affect fragile targets if run too aggressively.

Mitigation: Use bounded target lists, top or custom port selections, timeout settings, concurrency controls, and rate limiting for authorized environments.

Risk: Version-based risk hints can be misleading when banners are spoofed, incomplete, or patched.

Mitigation: Treat risk levels as triage hints and manually verify findings before concluding that a target is vulnerable or taking action.

Risk: Global installation can add this scanning capability across multiple agent environments.

Mitigation: Use the global installer only when intentionally enabling the skill broadly; otherwise install to a specific skill directory.

## Reference(s):

- [Scope Guard Authorization Discipline](references/scope-guard.md)
- [Service and Version Fingerprints](references/service-fingerprints.md)
- [Protocol Probe Notes](references/protocol-probes.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands; scanner outputs plain text tables, JSON, or Markdown reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires authorized target scope before scanning; generated reports include scan_id, timestamp, targets, and authorization source.]

## Skill Version(s):

0.1.4 (source: SKILL.md frontmatter, package.json, CHANGELOG.md, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
