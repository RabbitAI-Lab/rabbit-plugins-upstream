## Description:

Formaloo enables agents to read, create, update, and delete Formaloo forms and submitted rows through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate a connected Formaloo account: inspect forms and submitted rows, submit new rows, update existing rows, and delete rows after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: State-changing Formaloo actions can create or modify submitted data.

Mitigation: Confirm the exact action, target form or row, and JSON payload with the user before running create_row or update_row.

Risk: The delete_row action permanently removes submitted Formaloo data.

Mitigation: Get explicit approval for the specific row and form before running delete_row.

Risk: Setup and authentication commands may initiate account or connection changes.

Mitigation: Run setup, login, or connection steps only after a command fails with the matching auth or connection error.

## Reference(s):

- [ClawHub Formaloo skill page](https://clawhub.ai/oomol/skills/oo-formaloo)
- [Formaloo homepage](https://www.formaloo.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector commands return JSON when run with --json.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
