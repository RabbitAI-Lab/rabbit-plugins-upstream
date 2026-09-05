## Description:

Video human segmentation tool that invokes Aliyun SegmentVideoBody through the dLazy CLI and returns a same-length black-and-white mask video for downstream compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to run cloud video human segmentation from an agent workflow and obtain a mask video that can be used in compositing or matting pipelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos passed to the skill are uploaded to the third-party dLazy cloud service for processing.

Mitigation: Review data sensitivity and only submit media approved for third-party cloud processing.

Risk: Authentication stores a local dLazy API key for CLI use.

Mitigation: Use the documented dLazy login or auth flow, keep the key scoped to the intended organization, and rotate or revoke it from dLazy when needed.

Risk: Generated output URLs are hosted by dLazy media storage.

Mitigation: Handle returned URLs as third-party hosted assets and apply the user's retention, sharing, and access-control requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs or save generated mask video files locally when requested.]

## Skill Version(s):

1.3.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
