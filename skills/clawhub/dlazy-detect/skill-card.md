## Description:

Detects whether image, video, or audio media appears AI-generated, including visual deepfake signals and likely generator attribution, and returns confidence scores for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to check images, videos, or audio clips for AI-generated media signals through the dLazy CLI. It is suited for media authenticity screening, deepfake review, and generator-attribution workflows where confidence scores are interpreted by a human or downstream policy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local image, video, or audio paths may be uploaded to dLazy-hosted media storage for analysis.

Mitigation: Prefer public URLs when practical, avoid sensitive or regulated media unless the user accepts dLazy data handling, and confirm before passing local files to the CLI.

Risk: Broad trigger terms such as "detect" could cause unintended invocation.

Mitigation: Clarify the user's intent and media target before running detection, especially before uploading a local file.

Risk: The skill returns confidence scores rather than a definitive ground truth.

Mitigation: Treat the output as a screening signal and apply human review or policy thresholds before taking consequential action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-detect)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [JSON detection results plus a human-readable text summary and Markdown command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include AI-generated confidence, deepfake confidence, likely generator attribution, media type, and async task status when requested.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
