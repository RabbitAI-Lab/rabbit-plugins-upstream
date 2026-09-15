## Description:

Businessmap helps an agent read, create, update, and delete Businessmap boards and cards through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Businessmap workspaces, boards, and cards from an agent session while relying on OOMOL-mediated Businessmap access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can run unverified remote installer code on the user's machine.

Mitigation: Review the setup path first and run installer commands only after verifying the installer source and integrity through a safer channel.

Risk: Write and destructive Businessmap actions can change or permanently delete user data.

Mitigation: Confirm the exact Businessmap object, payload, and intended effect with the user before running write or delete actions.

Risk: Businessmap access is mediated by OOMOL rather than handled directly by the agent.

Mitigation: Use the skill only when the user is comfortable with OOMOL mediating Businessmap access.

## Reference(s):

- [Businessmap homepage](https://businessmap.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Skill page](https://clawhub.ai/oomol/skills/oo-businessmap)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON-formatted connector responses from Businessmap actions.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
