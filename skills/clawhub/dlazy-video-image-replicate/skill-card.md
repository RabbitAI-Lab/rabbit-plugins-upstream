## Description:

Helps recreate the look and structure of a reference image or video using the user's own subject, product, or characters through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use this skill to remake a reference image or video with their own subjects through a project-based dLazy session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached reference media are sent to dLazy's hosted service.

Mitigation: Send only material approved for third-party processing.

Risk: The dLazy API key is saved locally or supplied through an environment variable.

Mitigation: Protect the key, avoid including it in prompts, and rotate or revoke it if exposed.

Risk: Project sessions retain context across turns.

Mitigation: Use a fresh project or clear the session before sensitive work.

Risk: Running the pinned third-party CLI introduces a package dependency.

Mitigation: Review the pinned @dlazy/cli package and source before use in sensitive environments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-image-replicate)
- [dLazy CLI source (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Streaming text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project sessions can retain conversation context across turns.]

## Skill Version(s):

1.3.23 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
