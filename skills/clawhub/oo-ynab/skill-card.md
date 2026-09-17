## Description:

Provides agent guidance for reading YNAB data through an OOMOL-connected account with the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query YNAB account, budget, category, payee, plan, transaction, settings, and user data through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unverified remote installer commands can execute downloaded code on the user's machine.

Mitigation: Review the oo CLI installation path before installing, and prefer an official package manager or downloaded installer with published checksum or signature verification.

Risk: The skill routes read access to YNAB financial data through OOMOL's connector and account system.

Mitigation: Use the skill only when the user accepts OOMOL-mediated access to YNAB data and has connected the account intentionally.

Risk: Incorrect connector payloads could query unintended YNAB records.

Mitigation: Inspect the live connector schema with `oo connector schema` before constructing each payload.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [YNAB homepage](https://www.ynab.com)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ynab)
- [Skill icon](https://static.oomol.com/logo/third-party/ynab.svg)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the oo CLI and may return JSON connector responses.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
