## Description:

Converts PPT, PowerPoint, Keynote, and other documents into explainer, pitch, courseware, or training videos through the dLazy hosted file-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn slide decks or documents into explainer, report, courseware, pitch, or training videos by invoking the dLazy CLI and hosted file-to-video template.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and attached documents to the third-party dLazy service.

Mitigation: Use it only for content intended for dLazy processing, and avoid attaching sensitive files unless upload to that service is acceptable.

Risk: The skill stores or requires a dLazy API key for CLI authentication.

Mitigation: Protect the local CLI config, prefer scoped organization keys, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The release is presented as PPT-to-video but also supports broader document/file-to-video behavior.

Mitigation: Review the exact file types and task scope before installation or use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ppt-to-video)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill routes prompts and optional attached files through the dLazy CLI and hosted service.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
