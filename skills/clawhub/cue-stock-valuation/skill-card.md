## Description:

用 Cue 对个股进行全周期估值分析——融合短线资金流向与中长线估值模型，短期看情绪博弈与支撑压力，中长期看业绩兑现与安全边际。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to run Cue-powered stock valuation research for individual equities, holdings review, new-stock research, and peer comparison. It produces a structured report covering short-term market sentiment, medium-term earnings drivers, long-term valuation models, safety margin, risks, and source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends stock research prompts and uses a Cue API key with an external Cue service.

Mitigation: Do not include confidential trading plans, personal data, secrets, or proprietary research in prompts; protect the Cue API key stored in ~/.cue/config.json.

Risk: Report quality and timeliness depend on Cue service availability and external market data sources.

Mitigation: Review the generated report and its source links before relying on it, and rerun diagnostics or use the documented fallback sources when Cue or data sources are unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-stock-valuation)
- [Cue API key setup](https://cuecue.cn/hub/api-key)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [Example Cue report](https://cuecue.cn/share/NMJ36JGzIwOx8SPJXB_WR)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with source links, plus optional DOCX or PDF conversion guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Cue template_id template_8qNgr5 and writes one report per stock-focused query.]

## Skill Version(s):

1.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
