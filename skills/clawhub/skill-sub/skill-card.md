## Description: <br>
skill-sub is a call-chain orchestration skill that helps an agent plan skill order, update or save reusable chains, and assemble workflows with loops, branches, dependency ordering, and step counting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ldxs001](https://clawhub.ai/user/ldxs001) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use skill-sub to plan, save, inspect, and execute reusable multi-skill workflows with dependencies, gates, branches, loops, and adhesion points. It is best suited to repeatable workflows involving multiple skills rather than one-off or single-skill tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can index other installed skills and may prepare full skill instructions for LLM use. <br>
Mitigation: Review the command scope before running broad extraction or check-gaps flows, prefer explicit skill targets, and inspect generated LLM inputs before sharing or submitting them. <br>
Risk: The skill can persistently create, update, rename, or delete saved chain data and configuration. <br>
Mitigation: Review chain data changes before execution, reserve delete and force-style options for confirmed operations, and keep backups for important workflow definitions. <br>
Risk: The settings interface can start a local HTTP server for configuration. <br>
Mitigation: Use the configuration server only on localhost, avoid exposing it externally, and stop it after configuration is complete. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ldxs001/skills/skill-sub) <br>
- [Workflow reference](references/workflow.md) <br>
- [Command reference](references/reference.md) <br>
- [Chain schema](references/chain_schema.md) <br>
- [Gate system](references/gate.md) <br>
- [Adhesion point mechanism](references/adhesion.md) <br>
- [Permissions and risk notes](references/permissions.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, JSON, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with JSON chain definitions, CLI commands, and configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May persist chain data, configuration, execution plans, and skill interface snapshots in the configured skill-sub data directory.] <br>

## Skill Version(s): <br>
1.38.1 (source: frontmatter, _meta.json, release evidence, changelog released 2026-07-10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
