## Description:

Typhoon Tracker helps agents track live typhoon conditions and assess path, landfall, wind and rain impacts, travel safety, transport disruption, event feasibility, emergency preparation, and report generation for northwest Pacific storms affecting coastal China.

This skill is ready for commercial/non-commercial use.

## Publisher:

[firefljay](https://clawhub.ai/user/firefljay)

### License/Terms of Use:

MIT

## Use Case:

External users and operators use this skill to turn public typhoon forecasts, official notices, and historical case data into structured impact assessments and action guidance. It is especially focused on East China cities while retaining a quick assessment framework for other affected cities in China.

### Deployment Geography for Use:

China, with emphasis on East China coastal and inland cities affected by northwest Pacific typhoons.

## Known Risks and Mitigations:

Risk: Live weather and transport lookups can be incomplete, stale, or unavailable during fast-changing typhoon events.

Mitigation: Check official meteorological, emergency-management, airline, railway, metro, and local government notices before making final safety or travel decisions.

Risk: The skill may persist typhoon case data, daily logs, Markdown reports, and generated PDFs in the local workspace.

Mitigation: Avoid entering unnecessary personal travel details and review or delete generated files after use.

Risk: The publishing guide includes curl-to-bash installer guidance.

Mitigation: Do not use the curl-to-bash installer path; inspect installers before execution or use trusted installation methods.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/firefljay/skills/typhoon-tracker)
- [README](README.md)
- [Typhoon Tracker - 部署环境与容错指南](references/deployment_guide.md)
- [Typhoon Tracker - 报告模板与格式指南](references/report_template_guide.md)
- [Typhoon Tracker - 移动端/消息通道适配指南](references/mobile_channel_guide.md)
- [Typhoon Bavi (2609) Case Data](references/bavi_2609_case_data.md)
- [台风白海豚（Dolphin, 2613）案例数据](references/dolphin_2613_case_data.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or concise text, with optional shell commands for PDF export and generated report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write Markdown reports, generated PDFs, daily logs, and typhoon case-data files in the local workspace.]

## Skill Version(s):

1.0.0 (source: evidence release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
