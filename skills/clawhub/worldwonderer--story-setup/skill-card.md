## Description: <br>
Story Setup deploys a web-fiction writing toolbox across Claude Code, OpenCode, Codex, ZCode, OpenClaw, Reasonix, and generic agent environments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[worldwonderer](https://clawhub.ai/user/worldwonderer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, writing teams, and developers use this skill to set up project-level story-writing agents, commands, rules, hooks, and reference material for supported CLI and file-based agent environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs persistent project-level automation that can change future agent behavior. <br>
Mitigation: Install only when the project needs this writing toolbox, review the selected target platforms, and inspect hook and configuration changes before trusting them. <br>
Risk: Browser-CDP features can interact with an existing logged-in Chrome session. <br>
Mitigation: Disable or avoid browser-CDP use unless the user explicitly accepts authenticated browser control in that environment. <br>
Risk: Automatic update behavior and managed hooks can introduce unexpected changes after setup. <br>
Mitigation: Consider disabling the automatic update check and re-review managed hooks, commands, and config files after upgrades. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/worldwonderer/skills/story-setup) <br>
- [OpenClaw Metadata Source](https://github.com/worldwonderer/oh-story-claudecode) <br>
- [Skill Definition](SKILL.md) <br>
- [Upgrade Notes](UPGRADING.md) <br>
- [Agent Reference Bundle](references/agent-references/) <br>
- [Hook Templates](references/templates/hooks/) <br>
- [Codex Hook Configuration](references/codex/hooks/hooks.json) <br>
- [OpenCode Plugin Template](references/opencode/plugin.ts) <br>
- [ZCode Hook Configuration](references/zcode/hooks/hooks.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code, shell, and configuration file instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or merge project-level agent, hook, rule, command, and reference files depending on the selected target environment.] <br>

## Skill Version(s): <br>
1.1.14 (source: ClawHub release metadata; artifact frontmatter reports 1.2.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
