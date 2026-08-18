## Description:

Typhoon Tracker helps agents track Northwest Pacific typhoons, assess landfall, wind, rainfall, transport, activity, and residual-vortex risks, and produce structured decision-support reports for East China and broader China use cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[firefljay](https://clawhub.ai/user/firefljay)

### License/Terms of Use:

MIT

## Use Case:

External users and agent operators use this skill to evaluate typhoon paths, landfall timing, wind and rain impacts, travel disruption, event feasibility, emergency preparation, and post-dissipation residual-vortex effects. It is especially tailored to East China scenarios while providing a repeatable framework for other cities affected by Northwest Pacific typhoons.

### Deployment Geography for Use:

Global, with methodology focused on Northwest Pacific typhoons affecting China, especially East China.

## Known Risks and Mitigations:

Risk: The security review flags broad local history reuse and report or case-history writes as behaviors that may surprise users.

Mitigation: Review before installing, require confirmation before file writes, and limit access to prior workspace memory or report files to cases where the user explicitly needs historical context.

Risk: Automatic triggers can cause the skill to run for travel or transport questions even when a user did not explicitly ask about typhoons.

Mitigation: Narrow or disable automatic triggers in sensitive deployments and make clear when typhoon-background checks are being applied.

Risk: Installer documentation may encourage a curl-pipe-shell path that bypasses normal review.

Mitigation: Avoid curl-pipe-shell installation unless the script is independently verified; prefer inspecting the artifact and installing from a reviewed source.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/firefljay/skills/typhoon-tracker)
- [GitHub Homepage](https://github.com/FireflJay/typhoon-tracker)
- [Typhoon Tracker - 部署环境与容错指南](references/deployment_guide.md)
- [Typhoon Tracker - 移动端/消息通道适配指南](references/mobile_channel_guide.md)
- [Typhoon Tracker - 报告模板与格式指南](references/report_template_guide.md)
- [Typhoon Bavi (2609) Case Data](references/bavi_2609_case_data.md)
- [台风白海豚（Dolphin, 2613）案例数据](references/dolphin_2613_case_data.md)
- [台风浪卡（2617）案例数据](references/nangka_2617_case_data.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown reports and concise chat guidance, with optional generated report files and PDF-generation shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should distinguish official information, official warnings, and predictions; transport and safety guidance should include source timing and confidence where available.]

## Skill Version(s):

1.1.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
