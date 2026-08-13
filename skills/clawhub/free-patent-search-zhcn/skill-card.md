## Description:

Guides agents through Chinese-first patent searching with Patsnap's free MCP API, covering novelty search, FTO analysis, invalidity search, competitive intelligence, legal-status checks, design-risk screening, and upgrade guidance for deeper Patsnap products.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users and patent-focused agents use this skill to run preliminary patent search workflows through Patsnap services, classify user intent, summarize free-tier data boundaries, and route higher-confidence research or legal-risk work to appropriate Patsnap products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent search and FTO outputs may be incomplete or legally insufficient, especially when limited to free-tier fields.

Mitigation: Treat outputs as preliminary research, verify important results with complete patent data, and consult qualified patent counsel for legal decisions.

Risk: Using the skill requires sharing API keys or potentially sensitive invention details with Patsnap services.

Mitigation: Use the skill only after accepting Patsnap's terms and data handling, and avoid pasting confidential invention details or API keys unless that sharing is approved.

Risk: External API access and product links can affect data exposure and workflow dependency.

Mitigation: Confirm Patsnap service access, quota, and organizational approval before relying on the skill in production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/free-patent-search-zhcn)
- [Publisher profile](https://clawhub.ai/user/yuanzhian-patsnap)
- [Patsnap Open API](https://open.patsnap.com/)
- [Novelty Search Agent](https://eureka.patsnap.com/ip/checking/#/novelty-check-report?start_from=mktcampaign_ip_skills_novelty_search_skills_1)
- [FTO Agent](https://eureka.patsnap.com/ip/checking/#/fto-pro?start_from=mktcampaign_ip_skills_fto_search_skills_1)
- [Design FTO Agent](https://eureka.patsnap.com/ip/checking/#/design-fto?start_from=mktcampaign_ip_skills_design_fto_skills_1)
- [Patsnap Analytics](https://analytics.patsnap.com/search/input/simple#/simple?start_from=mktcampaign_ip_searching_skills_1)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, API Calls, Analysis]

**Output Format:** [Markdown with tables, structured summaries, JSON-like examples, and product links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are Chinese by default and switch to English when the user asks in English; patent-risk outputs are preliminary and depend on Patsnap API access.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter says 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
