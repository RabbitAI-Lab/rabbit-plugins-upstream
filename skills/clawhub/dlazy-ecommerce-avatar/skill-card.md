## Description:

Guides agents through creating ecommerce livestream avatar videos with base-portrait recipes, scripts, TTS, avatar driving, B-roll, and assembly steps for platforms such as TikTok Shop, Douyin, Amazon, Shopee, and brand stores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams, creators, and marketing operators use this skill to plan repeatable AI spokesperson workflows for product-selling videos, from reusable avatar portraits through voice, driven talking-head clips, product B-roll, and final assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on the third-party dLazy CLI and service, including API-key authentication and processing of product images, prompts, audio, and video files.

Mitigation: Install only if the dLazy CLI and service are trusted, use a revocable API key, avoid administrator/root execution, and avoid sending sensitive assets unless approved for third-party processing.

Risk: Generated ecommerce videos can contain unsupported product claims, platform policy issues, or missing AI-content disclosure.

Mitigation: Review scripts, visuals, and final videos against applicable advertising rules, marketplace policies, and AI-content labeling requirements before publishing.

Risk: Avatar-driving quality can fail when base portraits have obstructed mouths, multiple faces, poor lighting, high hand positions, or incompatible clip specifications.

Mitigation: Use the documented portrait constraints, run dry runs where available, segment long audio, and re-encode clips to a common video and audio specification during assembly.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-avatar)
- [dLazy Homepage](https://dlazy.com)
- [Skill Overview](artifact/SKILL.md)
- [Pipeline Guide](artifact/pipeline.md)
- [Base Portrait Recipes](artifact/recipes.md)
- [Troubleshooting and Compliance Notes](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces dLazy CLI command plans and cautions; generated media is produced by the dLazy service, not by the skill itself.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
