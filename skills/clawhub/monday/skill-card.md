## Description: <br>
Monday.com API integration with managed OAuth for managing boards, items, columns, groups, and workspaces using GraphQL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to query and manage Monday.com workspaces, boards, items, columns, and groups through Maton's managed OAuth proxy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and modify Monday.com data through Maton when a valid API key and OAuth connection are available. <br>
Mitigation: Keep MATON_API_KEY private and approve create, update, or delete operations only after checking the exact target and intended effect. <br>
Risk: Requests may use the wrong Monday.com account when multiple connections are linked. <br>
Mitigation: Specify the intended connection with the Maton-Connection header when multiple Monday.com connections exist. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/monday) <br>
- [Monday.com API Basics](https://developer.monday.com/api-reference/docs/basics) <br>
- [Monday.com GraphQL Overview](https://developer.monday.com/api-reference/docs/introduction-to-graphql) <br>
- [Monday.com Boards Reference](https://developer.monday.com/api-reference/reference/boards) <br>
- [Monday.com Items Reference](https://developer.monday.com/api-reference/reference/items) <br>
- [Monday.com Columns Reference](https://developer.monday.com/api-reference/reference/columns) <br>
- [Monday.com API Changelog](https://developer.monday.com/api-reference/changelog) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown with inline JSON, Python, JavaScript, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and an active Monday.com OAuth connection through Maton.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
