## Description:

Sendmator helps agents manage Sendmator contacts through an OOMOL-connected account, including creating, reading, listing, updating, and deleting contact records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Sendmator contacts from an agent session while relying on OOMOL for account connection and credential handling. It supports contact creation, lookup, listing, updates, and explicit-confirmation deletion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer scripts, which can introduce installation risk if run without review.

Mitigation: Install only after reviewing or verifying the OOMOL installer source, and prefer established package or internal approval workflows where available.

Risk: Create, update, and delete actions can make real changes in a connected Sendmator account.

Mitigation: Require user confirmation for mutation payloads, and require explicit approval for destructive contact deletion.

## Reference(s):

- [Sendmator homepage](https://sendmator.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sendmator)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or execute oo CLI connector commands that return JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
