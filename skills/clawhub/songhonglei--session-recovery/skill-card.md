## Description: <br>
Session Recovery recovers lost agent session content and file changes from on-disk OpenClaw conversation logs with streaming search, file-operation extraction, edit replay, and guarded restore workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to locate lost OpenClaw agent sessions, identify which session changed a file, extract write/edit operations, and recover or rebuild files from local JSONL logs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill searches local OpenClaw session logs, which may contain sensitive prompts, code, or file contents. <br>
Mitigation: Use narrow keywords, short date windows, and the default single-agent scope before broadening searches. <br>
Risk: Restore operations can overwrite existing files when explicitly confirmed. <br>
Mitigation: Review target paths and recovered content before using restore commands with --yes; restore to a separate path when unsure. <br>
Risk: Full-content output can expose large or sensitive recovered file content in the terminal or agent transcript. <br>
Mitigation: Prefer path filters, previews, JSON output, or restore-to-disk workflows, and use --show-content only when necessary. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [ClawHub skill page](https://clawhub.ai/songhonglei/session-recovery) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; scripts can emit plain text or JSON and restore recovered files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local filesystem session logs and supports scoped search by agent, date window, keyword, session ID, and file path.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and SKILL.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
