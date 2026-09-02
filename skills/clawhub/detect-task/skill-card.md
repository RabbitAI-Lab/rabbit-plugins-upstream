## Description:

投前 AI 图真实性质检：待检图生成风险等级、8 项逐条判定、投放建议，以及可追加到生成 prompt 的修正句。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, creative teams, and agents use this skill before listing or advertising AI-generated product images to identify visual defects, platform-compliance concerns, and concrete prompt fixes for reruns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can send product images and prompts to cloud providers.

Mitigation: Install and run it only when image and prompt data may be shared with the selected provider; explicitly choose the intended provider instead of relying on automatic provider selection.

Risk: The automatic rerun loop can save prompt history in a local manifest.

Mitigation: Avoid the rerun loop for confidential prompts unless local prompt-history retention is acceptable, and review generated manifests before sharing the workspace.

Risk: The security verdict is suspicious because bundled provider tooling is broader than the inspection task itself.

Mitigation: Review the bundled scripts and scan findings before installation, and restrict credentials to the providers needed for the intended workflow.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Model flags](references/model-flags.md)
- [Platform image specifications](references/platform-specs.md)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/detect-task)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown inspection report with risk tables, recommendations, and optional command examples or configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are typically written in Chinese, with prompt-fix sentences in English when rerun or manual repair is recommended.]

## Skill Version(s):

1.0.4 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
