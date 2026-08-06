## Description: <br>
Implements structured usage logging and audit trails for cost and session tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add session-aware JSONL usage logs, audit trails, cost tracking, and operational analytics to agent or plugin workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local usage logs can capture secrets, personal data, or sensitive operational metadata. <br>
Mitigation: Define allowed metadata before enabling logging, avoid secrets and personal data, and review log contents before sharing or exporting them. <br>
Risk: Operational logs may persist longer than needed in local JSONL files. <br>
Mitigation: Set a retention or cleanup policy for local usage logs and session files. <br>
Risk: The full plugin experience depends on the external leyline plugin beyond this documentation-style skill. <br>
Mitigation: Review the external plugin and its permissions before installing or relying on the full plugin experience. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-usage-logging) <br>
- [Leyline plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>
- [Log Formats](artifact/modules/log-formats.md) <br>
- [Session Patterns](artifact/modules/session-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline JSON, Python, YAML, and shell examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance centers on local JSONL logs, session metadata, query patterns, and integration snippets.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
