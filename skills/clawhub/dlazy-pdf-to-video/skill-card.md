## Description:

pdf to video, pdf to explainer video, pdf to presentation video - parse the PDF, outline, storyboard, voiceover, build, validate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn PDFs and other documents into explainer, report, courseware, or training videos through the dLazy hosted file-to-video agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attached documents are uploaded to dLazy media storage when using --files.

Mitigation: Install and use this skill only when uploading the selected documents to dLazy is acceptable for the user's data sensitivity and policy requirements.

Risk: Authentication stores a dLazy API key in the local CLI configuration or uses DLAZY_API_KEY for per-invocation access.

Mitigation: Use the documented login or auth flow, protect the local config file, and rotate or revoke API keys from the dLazy dashboard when needed.

Risk: The skill depends on a third-party SaaS and the pinned @dlazy/cli package.

Mitigation: Review the pinned CLI package and source before installation, especially for sensitive documents or regulated workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce dLazy project commands and guidance for authentication, file upload, project continuation, and error handling.]

## Skill Version(s):

1.0.16 (source: ClawHub server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
