## Description:

Guides agents through generating and editing e-commerce main-image candidates from approved product photos, including white-background baselines, visual-difference images, content-commerce scenes, color SKU sets, and single-variable A/B test variants while preserving product facts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and agents preparing e-commerce listings use this skill to create image-generation prompts and dLazy CLI commands for product main images and controlled A/B image tests. The workflow emphasizes approved source product photos, platform rule checks, and avoiding unsupported product claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approved product photos and prompts may be sent to dLazy hosted services when generated commands are executed.

Mitigation: Use only product images cleared for the intended listing workflow and confirm that the merchant is comfortable with dLazy API and media-storage processing before execution.

Risk: Running generated commands may consume dLazy credits.

Mitigation: Run banana-pro with --dry-run first when estimating payload and cost, and use npx or pinned CLI installation paths when tighter execution control is needed.

Risk: Generated main images can misrepresent products if source images, prompt constraints, or platform rules are incomplete.

Mitigation: Require approved product photos, preserve SKU facts in the prompt, check unsupported claims and platform rules, and review outputs before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-main-image)
- [dlazyai publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and CLI configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce dLazy banana-pro commands that upload approved product images and consume dLazy credits when executed.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
