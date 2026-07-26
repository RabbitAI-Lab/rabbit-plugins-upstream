## Description: <br>
Data Audit helps agents generate local SHA256 directory snapshots, compare file changes, record local operation history, and validate data-directory health for audit preparation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cqdev-ai](https://clawhub.ai/user/cqdev-ai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, data engineers, and compliance teams use this skill to prepare audit evidence by snapshotting data directories, comparing changes over time, exporting reports, and checking directory health. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Snapshots and exported reports may include file names, paths, file metadata, and hashes from scanned directories. <br>
Mitigation: Run the skill only on intended directories and handle generated JSON or CSV reports according to the sensitivity of those paths and metadata. <br>
Risk: The log feature stores user-provided action text and targets locally in ~/.data-audit-logs. <br>
Mitigation: Avoid putting secrets or sensitive business details in log messages, and clear ~/.data-audit-logs when the retained history is no longer needed. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON, CSV] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON or CSV report outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local audit snapshots, comparison reports, health-check summaries, and operation-log history.] <br>

## Skill Version(s): <br>
1.1.0 (source: CHANGELOG.md, package.json, evidence.release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
