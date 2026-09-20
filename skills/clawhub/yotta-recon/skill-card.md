## Description:

元析 yotta-recon helps agents perform authorized network reconnaissance with zero-dependency port scanning, service identification, version fingerprinting, and Scope Guard authorization checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Security testers, developers, and asset owners use this skill to inventory authorized targets, identify open ports and service versions, and produce reconnaissance findings before deeper security review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network reconnaissance can create legal or operational risk when run against targets without explicit permission.

Mitigation: Use the skill only for authorized targets, prefer a scope file, run check-scope before scanning, and avoid --assume-authorized --yes unless permission is confirmed.

Risk: Installer commands can write skill files into agent skill directories.

Mitigation: Use reviewed or pinned releases, choose explicit --agent or --dir install targets, and avoid global installation unless the skill is intended for multiple agents.

Risk: Version-based risk hints may be inaccurate because banners can be spoofed or patched systems may still report old versions.

Mitigation: Treat risk hints as prompts for manual verification rather than confirmed vulnerabilities or exploitation instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-recon)
- [Project homepage](https://github.com/YottaMeta/yotta-recon)
- [Scope Guard authorization discipline](references/scope-guard.md)
- [Service and version fingerprints](references/service-fingerprints.md)
- [Protocol probe behavior](references/protocol-probes.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Text summaries, JSON output, Markdown reports, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include scan_id, time, targets, authorization source, service fingerprints, and risk hints for manual verification.]

## Skill Version(s):

0.1.7 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
