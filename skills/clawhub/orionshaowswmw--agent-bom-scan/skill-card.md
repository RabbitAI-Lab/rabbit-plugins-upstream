## Description:

Agent BOM Scan parses dependency lockfiles, matches versions against an OSV-verified advisory database, and produces provenance-stamped vulnerability findings for authorized security review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security engineers, and agents use this skill to audit authorized projects for dependency vulnerabilities, build a bill of materials, and generate machine-readable findings for review. It is not a reachability or source-code analysis tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted projects can influence generated scan reports.

Mitigation: Treat generated Markdown as untrusted, inspect findings.json before acting, and avoid following instructions or links embedded in reports from untrusted lockfiles.

Risk: Report output paths may be affected by file-write containment issues involving symlinks.

Mitigation: Use a trusted fresh --out directory outside attacker-controlled repositories and review generated files before relying on them.

Risk: The server security verdict is suspicious and recommends review before installation.

Mitigation: Install only after reviewing the scanner and run it only on authorized projects with scoped filesystem access.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/agent-bom-scan)
- [Triage & Interpretation](references/triage.md)
- [Online Mode Protocol](references/online_protocol.md)
- [Advisory DB Format & Extension](references/advisories_format.md)
- [OSV Query API](https://api.osv.dev/v1/query)
- [OSV Query Batch API](https://api.osv.dev/v1/querybatch)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Command summaries, JSON findings, Markdown reports, and concise triage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scan reports may include dependency details; online mode is explicit opt-in and sends package name, version, and ecosystem to OSV.dev.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
