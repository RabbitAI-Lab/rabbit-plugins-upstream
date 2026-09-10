## Description:

Converts PDFs and other documents into explainer, report, courseware, or training videos by using dLazy to parse content, create outlines and storyboards, generate voiceover, build the video, and validate the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they have a PDF or document and want a narrated explainer, report broadcast, courseware asset, or training video generated through the dLazy hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents are sent to dLazy services and attached local files are uploaded to dLazy media storage.

Mitigation: Use the skill only with documents intended for upload to dLazy, and avoid confidential files unless that third-party processing is acceptable.

Risk: The dLazy CLI stores an API key locally or accepts it through DLAZY_API_KEY.

Mitigation: Use the documented login or auth flow, protect the local config file, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Global CLI installation persists third-party executable code on the system.

Mitigation: Prefer the pinned npx invocation or a restricted environment for occasional use, and review the CLI source or package before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides invocation of the dLazy CLI, including project continuation, file attachment, authentication, and common error handling.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
