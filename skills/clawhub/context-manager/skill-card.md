## Description: <br>
AI-powered context management for OpenClaw sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[plgonzalezrx8](https://clawhub.ai/user/plgonzalezrx8) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to inspect session token usage, generate summaries, and optionally compress long-running sessions while preserving a local backup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist sensitive session transcripts and repository context in local generated files. <br>
Mitigation: Avoid using it on sessions containing secrets or highly sensitive project data unless generated artifacts are reviewed, redacted, or deleted. <br>
Risk: Replacement mode can reset a session and continue from an AI-generated summary that may omit or misstate important context. <br>
Mitigation: Run summary generation without replacement first, confirm the backup exists, and review the summary before using replace/reset behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/plgonzalezrx8/skills/context-manager) <br>
- [Skill documentation](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files] <br>
**Output Format:** [CLI text with optional Markdown summary and local backup files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create AI summary and session-backup files under memory/compressed/ when replacement mode is used.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
