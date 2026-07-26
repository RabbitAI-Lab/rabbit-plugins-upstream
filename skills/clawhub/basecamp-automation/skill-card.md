## Description: <br>
Automate Basecamp project management, to-dos, messages, people, and to-do list organization via Rube MCP (Composio). Always search tools first for current schemas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sohamganatra](https://clawhub.ai/user/sohamganatra) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to guide agents through Basecamp project administration, including creating to-do lists and tasks, posting or updating messages, managing people, and organizing to-dos through Rube MCP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can publish or update Basecamp project content using the connected account's permissions. <br>
Mitigation: Before posting or editing, require the agent to show the exact project, message or to-do content, target users, and action, then wait for explicit approval. <br>
Risk: The agent can grant, revoke, or create project users through Basecamp access-management tools. <br>
Mitigation: Require explicit approval for access changes after resolving person IDs and showing the affected project and users. <br>
Risk: Incorrect Basecamp IDs can route work to the wrong project, to-do list, message board, or person. <br>
Mitigation: Resolve IDs top-down from current Basecamp data and present the resolved names and URLs before executing mutating calls. <br>


## Reference(s): <br>
- [Rube MCP](https://rube.app/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Configuration instructions] <br>
**Output Format:** [Markdown instructions with MCP tool names, ordered workflows, and parameter guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Rube MCP and an active Basecamp connection; Basecamp rich text fields use HTML.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
