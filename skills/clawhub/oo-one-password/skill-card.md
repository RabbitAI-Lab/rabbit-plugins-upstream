## Description:

Operates 1Password through an OOMOL-connected account for listing vaults and items, reading selected items, and checking activity and health data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to perform read-only 1Password Connect operations through OOMOL's oo CLI after connecting their account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can route sensitive 1Password data through OOMOL-connected tooling.

Mitigation: Use a narrowly scoped, read-only 1Password Connect token and confirm that routing secrets through OOMOL fits the user's security model.

Risk: The setup guidance includes remote shell and PowerShell installer commands.

Mitigation: Install the oo CLI through a verified, user-controlled process instead of allowing an agent to run remote installer commands automatically.

Risk: Retrieving full 1Password items may expose secrets beyond the user's immediate need.

Mitigation: Confirm the exact vault and item before retrieving full item data.

## Reference(s):

- [ClawHub 1Password skill page](https://clawhub.ai/oomol/skills/oo-one-password)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [1Password homepage](https://1password.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads; connector responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only 1Password data can include secrets, and connector commands depend on live action schema inspection.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
