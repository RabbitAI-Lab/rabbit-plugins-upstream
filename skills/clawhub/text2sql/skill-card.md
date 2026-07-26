## Description: <br>
Supports generating SQL queries from natural-language questions by guiding database or spreadsheet configuration, topic setup, and SQL generation through AskSqlAI services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[asksqlai](https://clawhub.ai/user/asksqlai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and data teams use this skill to configure structured data sources, define topic-specific semantic YAML files, and ask natural-language questions that produce SQL statements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may send natural-language questions, topic YAML, database metadata, sampled data values, or Excel files to asksql.ai. <br>
Mitigation: Use only with data approved for that service, remove sensitive values before configuration, and obtain explicit user consent before remote calls. <br>
Risk: Database credentials are handled during configuration and may be stored in a local JSON file. <br>
Mitigation: Use least-privilege read-only database accounts, avoid production credentials, and delete or protect generated configuration files after use. <br>
Risk: Generated SQL can be incorrect or unsuitable for direct execution. <br>
Mitigation: Review generated SQL before running it, test against non-production data first, and enforce database-side permissions. <br>


## Reference(s): <br>
- [Open Semantic Interchange Field Specification](references/open_semantic_interchange_description.md) <br>
- [TEXT2SQL ClawHub release page](https://clawhub.ai/asksqlai/skills/text2sql) <br>
- [AskSQL AI service](https://asksql.ai/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON status output, YAML topic configuration, and generated SQL text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates local output files for database configuration, table metadata, and topic YAML; SQL generation calls a remote AskSQL API.] <br>

## Skill Version(s): <br>
1.0.2 (source: server evidence release version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
