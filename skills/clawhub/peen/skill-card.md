## Description:

Configure and operate Peen, the durable coding-agent backend. Use when setting up a provider and Docker workspace, sending work over WebSocket, adding project harness rules, or inspecting and controlling durable sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use Peen to configure a provider and workspace, send tasks to a coding agent, and inspect or control durable sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security analysis flags setup instructions that pipe a mutable remote installer into Bash and exceed the stated permissions; the analysis is incomplete.

Mitigation: Review the installer and its filesystem changes, and use a reviewed, pinned release or commit before running it.

Risk: A Peen agent has direct shell and filesystem access to its configured workspace.

Mitigation: Open only projects the operator is willing to let the agent change, and avoid exposing credentials or unnecessary host directories.

## Reference(s):

- [Setup and use](references/setup.md)
- [API reference](https://github.com/psyb0t/peen/blob/main/docs/http-api.md)
- [Where Peen runs](https://github.com/psyb0t/peen/blob/main/docs/where-it-runs.md)
- [Deployment](https://github.com/psyb0t/peen/blob/main/docs/deployment.md)
- [Recovery and continuation](https://github.com/psyb0t/peen/blob/main/docs/agents.md#recovery-after-a-crash)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, API calls]

**Output Format:** [Markdown with inline shell, JSON, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.47.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
