## Description: <br>
Dragon Writer helps agents create, continue, audit, revise, and roll back file-backed long-form fiction projects while maintaining story state, canon, continuity, and a local progress dashboard. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragon-qx](https://clawhub.ai/user/dragon-qx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers and writing-assistant agents use Dragon Writer to manage long-form fiction projects across sessions, including new-book setup, chapter continuation, import, redirect, rewrite, rollback, continuity audit, and dashboard review. It is intended for projects that need persistent story files rather than one-off short-form generation or ordinary copy editing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can silently contact a remote service and replace its installed files before handling the writing task. <br>
Mitigation: Install only when the publisher and update source are trusted; consider disabling automatic updates in artifact/_meta.json or removing the startup update step before use. <br>
Risk: The skill is expected to create and modify files inside novel project folders. <br>
Mitigation: Review proposed file changes, keep project backups or snapshots, and use rollback workflows when revising existing chapters. <br>
Risk: The local dashboard may remember a browser folder handle after the user grants access. <br>
Mitigation: Grant access only to the intended project folder and revoke browser site permissions when persistent access is no longer desired. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dragon-qx/skills/d-writer) <br>
- [README](README.md) <br>
- [File Contract](references/file-contract.md) <br>
- [Workflow Guide](references/workflow.md) <br>
- [Audit Dimensions](references/audit-dimensions.md) <br>
- [Templates](references/templates.md) <br>
- [File Contract Schema](https://dragon-writer.github.io/schemas/file-contract.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code and shell command snippets; file edits and generated project files when used by an agent] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or modify structured novel project files and dashboard assets] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
