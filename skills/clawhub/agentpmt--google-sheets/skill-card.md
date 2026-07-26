## Description: <br>
Google Sheets helps agents create, read, update, format, share, and export spreadsheets through AgentPMT-hosted remote tool calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to work with Google Sheets through short, schema-defined actions for spreadsheet creation, tab management, safe row and column appends, selected row updates, formatting, sharing, and exports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read, edit, share, delete, and export Google Sheets through a remote integration. <br>
Mitigation: Install only if the publisher is trusted with the relevant spreadsheets, and confirm the exact spreadsheet, recipient, role, and retention need before sharing, domain, anyone, owner, delete, or export actions. <br>
Risk: Spreadsheet updates or exports may affect business data or expose file contents if the wrong tab, range, recipient, or format is selected. <br>
Mitigation: Scope inputs to the minimum data needed, prefer schema-defined append and selected-field update actions, and review returned warnings or correction targets before retrying. <br>


## Reference(s): <br>
- [ClawHub Google Sheets skill page](https://clawhub.ai/agentpmt/skills/google-sheets) <br>
- [AgentPMT Google Sheets marketplace page](https://www.agentpmt.com/marketplace/google-sheets-api) <br>
- [Google Sheets action schema](artifact/schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, API calls, JSON] <br>
**Output Format:** [Markdown instructions with JSON action examples and schema references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Remote AgentPMT tool calls return JSON responses; CSV, TSV, PDF, XLSX, ODS, HTML, or ZIP exports may be stored in File Manager.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
