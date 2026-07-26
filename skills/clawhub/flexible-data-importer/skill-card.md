## Description: <br>
AI-powered ingestion of CSV, JSON, and XLSX files with automatic schema generation and Supabase database integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sschepis](https://clawhub.ai/user/sschepis) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and data engineers use this skill to import CSV, JSON, and XLSX datasets into Supabase while using an LLM to propose schemas, relationships, and type mappings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for powerful Supabase credentials for schema creation. <br>
Mitigation: Use a staging or dedicated Supabase project, avoid production service-role keys where possible, back up data before imports, and rotate any keys used. <br>
Risk: Local records or samples may be sent to the LLM provider and Supabase during import. <br>
Mitigation: Do not import confidential or regulated datasets unless that external processing is accepted and approved. <br>
Risk: The published package contents may differ from the reviewed metadata. <br>
Mitigation: Verify the actual npm package contents before installing or running the importer. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sschepis/skills/flexible-data-importer) <br>
- [Publisher profile](https://clawhub.ai/user/sschepis) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, code, guidance] <br>
**Output Format:** [Markdown with inline shell commands and TypeScript examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a source file path, Supabase project credentials, and an LLM API key.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release, package.json, SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
