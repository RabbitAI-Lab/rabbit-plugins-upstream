## Description:

Creates marketing, promotional, advertising, and brand video workflows from a product, brand, listing, or brief for social and campaign use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce sellers, and marketing teams use this skill to start or continue dLazy product-to-ecommerce-video projects for conversion-focused product ads and promotional videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, options, and explicitly attached files are sent to dLazy services.

Mitigation: Share only approved product, brand, and campaign materials, and avoid attaching sensitive files unless dLazy is approved for that data.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Use `DLAZY_API_KEY` for per-invocation credentials when local storage is not desired, and rotate or revoke organization keys when access changes.

Risk: Project-scoped chat sessions can reuse prior context.

Mitigation: Use separate projects for separate tasks and clear project context when previous session data should not influence future runs.

Risk: The workflow depends on a pinned third-party npm CLI package.

Mitigation: Confirm trust in dLazy and review the pinned `@dlazy/cli@1.2.3` package before installing or running the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-marketing-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Terminal text and Markdown-style guidance with shell command invocations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference dLazy project ids, project-scoped chat context, and files explicitly attached through the dLazy CLI.]

## Skill Version(s):

1.0.15 (source: ClawHub release evidence; artifact frontmatter declares 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
