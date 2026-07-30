## Description: <br>
Builds and debugs Notion API integrations for data sources, pages, blocks, properties, filters, files, webhooks, bulk imports, access setup, version migration, pagination, and error handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation engineers use this skill to design, troubleshoot, and operate Notion API integrations from code, curl, or SDK clients. It helps produce correct requests, migration plans, bulk-operation guidance, and debugging steps for Notion-specific API behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Notion integration token or OAuth access token that can reach whatever pages and capabilities the user grants. <br>
Mitigation: Use least-privilege Notion capabilities, keep tokens in environment or secret stores, rotate on personnel or cadence changes, and never save token values in local memory files. <br>
Risk: Local memory can retain Notion workspace structure such as schemas, IDs, mappings, run records, and selected contacts. <br>
Mitigation: Review ~/Clawic/data/notion-api-integration/ when workspace structure should not be retained, and store only pointers for secrets or signed file URLs. <br>
Risk: Bulk writes, schema changes, block deletion, archive actions, or multi-page overwrites can alter user content. <br>
Mitigation: Keep write_mode set to confirm-writes or dry-run for migrations, state affected counts before destructive actions, checkpoint bulk jobs, and use readonly_targets for objects that must not be modified. <br>
Risk: Pagination or rate-limit mistakes can silently drop rows, duplicate work, or trigger Notion 429 errors. <br>
Mitigation: Loop on has_more and next_cursor for list endpoints, pace requests around the configured rate_limit_rps, honor Retry-After, and use resumable checkpoints for long jobs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/notion-api-integration) <br>
- [Clawic skill homepage](https://clawic.com/skills/notion-api-integration) <br>
- [Skill overview and security notes](artifact/SKILL.md) <br>
- [Access, integrations, and OAuth guidance](artifact/auth.md) <br>
- [Database and schema guidance](artifact/databases.md) <br>
- [Bulk import, export, and backfill guidance](artifact/bulk.md) <br>
- [Pagination and resumability guidance](artifact/pagination.md) <br>
- [Error, retry, and rate-limit guidance](artifact/errors.md) <br>
- [Local memory template and secret handling](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline JSON, code, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Notion API request bodies, curl commands, SDK-oriented code snippets, configuration notes, runbooks, and migration or debugging plans.] <br>

## Skill Version(s): <br>
1.0.4 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
