## Description:

A comprehensive generation skill that routes image, video, and audio requests to the appropriate dLazy CLI model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or transform images, videos, audio, and speech by selecting and invoking dLazy CLI models from natural-language intent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media files are sent to dLazy-hosted services.

Mitigation: Use only media and prompts you are authorized to submit, and avoid uploading sensitive content unless the deployment has approved that data flow.

Risk: Voice cloning features can upload voice samples and create synthetic speech.

Mitigation: Require clear consent from the speaker before uploading voice samples or generating cloned voices.

Risk: Using dlazy login may save an API key in the local CLI configuration.

Mitigation: Prefer DLAZY_API_KEY for ephemeral credentials when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Broad activation triggers can route requests to many different media-generation models.

Mitigation: Review the selected model, command, and uploaded file arguments before execution, especially for paid or externally hosted generation jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media URLs are returned by dLazy-hosted services; authentication uses a dLazy API key.]

## Skill Version(s):

1.3.7 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
