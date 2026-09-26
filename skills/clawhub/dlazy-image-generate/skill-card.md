## Description:

Image generation skill that automatically selects an appropriate dLazy CLI image model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate, edit, upscale, segment, vectorize, or replicate images through dLazy's hosted image models from natural-language prompts and optional reference media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and local media files explicitly passed to the CLI may be sent to dLazy's hosted service, and generated outputs may be hosted by dLazy.

Mitigation: Do not send private or sensitive reference files unless that data sharing is acceptable for the use case.

Risk: The dLazy CLI may store a paid-account API key in local configuration.

Mitigation: Use per-invocation environment authentication for temporary credentials when appropriate, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: The skill installs or runs a third-party npm CLI before contacting the hosted API.

Mitigation: Review the pinned package or listed source before trusting the CLI with credentials or private media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown with inline bash commands and JSON result URLs from the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned as hosted URLs; authentication uses a dLazy API key stored by the CLI or supplied per invocation.]

## Skill Version(s):

1.3.21 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
