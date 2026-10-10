## Description:

Configure and operate Peen, a durable coding-agent backend, including provider setup, Docker workspaces, WebSocket turns, project rules, and session management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to set up and operate Peen for coding work in a chosen workspace, manage project instructions, and inspect or control persistent sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup uses an unpinned Docker image that could change between deployments.

Mitigation: Trust the publisher and image, review the image before installation, and pin it to a reviewed digest.

Risk: The agent can access mounted projects and credentials available to its environment.

Mitigation: Mount only the intended project workspace, keep credentials minimal, and do not mount the Docker socket or sensitive directories.

Risk: Remote access and persistent transcripts can expose session content.

Mitigation: Set PEEN_API_TOKEN before non-local use, use TLS for remote access, and protect the state directory where transcripts and logs persist.

## Reference(s):

- [Peen skill release](https://clawhub.ai/psyb0t/skills/peen)
- [Setup, providers, WebSocket, and REST](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with shell, configuration, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include Docker and WebSocket setup steps; review commands before execution.]

## Skill Version(s):

0.17.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
