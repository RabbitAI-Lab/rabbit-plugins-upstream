## Description:

Lightfield (lightfield.app) helps agents search and read Lightfield data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to let an agent inspect schemas and run read-oriented Lightfield connector actions for accounts, contacts, opportunities, custom objects, object definitions, and API key metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Use a verified or package-manager installation path where possible, and do not allow an agent to run remote installer commands automatically.

Risk: The skill can access Lightfield account data through a connected OOMOL account.

Mitigation: Review authentication prompts and connected Lightfield API key scope before use, and run connector actions only for intended accounts and records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lightfield)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Lightfield homepage](https://lightfield.app)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke oo CLI connector schema and run commands that return JSON data from Lightfield.]

## Skill Version(s):

1.0.3 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
