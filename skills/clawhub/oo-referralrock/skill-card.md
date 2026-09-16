## Description:

Referral Rock helps agents search and read Referral Rock programs, members, referrals, and member performance statistics through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and teams with a connected Referral Rock account use this skill to inspect referral programs, search members and referrals, and review member performance statistics without handling raw credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote shell installer commands for the oo CLI.

Mitigation: Install the oo CLI through verified vendor instructions or a trusted package source with version and integrity checks before using the skill.

Risk: Future connector actions could change Referral Rock state if write or destructive actions are added.

Mitigation: Use direct execution only for the listed read/search actions and require explicit user confirmation for any clearly labeled write or destructive action.

## Reference(s):

- [Referral Rock homepage](https://referralrock.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Referral Rock skill page](https://clawhub.ai/oomol/skills/oo-referralrock)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Referral Rock icon](https://static.oomol.com/logo/third-party/referralrock.svg)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to fetch live connector schemas and run read-only Referral Rock actions that return JSON responses.]

## Skill Version(s):

1.0.2 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
