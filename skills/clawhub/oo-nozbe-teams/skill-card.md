## Description:

Enables agents to manage Nozbe teams, projects, tasks, and comments through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Nozbe teams, projects, tasks, and comments from an agent through an OOMOL-connected Nozbe account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can run an unverified remote installer on the user's machine.

Mitigation: Review the installer path before use and prefer a verified, pinned oo CLI installation method.

Risk: Write or destructive Nozbe actions can change or delete user data.

Mitigation: Check the exact target and payload, then require user confirmation for write actions and explicit approval for destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-nozbe-teams)
- [Nozbe homepage](https://nozbe.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger Nozbe API calls through the oo CLI; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
