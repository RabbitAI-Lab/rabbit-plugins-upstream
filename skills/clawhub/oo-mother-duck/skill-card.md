## Description:

MotherDuck (motherduck.com). Use this skill for ANY MotherDuck request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to administer MotherDuck through an OOMOL-connected account, including inspecting action schemas, listing account and token information, managing users, creating or deleting tokens, and updating Duckling configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that can execute arbitrary code.

Mitigation: Review the install path before use and prefer a version-pinned, checksum- or signature-verified oo CLI installation method.

Risk: Write actions can create users, create tokens, or change Duckling configuration.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running state-changing actions.

Risk: Destructive actions can invalidate access tokens or permanently delete a MotherDuck user and their data.

Mitigation: Require explicit approval for the target and action before running destructive operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mother-duck)
- [MotherDuck homepage](https://motherduck.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
