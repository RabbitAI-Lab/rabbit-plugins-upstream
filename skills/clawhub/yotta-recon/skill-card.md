## Description:

Helps agents inventory authorized network targets through port scanning, service identification, and version fingerprinting with built-in scope checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Security and IT operations teams use this skill to inventory open ports, identify services and versions, and review potential exposure on systems they are authorized to assess.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network probing outside an approved scope may affect systems without permission.

Mitigation: Confirm authorization, precheck targets against a scope file, and scan only permitted systems.

Risk: Unpinned installer downloads and unexpected install destinations introduce supply-chain or local file risks.

Mitigation: Install a trusted, pinned version and inspect target paths with --dry-run or --list before installation.

Risk: Banner-based version and risk matches can be inaccurate.

Mitigation: Manually verify reported services, versions, and risk matches before acting.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-recon)
- [Skill homepage](https://github.com/YottaMeta/yotta-recon)
- [Protocol probes](references/protocol-probes.md)
- [Scope Guard](references/scope-guard.md)
- [Service fingerprints](references/service-fingerprints.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Guidance]

**Output Format:** [Text tables, JSON scan results, or Markdown reports with findings and authorization details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Service and version fingerprints are indicative; risk matches require manual confirmation.]

## Skill Version(s):

0.1.8 (source: SKILL.md frontmatter, CHANGELOG.md, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
