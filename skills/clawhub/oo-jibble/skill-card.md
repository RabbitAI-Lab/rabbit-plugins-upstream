## Description:

Jibble lets an agent read, create, update, archive, and delete Jibble data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage Jibble organizations, members, and work locations from an agent while relying on live connector schemas for valid payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write, archive, or delete actions can change Jibble work-location data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before approving create, update, archive, or delete actions.

Risk: The connected oo CLI account grants connector access to the user's Jibble account.

Mitigation: Install and connect this skill only when Jibble management through OOMOL is intended, and review generated payloads before execution.

## Reference(s):

- [Jibble homepage](https://www.jibble.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-jibble)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
