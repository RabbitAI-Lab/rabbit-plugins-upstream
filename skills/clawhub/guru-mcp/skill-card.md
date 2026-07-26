## Description: <br>
Access Guru knowledge base via MCP to ask AI questions, search documents, create drafts, update cards, and connect to Guru sources including Slack, Drive, Confluence, and SharePoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pvoo](https://clawhub.ai/user/pvoo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and employees use this skill to connect an agent to Guru through MCP so it can answer workplace knowledge questions, search cards and connected sources, and help create or update Guru content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read broad workplace knowledge through the configured Guru API token. <br>
Mitigation: Use Guru only for approved data, configure the least-privileged token available, and avoid secrets or regulated personal data in questions. <br>
Risk: The skill can create drafts and update Guru cards with the user's token. <br>
Mitigation: Manually review any draft creation or card update before allowing the action to run. <br>


## Reference(s): <br>
- [Guru MCP Documentation](https://help.getguru.com/docs/connecting-gurus-mcp-server) <br>
- [Guru API Reference](https://developer.getguru.com) <br>
- [AI Agent Center](https://app.getguru.com/ai-agent-center) <br>
- [Guru Homepage](https://www.getguru.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/pvoo/skills/guru-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return Guru answer text, search results, card HTML content, draft URLs, and card update guidance through MCP tool calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
