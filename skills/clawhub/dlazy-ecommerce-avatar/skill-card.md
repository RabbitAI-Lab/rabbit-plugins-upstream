## Description:

Ecommerce livestream avatar / AI spokesperson for product selling videos, with 18 base-portrait recipes and a script-to-TTS-to-avatar-to-B-roll workflow for product-selling videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and marketing teams use this skill to plan and generate digital-human product-selling videos for TikTok Shop, Douyin, Amazon, Shopee, brand stores, and similar channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses a third-party npm CLI and sends prompts, product media, and generated content to dLazy API endpoints.

Mitigation: Install only from trusted dLazy package sources, run from a non-elevated shell, and use scoped or revocable API keys where available.

Risk: The workflow can consume paid model credits, and incorrect parameters or unsuitable source images can waste credits.

Mitigation: Run dry-runs before paid calls, validate model-specific size and duration limits, and review base portraits against the artifact's drivability checklist before generation.

Risk: Avatar videos and ecommerce claims may require platform-specific AI-content disclosure and advertising compliance review.

Mitigation: Review scripts and visuals for prohibited claims or misleading credentials, and apply required AI-generated-content disclosures before publishing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-avatar)
- [dLazy Homepage](https://dlazy.com)
- [dLazy API Key Dashboard](https://dlazy.com/dashboard/organization/api-key)
- [dLazy Credits Settings](https://dlazy.com/dashboard/organization/settings?tab=credits)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to produce prompts, CLI commands, payload files, troubleshooting steps, and assembly guidance for ecommerce avatar video workflows.]

## Skill Version(s):

1.0.8 (source: ClawHub release evidence; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
