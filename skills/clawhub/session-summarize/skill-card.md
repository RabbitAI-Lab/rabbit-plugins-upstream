## Description: <br>
Summarize helps Codex produce evidence-first task summaries, compact-context outputs, handoff prompts, diagnostics, and explicit project-local saved handoffs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gtbwpkwjnb-alt](https://clawhub.ai/user/gtbwpkwjnb-alt) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents working in Codex use this skill to turn current-session evidence into concise status summaries, context compaction, handoff reports, and diagnostics. The skill is read-only by default and saves project-local handoff files only when the user explicitly asks to save. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional one-line Bash installer performs remote shell installation and can delete and reclone an existing install when update fails. <br>
Mitigation: Review or avoid the installer; prefer a pinned release or inspected local copy, and back up any local changes before running the updater. <br>
Risk: Explicit save mode writes project-local handoff files that may preserve sensitive task context if used carelessly. <br>
Mitigation: Use normal summaries in read-only mode by default and run save mode only when a project-local handoff is intentional and has been reviewed. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [Skill Definition](SKILL.md) <br>
- [Changelog](references/CHANGELOG.md) <br>
- [Save and Restore Operations](references/operations.md) <br>
- [Recommendation Rules](references/recommendations.md) <br>
- [Layered Handoff](references/layered-handoff.md) <br>
- [History Diagnostics](references/history-diagnostics.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries and handoff reports, with optional shell commands or configuration guidance when supported by the session evidence.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default behavior is read-only; saved handoff files are produced only after explicit user request.] <br>

## Skill Version(s): <br>
11.0.0 (source: artifact/VERSION, artifact/manifest.json, evidence.release.version, references/CHANGELOG.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
