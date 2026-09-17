## Description:

Helps agents operate Metronome through the OOMOL oo CLI to retrieve customers, invoices, billable metrics, and related billing data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Metronome connector schemas and run read-oriented customer, invoice, billable metric, and customer-list actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes a remote installer command that security evidence flags as unverified.

Mitigation: Do not let an agent run the installer automatically; use official OOMOL installation documentation, inspect the installer first, and prefer pinned or verified releases where available.

Risk: The skill can retrieve customer, invoice, and billable metric data from a connected Metronome account.

Mitigation: Use a least-privileged Metronome connection, confirm the intended account before running actions, and avoid exposing sensitive customer or billing data in downstream outputs.

## Reference(s):

- [Metronome homepage](https://metronome.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Metronome skill page](https://clawhub.ai/oomol/skills/oo-metronome)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the OOMOL oo CLI to inspect live action schemas before running Metronome connector actions.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
