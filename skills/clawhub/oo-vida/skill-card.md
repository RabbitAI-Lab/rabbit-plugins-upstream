## Description:

Vida (vida.io). Use this skill for ANY Vida request - searching and reading data. Whenever a task involves Vida, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and read Vida account, usage, and task data through an OOMOL-connected account and the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include remote installer commands that can execute code on the user's machine.

Mitigation: Do not let an agent run those installers automatically; use a verified, pinned, user-reviewed oo CLI installation path.

Risk: The skill accesses Vida through an OOMOL-connected account.

Mitigation: Use it only when the user trusts OOMOL, the Vida connection, and the requested read action.

## Reference(s):

- [Vida homepage](https://vida.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-vida)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should inspect the live Vida connector schema before constructing payloads.]

## Skill Version(s):

1.0.2 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
