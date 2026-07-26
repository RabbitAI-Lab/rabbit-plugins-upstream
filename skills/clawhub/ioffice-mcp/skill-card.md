## Description: <br>
Access iOffice workspace and facility data through an MCP server for buildings, floors, spaces, reservations, visitors, maintenance requests, moves, and mail. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and workplace operations teams use this skill to query and manage iOffice or Eptura Workplace tenant data through MCP, including room reservations, visitors, maintenance requests, moves, users, buildings, floors, spaces, and mail. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes broad tenant administration and destructive actions, including record deletion, user management, approvals, check-ins, deliveries, and other persistent operational changes. <br>
Mitigation: Use a least-privilege iOffice or Eptura Workplace account and require explicit confirmation before delete, user-management, approval, check-in/out, delivery, or status-changing actions. <br>
Risk: The configured account can expose workplace data such as visitor, mail, reservation, user, and facility records. <br>
Mitigation: Install only when authorized by the employer, scope credentials to the intended tenant, and avoid bulk extraction or use outside approved workplace workflows. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/ioffice-mcp) <br>
- [ioffice-mcp npm package](https://www.npmjs.com/package/ioffice-mcp) <br>
- [Project source link from artifact](https://github.com/chrischall/ioffice-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and MCP tool-call instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses configured iOffice or Eptura Workplace credentials and may produce state-changing MCP tool calls when authorized.] <br>

## Skill Version(s): <br>
2.1.9 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
