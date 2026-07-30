## Description: <br>
Audit, search, enable, disable, and apply presets to installed Agent Skills without deleting their files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yunze7373](https://clawhub.ai/user/yunze7373) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to audit installed Agent Skills and safely enable, disable, search, or apply presets across Codex, Claude Code, GitHub Copilot CLI, OpenClaw, and Hermes without deleting skill files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change which installed skills supported agent platforms load. <br>
Mitigation: Run doctor or status first, use --dry-run before mutation, and review the listed config path and backup path before applying changes. <br>
Risk: Configuration changes can affect current or future agent sessions. <br>
Mitigation: Keep the generated .manage-agent-skills.bak backup and start a new session or restart the affected gateway when the platform requires it. <br>
Risk: Broad selectors can disable many skills at once. <br>
Mitigation: Use exact skill names, group selectors, or path selectors deliberately; protected management skills require --force before broad disabling. <br>


## Reference(s): <br>
- [Platform support](references/platforms.md) <br>
- [Preset file format](references/presets.md) <br>
- [Agent Skills specification](https://agentskills.io/specification) <br>
- [Codex app-server skill config methods](https://github.com/openai/codex/blob/main/codex-rs/app-server/README.md) <br>
- [Claude Code skills](https://code.claude.com/docs/en/skills) <br>
- [Claude Code settings](https://code.claude.com/docs/en/settings) <br>
- [GitHub Copilot CLI skill commands](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference) <br>
- [GitHub Copilot CLI configuration](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference) <br>
- [OpenClaw skills](https://docs.openclaw.ai/tools/skills) <br>
- [OpenClaw configuration CLI](https://docs.openclaw.ai/cli/config) <br>
- [Hermes Agent skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/) <br>
- [Hermes Agent configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/) <br>
- [Hermes native skill configuration implementation](https://github.com/NousResearch/hermes-agent/blob/main/hermes_cli/skills_config.py) <br>
- [Gemini CLI extensions](https://google-gemini.github.io/gemini-cli/docs/extensions/) <br>
- [ClawHub skill page](https://clawhub.ai/yunze7373/skills/manage-agent-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include dry-run previews, affected skill lists, config paths, backup paths, and restart or new-session guidance.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
