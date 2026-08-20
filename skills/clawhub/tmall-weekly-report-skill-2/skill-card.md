## Description:

制作天猫店铺经营周报（品牌方沟通版）。使用场景：当用户提供生意参谋、直通车/引力魔方等推广计划报表、客服绩效等数据文件，并要求制作天猫店铺周报时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gzbarry1980-bot](https://clawhub.ai/user/gzbarry1980-bot)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace users and commerce operations teams use this skill to turn Tmall store, advertising, traffic, product, live-stream, and customer service data into a brand-facing weekly business report with diagnostics and next-week action items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is intended for sensitive store operating data and produces local report artifacts.

Mitigation: Use only intended business data, keep generated reports in the appropriate workspace, and review report artifacts before sharing them.

Risk: The chart script contains hardcoded sample data and an absolute chart output path.

Mitigation: Replace the sample data and output path before use so current client data is not mixed with older report data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gzbarry1980-bot/skills/tmall-weekly-report-skill-2)
- [Server-resolved GitHub provenance](https://github.com/gzbarry1980-bot/pinmoo/tree/main/tmp/tmall-weekly-report-skill-2)
- [SKILL.md](artifact/SKILL.md)
- [Weekly report template](artifact/templates/report_template.md)
- [Chart generation script](artifact/scripts/make_charts.py)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown report guidance with chart-generation Python and PDF export instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local report artifacts and 12 standardized charts after the user updates the chart script with current operating data.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
