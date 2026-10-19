## Description:

Helps developers configure and operate Peen for coding-agent work in Docker workspaces, including project rules, WebSocket sessions, and stored work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to set up a provider and project workspace, send and follow coding-agent tasks, and inspect or control persistent sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recommended installer executes mutable remote shell code and starts a controller with Docker-level impact.

Mitigation: Review the installer before execution and use a version-pinned release or inspected installer instead of the curl-to-bash command.

Risk: Agents can modify accessible projects and expose secrets through retained transcripts.

Mitigation: Open only projects the agent may modify, keep credentials outside agent-readable workspaces, and account for retained sessions and transcripts.

Risk: An exposed controller without authentication can allow unauthorized access to agent sessions.

Mitigation: Set PEEN_API_TOKEN before non-local exposure and use encrypted connections.

## Reference(s):

- [Peen release on ClawHub](https://clawhub.ai/psyb0t/skills/peen)
- [Setup, providers, WebSocket, and REST](references/setup.md)
- [Deployment](https://github.com/psyb0t/peen/blob/main/docs/deployment.md)
- [Where it runs](https://github.com/psyb0t/peen/blob/main/docs/where-it-runs.md)
- [API reference](https://github.com/psyb0t/peen/blob/main/docs/http-api.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide changes to workspace configuration and session state.]

## Skill Version(s):

0.26.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
