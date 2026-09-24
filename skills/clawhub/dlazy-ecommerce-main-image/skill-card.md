## Description:

This skill guides agents to create and edit e-commerce main-image candidates from approved product photos, covering white-background baselines, visual-difference images, social-commerce scenes, color SKU sets, and single-variable A/B tests while preserving product facts and channel constraints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, marketers, and developers use this skill to turn approved product photos into channel-ready main-image prompts and dLazy CLI commands for baseline images, SKU color sets, and controlled A/B test candidates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and image files passed with --images are uploaded to the dLazy hosted service.

Mitigation: Use only approved, non-sensitive product images and avoid private or unapproved product materials.

Risk: The CLI may save an API key locally and API use may consume credits.

Mitigation: Use --dry-run before batch jobs, protect the local CLI config, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

Risk: Generated main images can misrepresent product facts, claims, accessories, or platform compliance if prompts are underspecified.

Mitigation: Require approved product photos, explicitly list product attributes that must not change, avoid unsupported claims, and review outputs against the publication checklist before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-main-image)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Text]

**Output Format:** [Markdown guidance with bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces dLazy CLI invocations for hosted image generation; generated images are returned as hosted output URLs by the CLI/API.]

## Skill Version(s):

1.0.12 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
