## Description:

1MP raster image generation with refined design judgment for everyday creative work and fast iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to call the dLazy Recraft V4 image-generation CLI, submit prompts and aspect-ratio options, and receive generated image results or task status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly selected local media may be uploaded to dLazy's hosted API, and generated files are hosted by dLazy.

Mitigation: Use the skill only with content appropriate for a hosted image-generation service and avoid submitting sensitive prompts or media unless approved.

Risk: Using dlazy login or dlazy auth set stores an API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials when persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image outputs are returned as dLazy-hosted URLs and can be saved locally with the CLI save option.]

## Skill Version(s):

1.3.9 (source: release evidence; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
