## Description:

Helps agents separate subjects from image backgrounds and return a transparent-background image URL for product photos, portraits, and compositions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to cut out subjects from images for product listings, character assets, and compositing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images or local files supplied to the tool may be uploaded to dLazy, and generated images are hosted there.

Mitigation: Avoid submitting sensitive images unless dLazy hosting and processing are acceptable; review the pinned CLI package before use.

Risk: Authentication may save an API key in local configuration.

Mitigation: Use a per-invocation DLAZY_API_KEY when local key persistence is not desired.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown instructions with shell examples; tool response contains JSON with an image URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transparent PNG result URL; optional local download]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
