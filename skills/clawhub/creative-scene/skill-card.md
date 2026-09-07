## Description:

Creates image-generation prompts and commands for original creative scenes or targeted model, pose, and styling edits from a short description and optional reference image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and commerce operators use this skill to turn scene descriptions or reference images into repeatable creative-scene generation prompts and commands for product and editorial imagery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unsafe Ark endpoint override could send an Ark API key and image-generation inputs to an arbitrary URL.

Mitigation: Use the Ark backend only with a trusted ARK_BASE_URL, and leave ARK_BASE_URL unset unless the endpoint has been reviewed.

Risk: Prompt files, brand files, and reference images may be uploaded to selected cloud generation providers.

Mitigation: Provide only generation inputs and reference images that are intended for the selected provider, and review provider choice before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/creative-scene)
- [Provider CLI Reference](references/provider-cli.md)
- [banana-pro Model Flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands; helper scripts can emit JSON and save generated image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run cost checks, optional reference images, provider selection, and configurable output paths.]

## Skill Version(s):

1.0.6 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
