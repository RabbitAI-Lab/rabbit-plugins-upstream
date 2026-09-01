## Description:

Converts flat-lay garment photos into ghost-mannequin style 3D product images with realistic volume while preserving color, material, pattern, and garment proportions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers, catalog teams, and agents use this skill to turn single-garment flat-lay photos into dimensional product images without using human models. It provides prompt guidance and CLI commands for generating product imagery through dLazy or another configured image provider.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected garment photos, prompts, and reference images may be sent to dLazy or the configured image provider.

Mitigation: Use only inputs appropriate for the selected provider, avoid sensitive local files and internal/private URLs, and confirm provider choice before execution.

Risk: Generation may incur cost or use an unintended provider when credentials and defaults are not checked.

Mitigation: Run dry-run or doctor checks first when cost, provider choice, or credentials matter.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/to-3d)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy product site](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Image files]

**Output Format:** [Markdown guidance with CLI commands; generated outputs are JPEG image files when executed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run cost checks, provider selection, reference images, batch generation, square or portrait output sizes, and local file saving.]

## Skill Version(s):

1.0.3 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
