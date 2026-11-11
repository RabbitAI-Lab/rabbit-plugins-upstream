## Description:

Guides developers in building, maintaining, upgrading, and auditing Tauri and Electron desktop apps, with read-only .NET SDK audits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to inspect or maintain Tauri and Electron desktop applications, plan dependency upgrades, improve security and performance, and review packaging, CI, and release workflows. It can also produce read-only .NET SDK and target-framework audits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports incomplete audit coverage and components that were not fully inspected.

Mitigation: Review the uncovered components and understand the audit-coverage gap before installing or running the skill; treat the current scan as incomplete.

## Reference(s):

- [Tauri guidance](references/tauri.md)
- [Electron guidance](references/electron.md)
- [Release flow](references/release-flow.md)
- [Verification and performance](references/verification-performance.md)
- [Electron security documentation](https://www.electronjs.org/docs/latest/tutorial/security)
- [Tauri dependency update documentation](https://v2.tauri.app/develop/updating-dependencies)

## Skill Output:

**Output Type(s):** [Guidance, Markdown reports and plans, JSON audit reports, Shell commands, Code and configuration examples]

**Output Format:** [Markdown guidance and reports, JSON audit output, shell commands, and code or configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include workflow templates and evidence-based findings; audit completeness depends on available project files and external metadata.]

## Skill Version(s):

0.9.1 (source: skill frontmatter metadata.version and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
