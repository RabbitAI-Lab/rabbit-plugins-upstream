## Description: <br>
Download workflow run results, export segment data, and monitor run metrics using the Cargo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cargo-ai](https://clawhub.ai/user/cargo-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and Cargo workspace users use this skill to measure workflow run health, count errors, download run or batch results, and export segment data. It is for analytics and retrieval workflows, not root cause diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cargo analytics commands can retrieve downloaded runs, segment exports, signed URLs, and records that may contain sensitive business data. <br>
Mitigation: Use Cargo permissions, filters, date ranges, and row limits to keep exports authorized and minimal. <br>
Risk: Broad analytics queries or downloads can expose more workspace data than intended. <br>
Mitigation: Prefer scoped workflow, batch, status, and date filters before downloading or exporting results. <br>


## Reference(s): <br>
- [Cargo Skills Repository](https://github.com/getcargohq/cargo-skills) <br>
- [Cargo Analytics on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-analytics) <br>
- [Response shapes](references/response-shapes.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Run analytics examples](references/examples/run-analytics.md) <br>
- [Data export examples](references/examples/exports.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Analysis, Files, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference Cargo CLI outputs, downloaded run or batch data, signed URLs, and exported CSV or JSON payloads.] <br>

## Skill Version(s): <br>
1.4.2 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
