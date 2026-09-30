## Description:

Use Decidealot REST or MCP to obtain local, typed classification, scoring, and true-or-false decisions with probabilities from configured Laya, Von, or CLM providers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query a trusted Decidealot service for bounded decisions and probabilities, inspect available models, or set up a local deployment. The caller retains responsibility for thresholds and consequential actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Decision probabilities may be mistaken for authorization to take consequential actions.

Mitigation: Keep authorization and final thresholds with the caller; seek human review for costly or irreversible actions.

Risk: Requests can disclose user data to the Decidealot service or a configured CLM embeddings endpoint.

Mitigation: Use only trusted endpoints and avoid sending sensitive data to services you do not control.

Risk: An exposed or mutable container deployment can increase access and update risk.

Mitigation: Bind the service to loopback or require an API key, and pin the Docker image to an immutable version or digest.

## Reference(s):

- [Decidealot on ClawHub](https://clawhub.ai/psyb0t/skills/decidealot)
- [Setup and connection guide](references/setup.md)
- [Decidealot API guide](https://github.com/psyb0t/decidealot/blob/main/docs/api.md)
- [Decidealot deployment guide](https://github.com/psyb0t/decidealot/blob/main/docs/deployment.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with decision results, probabilities, and optional commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typed choice, score, or true-or-false results; deployment and model-management guidance when requested.]

## Skill Version(s):

0.5.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
