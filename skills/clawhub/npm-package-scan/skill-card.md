## Description:

Audit JavaScript and TypeScript repository dependencies for security, supply-chain, maintenance, version, lockfile, and cleanup risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geoffrey-xiao](https://clawhub.ai/user/geoffrey-xiao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review npm, pnpm, Yarn, or Bun dependency risk in JavaScript and TypeScript repositories. It helps produce evidence-based dependency findings, verification steps, and a sequenced remediation plan without changing the repository by default.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registry-backed dependency checks may disclose package names and versions to a package registry.

Mitigation: Explain the disclosure before running registry-backed commands and skip them when network use is unavailable or inappropriate.

Risk: Automatic audit fixes, upgrades, installs, or lockfile regeneration can change repository state and introduce unintended compatibility or supply-chain effects.

Mitigation: Keep reviews read-only unless the user explicitly requests repository changes, and avoid mutating package-manager commands during review.

Risk: Package lifecycle scripts and arbitrary package binaries can execute untrusted code.

Mitigation: Prefer commands that ignore lifecycle scripts and do not execute package binaries merely to identify or inspect them.

## Reference(s):

- [Review checklist](references/checklist.md)
- [Read-only command guide](references/commands.md)
- [Dependency risk review template](references/report-template.md)
- [ClawHub skill page](https://clawhub.ai/geoffrey-xiao/skills/npm-package-scan)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only by default; registry-backed checks require disclosure and may be skipped when network use is unavailable or inappropriate.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
