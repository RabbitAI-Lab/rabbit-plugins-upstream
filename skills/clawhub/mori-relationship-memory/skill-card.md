## Description: <br>
Mori Relationship Memory helps real estate agents, brokers, and referral-driven service professionals connect Mori's app, API, or MCP server to search a private relationship graph, inspect provenance-backed contact facts, and draft referral recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kiwi-phantomworks](https://clawhub.ai/user/kiwi-phantomworks) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect to Mori, validate credentials, search account-private contacts, messages, and threads, and ask the graph for referral recommendations with citations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may access private relationship, contact, email-thread, and optional SMS-derived data. <br>
Mitigation: Install and use it only for Mori accounts where that data access is intended, and configure the API key with the stated read and ask preset. <br>
Risk: The local MCP setup runs an npm package through npx. <br>
Mitigation: Verify the MCP package and source before running the npx command. <br>
Risk: Recommendation retrievals may create saved graph questions. <br>
Mitigation: Use POST retrievals only when saving the question is acceptable, and avoid treating low-confidence or empty results as factual recommendations. <br>


## Reference(s): <br>
- [Mori homepage](https://www.heymori.ai) <br>
- [Mori app](https://app.heymori.ai) <br>
- [ClawHub skill page](https://clawhub.ai/kiwi-phantomworks/skills/mori-relationship-memory) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include MCP configuration, curl commands, API endpoint guidance, and cited contact or retrieval summaries when Mori access is available.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
