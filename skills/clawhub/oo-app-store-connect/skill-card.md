## Description:

Helps agents read and manage App Store Connect apps, builds, TestFlight groups, beta testers, reviews, and users through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release managers use this skill to inspect App Store Connect data and manage TestFlight or review workflows from an agent session. It supports read, write, and destructive operations, with confirmation expected before state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can ask the agent to execute an unverified remote installer for the oo CLI.

Mitigation: Review the installer path before installation, prefer a pinned and verifiable release or package manager, and install the CLI only after explicit user approval.

Risk: Write and destructive App Store Connect actions can alter TestFlight access, review responses, build notes, or team data.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before any write or destructive action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-app-store-connect)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [App Store Connect](https://appstoreconnect.apple.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI connector schema and run commands, JSON request payloads, and summaries of App Store Connect results.]

## Skill Version(s):

1.0.1 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
