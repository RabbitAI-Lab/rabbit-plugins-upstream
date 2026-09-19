## Description:

Missive helps agents search and read Missive data through an OOMOL-connected account and the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve Missive contacts, conversations, organizations, teams, users, and contact books through an OOMOL-connected Missive account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a pipe-to-shell installer path for the oo CLI.

Mitigation: Use a verified oo CLI installation method instead of piping remote installer output directly to a shell.

Risk: The allowed oo CLI authority is broader than the skill's read/search purpose.

Mitigation: Limit use to the listed Missive read actions and ensure the connected OOMOL and Missive account has only the scopes required for those actions.

Risk: Connector actions access Missive account data through connected credentials.

Mitigation: Inspect the live action schema before each request and run only payloads needed for the user's requested read or search task.

## Reference(s):

- [Missive homepage](https://missiveapp.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-missive)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
