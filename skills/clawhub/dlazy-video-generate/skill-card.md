## Description:

Generates videos from text prompts and supplied media using a dLazy video-generation model selected for the request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can create video clips from text prompts, images, and frame references. The skill selects a suitable dLazy-supported model and returns generated media results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are uploaded to dLazy-hosted services for generation.

Mitigation: Only submit media you are comfortable processing through the hosted service.

Risk: The CLI can store an organization API key in a local configuration file.

Mitigation: Use environment-variable authentication when appropriate, protect local credentials, and rotate or revoke keys if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)
- [dLazy CLI project listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [Generated video assets returned with hosted URLs and JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cloud-generated media; available options and results depend on the selected model and request.]

## Skill Version(s):

1.4.34 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
