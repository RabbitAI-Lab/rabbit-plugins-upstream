## Description:

对任意中文文本执行广告法合规、主流平台规范和AI写作痕迹检查，并输出结构化检查报告和可直接发布的平台适配改写版本。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yeshenyue12345](https://clawhub.ai/user/yeshenyue12345)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, marketers, editors, and compliance reviewers use this skill to check Chinese drafts against advertising-law, platform-policy, and AI-writing-pattern concerns before publication. The skill produces a review report plus a rewritten version adapted for the target publishing platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can auto-run on pasted Chinese draft content without asking for confirmation.

Mitigation: Use it only in environments where automatic content-compliance review is expected, and avoid pasting confidential or sensitive drafts unless review is intentional.

Risk: The skill requires live web searches during each check, which can expose topics, claims, or platform targets from the reviewed content.

Mitigation: Review drafts in a setting where web-search disclosure is acceptable, or disable the skill for workflows involving confidential launch, legal, medical, financial, or personal data.

Risk: The skill may read user-provided file paths as part of its review workflow.

Mitigation: Provide only files intended for content review and avoid pointing the agent at private local documents.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yeshenyue12345/skills/multi-platform-content-check)
- [广告法合规检查清单](references/ad-law-checklist.md)
- [各主流平台内容规范](references/platform-rules.md)
- [去AI化写作检查清单](references/anti-ai-checklist.md)
- [各平台发布格式指南](references/platform-format-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown report with tables, findings, recommendations, and a publish-ready rewritten text block]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include platform-specific titles, body formatting, hashtags, publishing suggestions, and self-check results.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact manifest.yaml shows 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
