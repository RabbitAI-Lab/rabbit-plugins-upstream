## Description: <br>
Provides advisory audits and prioritized optimization plans for OpenClaw workspaces, focused on cost-aware model routing, context discipline, delegation, reliability, and rollback-ready change proposals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[phenomenoner](https://clawhub.ai/user/phenomenoner) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to audit OpenClaw workspaces, compare optimization options, and receive exact change proposals with expected impact, rollback steps, and verification plans. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optimization recommendations can reduce monitoring coverage or alter persistent automation if applied without review. <br>
Mitigation: Require explicit approval before cron, heartbeat, configuration, memory-file, sub-agent, or openclaw-mem changes, and present the exact change, expected impact, rollback plan, and post-change verification first. <br>
Risk: Workspace optimization advice can be misleading when based on stale or incomplete context and cost measurements. <br>
Mitigation: Use fresh-session context or equivalent receipts where available, measure before and after changes, and prefer the smallest reversible fix first. <br>


## Reference(s): <br>
- [OpenClaw](https://openclaw.ai) <br>
- [ClawHub skill page](https://clawhub.ai/phenomenoner/skills/openclaw-agent-optimize) <br>
- [Optimization Playbook](references/optimization-playbook.md) <br>
- [Model Selection](references/model-selection.md) <br>
- [Context Management](references/context-management.md) <br>
- [Agent Orchestration](references/agent-orchestration.md) <br>
- [Cron Optimization](references/cron-optimization.md) <br>
- [Heartbeat Optimization](references/heartbeat-optimization.md) <br>
- [Memory Patterns](references/memory-patterns.md) <br>
- [Continuous Learning](references/continuous-learning.md) <br>
- [Safeguards](references/safeguards.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with prioritized plans, exact change proposals, rollback steps, and verification steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisory-first; no persistent changes without explicit approval.] <br>

## Skill Version(s): <br>
1.2.1 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
