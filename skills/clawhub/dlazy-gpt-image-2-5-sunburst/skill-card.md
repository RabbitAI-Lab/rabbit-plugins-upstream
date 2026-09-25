## Description:

GPT Image 2.5 Sunburst generates and edits images through the dLazy CLI, supporting reference images, aspect ratios up to 21:9, and quality settings up to max.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to generate or edit images from prompts and optional reference images via the dLazy hosted image generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, parameters, and selected reference files to dLazy's hosted service.

Mitigation: Review prompts and file paths before invocation, and avoid sending confidential or regulated content unless the deployment has approved dLazy for that data.

Risk: Authentication may store a dLazy API key in the local CLI configuration.

Mitigation: Verify that the user trusts dLazy and the pinned npm package before installation, protect the local config file, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: The skill depends on dLazy network endpoints and a pinned npm CLI package.

Mitigation: Install only the pinned package version from a trusted npm source and confirm outbound access to api.dlazy.com and files.dlazy.com is acceptable for the environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-sunburst)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [JSON responses with generated image URLs, optional downloaded image files, and agent-facing command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return asynchronous task identifiers when invoked with no-wait behavior.]

## Skill Version(s):

1.2.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
