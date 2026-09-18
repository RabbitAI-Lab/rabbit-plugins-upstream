## Description:

Provides Honeycomb support for reading, creating, and updating data through the OOMOL-connected Honeycomb connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Honeycomb datasets, boards, markers, and authentication metadata, and to create Honeycomb markers through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions run downloaded installer scripts directly in Bash or PowerShell.

Mitigation: Install the oo CLI from a verified, version-pinned, signed source or official package manager before using the skill.

Risk: Honeycomb marker creation changes Honeycomb state.

Mitigation: Confirm the exact action payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-honeycomb)
- [Honeycomb Homepage](https://www.honeycomb.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute Honeycomb connector actions through the oo CLI when used by an agent.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
