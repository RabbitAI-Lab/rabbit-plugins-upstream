## Description:

Microsoft Excel API integration with managed OAuth for reading and writing workbooks, worksheets, ranges, tables, and charts stored in OneDrive or SharePoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to inspect or update Microsoft Excel data through Maton-managed OAuth, including workbook, worksheet, range, table, and chart operations. It is suited for task-specific spreadsheet automation where writes, new connections, hosted functions, and trigger destinations are reviewed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can authorize Maton access to a Microsoft Excel account and perform write operations against workbook data.

Mitigation: Use OAuth, keep connections scoped to the needed account, default to read/list operations, and require explicit user approval before new connections or POST, PUT, PATCH, and DELETE calls.

Risk: Hosted functions and triggers can create ongoing automated access to connected data or forward event payloads to destinations.

Mitigation: Approve each function, trigger, and destination separately, prefer private Maton/API destinations, use least-privilege payload templates, and use deny-all outbound network policy unless the user approves named hosts.

Risk: Raw HTTP fallback requires handling a long-lived Maton API key in the process environment.

Mitigation: Prefer the Maton CLI with OAuth; when raw HTTP is unavoidable, never print, log, persist, or pass the key on the command line, and rotate it if exposed.

Risk: Package provenance is not server-resolved for this version, and pinned package versions do not include checksums or signatures.

Mitigation: Verify Maton package provenance separately before installation and upgrade pinned versions deliberately after reviewing release notes.

## Reference(s):

- [Microsoft Graph Excel API Overview](https://learn.microsoft.com/en-us/graph/api/resources/excel)
- [Working with Excel in Microsoft Graph](https://learn.microsoft.com/en-us/graph/excel-concept-overview)
- [Excel Workbook Resource](https://learn.microsoft.com/en-us/graph/api/resources/workbook)
- [Excel Worksheet Resource](https://learn.microsoft.com/en-us/graph/api/resources/worksheet)
- [Excel Range Resource](https://learn.microsoft.com/en-us/graph/api/resources/range)
- [Excel Table Resource](https://learn.microsoft.com/en-us/graph/api/resources/table)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, API paths, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Maton CLI commands, raw HTTP examples for constrained environments, hosted function examples, and trigger configuration guidance.]

## Skill Version(s):

1.2.2 (source: server release evidence; skill frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
