## Description:

Helps segment people in video through dLazy's cloud service and obtain a black-and-white mask for compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Video editors, creators, and developers use this skill to request human segmentation masks for downstream video compositing and matting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos are sent to a cloud service, and authentication may store an API key locally.

Mitigation: Send only videos approved for cloud processing; protect and rotate the dLazy API key as needed.

Risk: The third-party CLI is installed or executed to process video, and the documented --prompt example does not match the listed --video option.

Mitigation: Review the package before use, prefer the on-demand npx option if a global install is undesirable, and use --video for video input.

## Reference(s):

- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The described command returns a mask result URL or, in asynchronous mode, a task ID; results can be saved locally.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
