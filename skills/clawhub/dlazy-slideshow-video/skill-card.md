## Description:

Turns slides or documents into narrated slideshow videos with voiceover and transitions through the dLazy hosted slideshow-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn PPT, PDF, document, image, or slide inputs into explainer, report, courseware, or training slideshow videos. The skill delegates generation to dLazy's hosted file-to-video workflow through the pinned dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or runs a third-party npm CLI and authenticates with a locally stored dLazy API key.

Mitigation: Install only when the publisher is trusted, keep the CLI pinned to the reviewed version, and rotate or revoke the API key from the dLazy dashboard if needed.

Risk: Prompts and files attached with --files are uploaded to dLazy services for processing.

Mitigation: Do not submit confidential or regulated content unless the user's organization has approved dLazy for that data.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-slideshow-video)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance, Files]

**Output Format:** [Terminal text and Markdown with inline shell commands; generated media files are produced by the hosted dLazy workflow.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; prompts and attached files are sent to dLazy services.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
