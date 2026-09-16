## Description:

Helps agents design controlled A/B tests for e-commerce listing main images, generate variant groups, record hypotheses, check listing-image compliance, and prepare a post-test review template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace sellers, e-commerce operators, and agents use this skill to plan one-variable main-image experiments, create comparable image variants, and capture the data needed for later conversion review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images, prompts, and generated outputs may be sent to external generation providers.

Mitigation: Use trusted local image files, avoid sensitive internal URLs or unreleased product imagery, and choose the provider deliberately before running generation.

Risk: Helper code can fetch arbitrary image URLs from the local runtime.

Mitigation: Avoid untrusted image URLs and run dry-run first when reviewing what the skill will send.

Risk: CLI and provider integrations may execute third-party code with access to local files and inherited credentials.

Mitigation: Review the installed CLI package and limit available credentials in the execution environment.

## Reference(s):

- [Platform Image Specifications](references/platform-specs.md)
- [Provider CLI Reference](references/provider-cli.md)
- [Platform Compliance Skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/platform-compliance/skill.md)
- [Brand Kit Skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands, generated image files, and optional JSON CLI output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes dry-run support and review templates that require users to fill in performance data after the experiment.]

## Skill Version(s):

1.0.7 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
