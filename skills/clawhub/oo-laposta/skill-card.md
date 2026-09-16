## Description:

Laposta (laposta.nl). Use this skill for Laposta requests involving reading, creating, and updating mailing-list data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to inspect and manage Laposta mailing lists and members through the oo CLI. It supports read operations and confirmed write operations such as creating or updating lists and members.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that can execute local code.

Mitigation: Do not let an agent run remote installer commands automatically; install the oo CLI only through a user-approved, verified method.

Risk: Write actions can change Laposta mailing-list or member state.

Mitigation: Confirm the exact payload and expected effect with the user before running create or update actions.

Risk: Connector payloads may drift from the live Laposta action schema.

Mitigation: Inspect the live connector schema before constructing payloads for each action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-laposta)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Laposta homepage](https://laposta.nl/)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include oo CLI commands, connector action names, JSON payloads, and returned execution metadata.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
