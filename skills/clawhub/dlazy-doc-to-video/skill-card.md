## Description:

Turns user-provided documents into explainer, report, courseware, or training videos by using the dLazy CLI to run the hosted file-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill when they have a Doc, Word, Markdown, PDF, PPT, or spreadsheet document and want an explainer, report broadcast, courseware, or training video. The skill guides an agent to authenticate with dLazy, start or continue a file-to-video project, attach local files when needed, and handle common CLI/API errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy services for processing.

Mitigation: Review files before upload and avoid sending sensitive content unless the user's dLazy organization policies permit it.

Risk: Authentication can persist a dLazy API key in the local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY or npx when avoiding persistent credentials or global installation is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide an agent to call the pinned dLazy file-to-video template, pass prompts and file attachments, and continue project-scoped sessions.]

## Skill Version(s):

1.0.10 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
