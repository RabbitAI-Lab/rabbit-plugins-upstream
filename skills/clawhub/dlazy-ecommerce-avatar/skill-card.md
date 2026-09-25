## Description:

Ecommerce livestream avatar / AI spokesperson for product selling videos, with base-portrait recipes and a script-to-TTS-to-avatar-to-B-roll workflow for product selling videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and developers use this skill to plan and generate reusable digital-human product selling videos for platforms such as TikTok Shop, Douyin, Amazon, Shopee, and brand stores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends prompts, product details, media assets, and optional API credentials to dLazy services.

Mitigation: Use the skill only with approved dLazy accounts, avoid placing unrelated secrets in prompts or media, and manage DLAZY_API_KEY through the documented configuration or environment variable path.

Risk: Generated ecommerce videos can contain incorrect advertising claims or miss required AI-content disclosures.

Mitigation: Review product claims, prohibited wording, visual representations, and platform AI-disclosure requirements before publishing.

Risk: Model parameter limits, duration limits, and mismatched media formats can cause failed jobs, wasted credits, or broken final video assembly.

Mitigation: Use dry runs when uncertain, keep scripts segmented within the documented duration and prompt limits, and re-encode final video assets to a common format before assembly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-avatar)
- [dLazy homepage](https://dlazy.com)
- [Skill overview](artifact/SKILL.md)
- [Pipeline](artifact/pipeline.md)
- [Recipes](artifact/recipes.md)
- [Troubleshooting](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent through recipe selection, dLazy CLI commands, media-generation constraints, and video assembly checks.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter version is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
