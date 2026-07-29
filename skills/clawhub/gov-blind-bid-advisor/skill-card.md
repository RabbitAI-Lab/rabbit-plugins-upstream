## Description: <br>
投标人侧政府采购盲投参谋：基于公开数据做商机发现（采购公告采集+企业画像匹配排序）与投标决策（资格/能力/利润/风险 go-no-go 结构化判断），内置投标人防御视角风险自查（废标雷区+排他性/萝卜坑条款扫描）。纯本地+公开数据采集，零 API Key；可选挂载 IMA 知识库做检索增强。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External suppliers and procurement teams use this skill to discover public China government procurement opportunities, match them against a local enterprise profile, and produce bid/no-bid decision support with compliance and risk self-checks. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Generated bid advice may include incorrect pricing, competitor, locality, or legal-risk conclusions. <br>
Mitigation: Review generated reports manually and treat them as decision support rather than legal, financial, or guaranteed-outcome advice. <br>
Risk: The skill can run local Python scripts and save business-profile or report files locally. <br>
Mitigation: Run the scripts in an appropriate local workspace and review saved enterprise-profile and report files before sharing them. <br>
Risk: Public procurement collection makes network GET requests to the China government procurement site. <br>
Mitigation: Keep collection limited to ccgp.gov.cn, follow robots and rate limits, and stop collection on access errors such as 403, 429, or 503. <br>
Risk: Optional IMA knowledge-base retrieval can affect the grounding of legal, bid-file, or complaint-case references. <br>
Mitigation: Use IMA retrieval only when the host provides the tool, cite the retrieved library and document title, and state when retrieval is unavailable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/gov-blind-bid-advisor) <br>
- [China Government Procurement central site](http://www.ccgp.gov.cn) <br>
- [Anti-scraping best practices](references/anti-scraping-best-practices.md) <br>
- [Bid decision rubric](references/bid-decision-rubric.md) <br>
- [Category codes](references/category-codes.md) <br>
- [Compliance guardrails](references/compliance-guardrails.md) <br>
- [Enterprise profiling](references/enterprise-profiling.md) <br>
- [IMA knowledge bases](references/ima-knowledge-bases.md) <br>
- [Procurement platforms](references/procurement-platforms.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports with optional JSON files and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save local enterprise profiles and generated reports; public procurement collection is limited to read-only GET requests to ccgp.gov.cn.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release, artifact frontmatter, manifest.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
