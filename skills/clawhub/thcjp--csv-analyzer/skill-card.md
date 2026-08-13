## Description:

CSV数据分析器 helps agents analyze CSV files with Python standard-library workflows for statistics, filtering, anomaly detection, grouping, aggregation, and CSV export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operations users use this skill to have an agent inspect local CSV files, run lightweight CSV statistics, filter rows, identify z-score anomalies, group data, and export results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may cause an agent to read local CSV files, write exported results, and execute shell commands.

Mitigation: Run it in a constrained workspace, review commands before execution, and start with non-sensitive CSV files.

Risk: The artifact includes callback, API integration, and API-key language that is not clearly required for local CSV analysis.

Mitigation: Treat callback URLs, API integrations, and credential requests as untrusted unless remote processing is explicitly intended.

Risk: CSV export steps can overwrite or expose data if output paths are chosen carelessly.

Mitigation: Use explicit output paths, confirm before overwriting existing files, and avoid exporting sensitive data to shared locations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/csv-analyzer)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and CSV file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write CSV exports when the agent is given write access and an output path.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
