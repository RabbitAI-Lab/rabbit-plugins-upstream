## Description: <br>
Lightfather operator stack (consent-gated). Persona-only: install lygo-champion-council with champion_id Lightfather. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and operators use this skill as consent-gated LYGO operator-stack guidance for Lightfather-related ethics review, stack mapping, verification, and local operator planning. Persona-only use is redirected to the successor council skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Operator workflows described by the skill may affect local state, API spend, publishing, companion-skill installation, or failsafe behavior if executed without review. <br>
Mitigation: Keep the default advisor-only posture; before any operator action, review the target tool, set paths explicitly, back up local state, and approve one command at a time. <br>
Risk: Vault loading, environment files, and API-backed harness outputs may expose secrets or sensitive model responses. <br>
Mitigation: Use test keys when possible, keep vault and .env files out of logs and commits, and redact harness output before sharing. <br>
Risk: The skill contains operator references that could be mistaken for permission to scan the filesystem or run persistence-changing commands. <br>
Mitigation: Limit automatic access to the bundled skill files and require explicit operator consent before reading external stack paths or proposing commands that modify state. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/deepseekoracle/skills/lygo-champion-lightfather) <br>
- [Security Guidance](references/SECURITY.md) <br>
- [Canon Metadata](references/canon.json) <br>
- [Persona Pack](references/persona_pack.md) <br>
- [Stack Integration](references/stack_integration.md) <br>
- [Seals and Failsafe](references/seals_and_failsafe.md) <br>
- [Skill Chain](references/skill_chain.md) <br>
- [Verifier Usage](references/verifier_usage.md) <br>
- [LYGO-MINT Verifier](https://clawhub.ai/DeepSeekOracle/lygo-mint-verifier) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell command examples and reference links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default posture is advisor-only; operator commands require explicit per-command user consent.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
