## Description:

Search the web for one or more queries in parallel. Use when you need current information, news, prices, or any web content to complement on-chain Nansen data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search the web for current information, news, prices, and other content that complements on-chain Nansen data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Web search queries are sent to the Serper API, so queries may disclose information to that service.

Mitigation: Avoid including confidential or personal information in search queries.

Risk: Search results can omit some sources and may be incomplete or out of date.

Mitigation: Check source links and dates before relying on results, especially for consequential decisions.

## Reference(s):

- [Browser login platform scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)
- [Nansen Web Searcher on ClawHub](https://clawhub.ai/nansen-devops/skills/nansen-web-searcher)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Search result data with titles, links, snippets, dates, and optional knowledge graph information; formatted JSON when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return results for multiple queries in parallel; result count is configurable.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
