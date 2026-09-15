## Description:

Hookdeck helps agents read, create, update, list, and delete Hookdeck sources, destinations, and connections through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Hookdeck resources from an agent workflow, including listing and retrieving resources and performing confirmed write or delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to run remote installer scripts directly in a shell.

Mitigation: Install the oo CLI through a verified, versioned, checksum- or signature-checked method before using the skill.

Risk: Write and destructive Hookdeck actions can change or delete sources, destinations, and connections.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or delete actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-hookdeck)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Hookdeck Homepage](https://hookdeck.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI connector actions that return JSON data and execution metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
