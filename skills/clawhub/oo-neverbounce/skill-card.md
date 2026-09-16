## Description:

NeverBounce helps agents verify single email addresses, manage bulk verification jobs, check account credits, and retrieve job results through an OOMOL-connected NeverBounce account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate NeverBounce email verification workflows through the oo CLI, including single checks, bulk job lifecycle management, result downloads, and account credit review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that can execute code on the user's machine.

Mitigation: Review the installer source before use and prefer an official signed or checksum-verified installer path.

Risk: Bulk job actions can create or start NeverBounce jobs and may change account state or consume credits.

Mitigation: Inspect the live action schema and confirm the exact payload and effect with the user before running state-changing actions.

## Reference(s):

- [NeverBounce Homepage](https://neverbounce.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses, execution identifiers, paginated result data, or CSV job downloads from NeverBounce actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
