## Description: <br>
Neural web search via Exa AI for people, companies, news, research, code, deep search, domain filters, and date ranges. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jordyvandomselaar](https://clawhub.ai/user/jordyvandomselaar) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to search the web with Exa, retrieve search result snippets and summaries, and extract content from URLs while applying filters such as category, domains, dates, and location. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Searches, filters, locations, and content-extraction URLs are sent to Exa. <br>
Mitigation: Use a dedicated Exa API key and avoid submitting secrets, private internal URLs, confidential research targets, or personal data unless that sharing is acceptable. <br>
Risk: The skill reads an Exa API key from local credential configuration or the environment. <br>
Mitigation: Protect the credential file, limit access to the key, and rotate it if it is exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jordyvandomselaar/skills/exa-plus) <br>
- [Exa search API endpoint](https://api.exa.ai/search) <br>
- [Exa contents API endpoint](https://api.exa.ai/contents) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [JSON API responses and shell-oriented guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, and an Exa API key; search requests may include queries, filters, locations, URLs, snippets, highlights, and summaries.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
