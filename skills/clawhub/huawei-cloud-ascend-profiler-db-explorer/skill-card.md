## Description: <br>
Converts natural language questions into safe executable SQL for querying Ascend PyTorch Profiler and msprof SQLite databases for operator, communication, dispatch, and schema performance analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and performance engineers use this skill to inspect Ascend profiler databases, generate bounded SQL for common operator, communication, and dispatch questions, and interpret profiling results for bottleneck analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated SQL can be executed against local SQLite database files without an enforced read-only boundary. <br>
Mitigation: Review SQL before execution, run against the intended Ascend/msprof profiler database only, and use read-only database access where available. <br>
Risk: Broad trigger terms such as sqlite, table, and schema may activate the skill for unrelated or sensitive databases. <br>
Mitigation: Use explicit prompts that include the profiler database path and analysis goal, and avoid using this skill with unrelated or sensitive databases. <br>
Risk: Large result sets or file exports can expose more profiling data than needed. <br>
Mitigation: Keep queries aggregated or limited, prefer the documented LIMIT patterns, and export CSV only when the user explicitly requests file output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-ascend-profiler-db-explorer) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Profiler DB Data Format](artifact/references/profiler_db_data_format.md) <br>
- [Acceptance Criteria](artifact/references/acceptance-criteria.md) <br>
- [Verification Method](artifact/references/verification-method.md) <br>
- [Troubleshooting](artifact/references/troubleshooting.md) <br>
- [Schema extraction helper](artifact/scripts/get_schema.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown analysis with SQL snippets, shell command examples, and tabular query result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces read-oriented SQL drafts, schema lookup commands, profiling result summaries, and optimization suggestions for Ascend profiler databases.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
