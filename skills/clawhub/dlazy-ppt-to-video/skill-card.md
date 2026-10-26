## Description:

Turns PowerPoint presentations into explainer, pitch, courseware, or training videos through dLazy’s file-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to turn PowerPoint or Keynote presentations into explainer, pitch, courseware, or training videos with dLazy’s hosted assistant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents are sent to dLazy services.

Mitigation: Use only content approved for third-party processing and confirm attachments may be shared before sending.

Risk: Video-generation tasks may consume organization credits.

Mitigation: Check available credits and expected usage before starting a task.

Risk: Project sessions retain context, and the CLI stores an API key in local configuration.

Mitigation: Review saved project context, protect the local configuration file, and rotate or revoke exposed keys.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted dLazy assistant performs the video-generation workflow and returns its results; project sessions can retain conversation context.]

## Skill Version(s):

1.0.30 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
