## Description:

Guides agents in inspecting and managing Cargo workspace models, datasets, columns, relationships, records, and SQL queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace administrators use this skill to discover Cargo storage schemas, manage models and relationships, query business records, and configure external data ingestion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Storage changes can alter or delete workspace data, including through relationship replacement.

Mitigation: Confirm the workspace and obtain approval before deletes or relationship replacements.

Risk: Exports can disclose workspace records.

Mitigation: Require confirmation before exporting data and limit exports to the intended records.

Risk: Webhook URLs containing API tokens can expose credentials through chat, logs, files, or shell history.

Mitigation: Confirm token creation and webhook setup; prefer header-based or secret-manager delivery, avoid recording token-bearing URLs, and rotate exposed tokens.

## Reference(s):

- [Cargo Storage skill on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-storage)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, SQL queries, Configuration instructions]

**Output Format:** [Markdown with CLI and SQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include JSON response examples and instructions for CSV or Parquet exports.]

## Skill Version(s):

1.2.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
