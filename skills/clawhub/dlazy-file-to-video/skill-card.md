## Description:

ppt to video, word to video, excel to video, pdf to video, document to video — parse, outline, storyboard, voiceover, build, validate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, educators, and training teams use this skill to send documents to the dLazy hosted agent and generate explainers, report broadcasts, courseware, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attached local documents are uploaded to dLazy's hosted service before processing.

Mitigation: Only attach documents suitable for upload to dLazy, and review organizational data-handling requirements before use.

Risk: The skill relies on a third-party CLI that can be installed globally or run through npx.

Mitigation: Review the dLazy CLI source before installing, and use the pinned npx command when avoiding a persistent global install is preferred.

Risk: Authentication uses a dLazy API key that may be stored in the user's local CLI configuration.

Mitigation: Use normal OS user-level file protections and rotate or revoke the API key from the dLazy dashboard when needed.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include project-scoped dLazy CLI commands and guidance for authentication, file attachment, and session continuation.]

## Skill Version(s):

1.3.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
