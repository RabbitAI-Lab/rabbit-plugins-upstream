## Description:

文件转视频 File to Video uses the dLazy CLI and hosted service to help agents turn PPT, Word, Excel, PDF, and other documents into explainer, report, courseware, or training video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they have a document and want an agent-assisted workflow for generating an explainer, report broadcast, courseware, or training video through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents are sent to dLazy hosted services.

Mitigation: Avoid uploading sensitive documents unless dLazy's terms fit the user's needs.

Risk: Authentication may save a dLazy API key in the local CLI configuration.

Mitigation: Use per-invocation credentials when appropriate and rotate or revoke the API key from the dLazy dashboard if needed.

Risk: A global CLI install persists an executable on the user's system.

Mitigation: Use the pinned npx invocation when a persistent global CLI is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and streamed CLI text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference project ids and uploaded file URLs returned by the dLazy hosted service.]

## Skill Version(s):

1.3.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
