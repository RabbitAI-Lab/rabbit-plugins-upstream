## Description:

ppt to video, word to video, excel to video, pdf to video, document to video: parse, outline, storyboard, voiceover, build, and validate videos from user-provided documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content teams, educators, and business users use this skill to turn PPT, Word, Excel, PDF, and other document inputs into explainer, report, courseware, or training videos through the dLazy hosted agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents may be uploaded to the dLazy service.

Mitigation: Use the skill only with documents approved for dLazy processing and review service terms before submitting confidential material.

Risk: The dLazy API key may be saved in the local CLI configuration for future use.

Mitigation: Protect the local config file, prefer per-invocation environment variables when persistence is not desired, and rotate or revoke organization keys when needed.

Risk: The skill depends on a third-party CLI and hosted API.

Mitigation: Review the pinned CLI package, source link, and service behavior before installing or using it in production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with CLI commands and streamed agent responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated video workflow outputs and project-scoped follow-up sessions returned by the dLazy CLI.]

## Skill Version(s):

1.3.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
