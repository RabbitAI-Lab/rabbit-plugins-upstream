## Description:

Run local Laya, Von, CLM, or hosted Jev typed decisions through Decidealot REST or MCP for bounded classification and scoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Decidealot to request bounded choice, score, or true-or-false decisions from a configured local or hosted model, and to set up and connect to the service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Decision data may be sent to configured hosted or embeddings providers.

Mitigation: Confirm data-sharing permissions and use only trusted endpoints before selecting those providers.

Risk: Exposed services or leaked bearer tokens may permit unauthorized requests.

Mitigation: Keep tokens out of tracked files and shell history; use authentication and exact Host/Origin settings when exposing the service beyond loopback.

Risk: A mutable container image tag may change between deployments.

Mitigation: Pin an immutable Docker image tag or digest.

Risk: A model decision may be mistaken for authorization to take a consequential action.

Mitigation: Keep authorization and action thresholds with the caller, and route costly uncertainty to human review.

## Reference(s):

- [ClawHub release](https://clawhub.ai/psyb0t/skills/decidealot)
- [Setup guide](references/setup.md)
- [API guide](https://github.com/psyb0t/decidealot/blob/main/docs/api.md)
- [Deployment guide](https://github.com/psyb0t/decidealot/blob/main/docs/deployment.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with decision results and optional command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports typed decisions and probabilities; the caller controls any resulting action.]

## Skill Version(s):

0.6.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
