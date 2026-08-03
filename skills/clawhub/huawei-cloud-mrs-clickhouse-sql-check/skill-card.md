## Description: <br>
This skill statically checks ClickHouse SQL for version-specific syntax and MRS development specification issues across ClickHouse 24.8, 23.3, and 22.3. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and data engineers use this skill to review ClickHouse SQL before execution, checking version-specific syntax compatibility and MRS development specification rules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SQL text may be echoed in generated reports or shared terminal and CI logs. <br>
Mitigation: Do not submit production secrets or credentials in SQL; sanitize statements before sharing reports. <br>
Risk: The checker is a local static analyzer and may not validate every ClickHouse statement type or runtime behavior. <br>
Mitigation: Use it as a pre-review aid and confirm critical SQL against the target ClickHouse environment and release documentation. <br>


## Reference(s): <br>
- [ClickHouse 24.8 DDL Grammar Reference](references/ddl_grammar.md) <br>
- [ClickHouse 24.8 DML and Miscellaneous Grammar Reference](references/dml_misc_grammar.md) <br>
- [ClickHouse 24.8 SELECT Grammar Reference](references/select_grammar.md) <br>
- [ClickHouse Token Types Reference](references/token_types.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-mrs-clickhouse-sql-check) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with summary, violation detail, fix suggestion, and original SQL sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs local static checks with a selected ClickHouse version and check mode.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
