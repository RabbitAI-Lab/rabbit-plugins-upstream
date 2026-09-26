## Description:

Walletap lets an agent manage Walletap templates and issued passes through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to read Walletap templates and passes, issue new passes from templates, update pass data, and send pass-holder notifications. It is intended for Walletap work performed through an OOMOL-connected account rather than direct API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote shell and PowerShell installer one-liners that were flagged as unverified remote script execution.

Mitigation: Review the CLI installation path before use and prefer an official package manager, signed release, or manually inspected installer.

Risk: Write and destructive actions can create passes, notify pass holders, or update Walletap pass data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before allowing write or destructive actions.

## Reference(s):

- [ClawHub Walletap skill page](https://clawhub.ai/oomol/skills/oo-walletap)
- [Walletap homepage](https://www.walletap.io/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON when the skill runs oo connector commands with --json.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
