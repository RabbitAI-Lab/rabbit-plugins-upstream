## Description:

Pylon helps agents read, search, create, and update Pylon accounts, contacts, issues, and internal issue notes through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and teams with Pylon connected through OOMOL use this skill to inspect live Pylon action schemas and run read or confirmed write operations for accounts, contacts, issues, and internal notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remotely downloaded shell installer commands.

Mitigation: Prefer an official package-manager or verified installer path, inspect what will be installed, and avoid elevated shells unless required.

Risk: Write actions can create or update Pylon data.

Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged as write.

## Reference(s):

- [ClawHub Pylon skill page](https://clawhub.ai/oomol/skills/oo-pylon)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Pylon homepage](https://www.usepylon.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI and an OOMOL-connected Pylon account; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
