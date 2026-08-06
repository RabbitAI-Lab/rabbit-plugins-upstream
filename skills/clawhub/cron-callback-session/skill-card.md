## Description:

Helps OpenClaw and QClaw agents design session callbacks where cron jobs, external processes, or another session use sessions_send to inject messages into a target session so the agent can continue with its existing context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[onesfuture](https://clawhub.ai/user/onesfuture)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use this skill to route scheduled job results, external process updates, or cross-session handoffs back into an OpenClaw or QClaw conversation. It provides guidance for checking session visibility, configuring callbacks, restarting the gateway when needed, and verifying delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broadening session visibility can allow messages to be injected into other sessions under the configured scope.

Mitigation: Install only when cross-session callbacks are needed, prefer visibility=agent, avoid wildcard cross-agent routing, and restore visibility=tree after use.

Risk: Gateway restarts can interrupt active sessions, cron jobs, or other ongoing work.

Mitigation: Restart the gateway only when interrupting active sessions is acceptable, and verify callback delivery after the restart.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/onesfuture/skills/cron-callback-session)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell, PowerShell, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational instructions; it does not generate executable artifacts by itself.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata; artifact frontmatter lists 1.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
