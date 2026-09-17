## Description:

SeaTable helps agents read, create, update, and delete SeaTable data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill to operate SeaTable bases through an OOMOL-connected account, including schema inspection, row reads, row creation, row updates, and row deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes unsafe CLI installation guidance.

Mitigation: Install the oo CLI only through a safer verified method before using the skill.

Risk: The skill can append, update, or delete SeaTable data, and server security evidence notes that append rows can occur without the skill's own write-confirmation requirement.

Mitigation: Require explicit user confirmation of the target table, payload, and expected effect before any append, update, or delete action.

## Reference(s):

- [ClawHub SeaTable skill](https://clawhub.ai/oomol/skills/oo-seatable)
- [SeaTable homepage](https://seatable.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may call the oo CLI and can mutate SeaTable data when write or destructive actions are selected.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
