## Description:

将现成稿件与素材整理为多平台、多账号发布交接包，并按账号保留提交意图、历史和回执。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

面向准备或续接多平台发布的内容团队与代理：整理保留原稿的逐账号交接材料、跟踪授权和回执，并在审核中或结果未知时先回查，避免重复投稿。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The handoff package contains manuscript content and account history.

Mitigation: Limit access to people authorized for the task, and keep passwords, tokens, and other login credentials out of the package.

Risk: An unknown or already accepted submission could be posted again if its state is not checked.

Mitigation: Carry forward the relevant receipt history and read back the original task before retrying; only retry when evidence confirms no submission occurred.

Risk: A receipt may be inaccurate when it has not been checked against the publishing platform.

Mitigation: Distinguish user-reported receipts from independently verified ones, and record platform-native IDs, status, and links from an actual readback.

## Reference(s):

- [Input, command, and receipt contracts](references/contracts.md)
- [aimeGeo project](https://github.com/aiispower/aimegeo)
- [aimeGeo website](https://geo.aimmme.com/)

## Skill Output:

**Output Type(s):** [JSON files, Markdown files, Publishing guidance]

**Output Format:** [JSON and Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-account handoff materials preserve the supplied manuscript and track account-specific fields, assets, authorization, and receipts.]

## Skill Version(s):

1.0.0 (source: manifest.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
