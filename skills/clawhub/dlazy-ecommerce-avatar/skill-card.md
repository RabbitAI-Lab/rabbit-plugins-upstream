## Description:

Guides an agent through creating e-commerce livestream avatar and AI spokesperson videos with base-portrait recipes, scripts, text-to-speech, avatar driving, B-roll, and assembly guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and commerce teams use this skill to plan and generate reusable digital-human product-selling videos for TikTok Shop, Douyin, Amazon, Shopee, and brand stores. It helps agents produce prompts, CLI commands, payload examples, and production guidance for the Dlazy avatar workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads product images, prompts, audio, and generated media to Dlazy services.

Mitigation: Install and run it only when the user trusts the Dlazy CLI and is comfortable sending those inputs to the listed Dlazy service endpoints.

Risk: Generation commands can spend paid credits, and incorrect parameters or over-limit prompts can fail after request submission.

Mitigation: Use dry-run where available, check current model flags before building commands, and review estimated costs before running generation.

Risk: The Dlazy API key may be stored locally or supplied through an environment variable.

Mitigation: Keep ~/.dlazy/config.json and DLAZY_API_KEY protected, and avoid exposing credentials in prompts, logs, or shared artifacts.

Risk: E-commerce claims and synthetic-avatar content may violate advertising rules or platform disclosure requirements.

Mitigation: Review generated scripts for prohibited claims, avoid false credentials or medical efficacy claims, and disclose AI-generated content where required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-avatar)
- [Dlazy homepage](https://dlazy.com)
- [Skill overview](artifact/SKILL.md)
- [Pipeline guide](artifact/pipeline.md)
- [Portrait recipes](artifact/recipes.md)
- [Troubleshooting guide](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Dlazy CLI command plans, prompt recipes, local file-path conventions, and production checks for avatar-video workflows.]

## Skill Version(s):

1.0.9 (source: server release evidence; artifact frontmatter version is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
