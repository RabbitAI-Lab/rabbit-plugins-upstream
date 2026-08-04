## Description: <br>
Searches and reads Groupon deal data from the terminal using curl recipes for the public consumer GraphQL endpoint, including deal search, deal detail, and category taxonomy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they want an agent to find Groupon deals, inspect a specific deal, or browse city/category offers through terminal-ready curl and jq recipes without credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Groupon's public, undocumented consumer GraphQL endpoint or persisted query hashes may change, causing requests to fail or return non-JSON challenge responses. <br>
Mitigation: Treat responses as untrusted until parsed, handle empty or non-JSON responses explicitly, and refresh persisted query hashes from a browser network capture when Groupon returns PersistedQueryNotFound. <br>


## Reference(s): <br>
- [Groupon curl recipes](references/graphql-queries.md) <br>
- [Groupon GraphQL endpoint](https://www.groupon.com/mobilenextapi/graphql) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/groupon-mcp) <br>
- [Publisher profile](https://clawhub.ai/user/chrischall) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, API calls] <br>
**Output Format:** [Markdown with inline bash, curl, jq, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only, unauthenticated public deal-data requests; examples return JSON arrays from Groupon's consumer GraphQL endpoint.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
