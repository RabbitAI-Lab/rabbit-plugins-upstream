## Description: <br>
Meta-skill for building and managing agent persona skill packs (instruction-only; no bundled installer or auto-downloaded binaries). Credentials are never written into generated packs by the framework; publish/ACN/register require explicit user CLI. Use when the user wants to create a new agent persona, install/manage existing personas, or publish persona skill packs to OpenPersona. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[neiljo-gy](https://clawhub.ai/user/neiljo-gy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agent builders, and persona authors use this skill to create, install, manage, publish, and evolve OpenPersona skill packs for SKILL.md-compatible agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional memory, heartbeat, workspace, calendar, publishing, contribution, and external CLI features may expose local context, credentials, or data to network endpoints when enabled. <br>
Mitigation: Review the relevant local files, credentials, endpoints, and requested command before enabling these features; use dry-run or review modes before submitting public changes. <br>
Risk: Persona management commands can create, install, publish, register, or contribute skill packs through OpenPersona and related CLIs. <br>
Mitigation: Run these actions only after explicit user confirmation, especially for publishing, ACN registration, contribution workflows, external skill activation, or actions that may spend quota. <br>


## Reference(s): <br>
- [Open Persona on ClawHub](https://clawhub.ai/neiljo-gy/skills/open-persona) <br>
- [OpenPersona Repository](https://github.com/acnlabs/OpenPersona) <br>
- [OpenPersona Architecture Reference](references/ARCHITECTURE.md) <br>
- [Persona Presets](references/PRESETS.md) <br>
- [Faculty Reference](references/FACULTIES.md) <br>
- [Soul Evolution Reference](references/EVOLUTION.md) <br>
- [Economy & Vitality](references/ECONOMY.md) <br>
- [Heartbeat Reference](references/HEARTBEAT.md) <br>
- [ACN Skill Reference](https://github.com/acnlabs/ACN/blob/main/skills/acn/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write persona.json or skill pack files when the user asks to create or manage a persona.] <br>

## Skill Version(s): <br>
0.22.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
