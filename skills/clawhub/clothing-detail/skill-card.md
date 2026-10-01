## Description:

Guides the creation of close-up clothing detail images from product photos for e-commerce listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and product creators use the skill to create close-up views of visible fabric textures, seams, and garment construction from existing clothing photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to a configured cloud provider.

Mitigation: Use only approved providers and avoid confidential designs unless their terms permit uploads.

Risk: Generation can incur charges and uses provider credentials.

Mitigation: Check the request and estimated cost with dry-run first; keep API keys scoped and revocable.

Risk: Close-ups can depict garment details that are not visible in the source photo.

Mitigation: Start with clear, unobstructed source images and review each result against the original before publication.

## Reference(s):

- [Model flags](references/model-flags.md)
- [Provider CLI and data flow](references/provider-cli.md)
- [dLazy CLI source and usage](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Images]

**Output Format:** [Markdown instructions and generated image files (JPEG, PNG, or WebP)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Square or portrait close-ups; optional local save path and batch generation.]

## Skill Version(s):

1.0.15 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
