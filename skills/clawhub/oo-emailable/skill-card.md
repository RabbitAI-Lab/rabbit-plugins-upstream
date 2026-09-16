## Description:

Emailable helps agents retrieve account information, verify single or batch email addresses, and check batch job status through an OOMOL-connected Emailable account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Emailable account and email verification workflows from an agent. It supports account credit checks, single-address verification, batch verification, and batch status lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email verification actions can submit personal data and consume Emailable credits.

Mitigation: Confirm the exact email address list, destination, batch size, and expected credit use before running verification actions.

Risk: The skill documents remote installer commands for the OOMOL CLI.

Mitigation: Use the install guide and verify the installer source through an official OOMOL channel before executing remote installation commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-emailable)
- [Emailable homepage](https://emailable.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Emailable JSON responses from oo connector actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
