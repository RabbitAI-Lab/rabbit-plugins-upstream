## Description:

Generates cinematic product or brand ad video clips from a product description or photo using the Ofox video API, including a creative brief, timestamped prompt, cost estimate, submission, polling, download, and cost report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to turn product descriptions or product images into commercial-style brand ad clips with guided creative choices, cost estimates, and generated video outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback install guidance can install many unreviewed ofoxai skills and agent integrations instead of only the needed dependency.

Mitigation: Review before installing and install only ofox-video-core from a trusted, pinned source unless a broader install is intentional.

Risk: The skill can upload product images, unreleased branding, and sensitive ad copy to Ofox for video generation.

Mitigation: Avoid sending confidential product images, unreleased branding, or sensitive copy unless the user accepts that data being processed by Ofox.

Risk: Video generation may incur cost or continue running after a local timeout.

Mitigation: Show the cost estimate before submission and poll an existing job ID after timeout rather than re-running generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/seedance-ad-creative)
- [Skill homepage](https://github.com/ofoxai/skills/tree/main/skills/seedance-ad-creative)
- [Ofox app and API keys](https://app.ofox.ai)
- [Ofox model catalog](https://api.ofox.ai/v1/models/catalog)
- [ofox-video-core safety contract](../ofox-video-core/SKILL.md)
- [ofox-video-core prompt structure](../ofox-video-core/references/prompt-structure.md)
- [ofox-video-core creative brief](../ofox-video-core/references/creative-brief.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown with creative brief, prompt text, cost table, inline bash commands, and generated video file references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit jobs through ofox-video-core and download generated video assets with JSON sidecars after user approval.]

## Skill Version(s):

1.13.3 (source: frontmatter, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
