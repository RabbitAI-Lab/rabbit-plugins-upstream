## Description:

Generates images by automatically selecting a suitable dLazy CLI model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators can use this skill to generate or transform images with dLazy hosted models, choosing a model based on the requested task and prompt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy hosted services, and local media inputs are uploaded for processing.

Mitigation: Keep sensitive files out of generation inputs and review the service terms before sending media.

Risk: The service requires an API key and generation can spend account credits.

Mitigation: Protect the API key, rotate or revoke it when needed, and use the pinned CLI installation command.

## Reference(s):

- [dLazy](https://dlazy.com)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Image assets, SVG graphics, JSON]

**Output Format:** [Generated asset URLs in a JSON result envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return multiple generated outputs; image, video, and audio inputs may be uploaded for hosted processing.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
