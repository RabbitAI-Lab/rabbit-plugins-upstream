## Description:

Guides agents through Siluzan TSO advertising account management, Google and Meta campaign workflows, market analysis, and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit)

### License/Terms of Use:

MIT-0

## Use Case:

Advertising teams and their agents use this skill to analyze accounts and markets, prepare reports, and manage supported ad campaigns through Siluzan TSO.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer makes persistent system and assistant-profile changes.

Mitigation: Review the installer and use an isolated machine or user profile if possible; install only if you trust the publisher.

Risk: Raw lead data may expose personal information in the assistant transcript.

Mitigation: Avoid requesting or pasting raw lead JSON unless that disclosure is intended.

Risk: Ad, finance, permission, deletion, and activation actions can change live accounts.

Mitigation: Confirm each consequential action before allowing the CLI to run it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sigedev01-bit/skills/siluzan-tso)
- [Workflow routing](artifact/references/core/intent-routing.md)
- [Account and campaign workflows](artifact/references/core/workflows.md)
- [Report workflows](artifact/references/core/playbooks.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Reports]

**Output Format:** [Markdown guidance, CLI commands, JSON configuration, and report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+, an installed Siluzan TSO CLI, and authentication.]

## Skill Version(s):

1.1.54 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
