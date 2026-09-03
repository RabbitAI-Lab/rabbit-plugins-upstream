## Description:

从 Amazon 评论中的安装、使用和维护疑问提炼说明内容的改进重点与证据，用于改进产品使用说明。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and product operators use this skill to analyze review questions and identify evidence-backed improvements to installation, usage, and maintenance instructions. It supports instruction-improvement recommendations only, not medical, legal, safety-certification, or automatic publishing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes broader paid account, monitoring, export, and workflow controls than its instruction-improvement description suggests.

Mitigation: Review intended commands before use, turn autoConfirm off when explicit confirmation is required, and avoid monitor, export, or workbench commands unless those account-level features are intended.

Risk: Installing the skill requires trusting the ARI CLI with an API key, Amazon review and product data, and local exports.

Mitigation: Use only the official ARI endpoint, do not place API keys in prompts or reports, and confirm export destinations before sharing generated files.

## Reference(s):

- [ARI CLI 与 API 参考](artifact/references/reference.md)
- [Amazon 使用说明改进 专属运营工作流](artifact/references/operation-workflow.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/instruction-improve)
- [ARI Service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports and concise text guidance, with CLI commands when actions are required]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit confirmation before most paid operations unless the service auto-confirm policy applies.]

## Skill Version(s):

1.4.5 (source: frontmatter, _meta.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
