## Description: <br>
Runs a CRM for contacts, companies, deals, pipeline stages, follow-ups, imports, hygiene, and privacy-aware record keeping. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, founders, freelancers, fundraisers, and sales teams use this skill to set up, rescue, and operate a CRM across local files, SQLite, or external CRM workflows. It helps maintain contacts, deals, follow-ups, imports, exports, pipeline reviews, forecasts, deduplication, suppression lists, and retention decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify or delete local CRM and shared contact records. <br>
Mitigation: Require explicit confirmation for deletes, merges, imports, migrations, shared-contact edits, and file splits; prefer archive over hard delete. <br>
Risk: Bulk imports, migrations, merges, and local database edits can cause irreversible data loss or duplicate records. <br>
Mitigation: Create and verify dated backups before bulk operations, run dry runs for imports, and record row counts and rejected records after each pass. <br>
Risk: CRM records contain personal data and suppression requests that may be mishandled across backups, exports, and shared contact files. <br>
Mitigation: Read the do-not-contact list before recommending outreach, suppress before deletion, enumerate every copy of a record, and prune backups according to the retention policy. <br>
Risk: Inbox sync or enrichment can ingest or expose personal correspondence and third-party contact data without adequate authorization. <br>
Mitigation: Avoid inbox sync unless authorization and retention rules are clear; store metadata rather than message bodies by default, and keep credentials in environment variables or secret managers. <br>


## Reference(s): <br>
- [ClawHub CRM Skill Page](https://clawhub.ai/ivangdavila/skills/crm) <br>
- [Clawic CRM Skill Page](https://clawic.com/skills/crm) <br>
- [CRM Skill Instructions](artifact/SKILL.md) <br>
- [Privacy Guidance](artifact/privacy.md) <br>
- [Working File Templates](artifact/memory-template.md) <br>
- [Imports, Exports, and Migrations](artifact/import.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with tables, checklists, local record updates, and occasional code, SQL, or shell snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local configuration and data paths under ~/Clawic/data/ for CRM, contacts, projects, and profile information.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
