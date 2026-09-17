## Description:

Use this skill for Keen IO requests, including reading, creating, and updating data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Keen IO through an OOMOL-connected account, including publishing JSON events and querying event counts or numeric sums.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path recommends remote installer commands that can execute local code.

Mitigation: Review or replace the installer with a trusted package manager, pinned release, or downloaded installer with checksum or signature verification before installation.

Risk: The add_event action can write new event data to a Keen IO collection.

Mitigation: Confirm the exact JSON payload, target collection, and intended effect with the user before running write actions.

Risk: Connector schemas may change over time.

Mitigation: Fetch the live action schema with the oo CLI before constructing each action payload.

## Reference(s):

- [Keen IO homepage](https://keen.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Keen IO skill page](https://clawhub.ai/oomol/skills/oo-keen-io)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that inspect connector schemas or run Keen IO actions with JSON payloads.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
