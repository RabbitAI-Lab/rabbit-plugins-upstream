## Description:

Run local Laya, Von, CLM, or hosted Jev typed decisions through Decidealot REST or MCP for bounded classification and scoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Decidealot to request bounded choices, scores, and true-or-false assessments from local models or a configured hosted model. The skill also guides endpoint setup, Docker deployment, and model management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Decision state may be sent to an untrusted endpoint or hosted Jev.

Mitigation: Use a trusted Decidealot endpoint and obtain approval before sending sensitive state to hosted Jev.

Risk: An exposed Decidealot service may accept unauthorized requests.

Mitigation: Set authentication when exposing the service beyond loopback.

Risk: A mutable Docker image tag can change between deployments.

Mitigation: Pin the Docker image to a version tag or digest.

## Reference(s):

- [Decidealot setup guide](references/setup.md)
- [Decidealot API guide](https://github.com/psyb0t/decidealot/blob/main/docs/api.md)
- [Decidealot deployment guide](https://github.com/psyb0t/decidealot/blob/main/docs/deployment.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with JSON examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports typed decisions and probabilities; the caller determines thresholds and subsequent actions.]

## Skill Version(s):

0.7.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
