## Description:

Transforms flat-lay garment photos into dimensional ghost-mannequin product images while preserving visible garment details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, creative teams, and developers use this skill to convert qualifying flat-lay clothing photos into ghost-mannequin product shots with controlled volume, posture, collar depth, material detail, and output size.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected prompts and garment images may be sent to dLazy or another configured image provider.

Mitigation: Use non-sensitive product images, review the selected provider, and run dry-run mode before uploading or paying for generation.

Risk: Image inputs can point to local files or remote URLs, which can expose unintended files or fetch untrusted content.

Mitigation: Use explicit trusted image paths, avoid sensitive directories, and avoid untrusted image URLs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/to-3d)
- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Model Flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands; command execution can save JPEG image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses image inputs and prompts with a selected image-generation provider; dry-run mode can preview provider, prompt, paths, and estimated cost.]

## Skill Version(s):

1.0.6 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
