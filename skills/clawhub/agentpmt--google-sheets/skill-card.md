## Description:

Guides agents through creating, reading, updating, formatting, sharing, and exporting Google Sheets via AgentPMT.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can manage spreadsheet records, build reporting sheets, and export data through AgentPMT's Google Sheets integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sharing can grant public, domain-wide, or owner-level access to a spreadsheet.

Mitigation: Require explicit user approval and verify recipients and permission levels before sharing.

Risk: Deleting rows or tabs can permanently remove spreadsheet data.

Mitigation: Confirm the target with the user, re-read current rows, and verify an archive or backup before deletion.

Risk: Full-spreadsheet exports can expose sensitive data in File Manager.

Mitigation: Obtain explicit approval, select only necessary sheets or ranges, and limit access to exported files.

## Reference(s):

- [Google Sheets action schema](artifact/schema.md)
- [AgentPMT Google Sheets marketplace listing](https://www.agentpmt.com/marketplace/google-sheets-api)
- [AgentPMT account and API setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup)
- [ClawHub Google Sheets release](https://clawhub.ai/agentpmt/skills/google-sheets)

## Skill Output:

**Output Type(s):** [Guidance, API calls]

**Output Format:** [Markdown instructions with JSON action examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports spreadsheet reads and edits, sharing, and exports to AgentPMT File Manager.]

## Skill Version(s):

1.0.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
