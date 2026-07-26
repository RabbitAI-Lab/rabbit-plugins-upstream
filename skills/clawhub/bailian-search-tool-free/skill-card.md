## Description: <br>
bailian-search-tool-free helps agents query Alibaba Cloud Bailian WebSearch-style sources and return concise search results for fact lookup, lightweight research, and real-time information gathering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Use this skill when an agent needs public web-search context, quick factual lookup, or lightweight multi-topic research through Bailian-style search results. It is not appropriate for sensitive searches, private business terms, advertising management, black-hat SEO, or search manipulation. <br>

### Deployment Geography for Use: <br>
Usable wherever the agent environment, network policy, and applicable terms allow access to ClawHub, Alibaba Cloud Bailian or DashScope services, and the public web sources queried by the skill. <br>

## Known Risks and Mitigations: <br>
Risk: The authoritative security review marks the skill as suspicious because it appears intended for external web search but uses broader, less-scoped instructions than a simple read-only search tool should. <br>
Mitigation: Review the skill before installing, restrict use to non-sensitive public searches, and keep agent permissions limited to the minimum needed for search execution. <br>
Risk: The artifact describes command-line search behavior and an installed script, but the inspected artifact only includes SKILL.md. <br>
Mitigation: Confirm the expected script or runtime integration is present in the installed package before relying on the skill in an agent workflow. <br>
Risk: Search queries may be sent to external services and public web providers. <br>
Mitigation: Do not submit secrets, credentials, private business terms, regulated data, or user-sensitive content as search queries. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/bailian-search-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Search result text or structured command output, typically including titles, links, summaries, cleaned content, status fields, logs, and optional saved markdown/text files.] <br>
**Output Parameters:** [Search query text and an optional result count, with artifact evidence describing a default of 5 and a maximum of 20 results.] <br>
**Other Properties Related to Output:** [Requires network access and a configured DASHSCOPE_API_KEY for Bailian or DashScope access; results should be reviewed for accuracy and source quality before use.] <br>

## Skill Version(s): <br>
1.0.0 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
