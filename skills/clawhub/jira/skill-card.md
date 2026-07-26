## Description: <br>
Use when the user mentions Jira issues, asks about tickets, wants to create, view, or update issues, checks sprint status, or manages their Jira workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jdrhyne](https://clawhub.ai/user/jdrhyne) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and project teams use this skill to manage Jira issues, sprints, and workflow status through either the jira CLI or Atlassian MCP. It helps agents translate natural language requests into safe Jira read and write operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change live Jira data through create, update, move, assign, comment, and sprint actions. <br>
Mitigation: Require explicit confirmation before write operations, fetch the current issue state first, and verify the result after applying changes. <br>
Risk: Jira credentials or API tokens may grant broader access than the agent needs. <br>
Mitigation: Use least-privilege Jira credentials, avoid broad project-admin tokens, and prefer scoped CLI or MCP access over raw API-token workflows. <br>


## Reference(s): <br>
- [Commands Reference](references/commands.md) <br>
- [MCP Reference](references/mcp.md) <br>
- [jira CLI](https://github.com/ankitpokhrel/jira-cli) <br>
- [Declared Skill Repository](https://github.com/PSPDFKit-labs/agent-skills) <br>
- [ClawHub Skill Page](https://clawhub.ai/jdrhyne/skills/jira) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and MCP tool names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May request explicit user approval before create, update, move, assign, comment, or sprint actions; requires either the jira CLI or Atlassian MCP for live operations.] <br>

## Skill Version(s): <br>
1.3.3 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
