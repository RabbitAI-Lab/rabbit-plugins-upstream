## Description: <br>
Agent Config helps agents make structured, low-duplication updates to OpenClaw context files such as AGENTS.md, SOUL.md, TOOLS.md, MEMORY.md, and HEARTBEAT.md. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thatguysizemore](https://clawhub.ai/user/thatguysizemore) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and OpenClaw operators use this skill when they want an agent to update its own workspace configuration, behavior rules, memory procedures, safety guidance, or tool conventions while checking file fit, size, duplication, and rollback needs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can enable persistent changes to an agent's own behavior, configuration, and related logs beyond the most visible context files. <br>
Mitigation: Require explicit approval before edits to AGENTS.md, SOUL.md, TOOLS.md, MEMORY.md, HEARTBEAT.md, BOOTSTRAP.md, daily logs, templates, skills, or decision and failure logs. <br>
Risk: Configuration updates can introduce unwanted instructions, sensitive information, duplication, or oversized startup context. <br>
Mitigation: Review proposed diffs, scan changed context files, and periodically audit those files for sensitive information or unwanted behavior changes. <br>


## Reference(s): <br>
- [Agent Config skill page](https://clawhub.ai/thatguysizemore/skills/agent-config) <br>
- [OpenClaw Workspace File Map](artifact/references/file-map.md) <br>
- [Change Protocol](artifact/references/change-protocol.md) <br>
- [Claude Instruction Patterns](artifact/references/claude-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline command and edit examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose persistent edits to agent context and configuration files when the runtime grants file access.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
