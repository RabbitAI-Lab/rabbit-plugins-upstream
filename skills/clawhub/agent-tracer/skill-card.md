## Description:

Record every tool call into agent-tracer (self-hosted FastAPI), then run regression testing (golden case -> drift detection), attribute token costs by tool/model/agent, and surface recurring error root causes across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wholegale39](https://clawhub.ai/user/wholegale39)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to instrument agent runs, record tool-call traces, promote successful runs into golden cases, check future runs for drift or regression, attribute token costs, and aggregate recurring errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tracer records raw agent arguments, results, and errors in a persistent service, which can expose secrets, personal data, or sensitive business context.

Mitigation: Redact secrets and personal data before recording spans, classify trace data as sensitive logs, and define retention and deletion rules before using it with real agent runs.

Risk: The tracing service can expose recorded agent activity if it is reachable on an unprotected network.

Mitigation: Keep the service bound to localhost or a protected private network, and add authentication and TLS before exposing it beyond the host.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wholegale39/skills/agent-tracer)
- [agent-tracer repository link from skill content](https://github.com/wholegale39/agent-tracer)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include curl examples for creating traces, recording spans, checking drift, summarizing costs, and aggregating errors.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
