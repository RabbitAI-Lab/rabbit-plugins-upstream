## Description: <br>
Search and read Groupon deals from the terminal via curl — the consumer GraphQL API (deal search/browse, deal detail, category taxonomy). Anonymous, no key or login. Use when asked to find Groupon deals, look up a specific deal, or browse a city's offers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to search public Groupon deal listings, inspect deal details, and browse category taxonomy from a terminal workflow without credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill guides agents to make anonymous network requests to Groupon's public GraphQL endpoint. <br>
Mitigation: Use it only for public deal reads and do not add cookies, credentials, or personal account data to requests. <br>
Risk: Persisted public query hashes may become stale when Groupon changes its frontend queries. <br>
Mitigation: Refresh stale hashes from a current public browser network request before relying on the recipe. <br>
Risk: Challenge interstitials or non-JSON responses can break downstream parsing. <br>
Mitigation: Check response content before JSON parsing and retry or stop when the endpoint returns non-JSON content. <br>


## Reference(s): <br>
- [Groupon curl recipes](references/graphql-queries.md) <br>
- [Groupon GraphQL endpoint](https://www.groupon.com/mobilenextapi/graphql) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/groupon-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, guidance] <br>
**Output Format:** [Markdown with inline bash and jq code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces terminal-ready curl requests and JSON parsing guidance for public Groupon deal data.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
