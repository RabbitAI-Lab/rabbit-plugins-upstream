## Description:

Image generation skill. Automatically selects the best dlazy CLI image model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can create or edit images from prompts and reference images, then use the returned media URLs in later workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference media are sent to dLazy's hosted service, and the security review was partial because some referenced items were unavailable.

Mitigation: Avoid submitting sensitive prompts or media unless approved for the service; review the specific command and inputs before use.

Risk: The examples extend into video and speech workflows in addition to image generation.

Mitigation: Review the selected command and model before execution, and use only the media workflow needed for the request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Generated image and vector media URLs, JSON result envelopes, Shell commands, Configuration instructions]

**Output Format:** [JSON result envelopes containing hosted output URLs, with shell commands and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; local media supplied as input may be uploaded to dLazy storage.]

## Skill Version(s):

1.3.39 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
