## Description:

文件转视频 File to Video helps agents use dLazy's file-to-video template to convert PPT, Word, Excel, PDF, and other documents into explainer, report, courseware, or training videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, educators, and business users use this skill through an agent to turn source documents into video projects with outline, storyboard, voiceover, generation, and validation support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on the @dlazy/cli npm package and can be installed globally.

Mitigation: Install only if you trust dLazy, prefer the pinned npx invocation or an isolated environment, and review the linked source before global installation.

Risk: Prompts and attached files are sent to dLazy services, with file attachments uploaded before use.

Mitigation: Avoid attaching sensitive documents unless uploading them to dLazy is intended and approved for the user's workflow.

Risk: The dLazy API key is stored locally or may be supplied through an environment variable.

Mitigation: Use normal local credential protections and rotate or revoke the dLazy API key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)
- [dLazy CLI metadata link](https://github.com/dlazy-ai/cli)
- [dLazy website](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference dLazy project ids, uploaded file URLs, streamed agent replies, and authentication or billing remediation steps.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
