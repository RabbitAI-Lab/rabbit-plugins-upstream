## Description:

Okta helps authorized agents read and manage Okta users, groups, memberships, and lifecycle actions through an OOMOL-connected Okta account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

IT administrators, developers, and authorized operators use this skill to inspect Okta action schemas and manage Okta users, groups, memberships, and account lifecycle operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform sensitive Okta identity administration, including user lifecycle, group membership, write, and destructive actions.

Mitigation: Confirm the exact target, payload, and expected effect before any write or destructive action, and use an Okta connection with the narrowest practical permissions.

Risk: The documented setup path includes unverified remote installer commands.

Mitigation: Install the oo CLI through a trusted, versioned, integrity-verified method before using the skill in an administrative Okta environment.

## Reference(s):

- [ClawHub Okta skill](https://clawhub.ai/oomol/skills/oo-okta)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Okta homepage](https://www.okta.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Okta action names, schema inspection commands, connector run commands, and confirmation prompts for write or destructive operations.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
