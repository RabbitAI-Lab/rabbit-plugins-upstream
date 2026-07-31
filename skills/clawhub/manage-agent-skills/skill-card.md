## Description: <br>
Audit and manage installed Agent Skills across Codex, Claude Code, GitHub Copilot CLI, OpenClaw, and Hermes by searching, enabling, disabling, and applying presets without deleting skill files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yunze7373](https://clawhub.ai/user/yunze7373) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to audit installed Agent Skills, resolve exact skill names, preview changes, and enable, disable, or apply presets across supported coding-agent hosts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Changing skill visibility can change which context and capabilities an agent can use. <br>
Mitigation: Run doctor or status first, use search to resolve exact skill names, and preview mutations with --dry-run before applying them. <br>
Risk: Broad selectors and presets can affect multiple skills at once. <br>
Mitigation: Review the selected platform, affected skills, target config file, and backup path before applying broad selectors such as all or preset entries. <br>
Risk: Configuration edits may require a new agent session or gateway restart to take effect. <br>
Mitigation: Report whether a new session or restart is required after each change and keep the generated backup for recovery. <br>


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


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands can preview mutations with --dry-run and can emit JSON for automation.] <br>

## Skill Version(s): <br>
0.1.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
