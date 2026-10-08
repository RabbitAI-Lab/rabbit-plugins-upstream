## Description:

Helps agents generate PixVerse C1 videos from text prompts, images, first and last frames, or reference images through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short PixVerse C1 videos from text or image inputs through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media may be sent to dLazy, and generated media is hosted by dLazy.

Mitigation: Share only content approved for the cloud provider and review hosted results before distribution.

Risk: Authentication stores a dLazy API key locally.

Mitigation: Protect the local configuration and revoke or rotate the key if it is exposed.

Risk: The broad video-generation trigger and globally installed CLI may lead to unintended invocation or package exposure.

Mitigation: Request PixVerse C1 explicitly and review the pinned npm package before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands and JSON result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service returns a hosted generated-media URL or an asynchronous task identifier; the CLI can save the result locally.]

## Skill Version(s):

1.2.27 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
