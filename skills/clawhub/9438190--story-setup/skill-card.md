## Description: <br>
Deploys web-novel writing workflow infrastructure, including hooks, rules, agents, and project guidance files, into a user's project directory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[9438190](https://clawhub.ai/user/9438190) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users setting up Chinese web-novel writing projects use this skill to install Claude Code and OpenCode agents, rules, hooks, and reference bundles for story planning, drafting, review, and consistency checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs persistent writing-workflow hooks and local automation files. <br>
Mitigation: Review the generated settings, plugin, command files, and git hook before installation, and install only in projects where these workflow controls are intended. <br>
Risk: Browser CDP automation can act through an already logged-in Chrome session. <br>
Mitigation: Use browser automation only with accounts and browser profiles appropriate for the task, and avoid running it in sessions containing unrelated sensitive access. <br>
Risk: OpenCode and Claude automation may continue to affect project behavior after setup. <br>
Mitigation: Keep the deployed hook and plugin files visible in review, and remove or disable them when the writing workflow is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/9438190/skills/story-setup) <br>
- [OpenClaw metadata link](https://github.com/worldwonderer/oh-story-claudecode) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Upgrade guide](artifact/UPGRADING.md) <br>
- [OpenCode plugin controls](artifact/references/opencode/plugin.ts) <br>
- [Claude hook settings](artifact/references/templates/settings-hooks.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance plus project file and configuration changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or merges local Claude Code and OpenCode project infrastructure, including persistent hooks and automation files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter version is 1.2.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
