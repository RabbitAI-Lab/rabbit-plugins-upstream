## Description:

Run local Laya or Von typed classification, scoring, and true-or-false decisions through Decidealot REST or MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect to a trusted Decidealot endpoint, run bounded choice, score, or true-or-false decisions, and report probabilities or setup steps without treating model output as authority.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Decision results could be mistaken for authorization to perform irreversible or high-impact actions.

Mitigation: Treat model output as evidence only; keep authorization, final thresholds, and irreversible-action checks in the caller, with human review for costly mistakes.

Risk: Requests can contain user data and are sent to the configured Decidealot endpoint.

Mitigation: Use only trusted self-hosted endpoints, send data only to the endpoint the user named, and require an API key whenever traffic crosses a network boundary.

Risk: Long-lived Docker deployments that use the sample latest image tag can drift over time.

Mitigation: Pin production or durable deployments to a reviewed version tag or digest and keep the service loopback-bound unless authentication is configured.

## Reference(s):

- [Run and connect to Decidealot](references/setup.md)
- [Decidealot repository](https://github.com/psyb0t/decidealot)
- [Decidealot API guide](https://github.com/psyb0t/decidealot/blob/main/docs/api.md)
- [Decidealot deployment guide](https://github.com/psyb0t/decidealot/blob/main/docs/deployment.md)
- [MCP Streamable HTTP guide](https://github.com/psyb0t/decidealot/blob/main/docs/api.md#mcp-streamable-http)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON snippets, and decision results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bounded decision answers with probabilities, endpoint health checks, and setup steps; no ordinary file output is expected.]

## Skill Version(s):

0.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
