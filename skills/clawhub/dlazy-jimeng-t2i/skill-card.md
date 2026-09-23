## Description:

Text-to-image generation with Jimeng that helps agents convert prompts into high-quality generated images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images from text prompts through the dLazy Jimeng text-to-image CLI. It can also use up to 10 reference image URLs or local paths when the user chooses to provide them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation parameters, and supplied media paths may be sent to dLazy cloud services.

Mitigation: Use only when the user accepts dLazy cloud processing, and avoid sending sensitive prompts or media unless that use is approved.

Risk: Local media paths passed as inputs may be uploaded to files.dlazy.com for model access.

Mitigation: Review local file paths before invocation and confirm that uploaded media is appropriate for third-party processing.

Risk: The dLazy CLI may store an API key in the local user configuration.

Mitigation: Prefer per-invocation credentials or protect and rotate the API key using dLazy account controls.

Risk: Global installation of the npm CLI persists executable code on the system.

Mitigation: Prefer the pinned npx invocation or review the pinned npm package before global installation.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON response with generated image URLs, optional downloaded image files, and brief agent guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run mode, asynchronous generation IDs, polling, timeout control, and saving generated assets to a local path.]

## Skill Version(s):

1.3.19 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
