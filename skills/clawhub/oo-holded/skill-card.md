## Description:

Use Holded through an OOMOL-connected account to read contacts and products and create basic contacts via the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Holded account data from an agent, including listing or retrieving contacts and products and creating basic contacts after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer snippets include pipe-to-shell commands.

Mitigation: Verify the installer source and trust the publisher before running those snippets.

Risk: Holded request data and responses are routed through OOMOL.

Mitigation: Use the skill only when that routing is acceptable for the user's Holded data.

Risk: Write actions can change Holded state.

Mitigation: Confirm the exact payload and expected effect with the user before running any write action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-holded)
- [Holded Homepage](https://www.holded.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON responses that include data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
