## Description:

GPT Image 2.5 Sunburst, the precision tier of OpenAI's GPT Image 2.5 series, supports text-to-image generation and image editing with reference images, aspect ratios up to 21:9, and quality up to max.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate or edit images through the dLazy CLI, including workflows that need reference images, precise composition, in-image text, wide aspect ratios, or high quality output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill executes external npm code through the dLazy CLI.

Mitigation: Review and trust the @dlazy/cli package and dLazy service before installation; use npx or another isolated install path if a persistent global binary is not desired.

Risk: Prompts and selected local media files are sent to dLazy-hosted endpoints for cloud image generation.

Mitigation: Avoid submitting sensitive content unless the dLazy service terms and data handling meet the intended use case.

Risk: The workflow uses a dLazy API key stored in local CLI configuration or supplied through an environment variable.

Mitigation: Use a revocable API key and rotate or revoke it from the dLazy dashboard when access should change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-sunburst)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI can return generated image URLs, downloaded image files when --save is used, or an asynchronous task identifier when --no-wait is used.]

## Skill Version(s):

1.2.4 (source: release metadata; artifact frontmatter and CLI install spec reference 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
