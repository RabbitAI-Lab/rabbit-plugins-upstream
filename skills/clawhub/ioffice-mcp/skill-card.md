## Description:

Access iOffice workspace and facility data via MCP for buildings, floors, spaces, reservations, visitors, maintenance requests, moves, and mail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized workplace operations users use this skill to connect an agent to an organization's iOffice or Eptura Workplace tenant for room booking, visitor handling, maintenance requests, moves, mail workflows, and related facility data lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes tenant-level workplace and user administration tools, including update, delete, and state-changing actions.

Mitigation: Install only for authorized iOffice or Eptura tenants, use least-privilege credentials, and require explicit confirmation before any write or state-changing operation.

Risk: The artifact frames the connector for personal, single-employee use while exposing data and actions that may be governed by employer policy.

Mitigation: Confirm employer IT and security authorization before use, and do not bulk-extract directories, floor plans, visitor records, or other workplace data.

Risk: Full responses can include media or sensitive facility and user details that compact responses omit.

Mitigation: Use compact views by default, request full views only when the additional data is necessary, and protect iOffice tokens or passwords as tenant credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ioffice-mcp)
- [npm package](https://www.npmjs.com/package/ioffice-mcp)
- [Eptura Acceptable Use Policy](https://eptura.com/terms/acceptable-use-policy/)

## Skill Output:

**Output Type(s):** [text, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown text with MCP tool calls, JSON configuration examples, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read tools can return compact or full iOffice payloads; write and state-changing tools should be treated as administrative actions requiring explicit confirmation.]

## Skill Version(s):

3.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
