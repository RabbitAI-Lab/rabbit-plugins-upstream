## Description:

PPT 转视频、PowerPoint 转视频、幻灯片转视频、演示文稿转视频——解析、大纲、分镜、配音、合成、校验。当用户给一份 PPT / PowerPoint / Keynote、想要讲解视频 / 路演 / 课件 / 培训视频时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content teams use this skill to turn presentations or documents into explainer, pitch, courseware, or training videos through the dLazy CLI and hosted file-to-video workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files attached with --files may be uploaded to dLazy's hosted service.

Mitigation: Use only when dLazy's terms and organizational policy allow the material to be sent to that service; avoid confidential documents unless approved.

Risk: The dLazy CLI stores an API key locally for authentication.

Mitigation: Protect the local CLI configuration, prefer scoped organization keys, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: The skill depends on npm or npx to run the pinned dLazy CLI package.

Mitigation: Install the pinned package version from the declared npm source and review the linked CLI source before deployment.

## Reference(s):

- [dLazy CLI source link from metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown with inline bash commands and dLazy CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or continue dLazy project sessions and may produce video outputs through the dLazy service.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
