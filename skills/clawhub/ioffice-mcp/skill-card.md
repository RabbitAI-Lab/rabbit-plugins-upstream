## Description:

Access iOffice workspace and facility data through an MCP server for buildings, floors, spaces, reservations, visitors, maintenance requests, moves, mail, and health checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, workplace operations teams, and developers use this skill to let an agent query and update iOffice/Eptura Workplace tenant records for room booking, visitor management, maintenance requests, moves, mail handling, and connector health checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose broad iOffice/Eptura Workplace tenant data.

Mitigation: Install only with employer authorization, use the least-privilege token available, and keep credentials out of shared project files.

Risk: The skill includes destructive or business-critical actions such as delete, approve, cancel, check-in/check-out, deliver, return, archive, and user-management operations.

Mitigation: Require explicit human review before executing those actions and confirm the target record, tenant, and expected outcome.

Risk: Automation may conflict with iOffice/Eptura Workplace or employer acceptable-use rules.

Mitigation: Use the skill only for authorized workplace workflows and stop using it if the employer or service provider objects.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ioffice-mcp)
- [npm package](https://www.npmjs.com/package/ioffice-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May instruct an agent to call iOffice MCP tools that read tenant data or perform create, update, delete, approval, check-in, check-out, delivery, return, archive, and health-check actions.]

## Skill Version(s):

2.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
