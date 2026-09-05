## Description:

Diagnose MCP HTTP 401/405 fallback errors by isolating credentials, transport, and runtime interpolation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to diagnose MCP HTTP authentication failures, especially confusing 401 responses followed by fallback or SSE-related 405 errors. It helps isolate credential drift, transport assumptions, and runtime environment interpolation without exposing credential values.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Troubleshooting may involve configured MCP endpoints and credentials.

Mitigation: Use the skill only with servers and credentials you are authorized to troubleshoot, and capture status or protocol responses without printing token values.

Risk: Fallback or SSE-related 405 errors can distract from the first authentication failure.

Mitigation: Resolve and verify the primary MCP initialize request before treating later fallback statuses as the root cause.

## Reference(s):


## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with diagnostic steps and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Emphasizes status/protocol evidence and avoids printing credential values.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
