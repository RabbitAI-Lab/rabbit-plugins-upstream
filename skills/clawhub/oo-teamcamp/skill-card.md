## Description:

Teamcamp enables agents to read, create, and update Teamcamp data through the OOMOL-connected oo CLI instead of calling the Teamcamp API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Teamcamp workspaces from an agent, including retrieving projects, tasks, workspace users, and customers, and posting task comments after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts without verification.

Mitigation: Install the oo CLI only through a trusted method, preferably with version pinning or verification, and do not let an agent run the remote installer automatically.

Risk: The `post_task_comment` action changes Teamcamp state.

Mitigation: Confirm the exact task, payload, and expected effect with the user before sending a Teamcamp write action.

## Reference(s):

- [Teamcamp homepage](https://www.teamcamp.app)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Teamcamp skill listing](https://clawhub.ai/oomol/skills/oo-teamcamp)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; connector responses are JSON.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
