## Description:

Emailable lets agents inspect account details and verify single or batch email addresses through an OOMOL-connected Emailable account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Emailable account details and run single or batch email verification through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include piping a downloaded installer script directly into a shell.

Mitigation: Prefer OOMOL's official installation guide or a verified package method before running setup commands.

Risk: Batch email verification creates a new Emailable job and may consume account credits or change account state.

Mitigation: Review the exact payload and user intent before approving write actions.

Risk: Connector use depends on OOMOL-managed credentials and account connectivity.

Mitigation: Install only when the user accepts OOMOL as the Emailable connector provider and handle auth or connection errors through first-time setup.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-emailable)
- [Emailable homepage](https://emailable.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL's oo CLI and returns connector JSON when actions run.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
