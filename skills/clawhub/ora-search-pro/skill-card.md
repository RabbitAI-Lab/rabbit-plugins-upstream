## Description: <br>
外贸人专属搜索引擎，通过国家、产品行业关键词精准检索，一键生成外贸企业列表。作为一款专业的外贸营销获客软件与外贸获客系统，整合多渠道公开数据，提供高效的外贸找客户服务。适用于外贸营销软件选型、B2B客户开发等场景。当用户需要使用外贸找客户软件获取某国某行业采购商名单、搜索企业信息或查找外贸企业列表时使用此技能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oraagent](https://clawhub.ai/user/oraagent) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External trade and B2B sales users use this skill to search for companies by product keywords, company names, and country filters, then review matching company names, countries, and websites. It is intended for customer development workflows such as finding prospective buyers or business lists in a target market. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms and the Ora API key are sent to h.smtso.com for lookup. <br>
Mitigation: Use the skill only when that external lookup is intended, avoid confidential business research terms, and use an API key scoped to the Ora service. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oraagent/skills/ora-search-pro) <br>
- [Ora homepage](https://www.topeasychina.com) <br>
- [Ora business-search API endpoint](https://h.smtso.com/skill/domaininfo/queryYellowPage) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results include total count and company list fields such as title, country, and website when the external API returns matches.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
