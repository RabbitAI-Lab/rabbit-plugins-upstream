## Description:

元析 performs authorized network reconnaissance by identifying open ports, services, and version fingerprints, with built-in scope checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Security engineers and developers use it to inventory authorized assets and map exposed ports, services, and version fingerprints before security testing. Use it only for explicitly authorized targets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorization safeguards may allow probing beyond the approved target range.

Mitigation: Use approved numeric IP targets, explicit scope files, and network restrictions; avoid broad authorization overrides.

Risk: Installing the skill can affect files in the selected destination.

Mitigation: Pin and review the installer version, select one installation destination, and preview with --dry-run.

## Reference(s):

- [Scope Guard authorization guide](references/scope-guard.md)
- [Service fingerprints reference](references/service-fingerprints.md)
- [Protocol probes reference](references/protocol-probes.md)
- [Project homepage](https://github.com/YottaMeta/yotta-recon)
- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-recon)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-recon)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Text tables, JSON results, and Markdown reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include scan identifiers, timestamps, and authorization source; version risk matches are prompts for manual verification.]

## Skill Version(s):

0.1.9 (source: frontmatter, CHANGELOG, package.json, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
