## Description: <br>
Automates end-to-end anomaly detection for time-series data stored in KaiwuDB / KWDB. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kwdb](https://clawhub.ai/user/kwdb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, data engineers, and operators use this skill to inspect KaiwuDB / KWDB time-series tables for spikes, dips, drift, outliers, and other abnormal numeric telemetry patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests KWDB connection parameters and may handle sensitive database credentials or telemetry. <br>
Mitigation: Use a read-only KWDB account, avoid privileged production credentials, and delete retained local reports when they contain sensitive telemetry or business data. <br>
Risk: The bundled SQL runner is broad enough to modify data if unsafe SQL is approved or substituted. <br>
Mitigation: Verify every displayed SQL statement before execution and use least-privilege credentials that cannot create, drop, write, or mutate production data. <br>
Risk: Query results and reports may be written locally under /tmp. <br>
Mitigation: Treat generated files as sensitive artifacts and remove retained result or report files after review. <br>


## Reference(s): <br>
- [Workflow](references/workflow.md) <br>
- [Constraints](references/constraints.md) <br>
- [Error Handling](references/error-handling.md) <br>
- [Metadata Query](references/metadata-query.md) <br>
- [Column Comment](references/column-comment.md) <br>
- [TS Select](references/ts-select.md) <br>
- [Markdown Report Template](references/report-template.md) <br>
- [HTML Report Template](references/report-template-html.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kwdb/skills/kwdb-ts-anomaly-detection) <br>
- [KWDB Publisher Profile](https://clawhub.ai/user/kwdb) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with SQL and shell command blocks; optional Markdown, PDF, or HTML report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save query results and generated reports under /tmp during execution.] <br>

## Skill Version(s): <br>
1.2.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
