## Description:

Cronly (cronly.app) helps an agent read, create, update, and delete Cronly data through the OOMOL oo CLI connector instead of calling the Cronly API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Cronly projects and job monitors from an agent session. It supports read actions as well as confirmed write and destructive actions against a connected Cronly account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can create or change Cronly projects and job monitors.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: Destructive actions can delete Cronly projects or job monitors by ID.

Mitigation: Confirm the exact target ID and obtain explicit approval before running destructive actions.

Risk: The skill operates a connected Cronly account through OOMOL.

Mitigation: Install only when the agent is intended to operate that account, and run CLI login or connection setup only when requested or when a command fails for that reason.

## Reference(s):

- [Cronly skill page](https://clawhub.ai/oomol/skills/oo-cronly)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Cronly homepage](https://cronly.app/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands operate through the OOMOL oo CLI and may return JSON data from Cronly connector actions.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
