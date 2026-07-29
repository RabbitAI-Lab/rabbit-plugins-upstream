## Description: <br>
Audit, search, enable, disable, and apply presets to installed Agent Skills without deleting their files across Codex, Claude Code, GitHub Copilot CLI, OpenClaw, and Hermes Agent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yunze7373](https://clawhub.ai/user/yunze7373) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to inspect installed Agent Skills, reduce idle skill context, keep rarely used skills manual, and safely toggle skill availability across supported coding-agent platforms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change which Agent Skills are active in future agent sessions. <br>
Mitigation: Use dry-run first, review the affected skills and backup path, and apply exact platform-specific selectors deliberately. <br>
Risk: Preset files and the all selector can modify multiple skill states at once. <br>
Mitigation: Review preset contents before applying them, run one platform per invocation, and use force only for an explicit disable-all request. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/yunze7373/manage-agent-skills/tree/main/skills/manage-agent-skills) <br>
- [ClawHub skill page](https://clawhub.ai/yunze7373/skills/manage-agent-skills) <br>
- [Platform support](references/platforms.md) <br>
- [Preset file format](references/presets.md) <br>
- [Agent Skills specification](https://agentskills.io/specification) <br>
- [Claude Code skills](https://code.claude.com/docs/en/skills) <br>
- [GitHub Copilot CLI skill commands](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference) <br>
- [OpenClaw skills](https://docs.openclaw.ai/tools/skills) <br>
- [Hermes Agent skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports platform, affected skills, config or native command used, backup path, and whether a new session or restart is required.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
