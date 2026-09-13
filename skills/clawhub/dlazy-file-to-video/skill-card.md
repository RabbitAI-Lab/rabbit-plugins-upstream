## Description:

Converts PPT, Word, Excel, PDF, and other documents into explainer, report, courseware, or training video workflows through dLazy's hosted file-to-video agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to turn source documents into project-scoped video generation tasks, including explainers, report broadcasts, courseware, and training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a pinned npm CLI and depends on a third-party package supply chain.

Mitigation: Prefer on-demand npx use when possible and review the package or source before installation.

Risk: Selected documents, prompts, and attached files are sent to dLazy hosted services.

Mitigation: Avoid uploading sensitive documents unless dLazy's service terms and data handling fit the user's requirements.

Risk: The dLazy API key is stored locally or supplied through an environment variable.

Mitigation: Rotate or revoke the API key when it is no longer needed and keep local credential files protected.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate dLazy CLI calls that stream hosted agent responses and upload user-selected files to dLazy media storage.]

## Skill Version(s):

1.3.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
