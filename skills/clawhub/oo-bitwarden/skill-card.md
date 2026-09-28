## Description:

This skill helps agents read Bitwarden organization data through an OOMOL-connected Bitwarden connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Bitwarden organization collections, groups, members, policies, audit events, and subscription capacity through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The remote installer command can execute code on the user's machine.

Mitigation: Prefer a reviewed official installation method with verification, and run an installer only when the oo CLI is missing and the user approves.

Risk: The skill routes sensitive Bitwarden organization requests through OOMOL as an intermediary.

Mitigation: Use the skill only when that intermediary is acceptable, and keep activity to the listed read-only Bitwarden actions unless the connector schema and user approval clearly support more.

Risk: Bitwarden organization responses can contain sensitive membership, policy, collection, and audit-event data.

Mitigation: Request the minimum necessary data, treat returned results as confidential, and avoid storing or sharing outputs unnecessarily.

## Reference(s):

- [Bitwarden homepage](https://bitwarden.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill fetches live connector schemas before running Bitwarden actions.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
