## Description:

Video human segmentation tool that invokes Aliyun's async SegmentVideoBody through dLazy and returns a same-length black/white mask video for downstream compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content-production agents use this skill to submit a video to dLazy's hosted video segmentation workflow and retrieve a black/white mask video for compositing or matting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos and parameters are sent to dLazy/Aliyun-backed cloud processing.

Mitigation: Use the skill only with media approved for third-party cloud processing and avoid submitting sensitive content unless the user's organization permits it.

Risk: Authentication uses a dLazy organization API key that may be stored in local CLI configuration.

Mitigation: Prefer npx or DLAZY_API_KEY for less persistent setup when appropriate, restrict local config permissions, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Global CLI installation persists a pinned third-party executable on the system.

Mitigation: Use the pinned npx invocation when a non-persistent CLI is preferred, and review the dLazy CLI package before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a hosted result URL, a downloaded mask video when --save is used, or an async generateId when --no-wait is used.]

## Skill Version(s):

1.3.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
