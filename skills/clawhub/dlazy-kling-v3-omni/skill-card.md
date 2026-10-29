## Description:

Generates videos with Kling v3 Omni from prompts and multimodal references such as images and videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can create Kling v3 Omni videos from text prompts and image or video references, with options for duration, aspect ratio, sound, and generation mode.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media provided for generation are sent to dLazy, and media files may be uploaded to its storage.

Mitigation: Submit only prompts and media you are comfortable sharing with the service.

Risk: Video generation may incur charges, and the saved organization API key grants access to the account’s API usage.

Mitigation: Check expected costs before generating, protect the key, and rotate or revoke it if exposed.

Risk: The skill relies on an external CLI package for requests and local file handling.

Mitigation: Review the pinned @dlazy/cli package before installing or invoking it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI repository link](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files, Media URLs, JSON task and result data]

**Output Format:** [JSON result envelope containing generated media URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is hosted by dLazy; results can be saved to a local path.]

## Skill Version(s):

1.3.34 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
