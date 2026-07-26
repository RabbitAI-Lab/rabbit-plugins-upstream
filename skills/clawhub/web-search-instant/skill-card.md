## Description: <br>
Web Search Instant searches DuckDuckGo Instant Answer results for quick facts, definitions, calculations, conversions, abstracts, and related topics without requiring an API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hahahxx](https://clawhub.ai/user/hahahxx) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, researchers, and agents use this skill to answer quick factual, definition, calculation, and conversion queries through DuckDuckGo Instant Answer results when no API key is available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to DuckDuckGo and may expose sensitive text to an external service. <br>
Mitigation: Avoid secrets, credentials, private incident details, proprietary names, and other sensitive text; invoke the skill only for explicit web-search needs. <br>
Risk: DuckDuckGo Instant Answer coverage is limited and may miss recent news, full search results, complex math, or some definitions. <br>
Mitigation: Treat results as quick lookup assistance, try query variations, and use the provided DuckDuckGo link or another source when completeness or recency matters. <br>
Risk: Fallback parsing without jq can produce character encoding issues in some abstracts. <br>
Mitigation: Install jq where accurate JSON parsing and cleaner output are important. <br>


## Reference(s): <br>
- [DuckDuckGo Instant Answer API](https://duckduckgo.com/api) <br>
- [ClawHub Skill Page](https://clawhub.ai/hahahxx/skills/web-search-instant) <br>
- [README.md](README.md) <br>
- [TEST-SUMMARY.md](TEST-SUMMARY.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Text, plain text, or Markdown search summaries with source links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access; optional jq improves JSON parsing; related topic count is configurable.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata and CHANGELOG-v1.1.0.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
