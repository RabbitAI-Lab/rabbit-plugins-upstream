## Description: <br>
Privacy Check scans local files and directories for common personal and sensitive data patterns and produces masked findings in JSON, CSV, HTML, or terminal summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cqdev-ai](https://clawhub.ai/user/cqdev-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security reviewers, and data governance teams use this skill to scan files or directories for PII before data release, compliance review, or de-identification work. It helps produce masked findings and report artifacts for manual review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated reports can reveal sensitive structure even when findings are masked. <br>
Mitigation: Keep reports private, restrict access to intended reviewers, and avoid sharing or retaining them longer than necessary. <br>
Risk: Context lines and HTML reports can increase exposure from scanned content or filenames. <br>
Mitigation: Prefer the default no-context mode unless surrounding lines are necessary, and avoid HTML reports for untrusted scan inputs or filenames. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cqdev-ai/skills/privacy-check) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, JSON, CSV, HTML, Guidance] <br>
**Output Format:** [Markdown guidance with command examples and scanner reports in JSON, CSV, HTML, or terminal text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally against user-selected paths; reports contain masked findings and should be handled as sensitive.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence, package.json, changelog dated 2026-07-19) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
