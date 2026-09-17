## Description:

Jumpseller (jumpseller.com) skill for reading, creating, and updating store data through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a Jumpseller store through an OOMOL-connected account, including reading store data and creating or updating categories, customers, products, and orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path instructs users to execute remote installer scripts directly.

Mitigation: Install the oo CLI from a verified, pinned release or trusted package manager, and avoid piping remote scripts directly into Bash or PowerShell.

Risk: Create and update actions can change Jumpseller store data.

Mitigation: Fetch the live action schema, confirm the exact payload and expected effect with the user, and then run the state-changing action.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/oomol/skills/oo-jumpseller)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Jumpseller Homepage](https://jumpseller.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Code, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before payload construction and requires confirmation before state-changing actions.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
