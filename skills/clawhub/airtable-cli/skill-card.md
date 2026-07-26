## Description: <br>
Read, create, update, delete, and search Airtable records; list bases and tables, filter records, and batch upsert. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operations teams, no-code builders, and automation agents use this skill to work with Airtable bases from a command line, including schema inspection, record CRUD, filtering, CSV import/export, and batch upsert workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The tool can operate on Airtable bases available to the configured token. <br>
Mitigation: Use a least-privileged Airtable personal access token scoped only to the bases and operations needed. <br>
Risk: Create, update, upsert, import, and delete commands can change or remove Airtable records, including in bulk. <br>
Mitigation: Verify base, table, and record IDs before write or delete operations, and test or back up production data before bulk changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/itspremkumar/skills/airtable-cli) <br>
- [Artifact README](artifact/README.md) <br>
- [Airtable personal access tokens](https://airtable.com/create/tokens) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, code, files] <br>
**Output Format:** [Markdown guidance with CLI commands; runtime command output may be text, JSON, or CSV.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses AIRTABLE_API_KEY for authenticated Airtable API operations.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata; artifact frontmatter reports 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
