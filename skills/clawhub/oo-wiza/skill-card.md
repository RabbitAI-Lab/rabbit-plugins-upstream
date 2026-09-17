## Description:

Wiza (wiza.co) operations for reading, creating, and updating connected account data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents assisting users with Wiza account operations use this skill to inspect connector schemas, run read actions for credits, lists, reveals, and prospect searches, and start individual reveal workflows after payload confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Use a verified package manager when available, or download and inspect or verify the installer before running it.

Risk: The start_individual_reveal action changes Wiza account state.

Mitigation: Confirm the exact payload and intended effect with the user before executing the write action.

## Reference(s):

- [Wiza homepage](https://wiza.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wiza)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write actions require payload and effect confirmation.]

## Skill Version(s):

1.0.4 (source: server evidence release.version and SKILL.md frontmatter metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
