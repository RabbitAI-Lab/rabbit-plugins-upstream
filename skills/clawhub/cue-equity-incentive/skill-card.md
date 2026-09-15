## Description:

用 Cue 查询和分析上市公司股权激励计划，覆盖 A 股上市公司公开披露的历史方案要素、实施效果、同行竞品对比和竞争力评估。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as listed-company investor relations teams, HR and compensation leaders, investors, analysts, and consultants use this skill to request Cue reports on A-share listed-company equity incentive plans. It supports plan design benchmarking, reasonableness review, investor due diligence, and peer comparison using public disclosure data.

### Deployment Geography for Use:

Global; intended data coverage is A-share listed companies in China.

## Known Risks and Mitigations:

Risk: The workflow sends the user's query and Cue API key to an external Cue service and returns Cue-hosted share links.

Mitigation: Install only if that external-service workflow is acceptable; review generated reports and links before sharing them.

Risk: The security summary flags forced vendor-hosted links and verbatim remote report delivery as review concerns.

Mitigation: Treat generated reports as third-party remote content and verify important claims against cited public disclosures.

Risk: The artifact includes referral and payment wording for insufficient Cue credits.

Mitigation: Override or omit commercial prompts when they are inappropriate for the user-facing response.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-equity-incentive)
- [Cue platform](https://cuecue.cn)
- [Cue API key management](https://cuecue.cn/api-key)
- [Cue example report](https://cuecue.cn/share/TIxQDFYs)
- [CNInfo disclosures](https://www.cninfo.com.cn)
- [Eastmoney equity incentive data](https://data.eastmoney.com)
- [SEC EDGAR](https://www.sec.gov/edgar)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with source links and a Cue share URL, plus shell commands and configuration guidance when setup or conversion is needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue API key and access to the external Cue service; report generation is described as typically taking 2-15 minutes depending on load and source availability.]

## Skill Version(s):

1.1.8 (source: server-resolved release metadata; artifact frontmatter reports 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
