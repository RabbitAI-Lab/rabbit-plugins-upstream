## Description: <br>
Select hook scope (plugin, project, global) by audience. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to choose whether Claude Code hooks belong at plugin, project, or global scope based on audience, persistence, and version-control needs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Global hooks can affect all Claude Code sessions when a reader applies the guidance manually. <br>
Mitigation: Review the intended scope before adding a hook, test global hooks carefully, and prefer plugin or project scope when the behavior should be limited. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-abstract-hook-scope-guide) <br>
- [Claude Night Market Abstract Plugin](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>
- [Claude Code Hooks Documentation](https://docs.anthropic.com/en/docs/claude-code/hooks) <br>
- [Claude Code Settings Configuration](https://docs.anthropic.com/en/docs/claude-code/settings) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration, code] <br>
**Output Format:** [Markdown guidance with JSON, shell, and Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; no hooks are installed or executed by the skill.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
