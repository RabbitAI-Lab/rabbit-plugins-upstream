## Description:

Moxie (withmoxie.com). Use this skill for ANY Moxie request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to inspect live Moxie connector schemas and run read-only list or search actions against a user's connected Moxie workspace through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and search Moxie workspace data through a connected OOMOL account.

Mitigation: Install it only for agents and users that should access Moxie workspace data, and keep OOMOL and Moxie connection scopes aligned with that need.

Risk: Requests outside the listed read-only actions could change or delete Moxie data if future connector actions expose write or destructive behavior.

Mitigation: Require explicit user confirmation of the exact target, payload, and expected effect before running any write or destructive action.

Risk: Authentication, missing connection, expired credential, or billing failures can interrupt connector use.

Mitigation: Run first-time setup, reconnection, or billing steps only after the corresponding command failure is observed.

## Reference(s):

- [Moxie homepage](https://www.withmoxie.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-moxie)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON when commands are run with --json.]

## Skill Version(s):

1.0.0 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
