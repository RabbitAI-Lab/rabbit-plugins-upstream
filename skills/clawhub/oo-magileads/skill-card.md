## Description:

Magileads (magileads.com). Use this skill for ANY Magileads request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate Magileads through an OOMOL-connected account, including contact list retrieval, creation, update, and deletion. It is intended for workflows that need schema-checked Magileads actions through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, and delete Magileads contact lists through a connected OOMOL account.

Mitigation: Confirm the exact target, payload, and intended effect with the user before running write or destructive actions.

Risk: Incorrect payloads or stale assumptions about connector fields could affect the wrong Magileads data.

Mitigation: Inspect the live action schema with the oo CLI before constructing each payload.

Risk: Setup steps may require installing the oo CLI or authenticating an OOMOL account.

Mitigation: Install or authenticate only from OOMOL sources, and only when an action fails because setup is missing.

## Reference(s):

- [Magileads homepage](https://www.magileads.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-magileads)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
