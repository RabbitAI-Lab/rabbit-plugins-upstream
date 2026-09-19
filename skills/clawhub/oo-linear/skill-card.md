## Description:

Linear (linear.app). Use this skill for reading, creating, updating, and deleting Linear data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect Linear connector schemas and perform Linear issue, project, team, label, cycle, comment, attachment, reaction, query, and mutation workflows through the oo CLI with connected OOMOL credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes an unsafe remote installer pattern for the oo CLI.

Mitigation: Prefer installing the oo CLI through a verified, pinned, or package-manager path instead of piping remote scripts directly to a shell.

Risk: The skill exposes broad raw GraphQL mutation access to Linear.

Mitigation: Require explicit review of the payload and intended effect before running raw mutations.

Risk: Write and destructive Linear actions can change or remove workspace data.

Mitigation: Confirm the target, payload, and expected effect with the user before write actions, and get explicit approval before destructive actions.

Risk: The skill depends on OOMOL-connected Linear credentials.

Mitigation: Install only if the user trusts OOMOL and is comfortable connecting it to Linear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-linear)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Linear homepage](https://linear.app)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands target the oo CLI linear connector; connector responses are JSON with data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
