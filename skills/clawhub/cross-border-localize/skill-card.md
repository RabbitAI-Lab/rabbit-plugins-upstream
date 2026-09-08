## Description:

This skill helps agents localize e-commerce product assets for cross-border listings by producing regional copy, size-conversion guidance, marketplace image-generation commands, and compliance prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, e-commerce operators, and developers use the skill to adapt one product asset set for multiple regional marketplace channels, including localized copy, size tables, generated listing images, and platform checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and product images may be sent to the selected cloud generation provider.

Mitigation: Use only approved providers and avoid submitting sensitive product images or confidential listing material.

Risk: The helper scripts can fetch user-supplied image URLs and generated output URLs.

Mitigation: Prefer trusted local files or trusted public image URLs, and run the skill where sensitive internal HTTP services are not reachable.

Risk: Provider routing and custom provider endpoints can redirect generation requests based on configuration.

Mitigation: Review provider environment variables before use and set custom base URLs only for endpoints you control and trust.

Risk: Regional compliance labels and marketplace guidance are prompts and checks, not legal advice.

Mitigation: Verify final listings against current platform rules and local professional guidance before publishing.

## Reference(s):

- [Platform Image Specifications](artifact/references/platform-specs.md)
- [Provider CLI Reference](artifact/references/provider-cli.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/cross-border-localize)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, files]

**Output Format:** [Markdown guidance with inline shell commands; generation runs can save image files and emit JSON status envelopes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May send prompts and product images to the selected generation provider; platform checks can emit pass, warn, or reject-risk reports.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
