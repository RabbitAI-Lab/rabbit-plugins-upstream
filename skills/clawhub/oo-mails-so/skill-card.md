## Description:

Operates Mails (mails.so) email validation through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to validate email addresses and manage Mails batch validation jobs through an OOMOL-connected Mails account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions pipe remote install scripts directly into shell interpreters.

Mitigation: Review the setup path before installing and prefer a verified package manager or a downloaded installer with a published checksum or signature.

Risk: Creating a validation batch is a write action that can process unintended email lists or consume account resources.

Mitigation: Confirm the exact batch payload and expected effect with the user before running the action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mails-so)
- [Mails homepage](https://mails.so)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
