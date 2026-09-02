## Description:

Ecommerce livestream avatar / AI spokesperson for product selling videos — 18 production-grade base-portrait recipes plus the full script→TTS→avatar→B-roll pipeline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and marketing teams use this skill to plan and produce AI avatar product-selling videos for TikTok Shop, Douyin, Amazon, Shopee, and brand-store workflows. It guides base portrait generation, segmented scripts, TTS, avatar driving, B-roll, and final assembly choices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends product images, prompts, audio, and generated media through the dLazy cloud service.

Mitigation: Use only when the user is comfortable with that external service path, and review account, API-key, and data-handling requirements before production use.

Risk: The workflow depends on stored dLazy credentials and may use the DLAZY_API_KEY environment variable.

Mitigation: Keep API keys out of prompts, logs, and committed files; use the documented dLazy authentication flow or environment variable handling.

Risk: Ecommerce avatar videos can trigger advertising compliance or AI-generated-content disclosure obligations.

Mitigation: Review platform disclosure rules and advertising claims before publishing, especially for regulated or high-risk product categories.

Risk: The documented media generation pipeline can consume paid dLazy credits, especially for avatar driving and retries.

Mitigation: Use dry runs and segmented generation, confirm command flags, and review expected credit costs before running production jobs.

## Reference(s):

- [Skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-avatar)
- [dLazy homepage](https://dlazy.com)
- [recipes.md](artifact/recipes.md)
- [pipeline.md](artifact/pipeline.md)
- [troubleshooting.md](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline bash commands and model parameter recipes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing workflow guidance; generated media is created by external dLazy CLI/API calls, not by the skill text itself.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
