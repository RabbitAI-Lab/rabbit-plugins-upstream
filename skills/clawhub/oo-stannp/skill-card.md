## Description:

Stannp helps agents manage Stannp recipients, recipient groups, account balance lookups, and address validation through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Stannp through an OOMOL-connected account, including recipient and group management, balance checks, and address validation. Users should confirm write and destructive actions before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include piping remote installer scripts directly into a shell without verification.

Mitigation: Prefer installing the oo CLI through a verified, pinned, or package-manager method before using the skill.

Risk: Write and destructive Stannp actions can create, modify, remove, or delete recipient and group data.

Mitigation: Review the exact action, target, and JSON payload with the user before approving write or destructive actions.

## Reference(s):

- [Stannp homepage](https://www.stannp.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-stannp)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
