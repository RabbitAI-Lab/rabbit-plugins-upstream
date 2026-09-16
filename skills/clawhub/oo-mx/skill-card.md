## Description:

MX (mx.com) lets agents read, create, update, and delete MX Platform API user data through an OOMOL-connected account using the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage MX Platform API users through OOMOL-connected MX accounts, including listing, reading, creating, updating, and deleting users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote shell installer commands that can run unverified code.

Mitigation: Install the oo CLI only from a trusted, verified, pinned, or package-manager path before using the skill.

Risk: Create, update, and delete actions can change or remove MX user data.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write or destructive commands.

## Reference(s):

- [MX homepage](https://www.mx.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub MX skill page](https://clawhub.ai/oomol/skills/oo-mx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live schema inspection before action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
