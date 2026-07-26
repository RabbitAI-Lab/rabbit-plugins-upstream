## Description: <br>
Generates SQL from natural-language requests for multiple database dialects, with explanations and optimization suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[g620710](https://clawhub.ai/user/g620710) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Data analysts, product managers, developers, and SQL learners use this skill to draft SQL queries from natural-language requests and schema context. It helps produce query text, execution explanations, and optimization guidance for supported relational database dialects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, schema text, and a user key may be sent to a default plain-HTTP backend. <br>
Mitigation: Use only non-sensitive schemas or sanitized examples, and configure a trusted HTTPS SQL_API_URL before sending real data or credentials. <br>
Risk: The API-key documentation is confusing about whether SQL_API_USER_KEY should contain a DeepSeek API key or a service user key. <br>
Mitigation: Do not put a real DeepSeek API key in SQL_API_USER_KEY unless the publisher clarifies the mismatch; use a dedicated credential and rotate it if exposed. <br>
Risk: Generated SQL may be incorrect or unsuitable for production data. <br>
Mitigation: Review generated SQL, validate it in a test environment first, and confirm query plans before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/g620710/skills/sql-query-generator) <br>
- [DeepSeek API base URL referenced by artifact](https://api.deepseek.com/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown or JSON-like text containing generated SQL, explanation, tables used, key points, and optimization tips.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and SQL_API_USER_KEY; SQL_API_URL may be configured to use a trusted endpoint.] <br>

## Skill Version(s): <br>
1.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
