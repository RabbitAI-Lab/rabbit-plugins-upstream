## Description:

Generates images from text and edits or combines images using reference inputs through dLazy's hosted GPT Image 2 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from text prompts or edit and synthesize images using reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference files explicitly provided to the skill may be sent to dLazy, and generated images are hosted on dLazy storage.

Mitigation: Confirm the hosted service is appropriate for the content before submitting prompts or reference files.

Risk: Logging in can save an API key in local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key if it is exposed.

Risk: Installing the CLI globally keeps a third-party executable on the system.

Mitigation: Use the pinned on-demand npx command if a global install is not desired.

## Reference(s):

- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with image links and optional CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images are returned as hosted URLs and can optionally be saved locally; asynchronous requests may require polling.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
