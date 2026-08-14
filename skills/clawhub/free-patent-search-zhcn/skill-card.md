## Description:

Guides agents through Chinese-first patent search workflows using Patsnap's free patent service, including novelty search, FTO analysis, invalidity search, legal-status checks, competitive intelligence, and upgrade guidance when free-field limits apply.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users and patent-focused teams use this skill to run preliminary patent searches, classify search intent, review limited free-tier patent fields, and decide when professional Patsnap products are needed. Outputs are preliminary research support and should not be treated as legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may share confidential invention details, launch plans, competitor strategy, or infringement concerns while using the skill.

Mitigation: Warn users not to provide sensitive patent or business information unless they are authorized to share it with Patsnap services.

Risk: The skill routes searches and user-provided API keys toward external Patsnap services.

Mitigation: Make the external service dependency and API key requirement clear before search execution.

Risk: Free-tier patent results are limited and may be mistaken for legal or complete FTO advice.

Mitigation: Present results as preliminary, disclose the 10-field limit, and direct legal decisions to qualified patent counsel or full professional review.

Risk: Promotional product guidance is built into the workflow.

Mitigation: Keep product recommendations tied to concrete capability gaps such as missing claims, patent families, citations, litigation records, or image-based design search.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/free-patent-search-zhcn)
- [Publisher profile](https://clawhub.ai/user/yuanzhian-patsnap)
- [Patsnap Open Platform](https://open.patsnap.com/)
- [Novelty Search Agent](https://eureka.patsnap.com/ip/checking/#/novelty-check-report?start_from=mktcampaign_ip_skills_novelty_search_skills_1)
- [FTO Agent](https://eureka.patsnap.com/ip/checking/#/fto-pro?start_from=mktcampaign_ip_skills_fto_search_skills_1)
- [Design FTO Agent](https://eureka.patsnap.com/ip/checking/#/design-fto?start_from=mktcampaign_ip_skills_design_fto_skills_1)
- [Patent Data API](https://open.patsnap.com/?start_from=mktcampaign_ip_searching_skills_1)
- [Patsnap Analytics](https://analytics.patsnap.com/search/input/simple#/simple?start_from=mktcampaign_ip_searching_skills_1)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Guidance]

**Output Format:** [Markdown with tables, structured search summaries, product links, and JSON-like examples for quota or upgrade handling.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided Patsnap API key; free-tier outputs are limited to 10 patent fields.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
