## Description:

Convert static images into dynamic videos using Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use the CLI to turn still images into short videos with Vidu Q2, configuring prompts, reference images or first and last frames, duration, aspect ratio, resolution, and optional audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial: it did not inspect the external CLI or confirm the advertised conversion behavior. The documented workflow sends prompts and local media to dLazy-hosted services and requires an API key.

Mitigation: Review the pinned CLI installation and authentication steps, verify its behavior before use, and provide only credentials and media appropriate for the hosted service.

## Reference(s):

- [CLI project page listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Media URLs, JSON result metadata, Shell commands]

**Output Format:** [CLI commands and JSON result metadata with media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill documents image-to-video output, but the security scan did not confirm conversion behavior. Local media inputs are uploaded to dLazy-hosted storage.]

## Skill Version(s):

1.3.42 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
