## Description: <br>
Manage Agent Skills across Codex, Claude Code, Copilot CLI, OpenClaw, and Hermes by auditing, searching, enabling, disabling, and applying presets without deletion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yunze7373](https://clawhub.ai/user/yunze7373) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to audit installed agent skills, find exact skill selectors, and safely enable, disable, or apply presets across supported coding-agent hosts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A requested enable or disable operation may affect the wrong host or skill when the platform or selector is ambiguous. <br>
Mitigation: Run status or doctor first, use search to resolve exact selectors, and pass an explicit --platform for mutations. <br>
Risk: Configuration changes may not match the user's intent until reviewed. <br>
Mitigation: Preview every mutation or preset with --dry-run before applying it. <br>
Risk: A host configuration change may need to be rolled back after testing. <br>
Mitigation: Keep the generated .manage-agent-skills.bak files until the new skill state is confirmed. <br>
Risk: Some host changes may not be visible in an already-running agent session. <br>
Mitigation: Start a new session or restart the affected gateway when the platform requires it. <br>


## Reference(s): <br>
- [Platform support](references/platforms.md) <br>
- [Preset file format](references/presets.md) <br>
- [Agent Skills specification](https://agentskills.io/specification) <br>
- [Codex app-server skill config methods](https://github.com/openai/codex/blob/main/codex-rs/app-server/README.md) <br>
- [Claude Code skills](https://code.claude.com/docs/en/skills) <br>
- [Claude Code skillOverrides](https://code.claude.com/docs/en/settings) <br>
- [GitHub Copilot CLI skill commands](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference) <br>
- [GitHub Copilot CLI disabledSkills](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference) <br>
- [OpenClaw skills](https://docs.openclaw.ai/tools/skills) <br>
- [OpenClaw configuration CLI](https://docs.openclaw.ai/cli/config) <br>
- [Hermes Agent skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/) <br>
- [Hermes Agent configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/) <br>
- [Hermes native skill configuration implementation](https://github.com/NousResearch/hermes-agent/blob/main/hermes_cli/skills_config.py) <br>
- [Gemini CLI extensions](https://google-gemini.github.io/gemini-cli/docs/extensions/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and optional JSON command output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled command can emit machine-readable JSON when --json is passed.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
