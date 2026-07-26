## Description: <br>
查询、介绍和预约小安智能健身的一对一线下私教训练服务。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[han815757857-cmd](https://clawhub.ai/user/han815757857-cmd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and booking agents use this skill to answer questions about Xiaoan Smart Fitness services, collect appointment details, create confirmed booking requests through the merchant MCP service, and query existing bookings. <br>

### Deployment Geography for Use: <br>
China, focused on the Beijing offline service area. <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends name, full phone number, fitness goal, appointment details, and limited health-risk status to an external booking system. <br>
Mitigation: Before customer use, require a clear privacy notice that explains what is written to Feishu, who can access it, and how records can be corrected or deleted. <br>
Risk: The skill can create real booking records through a remote MCP service. <br>
Mitigation: Use it only when the merchant MCP authorization is intentionally configured, require explicit user confirmation before booking, and avoid retrying uncertain create requests without checking the result. <br>


## Reference(s): <br>
- [MCP Tool Contract](references/mcp-tools.md) <br>
- [Service Catalog](references/service-catalog.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/han815757857-cmd/skills/xiaoan-smart-fitness) <br>
- [Homepage from ClawHub metadata](https://github.com/han815757857-cmd/xiaoan-smart-fitness) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance, shell commands, configuration] <br>
**Output Format:** [Markdown or plain text with optional shell command examples and MCP tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or query real merchant booking records when authorized; appointment creation requires explicit user confirmation.] <br>

## Skill Version(s): <br>
0.3.0 (source: server evidence release.version and artifact skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
