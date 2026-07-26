## Description: <br>
Guides agents through Salesforce REST, Bulk, Composite, and Metadata API work, including SOQL, record CRUD, upserts, OAuth, sync, migrations, reports, error handling, and guarded Salesforce writes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to query, load, export, sync, and troubleshoot Salesforce data and integrations while choosing the appropriate API, authentication flow, limits, and safety checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Salesforce API credentials can authorize reads, writes, exports, and metadata operations in the configured org. <br>
Mitigation: Use least-privilege Salesforce permissions, confirm destructive or large-scale write actions before execution, and rehearse bulk or metadata changes in a sandbox when applicable. <br>
Risk: Local operational notes can expose sensitive customer, org, or credential details if copied directly into shared files. <br>
Mitigation: Store pointers to secrets instead of secret values, keep tokens and unnecessary PII out of ~/Clawic/data, and review shared contacts, projects, and finances entries before saving. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/salesforce-api-integration) <br>
- [Skill homepage](https://clawic.com/skills/salesforce-api-integration) <br>
- [Authentication guidance](auth.md) <br>
- [SOQL and SOSL guidance](soql.md) <br>
- [Record CRUD guidance](records.md) <br>
- [Bulk API guidance](bulk.md) <br>
- [Composite API guidance](composite.md) <br>
- [Metadata guidance](metadata.md) <br>
- [Error handling guidance](errors.md) <br>
- [Limits guidance](limits.md) <br>
- [Sync guidance](sync.md) <br>
- [Migration guidance](migration.md) <br>
- [Apex REST and actions guidance](apex.md) <br>
- [Files guidance](files.md) <br>
- [Reports guidance](reports.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API Calls] <br>
**Output Format:** [Markdown guidance with SOQL, SOSL, REST, curl, and language-specific code examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use Salesforce environment variables and may update local operational notes under ~/Clawic/data when durable Salesforce context is produced.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
