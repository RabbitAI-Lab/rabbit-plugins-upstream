## Description: <br>
ClickUp API integration with managed OAuth for accessing and managing tasks, lists, folders, spaces, workspaces, users, and webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, project managers, and agent operators use this skill to query and manage ClickUp work items, project hierarchy, users, OAuth connections, and webhooks through Maton-managed OAuth. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform write, delete, connection, and webhook actions in a connected ClickUp account. <br>
Mitigation: Confirm the exact ClickUp account, connection, target resource, intended effect, and webhook destination before approving those actions. <br>
Risk: MATON_API_KEY grants access through Maton-managed OAuth and must remain private. <br>
Mitigation: Store MATON_API_KEY only in the agent environment or approved secret storage, and do not paste or log the key in prompts, commands, or output. <br>
Risk: Maton brokers access to the user's ClickUp account. <br>
Mitigation: Install and use the skill only when the user trusts Maton for the relevant ClickUp account and workflow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/clickup-api) <br>
- [ClickUp API Overview](https://developer.clickup.com/docs/Getting%20Started.md) <br>
- [ClickUp LLM Reference](https://developer.clickup.com/llms.txt) <br>
- [Maton](https://maton.ai) <br>
- [Maton Settings](https://maton.ai/settings) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API endpoint snippets and Python, JavaScript, and shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and MATON_API_KEY. Generated requests can read, create, update, delete, and manage webhooks in the connected ClickUp account.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
