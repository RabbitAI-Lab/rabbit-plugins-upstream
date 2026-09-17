## Description:

This skill lets an agent operate Amplemarket through the OOMOL oo CLI to read account, contact, lead list, and task data and complete or skip tasks with confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Amplemarket account, contact, lead list, task type/status, and task data, and to complete or skip Amplemarket tasks through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change Amplemarket task state by completing or skipping tasks.

Mitigation: Require explicit user confirmation of the exact payload and expected effect before running any state-changing action.

Risk: Setup guidance includes CLI installation and account connection paths.

Mitigation: Use verified oo CLI installation steps and only run setup or connection commands after an authentication or connection failure.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-amplemarket)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Amplemarket](https://www.amplemarket.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON connector responses from Amplemarket actions.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
