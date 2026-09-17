## Description:

Ongage connector skill for reading, creating, and updating Ongage data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Ongage through an OOMOL-connected account, including list and contact lookup plus confirmed contact updates or upserts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can introduce supply-chain risk if executed without review.

Mitigation: Review the OOMOL CLI installer before running it and avoid elevated shells.

Risk: Contact status changes and bulk contact updates can alter Ongage data.

Mitigation: Require explicit user confirmation of the exact payload and effect before running write actions.

## Reference(s):

- [Ongage homepage](https://www.ongage.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ongage)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL-managed credentials; write actions require explicit user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
