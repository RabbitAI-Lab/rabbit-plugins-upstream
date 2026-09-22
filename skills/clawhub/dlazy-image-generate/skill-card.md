## Description:

Image generation skill that selects an appropriate dLazy CLI image model based on the user's prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to route image-generation, image-editing, upscaling, background-removal, and vectorization requests to the dLazy CLI. It is intended for workflows that need generated image URLs, SVG/vector assets, transparent-background cutouts, or shell-command guidance for invoking the appropriate model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and local media paths may be sent to dLazy's cloud service for generation.

Mitigation: Do not submit private or sensitive prompts or files unless that use is acceptable for the user's dLazy account and organization.

Risk: Generated outputs are hosted by dLazy and may be accessible through returned media URLs.

Mitigation: Review generated URLs and content-handling expectations before sharing outputs outside the intended workflow.

Risk: The CLI may use stored API credentials and consume account credits.

Mitigation: Use scoped API keys, rotate or revoke keys from the dLazy dashboard when needed, and review commands before execution.

Risk: Global installation persists a dLazy CLI binary on the system.

Mitigation: Use the pinned npx invocation when a non-persistent install is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON CLI result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs from files.dlazy.com through the dLazy CLI.]

## Skill Version(s):

1.3.20 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
