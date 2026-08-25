## Description:

青虎AI 双人爆款视频模仿 helps an agent submit a two-person reference video workflow through qhkit to synchronize both people's actions and expressions and produce a two-person promotional video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and agents use this skill when a user needs a two-person imitation or product-promotion video generated from authorized reference media. It is intended for double-person scenes such as parent-child, partner, or livestream-commerce content where both people's movements need to stay synchronized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party qhkit CLI that may upload user media to the Qinghu service.

Mitigation: Use only media the user owns or is authorized to process, and review the destination service before uploading sensitive or regulated content.

Risk: The workflow can consume paid Qinghu credits after task submission.

Mitigation: Run an estimate first and require explicit user approval before calling the generate action.

Risk: API credentials could be exposed if pasted into chat or stored casually.

Mitigation: Configure credentials locally through a secure secret mechanism such as qhkit config, QHKIT_TOKEN, or OPENCLAW_CONFIG_PATH.

Risk: The setup path may install npm, Node, or system-level tooling.

Mitigation: Approve installation only on trusted machines and only after confirming the package source and required permission level.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-duo-viral-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key tutorial](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON and bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit workflow options, estimate, generate, status, and credential configuration; completed workflow results are returned as media URLs by the qhkit service.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
