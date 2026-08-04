## Description: <br>
Local Ollama automation for queue-driven multi-role work, reviewed task proposals, and local monitoring with social, planting, public probe, and privileged actions kept behind explicit opt-in gates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
LYGO Sovereign License v2.0 <br>


## Use Case: <br>
Developers and local operators use this skill to coordinate Ollama-backed worker roles, propose reviewed queue tasks, inspect local health state, and run optional LYGO stack checks from a trusted local workspace. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Included launch and tuning paths can run long-lived local automation, spawn Python processes, or change configuration. <br>
Mitigation: Review before installing, use the documented safe first run for initial testing, and avoid start_army_full_capacity.ps1 unless you accept autonomous background work. <br>
Risk: Optional public probes, self tuning, planting, social publishing, privileged roles, and external memory writes increase operational risk when enabled. <br>
Mitigation: Leave self_tune, planting, social_publish, public probe flags, allow_privileged_roles, and allow_external_memory_write disabled unless explicitly needed and reviewed. <br>
Risk: The optional LYGO_STACK_ROOT integration can touch tools from an external local stack clone. <br>
Mitigation: Set LYGO_STACK_ROOT only to a trusted clone controlled by the operator. <br>


## Reference(s): <br>
- [Security Guide](references/SECURITY.md) <br>
- [Agent Contract](references/AGENT_CONTRACT.md) <br>
- [Security Audit](references/SECURITY_AUDIT.md) <br>
- [SkillSpector Audit](references/SKILLSPECTOR_AUDIT.md) <br>
- [LYGO protocol stack homepage](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-ollama-army) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON task proposals and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose queue task JSON for human review and may produce local status, result, and log files when the operator runs the included utilities.] <br>

## Skill Version(s): <br>
0.8.0 (source: target metadata, SKILL.md frontmatter, claw.json, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
