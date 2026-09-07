## Description:

Generates ecommerce item detail image modules with Chinese typography from product images and concise selling points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, designers, and agents use this skill to turn a product image and short selling points into ready-to-use Chinese item-detail modules such as banners, icon rows, material blocks, detail closeups, and parameter sections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and generated assets may be sent to the selected cloud provider.

Mitigation: Use only approved providers for the intended data, avoid sensitive or unauthorized product assets, and review provider data handling before execution.

Risk: Helper code includes broad provider-routing and credential-handling paths.

Mitigation: Verify provider environment variables before running, prefer scoped and rotated API keys, and use documented dry-run or doctor checks before paid generation.

Risk: Untrusted image URLs can expose users to unsafe or unintended remote content handling.

Mitigation: Prefer local files or trusted public image hosts and avoid passing untrusted image URLs.

Risk: Watermark-removal guidance may be misused on assets the user does not own.

Mitigation: Use the workflow only for assets the user owns or has explicit permission to edit.

## Reference(s):

- [Provider CLI Reference](artifact/references/provider-cli.md)
- [seedream-5.0-pro Model Flags](artifact/references/model-flags.md)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/item-detail)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown instructions with bash command examples and JSON-capable CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to save generated ecommerce image modules to local files through selected cloud image providers; dry-run and batch generation options are documented.]

## Skill Version(s):

1.0.6 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
