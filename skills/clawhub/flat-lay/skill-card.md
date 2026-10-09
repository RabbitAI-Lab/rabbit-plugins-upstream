## Description:

Turns garment flat-lay and pose reference images into on-model product photos for e-commerce.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use garment photos and pose references to generate on-model catalog images, including multi-garment looks and optional consistent model references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and uploaded images, including model face references, are sent to the selected cloud image provider.

Mitigation: Use only images you own or have permission to use; avoid unauthorized likenesses and confirm the selected provider before uploading.

Risk: Image generation can spend provider credits and produce imperfect garment or likeness details.

Mitigation: Run --dry-run to check provider, model, inputs, estimated cost, and save path; review generated images before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/flat-lay)
- [Provider setup and output reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [dLazy CLI documentation and source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [JPEG, PNG, or WebP images; Markdown guidance and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images can be saved locally; visually check garment details and model likeness before use.]

## Skill Version(s):

1.0.18 (source: ClawHub release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
