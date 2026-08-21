## Description:

当用户需要做小红书竞品研究、小红书竞品分析、同赛道观察、内容角度对比、内容策略对比或品牌内容调研时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External brand, MCN, content operations, and creator teams use this skill to search Xiaohongshu content and compare competitor topics, content angles, audience signals, creator positioning, and strategy opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the SocialDataX npm package and API service.

Mitigation: Confirm the package and service are trusted before installation, and provide the API key only through the SOCIALDATAX_API_KEY environment variable.

Risk: Returned Xiaohongshu note URLs may contain tokens or links intended only for the research audience.

Mitigation: Keep full returned URLs intact for traceability, but share them only with people who should receive the research results.

Risk: Search pages and recent-topic filters may not represent full-platform coverage.

Mitigation: State the query, filters, page count, and time window used, and avoid presenting sampled results as complete market coverage.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/devinchen2014/skills/xhs-competitor-research-v2)
- [SocialDataX API Key and Product Page](https://socialdatax.com/ai?from=clawhub)
- [ClawHub Publisher Profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and structured research notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results may include titles, authors or accounts, note URLs, note IDs, pagination tokens, and follow-up analysis angles.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
