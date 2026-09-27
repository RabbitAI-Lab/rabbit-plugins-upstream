## Description:

A comprehensive generation skill that routes image, video, and audio generation requests to the appropriate dLazy CLI model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images, videos, and audio through dLazy's hosted CLI-backed media generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files may be sent to dLazy's hosted service.

Mitigation: Use the skill only for content you intend to send to dLazy, and avoid passing private local files unless upload is expected.

Risk: The dLazy CLI can store an API key in a local configuration file.

Mitigation: Prefer DLAZY_API_KEY for temporary use on shared machines, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [ClawHub publisher profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash commands and generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the selected dLazy model and may include hosted image, video, or audio URLs.]

## Skill Version(s):

1.3.21 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
