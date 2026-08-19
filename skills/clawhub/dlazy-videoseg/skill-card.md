## Description:

Video human segmentation tool that invokes Aliyun's asynchronous SegmentVideoBody service through dLazy and returns a same-length black-and-white mask video for compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to run cloud-hosted human video segmentation and obtain mask-video outputs for downstream compositing, matting, or editing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input videos, parameters, and generated outputs may be processed or hosted by dLazy cloud services.

Mitigation: Use the skill only with videos and parameters appropriate for dLazy cloud processing, and review organizational data-handling requirements before use.

Risk: The skill requires a dLazy API key, which may be stored in a local CLI configuration file.

Mitigation: Use the per-run DLAZY_API_KEY environment variable when local key persistence is undesirable, and rotate or revoke keys through the dLazy dashboard when needed.

Risk: Submitted documentation has command and output inconsistencies.

Mitigation: Run dlazy videoseg -h and verify the current command arguments before executing a paid or production request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; selected input videos and parameters may be sent to dLazy cloud services, and generated outputs may be returned as hosted URLs.]

## Skill Version(s):

1.3.9 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
