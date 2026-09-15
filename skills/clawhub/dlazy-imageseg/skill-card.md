## Description:

Image matting tool: separates foreground from background and returns a transparent-background image URL for product image processing, character cutout, and composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content-production agents use this skill to invoke dLazy image segmentation for removing image backgrounds and returning hosted transparent PNG outputs. It is suited for product imagery, character cutouts, and image-composition workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images supplied as local paths are uploaded to dLazy-hosted storage for processing.

Mitigation: Only submit images that are appropriate for upload to the dLazy service and avoid sensitive or regulated content unless the user's policy permits it.

Risk: The skill requires a dLazy API key and stores or accepts credentials for CLI use.

Mitigation: Use a revocable API key, prefer per-invocation environment variables or protected local config, and rotate or revoke the key when the tool is no longer needed.

Risk: Using a globally installed npm CLI can increase local persistence and supply-chain exposure.

Mitigation: Prefer pinned, temporary execution with npx where practical and review the linked CLI source and npm package before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source link from metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to run the dLazy CLI and may return hosted image URLs or async task identifiers.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
