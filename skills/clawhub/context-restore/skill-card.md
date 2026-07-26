## Description: <br>
Restores saved conversation context by reading compressed context files, extracting recent operations, projects, and tasks, and returning structured summaries so users can resume work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexunitario-sketch](https://clawhub.ai/user/alexunitario-sketch) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to restore work state after a new or interrupted session by summarizing compressed context into current projects, pending tasks, recent operations, and optional timelines. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Saved context may contain private project details, secrets, or client data. <br>
Mitigation: Review the saved context source before use, run restoration only on trusted local files, and avoid sharing generated reports without checking their contents. <br>
Risk: Optional auto mode and cron setup can create recurring monitoring behavior. <br>
Mitigation: Use the basic restore command by default; enable --auto or --install-cron only after reviewing the context file paths, generated monitor script, and log destinations. <br>
Risk: External notification hooks may run if a notification script exists in the expected path. <br>
Mitigation: Inspect or remove any notification script before enabling automated monitoring, especially when restored context may include sensitive work details. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alexunitario-sketch/skills/context-restore) <br>
- [README](artifact/README.md) <br>
- [Usage guide](artifact/docs/USAGE.md) <br>
- [API reference](artifact/docs/API.md) <br>
- [Design reference](artifact/references/design.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text reports, JSON summaries, and inline shell/Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports minimal, normal, and detailed restoration levels; optional file output and platform-specific message chunking are documented.] <br>

## Skill Version(s): <br>
1.1.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
