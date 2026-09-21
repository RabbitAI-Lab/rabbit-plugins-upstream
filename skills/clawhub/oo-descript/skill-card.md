## Description:

Descript (descript.com). Use this skill for ANY Descript request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Descript through an OOMOL-connected account, including listing projects and jobs, importing URL-hosted media, prompting Underlord, publishing compositions, and managing Descript jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform write actions in Descript, such as importing media or prompting Underlord to create or edit projects.

Mitigation: Confirm the exact action payload and expected effect with the user before running write actions.

Risk: The skill can perform destructive actions, including canceling jobs and publishing or republishing compositions.

Mitigation: Require explicit approval for the target resource and operation before running destructive actions.

Risk: The connected Descript account or workspace determines what the agent can access.

Mitigation: Connect only the Descript account or workspace intended for agent use and review OOMOL connection status before granting access.

## Reference(s):

- [ClawHub Descript skill page](https://clawhub.ai/oomol/skills/oo-descript)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Descript homepage](https://www.descript.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Configuration guidance]

**Output Format:** [Markdown with inline bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
