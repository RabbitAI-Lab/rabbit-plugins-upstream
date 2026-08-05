## Description: <br>
Select hook scope (plugin, project, global) by audience <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and plugin authors use this skill to choose whether Claude Code hooks belong at plugin, project, or global scope based on audience, persistence, and version-control needs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Logging hook examples can capture secrets, proprietary code, prompts, or sensitive file paths if copied without review. <br>
Mitigation: Redact sensitive values, log only the minimum necessary fields, restrict log file permissions, and define retention limits before enabling logging hooks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-hook-scope-guide) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>
- [Claude Code hooks documentation](https://docs.anthropic.com/en/docs/claude-code/hooks) <br>
- [Claude Code settings configuration](https://docs.anthropic.com/en/docs/claude-code/settings) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes scope-selection criteria, hook configuration examples, and security considerations.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
