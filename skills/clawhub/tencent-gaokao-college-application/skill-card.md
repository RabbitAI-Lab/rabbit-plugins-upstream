## Description:

面向中国普通高考常规批次考生的腾讯高考志愿填报工具，用于查询一分一段、省控线、院校或专业历年录取数据，并根据省份、分数、位次、选科和偏好生成院校优先或专业优先的冲稳保志愿参考方案及 HTML 报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencentnewsteam](https://clawhub.ai/user/tencentnewsteam)

### License/Terms of Use:

MIT-0

## Use Case:

External students, families, and education advisors use this skill to query Tencent News CLI-backed Gaokao admissions data and prepare regular-batch college or major application reference plans. It is intended for data lookup, score-rank checks, admission-line review, and HTML report generation, not as a final admissions decision authority.

### Deployment Geography for Use:

Mainland China provincial regions supported by the skill; unsupported Hong Kong, Macao, Taiwan, Tibet, and Xinjiang data are excluded.

## Known Risks and Mitigations:

Risk: Installer, update, and local CLI execution behavior can affect the user's machine.

Mitigation: Install only if TencentNews and the Tencent News CLI distribution path are trusted; review the installer and verify checksums or signatures where available.

Risk: A real API key could be exposed if shared with an agent or included in logs or reports.

Mitigation: Configure the API key locally, use placeholders in prompts and documentation, and avoid sending, echoing, or storing the real key in agent-visible content.

Risk: Admissions-query details may be sent through the local Tencent News CLI.

Mitigation: Provide only the data needed for the query and review the CLI's expected data handling before use.

Risk: College application recommendations can be mistaken for final admissions decisions.

Mitigation: Use the generated plan as reference only, preserve the required disclaimer, and independently verify admissions data before submitting applications.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tencentnewsteam/skills/tencent-gaokao-college-application)
- [tencent-news-cli installation guide](references/installation-guide.md)
- [tencent-news-cli API Key setup guide](references/env-setup-guide.md)
- [tencent-news-cli update guide](references/update-guide.md)
- [Gaokao HTML interaction reference](references/gaokao-html-interaction-reference.html)
- [Tencent News API Key page](https://news.qq.com/exchange?scene=appkey)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, HTML files]

**Output Format:** [Markdown responses with optional local HTML reports and setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [All admissions data and recommendations must come from a successful Tencent News CLI response, and user-facing results must include the fixed Chinese disclaimer.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
