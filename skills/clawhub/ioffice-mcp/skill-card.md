## Description:

Access iOffice workspace and facility data via MCP for buildings, floors, spaces, reservations, visitors, maintenance requests, moves, and mail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and workplace operations teams use this skill to let an agent interact with their authorized iOffice or Eptura Workplace tenant for room booking, visitor handling, maintenance requests, moves, mail, and related facility workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector can read and modify real workplace records, including facility, employee, visitor, reservation, move, and mail data.

Mitigation: Install it only with employer authorization, use least-privilege credentials, and remove MCP configuration or credentials when access is no longer needed.

Risk: Write and action tools can make tenant-visible changes when confirmed.

Mitigation: Review dry-run previews before passing confirm:true and avoid broad employee or visitor lookups unless they are needed for the task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ioffice-mcp)
- [npm package: ioffice-mcp](https://www.npmjs.com/package/ioffice-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed ioffice-mcp server and authorized iOffice or Eptura Workplace credentials.]

## Skill Version(s):

3.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
