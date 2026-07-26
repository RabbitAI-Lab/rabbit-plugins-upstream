## Description: <br>
Ai Sidekick provides OpenClaw agent configuration guidance for persona, user profile, persistent memory, safety practices, skill management, workflows, and token optimization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bbroot](https://clawhub.ai/user/bbroot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to configure an agent's behavior, memory files, safety checks, skill lifecycle practices, workflow routines, and context-management habits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables persistent local memory and backups of personal or project details without clear consent or retention controls. <br>
Mitigation: Install only when persistent memory is intended; decide in advance what may be written to USER.md, MEMORY.md, memory logs, and backups, and periodically inspect or delete retained files and archives. <br>
Risk: Memory files and backups may capture secrets or secret-adjacent locations. <br>
Mitigation: Avoid storing secret values or sensitive file locations in retained memory, and prefer secure storage such as environment variables or keychains for credentials. <br>


## Reference(s): <br>
- [Ai Sidekick on ClawHub](https://clawhub.ai/bbroot/skills/ai-sidekick) <br>
- [Server-resolved GitHub provenance](https://github.com/bbroot/ai-sidekick) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline code and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local files for persona, user profile, memory logs, backups, and workflow configuration.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
