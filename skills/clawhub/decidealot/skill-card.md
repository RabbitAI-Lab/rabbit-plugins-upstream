## Description:

Run local Laya, Von, CLM, or hosted Jev typed decisions through Decidealot REST or MCP for bounded classification and scoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can request bounded choice, score, or true-or-false decisions, inspect the resulting probabilities, and set up a local or hosted Decidealot connection. The caller retains responsibility for thresholds and subsequent actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Decision inputs may contain sensitive data and be sent to an untrusted endpoint or onward to hosted Jev or an external embeddings service.

Mitigation: Use a trusted Decidealot endpoint and approve any data sent to hosted Jev or external embeddings before use.

Risk: An unauthenticated Decidealot service exposed beyond the local machine may accept unauthorized requests.

Mitigation: Keep local-only services bound to loopback and enable authentication whenever the service crosses a network boundary.

Risk: Using a mutable Docker image tag can change a long-running deployment unexpectedly.

Mitigation: Pin the image to an immutable version or digest for lasting deployments.

Risk: A model decision or probability may be mistaken for permission to take an irreversible action.

Mitigation: Keep authorization, action thresholds, and irreversible-action checks with the caller; request human review when mistakes are costly.

## Reference(s):

- [Decidealot on ClawHub](https://clawhub.ai/psyb0t/skills/decidealot)
- [Setup and connection guide](references/setup.md)
- [Decidealot API guide](https://github.com/psyb0t/decidealot/blob/main/docs/api.md)
- [Decidealot deployment guide](https://github.com/psyb0t/decidealot/blob/main/docs/deployment.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with decision results and probabilities, plus optional setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Decision outputs may include choice, score, or true-or-false results; the caller decides whether to act.]

## Skill Version(s):

0.7.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
