## Description: <br>
Operation Tracer records tool calls, LLM calls, errors, and context compression events in SQLite for post-run analysis and performance tuning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to persist local traces of agent operations, inspect slow or failed operations, and export trace data for debugging and optimization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local trace records may include sensitive tool parameters, file paths, results, and errors. <br>
Mitigation: Install only when local operation logging is intended; restrict metadata passed to the tracer and use cleanup when traces should not be retained. <br>


## Reference(s): <br>
- [Trace Schema](references/trace_schema.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/paudyyin/skills/operation-tracer) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, CSV, Code] <br>
**Output Format:** [SQLite trace records, analysis summaries, and JSON or CSV exports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local trace data to traces/agent_traces.db by default.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
