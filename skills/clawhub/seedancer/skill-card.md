## Description:

Turns scripts into structured shot plans and prompts for AI video and image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taosiuman](https://clawhub.ai/user/taosiuman)

### License/Terms of Use:

MIT-0

## Use Case:

Filmmakers and creative teams use this Chinese-first workflow to analyze scripts, plan shots and assets, and prepare prompts for AI video and image services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project-local production state may include scripts and sensitive reference material.

Mitigation: Agree which project files the agent may read or write before starting.

Risk: Using external generation services may expose media or real-person likenesses.

Mitigation: Confirm the receiving service and permissions, obtain consent for real-person material, and share only necessary files.

Risk: External image and video generation may incur unexpected charges.

Mitigation: Set a budget and confirm costs before enabling paid generation.

## Reference(s):

- [Seedancer on ClawHub](https://clawhub.ai/taosiuman/skills/seedancer)
- [English overview](artifact/README.md)
- [Video prompt structure](artifact/references/cinedance-video-prompt.md)
- [Image prompt structure](artifact/references/lira-image-prompt.md)
- [Output formats](artifact/references/output-format.md)
- [Real-person asset safeguards](artifact/references/asset-whitelist.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured shot plans and generation prompts in Markdown, with optional bilingual JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces plans and prompts, not finished media; primarily Chinese-language output.]

## Skill Version(s):

10.0.1 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
