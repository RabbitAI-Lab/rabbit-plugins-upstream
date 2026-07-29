## Description: <br>
Helps agents query, load, sync, and troubleshoot Salesforce data through Salesforce REST, Bulk, Composite, Metadata, and related APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and integration engineers use this skill to plan and execute Salesforce API work, including SOQL and SOSL queries, record CRUD and upserts, bulk loads, migrations, sync designs, OAuth setup, metadata operations, and API error troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Salesforce credentials, org identifiers, schema notes, contacts, job IDs, or business context could be exposed if broad tokens or local notes are mishandled. <br>
Mitigation: Keep integration-user permissions narrow, use environment or secret-manager pointers for credentials, and review local Clawic notes before sharing or publishing outputs. <br>
Risk: Deletes, hard deletes, mass updates, metadata deploys, or high-volume jobs can affect production data or consume shared Salesforce API allocation. <br>
Mitigation: Use sandbox rehearsal and require explicit confirmation with a stated blast radius before production deletes, hard deletes, mass updates, or metadata deploys. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/salesforce-api-integration) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/ivangdavila) <br>
- [Clawic skill page](https://clawic.com/skills/salesforce-api-integration) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline SOQL, JSON, and bash/curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses SF_ACCESS_TOKEN and SF_INSTANCE_URL; may reference local Clawic notes but does not store credentials.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
