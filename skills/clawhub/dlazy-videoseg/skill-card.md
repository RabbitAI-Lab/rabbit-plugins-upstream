## Description:

Video human segmentation tool: invokes Aliyun's async SegmentVideoBody and returns a same-length black/white mask video, suitable for downstream compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and media-production agents use this skill to submit a video to dLazy's hosted video segmentation service and receive a same-length black-and-white mask video for compositing or matting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-supplied media paths may be uploaded to the dLazy cloud service for processing.

Mitigation: Use the skill only with media that is appropriate for upload to dLazy, and review the service terms before processing sensitive content.

Risk: Authentication may store a dLazy API key in the local CLI configuration.

Mitigation: Prefer per-invocation credentials or rotate and revoke organization API keys when access changes.

Risk: A persistent global CLI install may be undesirable in tightly controlled environments.

Mitigation: Use the documented npx invocation when a non-persistent CLI run is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown with bash examples and JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can return hosted output URLs, asynchronous task identifiers, or saved local result files when the CLI save option is used.]

## Skill Version(s):

1.3.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
