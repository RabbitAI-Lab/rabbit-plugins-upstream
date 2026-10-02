## Description:

Helps agents segment people in videos through dLazy's hosted service and obtain black-and-white mask videos for compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use this skill to request human segmentation of a video and obtain a same-length mask video for downstream editing or compositing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local videos are uploaded to dLazy for processing.

Mitigation: Submit only videos approved for upload to this external service.

Risk: Installing and running the external CLI executes third-party software.

Mitigation: Review the CLI before installation; use the pinned on-demand npx command if a persistent global binary is not desired.

Risk: Login or manual authentication may store an API key locally.

Mitigation: Protect the local credentials and rotate or revoke the key when it is no longer needed.

Risk: The documented prompt flag and image response example conflict with video segmentation usage.

Mitigation: Check the CLI's video option and actual response instead of relying on those examples.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command examples and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Describes asynchronous results and optional saving of the generated mask video.]

## Skill Version(s):

1.3.25 (source: server-resolved ClawHub release; artifact frontmatter states 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
