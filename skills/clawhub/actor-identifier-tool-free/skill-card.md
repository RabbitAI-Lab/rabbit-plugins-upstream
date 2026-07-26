## Description: <br>
Provides privacy-first, zero-dependency Git repository collaboration analysis for individual developers, producing repository-level aggregate reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers use this skill to inspect Git repository collaboration patterns, including commit timing, churn, conventional commit compliance, and file-level bus-factor signals. It is intended for repository-level aggregate analysis rather than personal ranking or performance review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports conflicting behavior that could allow write-like actions or network diagnostics despite the skill claiming read-only, offline operation. <br>
Mitigation: Review before installing, run dry-run first, enforce the documented read-only git command whitelist, and avoid save/export, modify/reset/import, ping, or network behavior unless explicitly approved. <br>
Risk: Local Git analysis can expose repository-sensitive information such as commit messages, file paths, and contributor names. <br>
Mitigation: Use the skill only on repositories the user is authorized to analyze, keep processing local, and limit outputs to aggregate repository-level reporting with sensitive values redacted where applicable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/actor-identifier-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with inline shell command previews] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Repository-level aggregate Git metrics; dry-run command review is supported.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
