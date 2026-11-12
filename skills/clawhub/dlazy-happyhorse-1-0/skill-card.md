## Description:

Happy Horse 1.0 supports text-to-video, first-frame-to-video, reference-to-video, and video editing, routing each request to the matching mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to generate or edit videos from a text prompt, a first frame, reference images, or an existing video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is partial with medium confidence and notes that the inspected material emphasizes CLI authentication, which may not match the video-generation description.

Mitigation: Review the full skill and its installation instructions, and confirm that the authentication-focused commands fit the intended video-generation use before installation.

Risk: Prompts and local image or video inputs are sent to dLazy-hosted services; media may contain sensitive information.

Mitigation: Avoid submitting sensitive media unless its transfer to the service is approved, and review the service terms before use.

## Reference(s):

- [CLI project (metadata homepage/source)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package (metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video assets, JSON]

**Output Format:** [JSON result with hosted output URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is hosted by dLazy; local input media may be uploaded to the service.]

## Skill Version(s):

1.3.40 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
