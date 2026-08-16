## Description: <br>
Jira API integration with managed OAuth for searching issues with JQL, creating and updating issues, and managing projects and transitions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and workflow operators use this skill to interact with Jira Cloud issues, projects, transitions, comments, users, and metadata through Maton's managed OAuth API gateway. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, transition, comment on, or delete Jira resources through the connected account. <br>
Mitigation: Confirm the target Jira cloud, connection, resource, and intended effect with the user before any write or delete operation. <br>
Risk: Using the wrong Jira connection or cloud ID could send requests to an unintended workspace. <br>
Mitigation: Fetch accessible resources first and specify the intended cloud ID and connection when multiple Jira connections exist. <br>
Risk: The skill requires a Maton API key and network access to proxy requests to Jira. <br>
Mitigation: Store MATON_API_KEY as a secret, avoid printing it, and grant only the Jira access needed for the task. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/jira-api) <br>
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway) <br>
- [Maton CLI Manual](https://cli.maton.ai/manual) <br>
- [Jira API Introduction](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/) <br>
- [Search Issues with JQL](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/#api-rest-api-3-search-jql-get) <br>
- [JQL Reference](https://support.atlassian.com/jira-service-management-cloud/docs/use-advanced-search-with-jira-query-language-jql/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with inline bash, JavaScript, Python, HTTP, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, a valid MATON_API_KEY, a Jira OAuth connection, and a Jira Cloud ID.] <br>

## Skill Version(s): <br>
1.0.8 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
