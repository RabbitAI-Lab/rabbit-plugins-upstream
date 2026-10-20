## Description:

Helps agents segment people in video into a black-and-white mask for compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Video editors and developers use this skill to obtain human-segmentation masks for video compositing or matting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video or media files are uploaded to dLazy for cloud processing.

Mitigation: Confirm that the selected media may be shared with the service before submitting it.

Risk: The third-party CLI uses a dLazy API key that may be stored locally.

Mitigation: Review the CLI before installation and rotate or revoke the key from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI source linked in release metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return a hosted result URL or an asynchronous task ID.]

## Skill Version(s):

1.3.33 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
