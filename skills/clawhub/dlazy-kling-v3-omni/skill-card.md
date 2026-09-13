## Description:

Versatile video generation with Kling v3 Omni, supporting text prompts and multi-modal image or video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's hosted Kling v3 Omni video-generation workflow from an agent, using prompts and optional media inputs to produce generated media URLs or saved outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, parameters, and selected local media files to dLazy's cloud API and media storage.

Mitigation: Only pass media intended for upload, and review dLazy as a cloud video-generation provider before installation or use.

Risk: The dLazy API key is stored in local CLI configuration or supplied through an environment variable.

Mitigation: Use scoped keys where available, rotate or revoke keys from the dLazy dashboard when needed, and avoid exposing DLAZY_API_KEY in logs or shared shells.

Risk: Global npm installation creates a persistent CLI binary on the host.

Mitigation: Prefer the documented npx invocation for temporary use, review the linked CLI source or package before installation, and avoid running npm as administrator or root.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs, asynchronous task identifiers, or saved files through the dLazy CLI.]

## Skill Version(s):

1.3.14 (source: server release evidence; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
