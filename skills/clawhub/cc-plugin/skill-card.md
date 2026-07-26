## Description: <br>
Claude Code plugin lifecycle management for creating, installing, updating, maintaining, and troubleshooting plugins. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to manage Claude Code plugin authoring, marketplace setup, cache cleanup, local development reflection, HUD configuration, plugin clustering, and plugin troubleshooting workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide persistent changes to local Claude Code plugin state. <br>
Mitigation: Use dry-run paths first, review backups before enabling plugins, and inspect changes before applying them. <br>
Risk: Plugin troubleshooting guidance may involve running build code from installed plugin content. <br>
Mitigation: Run cache sync only for trusted marketplace content and inspect package.json or lockfiles before following npm install or build instructions. <br>


## Reference(s): <br>
- [Cc Plugin on ClawHub](https://clawhub.ai/drumrobot/skills/cc-plugin) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, code snippets, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Some workflows can propose or run local plugin-state changes; use dry-run options and review generated changes before applying them.] <br>

## Skill Version(s): <br>
0.5.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
