## Description:

Video human segmentation tool that invokes Aliyun's asynchronous SegmentVideoBody service through the dLazy CLI and returns a same-length black-and-white mask video for compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run dLazy video human segmentation on a video URL or local video path, producing a mask video for downstream compositing or matting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends video inputs to dLazy cloud endpoints for processing and stores generated output URLs on dLazy-hosted file storage.

Mitigation: Only pass videos that are appropriate for upload to dLazy's cloud service, and review the service terms before processing sensitive content.

Risk: The release security summary notes inconsistent command and output examples in the documentation.

Mitigation: Confirm the real dLazy videoseg CLI syntax and expected output type with the pinned CLI before relying on an automated workflow.

Risk: The dLazy API key is stored in local CLI configuration or supplied through the environment.

Mitigation: Use OS user permissions for the config file and rotate or revoke the API key when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown instructions with bash command examples and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns hosted output URLs and can save result assets locally with --save; async mode may return a generateId for polling.]

## Skill Version(s):

1.3.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
