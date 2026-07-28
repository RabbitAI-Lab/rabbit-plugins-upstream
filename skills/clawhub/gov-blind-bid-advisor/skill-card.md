## Description: <br>
投标人侧政府采购盲投参谋：基于公开数据做商机发现（采购公告采集+企业画像匹配排序）与投标决策（资格/能力/利润/风险 go-no-go 结构化判断），内置投标人防御视角风险自查（废标雷区+排他性/萝卜坑条款扫描）。纯本地+公开数据采集，零 API Key；可选挂载 IMA 知识库做检索增强。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External suppliers and bid teams use this skill to find public China government procurement opportunities, rank them against an enterprise profile, and produce structured bid/no-bid analysis with compliance and risk checks. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The public-data collector can fetch arbitrary URLs despite the stated single-government-source scope. <br>
Mitigation: Keep collection URLs restricted to www.ccgp.gov.cn and avoid running the collector against internal, private, or arbitrary third-party URLs. <br>
Risk: Saved enterprise profiles and bid analysis outputs may contain business-sensitive procurement information. <br>
Mitigation: Review generated JSON and Markdown files before sharing and store them with access limited to authorized bid-team members. <br>
Risk: The skill runs local Python scripts that perform public web collection. <br>
Mitigation: Review scripts and dependencies before execution and follow the skill guidance for robots.txt checks, rate limits, and stopping on access errors. <br>


## Reference(s): <br>
- [反爬策略与数据采集最佳实践](references/anti-scraping-best-practices.md) <br>
- [投标决策评分框架](references/bid-decision-rubric.md) <br>
- [政府采购类别码与品目分类参考](references/category-codes.md) <br>
- [合规护栏与风险识别指引](references/compliance-guardrails.md) <br>
- [企业画像构建与匹配算法参考](references/enterprise-profiling.md) <br>
- [IMA 知识库挂载](references/ima-knowledge-bases.md) <br>
- [数据源平台清单与合规指南](references/procurement-platforms.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports, JSON outputs, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include opportunity rankings, bid decision reports, risk self-checks, enterprise profile configuration, and local script commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, manifest, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
