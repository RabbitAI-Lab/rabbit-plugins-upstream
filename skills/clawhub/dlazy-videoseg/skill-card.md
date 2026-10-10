## Description:

Helps agents segment people in videos and obtain black-and-white masks for compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request a person-segmentation mask for a video and use the result in compositing or matting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provided videos may be uploaded to dLazy's cloud service.

Mitigation: Confirm the user permits cloud processing before submitting sensitive videos.

Risk: Logging in may store a dLazy API key locally.

Mitigation: Protect local credentials and use a per-invocation API key when persistent storage is inappropriate.

Risk: Examples disagree with command options and describe an image result for a video task.

Mitigation: Check the installed CLI's help and actual result before following examples or processing the output.

Risk: The skill installs a third-party npm CLI package.

Mitigation: Review the package and linked source before installation when supply-chain assurance is required.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown guidance and CLI commands; the CLI returns JSON with a hosted result URL or asynchronous task ID.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A mask asset can be downloaded to a local path using the CLI's save option.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata; skill frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
