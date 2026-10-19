## Description:

Uses dLazy's video segmentation service to create human-subject mask videos for compositing and matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video editors use this skill to request human-subject segmentation of a video and obtain a mask for downstream compositing or matting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos and parameters are sent to dLazy's cloud service.

Mitigation: Upload only videos you are authorized to share and review the service terms before use.

Risk: The external CLI requires an API key and may be installed globally or store the key locally.

Mitigation: Review the CLI before use; consider the documented pinned npx invocation and a per-invocation DLAZY_API_KEY instead of a global install or saved key.

Risk: The usage example names --prompt while command help names --video, and the sample image output conflicts with the described video mask.

Mitigation: Check live command help and verify the returned asset type before using it in a video workflow.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include a hosted result URL or an asynchronous task ID.]

## Skill Version(s):

1.3.32 (source: ClawHub release metadata; skill frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
