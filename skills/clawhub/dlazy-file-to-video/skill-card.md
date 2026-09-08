## Description:

Converts PPT, Word, Excel, PDF, and other documents into explainer, report, courseware, or training videos by using the dLazy hosted file-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content teams, educators, and business users use this skill to turn source documents into video drafts or finished videos for explanations, reports, courseware, and training.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents are sent to dLazy's hosted service.

Mitigation: Install and use the skill only when the organization approves the dLazy vendor and the associated data flow; avoid uploading sensitive documents without approval.

Risk: The skill depends on a third-party CLI and hosted API.

Mitigation: Review the CLI source or use the npx invocation before adopting a persistent global installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference uploaded documents and dLazy project sessions when continuing multi-turn video work.]

## Skill Version(s):

1.3.13 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
