## Description:

Retently helps agents read, create, and update Retently data through the OOMOL-connected oo CLI instead of calling the Retently API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Retently accounts from an agent, including account checks, customer and feedback lookups, campaign and template listing, and confirmed bulk customer upserts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to run remote installer scripts directly in a shell.

Mitigation: Use official, verifiable installation steps and inspect or verify installer content before execution.

Risk: The upsert_customers action can create or update Retently customer records in bulk.

Mitigation: Confirm the exact payload and intended effect with the user before allowing the skill to run write actions.

## Reference(s):

- [ClawHub Retently skill page](https://clawhub.ai/oomol/skills/oo-retently)
- [Retently homepage](https://www.retently.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Retently connector JSON responses.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
