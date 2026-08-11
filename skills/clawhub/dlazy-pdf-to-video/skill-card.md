## Description:

PDF 转视频 PDF to Video helps agents drive dLazy's document-to-video workflow for PDF, presentation, report, courseware, and training-video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to create or continue dLazy file-to-video projects that turn PDFs and other documents into explainer, report, courseware, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and attached files to dLazy's hosted service, and the saved dLazy API key may not be protected as strongly as described.

Mitigation: Install only when hosted processing is acceptable; prefer per-run DLAZY_API_KEY use or check permissions on ~/.dlazy/config.json after login, and rotate or revoke the key if the machine is shared.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference dLazy project ids and responses returned by the dLazy CLI.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
