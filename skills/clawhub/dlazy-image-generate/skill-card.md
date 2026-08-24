## Description:

Image generation skill that helps an agent choose and run an appropriate dLazy CLI image model based on the user's prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to generate, edit, upscale, segment, vectorize, or replicate images through the dLazy CLI. It is intended for image-production workflows where the agent selects a suitable model and issues the corresponding command.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files may be sent to dLazy cloud services for generation or processing.

Mitigation: Review prompt text and file paths before execution, and avoid sending confidential or regulated media unless that use is approved.

Risk: The dLazy CLI can store an API key in the local user configuration.

Mitigation: Use npx or per-invocation DLAZY_API_KEY when a persistent global binary or saved key is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Generation requests consume dLazy account credits and depend on third-party hosted APIs.

Mitigation: Confirm account authorization and credit availability before relying on the skill in a workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and dLazy CLI JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs hosted by dLazy services.]

## Skill Version(s):

1.3.9 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
