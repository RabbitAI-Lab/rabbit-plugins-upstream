## Description:

Nimble helps agents read, create, list, search, and update Nimble CRM contacts through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Nimble CRM contact workflows from an agent, including listing, retrieving, creating, and updating contacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify Nimble contact records through create and update actions.

Mitigation: Review the exact payload and expected effect with the user before approving write actions.

Risk: The skill may require installing or signing into the external oo CLI and connecting a Nimble account.

Mitigation: Run setup only after an authentication or connection failure, and review installation and account-connection steps before proceeding.

## Reference(s):

- [Nimble homepage](https://www.nimble.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-nimble)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce read results or proposed write payloads for Nimble contact records.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
