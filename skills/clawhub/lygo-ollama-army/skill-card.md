## Description: <br>
Local Ollama daemons and optional LYGO stack queue roles run when LYGO_STACK_ROOT is configured, with security guidance against remote LLM use, git push, ClawHub publishing, and autonomous social posting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to run local Ollama assistant daemons, queue reviewed LYGO stack tasks, monitor local stack status, and generate local drafts or analysis. Stack-touching roles require a controlled LYGO_STACK_ROOT clone and explicit user approval before queue files or long-running automation are started. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence flags this as a real local automation skill with queue-driven stack mutation and account or social pulse roles broader than the top-level safety claims. <br>
Mitigation: Install only on a machine and LYGO_STACK_ROOT clone the operator controls; review SECURITY.md, SECURITY_AUDIT.md, AGENT_CONTRACT.md, and command-center configuration before enabling stack roles. <br>
Risk: Long-running supervisors, cron flows, and daemon roles can keep processing local queues after startup. <br>
Mitigation: Do not run army_autonomous_supervisor.py, cron examples, desktop launchers, seed scripts, or full-capacity scripts unless the operator has reviewed the scripts and intentionally wants those effects. <br>
Risk: Queue task files can trigger stack audits, self-tuning, planting, registry operations, or other local mutations when daemons are active. <br>
Mitigation: Agents should propose task JSON for human approval first; write queue files only after approval and only for a validated LYGO_STACK_ROOT. <br>
Risk: Outbound webhook and social or account pulse behavior can interact with external services if explicitly enabled. <br>
Mitigation: Keep webhook environment variables, social pulse roles, publishing paths, and sensitive account tooling disabled unless the operator has reviewed the code and requested that behavior. <br>
Risk: Planting, self-tune, seed, and full-capacity paths can change local workspace state or expand automation scope. <br>
Mitigation: Keep default configuration gates disabled, including planting.enabled, self_tune.enabled, LYGO_ARMY_FULL_CAPACITY, LYGO_ARMY_SEED_TASKS, and LYGO_ARMY_WEBHOOK_ENABLE, until intentionally enabled by the operator. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-ollama-army) <br>
- [LYGO RESONANCE companion site](https://deepseekoracle.github.io/Excavationpro/LYGORESONANCE.html) <br>
- [Security guidance](references/SECURITY.md) <br>
- [SkillSpector security audit response](references/SECURITY_AUDIT.md) <br>
- [Agent contract](references/AGENT_CONTRACT.md) <br>
- [Command center README](ollama_command_center/README.md) <br>
- [Example command-center configuration](ollama_command_center/config/army_config.example.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with shell command snippets, configuration notes, and reviewed JSON task proposals.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended for local Ollama and LYGO stack workflows; queue tasks and long-running daemons require human review before execution.] <br>

## Skill Version(s): <br>
0.5.0 (source: server release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
