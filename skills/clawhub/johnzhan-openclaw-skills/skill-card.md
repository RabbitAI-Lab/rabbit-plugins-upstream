## Description: <br>
Project-based conversation logging for OpenClaw that helps agents set up daily per-project chat history, read previous logs for continuity, and support manual history lookup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhan5331](https://clawhub.ai/user/zhan5331) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to configure project-scoped daily conversation logs, retrieve past logs by date or keyword, and carry context across sessions. It is most relevant for workspaces that run parallel projects and need isolated local history folders. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill directs agents to silently persist conversation summaries, which may capture sensitive project, customer, credential, or regulated data without clear consent. <br>
Mitigation: Enable only with explicit user or team consent; define log location, access, retention, deletion, and redaction rules before use. <br>
Risk: The skill directs agents to auto-load prior logs on the first daily turn, which may reintroduce stale, unrelated, or sensitive context. <br>
Mitigation: Make prior-log loading visible or opt-in, and let users inspect, limit, or skip loaded history. <br>
Risk: Main agents and sub-agents can write to project-scoped files, increasing exposure if folder mappings or permissions are wrong. <br>
Mitigation: Keep log folders least-privilege, verify project-folder mappings, and avoid logging secrets or regulated information. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhan5331/skills/johnzhan-openclaw-skills) <br>
- [Server-resolved GitHub source](https://github.com/zhan5331/Johnzhan-OpenClaw-Skills) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Files] <br>
**Output Format:** [Markdown instructions with shell command snippets and log-entry templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or append local Markdown log files when installed and configured.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
