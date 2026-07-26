## Description: <br>
Smart Web Search v3.1 helps an agent choose China-focused or international search engines, apply time filters, aggregate results, filter ads, and summarize current web results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[davidme6](https://clawhub.ai/user/davidme6) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to ask an agent for current web, news, technical, China-focused, or international search results without manually choosing a search engine. It is intended for search assistance, source discovery, and concise result synthesis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms may be sent to external search providers and destination pages. <br>
Mitigation: Do not use the skill with secrets, confidential business terms, personal identifiers, or sensitive medical or financial queries. <br>
Risk: Safe-search, ad filtering, and misinformation filtering are advisory and may miss harmful or misleading content. <br>
Mitigation: Review sources before acting on results, especially for medical, legal, financial, or current-event decisions. <br>
Risk: Broad trigger phrases may invoke the skill when a user asks for latest or web-search information. <br>
Mitigation: Confirm user intent and query scope before sending sensitive or ambiguous searches to third-party engines. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/davidme6/smart-web-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with search URLs, fetched-result summaries, source notes, and optional command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route queries to third-party search engines and web pages selected by the agent.] <br>

## Skill Version(s): <br>
3.1.0 (source: evidence.json release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
