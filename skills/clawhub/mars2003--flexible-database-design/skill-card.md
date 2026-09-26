## Description:

Guides agents and users to design and implement SQLite flexible databases for semi-structured, multi-source archives such as personal knowledge bases, PDF/report archives, policy tracking, forms, aggregation, and event logs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mars2003](https://clawhub.ai/user/mars2003)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to have an agent plan, scaffold, validate, and operate a local SQLite archive for flexible records, dynamic fields, full-text search, batch import, export, and scenario-specific views.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Archived raw content and exported JSON or CSV files may contain sensitive user or project data.

Mitigation: Keep the database and exports in a project-specific path, protect local files, and review exported data before sharing or opening it in spreadsheet tools.

Risk: Untrusted schema files or extractor modules can change what the scripts execute or import.

Mitigation: Use only trusted FLEXIBLE_DB_SCHEMA paths and extractor modules, and review custom extractor code before enabling --llm-extract or FLEXIBLE_EXTRACTOR.

Risk: Optional Python packages used for document extraction or search can add supply-chain exposure.

Mitigation: Install optional packages in a virtual environment and pin package versions appropriate for the project.

Risk: SQLite FTS and LIKE fallback can miss Chinese terms or become slow on larger datasets.

Mitigation: Validate recall with representative phrases and consider jieba, Meilisearch, Elasticsearch, or another search layer for larger Chinese-language archives.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mars2003/skills/flexible-database-design)
- [README](README.md)
- [FlexibleDatabase API](docs/API.md)
- [Schema template](references/schema_template.sql)
- [Business view examples](references/view_examples.sql)
- [Chinese full-text search notes](references/fulltext_chinese.md)
- [Schema migration guide](references/migrations/README.md)
- [Financial reporting scenario](docs/examples/财务报表场景说明.md)
- [Questionnaire collection scenario](docs/examples/问卷收集场景适配.md)
- [Multi-source message aggregation scenario](docs/examples/多源消息聚合场景适配.md)
- [Foreign exchange database scenario](docs/examples/外汇数据库场景适配.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with SQL, Python, JSON, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local SQLite database files and JSON or CSV exports when the agent runs the bundled scripts.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
