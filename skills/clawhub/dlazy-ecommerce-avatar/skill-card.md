## Description:

Guides agents through creating ecommerce livestream avatar videos with the dLazy CLI, including base portrait recipes and a script, TTS, avatar, B-roll, and assembly workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and ecommerce operators use this skill to produce product-selling digital human videos for TikTok Shop, Douyin, Amazon, Shopee, or brand storefronts. It helps choose a reusable base portrait, generate segmented scripts and TTS audio, drive avatar clips, create product B-roll, and assemble deliverable vertical video assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, audio, and generated media are sent through dLazy's third-party service.

Mitigation: Review data-sharing expectations before use and avoid sending content that cannot be processed by that service.

Risk: A dLazy API key may be stored locally for CLI authentication.

Mitigation: Store the key only in the documented CLI configuration or environment variable and rotate it if local access is shared or compromised.

Risk: Video generation can consume paid credits, and failed or invalid requests may still affect cost.

Mitigation: Use dry runs, confirm current CLI flags, segment audio within documented limits, and estimate credit usage before production runs.

Risk: Ecommerce avatar videos may be subject to advertising rules and AI-content disclosure requirements.

Mitigation: Review platform and regional advertising requirements, avoid unsupported product claims, and disclose AI-generated content where required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-avatar)
- [dLazy homepage](https://dlazy.com)
- [Skill overview](artifact/SKILL.md)
- [Pipeline guide](artifact/pipeline.md)
- [Portrait recipes](artifact/recipes.md)
- [Troubleshooting and compliance notes](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with bash commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the dLazy CLI through npm or npx; may use DLAZY_API_KEY for authentication.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
