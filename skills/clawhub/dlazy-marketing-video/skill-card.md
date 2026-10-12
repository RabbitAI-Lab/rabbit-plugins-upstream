## Description:

Creates promotional shopping videos from product details, listings, or briefs for social media and advertising campaigns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to turn product information or storefront listings into promotional videos for ecommerce and social campaigns, with optional multilingual voiceover and a virtual host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy's hosted service.

Mitigation: Review content before submission and attach only files you intend to share.

Risk: A third-party CLI uses saved API credentials.

Mitigation: Review the pinned CLI before installation and rotate or revoke the dLazy API key if needed.

Risk: Continuing an existing project can reuse prior session context.

Mitigation: Start a new project for unrelated work and continue an existing one only intentionally.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-marketing-video)
- [dLazy CLI source (listed in release metadata; skill provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Video links]

**Output Format:** [Streaming text response with generated video references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Videos are created through a hosted service; project sessions can retain context across requests.]

## Skill Version(s):

1.0.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
