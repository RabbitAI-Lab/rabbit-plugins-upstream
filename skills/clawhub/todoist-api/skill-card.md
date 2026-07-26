## Description: <br>
Todoist API integration with managed OAuth for managing tasks, projects, sections, labels, and comments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to read and modify Todoist tasks, projects, sections, labels, and comments through Maton-managed OAuth. It is suited for creating, updating, completing, organizing, and troubleshooting Todoist work items from an agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Maton proxies Todoist requests and manages OAuth for the connected Todoist account. <br>
Mitigation: Install only if you trust Maton for Todoist access and keep MATON_API_KEY private. <br>
Risk: Write operations can create, update, complete, reopen, or delete Todoist resources. <br>
Mitigation: Approve only specific intended changes and confirm the target resource before executing write calls. <br>
Risk: Multiple Todoist connections can route requests to the wrong account. <br>
Mitigation: Use the Maton-Connection header when multiple active Todoist connections exist. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/todoist-api) <br>
- [Todoist API v1 Documentation](https://developer.todoist.com/api/v1) <br>
- [Todoist Filter Syntax](https://todoist.com/help/articles/introduction-to-filters) <br>
- [Todoist OAuth Documentation](https://developer.todoist.com/guides/#oauth) <br>
- [Related ClawHub API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with API endpoints and inline Python, JavaScript, and shell examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and a connected Todoist OAuth account.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
