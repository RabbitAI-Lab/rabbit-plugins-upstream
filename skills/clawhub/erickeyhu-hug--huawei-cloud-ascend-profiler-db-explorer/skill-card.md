## Description: <br>
Converts natural language profiling questions into SQL for Ascend PyTorch Profiler and msprof SQLite databases, including operator time, communication, dispatch, and schema analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and performance engineers use this skill to inspect Ascend profiler databases, generate bounded SQL drafts, compare operator, communication, and dispatch timings, and summarize bottlenecks from query results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be triggered for unrelated SQL or schema questions because its trigger terms are broad. <br>
Mitigation: Use it only for Ascend PyTorch Profiler or msprof profiling database analysis, and confirm the target database path before running queries. <br>
Risk: Local profiler databases can contain performance details that users may not intend to share broadly. <br>
Mitigation: Provide only profiler database paths intended for analysis and review generated SQL before execution. <br>


## Reference(s): <br>
- [Profiler DB Data Format](references/profiler_db_data_format.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Verification Methods](references/verification-method.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown with SQL and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes generated SQL, returned-row summaries, selected result previews, schema guidance, and performance diagnosis recommendations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
