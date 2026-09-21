## Description:

Typefully operates Typefully through an OOMOL-connected account for reading, creating, updating, and deleting draft-related data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Typefully through an OOMOL-connected account, including reading user, draft, and social set data and creating, updating, or deleting drafts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, and delete Typefully drafts through the connected account.

Mitigation: Require explicit confirmation of the target, payload, and expected effect before write or destructive actions.

Risk: First-time setup may involve running a one-line CLI installer.

Mitigation: Confirm the user trusts OOMOL and review the install guide or installer before running curl or PowerShell installer commands.

## Reference(s):

- [Typefully homepage](https://typefully.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-typefully)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before building action payloads.]

## Skill Version(s):

1.0.5 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
