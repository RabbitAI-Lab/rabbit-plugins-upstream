## Description:

Helps agents segment people in video and obtain a black-and-white mask for compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request a human-segmentation mask for video compositing and matting through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an external CLI package may introduce unreviewed code.

Mitigation: Review the pinned @dlazy/cli@1.2.3 package before installation; use npx or a dry run rather than a global install when appropriate.

Risk: Selected media and parameters are sent to dLazy, and an API key may be saved locally.

Mitigation: Obtain permission before uploading sensitive media and protect or rotate the API key as needed.

Risk: The examples disagree about --video versus --prompt and whether the result is an image or video.

Mitigation: Check dlazy videoseg -h and verify the result type before running or using real jobs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns a hosted result URL or an asynchronous task ID; check the actual media type before use.]

## Skill Version(s):

1.3.24 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
