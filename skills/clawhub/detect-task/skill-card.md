## Description:

投前 AI 图真实性质检。待检图 → 风险等级 + 8 项逐条判定 + 可直接追加到 prompt 的修正句，可自动重跑直到达标。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商团队用它在商品图上架或投放前审查 AI 生成的图片，定位商品、人物、文字、光影和平台合规问题，并决定直接使用、重跑或人工修图。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The automated review subprocess may use a different cloud provider than the selected provider, affecting where prompts and images are sent.

Mitigation: Review provider routing before using confidential images or the automated loop; explicitly use dLazy for the documented text review, and set PROVIDER=dlazy to constrain the loop's review subprocess.

Risk: Preview and batch runs can overwrite existing reports or queues.

Mitigation: Preserve existing reports and queues, and use fresh output paths for every run, including previews.

Risk: Automated image judgments can miss defects or flag acceptable images incorrectly.

Mitigation: Keep human approval before publishing images.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/detect-task)
- [Provider CLI and data flow](artifact/references/provider-cli.md)
- [Model flags](artifact/references/model-flags.md)
- [Platform image specifications](artifact/references/platform-specs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Risk level, eight item-by-item findings, a publication recommendation, and prompt-ready correction sentences; requires human review before publication.]

## Skill Version(s):

1.0.30 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
