## Description:

Ingest pasted PC parts receipts or specs into Notion DIY_PC tables with classification, enrichment, follow-up, and upsert.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Notion power users use this skill to turn pasted PC parts receipts or specification notes into planned and applied upserts for DIY_PC Notion tables. It supports local extraction, optional web enrichment, duplicate-safe planning, and explicit apply flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write to and archive rows in configured Notion DIY_PC tables.

Mitigation: Use a Notion integration shared only with the intended DIY_PC targets, review plan output before running with --apply, and confirm archive or overwrite operations explicitly.

Risk: The required notion-api-automation dependency is unpinned and runs with the host environment.

Mitigation: Verify or pin the dependency before use and run the skill in an environment that does not contain unrelated secrets.

Risk: Optional web enrichment may disclose partial product text to external web providers.

Mitigation: Skip web_search and web_fetch when external enrichment is not desired and proceed with local extraction only.

Risk: The artifact includes a deprecated Python script with broader page-mutation behavior.

Mitigation: Use the JavaScript apply script for plan and apply operations, and do not use the deprecated Python script for real writes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/diy-pc-ingest)
- [Notion target IDs](references/notion-ids.md)
- [Example Notion target configuration](references/config.example.json)
- [Notion integrations](https://www.notion.so/my-integrations)
- [Notion API](https://api.notion.com/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSONL records and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Notion update plans by default; writes require an explicit apply command and configured Notion target IDs.]

## Skill Version(s):

2.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
