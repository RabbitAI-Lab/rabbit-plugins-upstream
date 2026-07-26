## Description: <br>
依托 LinkedIn 数据库，按照企业名称、所属行业、公司规模以及成立年份筛选企业资料，助力外贸从业者开发客户、开展市场调研，完成领英企业画像搭建以及 ABM 账户营销的目标客户筛选工作。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sales, marketing, and B2B lead-generation users use this skill to search LinkedIn company profiles by name, industry, company size, founding year, geography, and contact-data availability. It supports prospecting, market research, competitor analysis, account-based sales, and enrichment of company profile data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid third-party API key that may be stored in ~/.upkuajing/.env. <br>
Mitigation: Use a dedicated least-privilege API key, restrict local file permissions, and rotate the key if it may have been exposed. <br>
Risk: Company and contact search results can be saved under the skill directory. <br>
Mitigation: Store result files only in approved locations, limit retention, and review files for personal or sensitive contact data before sharing. <br>
Risk: Contact-data searches may create privacy, anti-spam, or lawful-basis obligations. <br>
Mitigation: Use contact-data features only for permitted business purposes and follow applicable privacy, consent, and outreach rules. <br>
Risk: A daily provider version-check call may create additional network egress. <br>
Mitigation: Review network policy before installation and monitor or disable provider update checks where required by policy. <br>


## Reference(s): <br>
- [领英公司列表 API](references/linkedin-company-list-api.md) <br>
- [ClawHub skill release page](https://clawhub.ai/upkuajing/skills/linkedin-company-search-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing open API pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, files, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples, JSON API summaries, and JSONL company result files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search result files are written under the skill task data directory; list searches accept 20 to 1000 requested records and can be continued by task ID.] <br>

## Skill Version(s): <br>
1.0.2 (source: server evidence and frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
