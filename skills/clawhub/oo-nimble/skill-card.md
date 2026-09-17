## Description:

Nimble (nimble.com). Use this skill for reading, creating, and updating Nimble CRM contact data through the OOMOL `oo` CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage Nimble CRM contacts from an agent workflow, including listing, retrieving, creating, and updating contact records through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run remote installer scripts that execute code on the user's machine.

Mitigation: Review the oo CLI installation path first, prefer an official signed or checksummed package, or download and inspect the installer before running it.

Risk: Create and update actions can modify Nimble contact records.

Mitigation: Confirm the exact payload and expected effect with the user before running any write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-nimble)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Nimble homepage](https://www.nimble.com/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and requires confirmation before write actions.]

## Skill Version(s):

1.0.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
