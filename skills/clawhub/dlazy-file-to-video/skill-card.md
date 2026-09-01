## Description:

Converts documents such as PPT, Word, Excel, and PDF files into explainer, report, courseware, or training videos through the dLazy file-to-video template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to send documents to the dLazy hosted file-to-video workflow and receive a project-scoped video generation process for explainers, report broadcasts, courseware, or training materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document contents, prompts, and attached files are sent to dLazy hosted services during normal use.

Mitigation: Use the skill only with documents the user is authorized to upload, and confirm organizational approval before sending sensitive or regulated content.

Risk: Authentication may store a dLazy API key in local CLI configuration.

Mitigation: Use per-invocation credentials such as DLAZY_API_KEY when local persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include project-scoped continuation instructions and references to uploaded user files.]

## Skill Version(s):

1.3.9 (source: server release evidence; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
