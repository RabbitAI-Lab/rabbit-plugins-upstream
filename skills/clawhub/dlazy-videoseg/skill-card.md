## Description:

Uses the dLazy cloud CLI to segment people in video and return a black-and-white mask video for compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use this skill to request person segmentation and obtain a mask video for downstream compositing or matting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an external npm CLI.

Mitigation: Review the CLI package and its permissions before installation.

Risk: Selected video or media inputs are sent to dLazy cloud services.

Mitigation: Only submit media authorized for external processing.

Risk: Authentication may save an API key locally.

Mitigation: Use DLAZY_API_KEY per run when local key storage is undesirable.

Risk: Some documented command examples appear stale.

Mitigation: Confirm supported options with dlazy videoseg -h before running a request.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI repository (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Text]

**Output Format:** [Markdown guidance and CLI JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service returns a mask-video result link or an asynchronous task ID; results may be saved locally.]

## Skill Version(s):

1.3.23 (source: server release metadata; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
