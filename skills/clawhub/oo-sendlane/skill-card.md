## Description:

Sendlane (sendlane.com) skill for reading, creating, updating, and deleting Sendlane data instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Sendlane connector schemas and run Sendlane read, create, update, and delete actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run Sendlane write and delete actions that change or remove contact lists, tags, and custom fields.

Mitigation: Confirm the exact payload, target, and expected effect with the user before write actions, and require explicit approval before destructive actions.

Risk: Using the skill requires trusting OOMOL with the Sendlane integration and completing OOMOL CLI login and connection steps.

Mitigation: Install and authenticate the OOMOL CLI only when the user trusts OOMOL for this connector, and use first-time setup steps only after an auth or connection failure.

## Reference(s):

- [Sendlane homepage](https://www.sendlane.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Sendlane connection page](https://console.oomol.com/app-connections?provider=sendlane)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live connector schema inspection and JSON command responses from the oo CLI.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
