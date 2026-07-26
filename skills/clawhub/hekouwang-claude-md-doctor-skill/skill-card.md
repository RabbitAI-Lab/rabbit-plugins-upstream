## Description: <br>
Audits project CLAUDE.md files as runtime configuration, returns a scorecard with prioritized repair guidance, and can help apply confirmed fixes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huiyonghkw](https://clawhub.ai/user/huiyonghkw) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and teams use this skill to review CLAUDE.md files for context hygiene, actionable project instructions, secret-safety checks, and prioritized improvements before using them in Claude Code. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Suggested repairs can change persistent project instructions that affect future agent sessions. <br>
Mitigation: Review proposed edits to CLAUDE.md and MEMORY.md before accepting them, and keep the audit report separate from approved configuration changes. <br>
Risk: Hook configuration changes can influence future tool execution. <br>
Mitigation: Inspect any proposed .claude/settings.json hook commands and approve only commands whose scope and side effects are understood. <br>
Risk: The checker combines deterministic heuristics with qualitative review, so a score can miss project-specific context. <br>
Mitigation: Treat the scorecard as review guidance and verify important recommendations against the project's tests, linters, and security requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huiyonghkw/skills/hekouwang-claude-md-doctor-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown or text report with optional JSON output and inline code or shell-command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can propose edits to CLAUDE.md, MEMORY.md, and hook configuration after user confirmation.] <br>

## Skill Version(s): <br>
1.2.2 (source: frontmatter, changelog, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
