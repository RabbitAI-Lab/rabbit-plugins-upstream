## Description:

pretix (pretix.eu). Use this skill for ANY pretix request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and operators use this skill to inspect pretix organizers, events, ticket items, and orders through an OOMOL-connected account. It guides schema-first oo CLI calls and asks for confirmation before actions that may change pretix data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access organizer, event, item, and order information through the user's connected pretix account.

Mitigation: Install it only for intended pretix accounts, keep connector access scoped to the needed data, and review requested organizer, event, item, or order access before running commands.

Risk: The description mentions creating and updating data while the documented action list is narrower and includes actions that may change pretix state.

Mitigation: Check the live connector schema before each action and get explicit user confirmation for the exact payload and expected effect before running any write or destructive action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pretix)
- [pretix homepage](https://pretix.eu)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI and a connected pretix account.]

## Skill Version(s):

1.0.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
