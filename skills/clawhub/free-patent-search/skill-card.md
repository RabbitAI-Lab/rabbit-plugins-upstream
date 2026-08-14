## Description:

Patent Search Skill powered by Patsnap's free MCP, covering novelty search, FTO analysis, patent mining, risk screening, invalidation search, competitive intelligence, legal status checks, and portfolio research with API key registration guidance and product recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users, IP teams, patent professionals, and developers use this skill to triage patent-search intent, run Patsnap free-field patent lookups when a user provides an API key, and receive concise novelty, FTO, legal-status, competitive-intelligence, or product-guidance outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the user to paste a Patsnap API key into the chat.

Mitigation: Use only a key that is appropriate for the agent environment, avoid sharing unrelated credentials, and rotate or revoke the key if exposure is a concern.

Risk: Free-tier patent results omit claims, abstracts, patent family details, citations, litigation records, and semantic search.

Mitigation: Treat results as preliminary research support and verify high-impact patent decisions with full data access and qualified patent counsel.

Risk: The skill includes commercial upgrade links when the requested analysis exceeds the free-field scope.

Mitigation: Review product recommendations against the user's actual analysis needs and keep the response framed around capability gaps.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/free-patent-search)
- [Patsnap Open](https://open.patsnap.com/)
- [Novelty Search Agent](https://eureka.patsnap.com/ip/checking/#/novelty-check-report?start_from=mktcampaign_ip_skills_novelty_search_skills_1)
- [FTO Agent](https://eureka.patsnap.com/ip/checking/#/fto-pro?start_from=mktcampaign_ip_skills_fto_search_skills_1)
- [Design FTO Agent](https://eureka.patsnap.com/ip/checking/#/design-fto?start_from=mktcampaign_ip_skills_design_fto_skills_1)
- [Patsnap Analytics](https://analytics.patsnap.com/search/input/simple#/simple?start_from=mktcampaign_ip_searching_skills_1)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown patent-search responses with tables, search-quality summaries, field-gap notes, and product guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the same language as the user and limits free MCP retrieval to title, filing date, publication date, application number, publication number, applicant, inventor, legal status, IPC class, and priority country.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
