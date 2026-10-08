## Description:

Helps agents use the dLazy CLI to segment people in video and obtain a mask video for compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use this skill to request person-segmentation masks from video through dLazy and prepare the results for compositing or matting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running a third-party cloud CLI executes external software.

Mitigation: Review the pinned npm package and linked repository before installation.

Risk: Local media supplied to the CLI may be uploaded to dLazy endpoints.

Mitigation: Use only media authorized for upload to a third-party service.

Risk: Logging in persists an API key in local CLI configuration.

Mitigation: Store the key only if acceptable; otherwise pass it per invocation through DLAZY_API_KEY.

Risk: The documented --prompt example and image output disagree with the listed video option and mask-video purpose.

Mitigation: Check the CLI help and actual result type before relying on examples or downstream processing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides asynchronous retrieval or saving of a segmentation mask video; actual media is returned by the external service.]

## Skill Version(s):

1.3.27 (source: server-resolved release; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
