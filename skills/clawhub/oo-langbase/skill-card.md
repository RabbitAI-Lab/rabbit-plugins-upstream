## Description:

This skill lets an agent operate Langbase through an OOMOL-connected account, including creating, deleting, listing, and retrieving Langbase memory data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with Langbase memories through an OOMOL-connected account, using the oo CLI to inspect connector schemas, run actions, and handle setup or billing errors when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents one-line remote installer commands that execute downloaded scripts.

Mitigation: Verify the installer source and integrity before use, or prefer an official package manager, pinned release, or reviewed download.

Risk: Langbase actions run through OOMOL as an intermediary.

Mitigation: Use the skill only when the user is comfortable with OOMOL brokering Langbase actions and credentials server-side.

Risk: Create and delete memory actions can change or remove Langbase data.

Mitigation: Confirm the exact payload, target memory, and intended effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Langbase Skill](https://clawhub.ai/oomol/skills/oo-langbase)
- [Langbase Homepage](https://langbase.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute Langbase connector actions through the oo CLI after schema inspection and user confirmation for write or destructive actions.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
