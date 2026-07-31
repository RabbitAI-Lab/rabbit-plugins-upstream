## Description: <br>
Search and read Groupon deals from the terminal via curl -- the consumer GraphQL API for deal search, deal detail, and category taxonomy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to find Groupon deals by city, inspect deal details, and browse Groupon category taxonomy through public, unauthenticated GraphQL requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Groupon search terms and city slugs may be sent to Groupon's public API. <br>
Mitigation: Avoid entering sensitive or private search terms, and review requests before running them. <br>
Risk: Users could expose unnecessary credentials if they add Groupon login data, cookies, API keys, or payment information to requests. <br>
Mitigation: Use only the documented anonymous public requests; do not provide credentials or payment information to this skill. <br>
Risk: Persisted-query hashes can become stale after Groupon frontend changes. <br>
Mitigation: If Groupon returns PersistedQueryNotFound, re-capture the public persisted-query hash from a browser network request and update the reference recipe. <br>
Risk: Empty or non-JSON responses can occur when a challenge interstitial is returned. <br>
Mitigation: Check that responses are valid JSON before parsing and retry when the endpoint returns an interstitial. <br>


## Reference(s): <br>
- [Groupon curl recipes](references/graphql-queries.md) <br>
- [Groupon consumer GraphQL endpoint](https://www.groupon.com/mobilenextapi/graphql) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown with inline curl and jq examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agent responses may include public Groupon deal data, GraphQL request bodies, and troubleshooting guidance for stale persisted-query hashes or non-JSON responses.] <br>

## Skill Version(s): <br>
0.1.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
