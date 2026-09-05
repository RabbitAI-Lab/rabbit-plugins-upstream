## Description:

多单品融合成一整套 Look。最多 8 张单品图 → 同一模特身上的完整搭配商拍图，每件单品保真。当用户说「多件搭配」「融图」「组一套 look」「搭配图」「几件衣服合成一张」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, creative teams, and developers use this skill to turn up to eight product images into a complete outfit photo on one model, with prompts and shell commands for repeatable commercial product imagery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected product, model, or reference images may be sent to dLazy or another configured cloud image provider.

Mitigation: Use the skill only with images approved for the selected provider, and avoid private local files or internal URLs as image inputs.

Risk: Cloud generation can consume credits or call external services when run without dry-run.

Mitigation: Use dry-run to check cost and routing before paid execution.

Risk: Provider credentials are required for some routes and could expose account access if over-privileged.

Mitigation: Use scoped, revocable API keys and rotate or revoke them when no longer needed.

## Reference(s):

- [seedream-5.0 parameter reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/image-fusion)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands and saved image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call cloud image providers, support dry-run cost checks, and save generated image files locally.]

## Skill Version(s):

1.0.5 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
