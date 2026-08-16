## Description:

围绕一个法律争议点检索公开裁判文书、监管问答与实务案例，并归纳裁判要点、争议焦点、实操口径、风险提示和来源链接。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Legal and compliance practitioners use this skill to research difficult China-focused legal practice questions by comparing public judgments, regulatory answers, arbitration materials, and practical case examples. It is intended to provide case-based reference material, not legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the user's legal query and Cue API key to cuecue.cn.

Mitigation: Review the external Cue runner and only use appropriate queries and credentials before installation or execution.

Risk: The generated report may contain incorrect or incomplete legal conclusions.

Mitigation: Verify important conclusions against cited source documents and treat the report as reference material rather than legal advice.

Risk: The skill relies on Cue service availability and public legal or regulatory data sources.

Mitigation: Run the documented health checks before use and fall back to the listed public sources when the service or data source is unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-legal-practice-cases)
- [Cue API key page](https://cuecue.cn/api-key)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [中国裁判文书网](https://wenshu.court.gov.cn)
- [证监会](https://www.csrc.gov.cn)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Guidance]

**Output Format:** [Chinese Markdown report saved to a local file, with cited case numbers and source links where available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports summarize public legal and regulatory materials; conclusions should be checked against cited source documents.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter version 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
