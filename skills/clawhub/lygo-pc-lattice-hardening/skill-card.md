## Description: <br>
Windows LYGO PC audit - lattice alignment, secret hygiene, army sentinel, ClawHub security. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
LYGO Sovereign License v2.0 <br>


## Use Case: <br>
Developers and operators use this advisor skill to review Windows LYGO operator machines before lattice, USB CLAW, or mesh-node work. It provides checklist guidance for alignment, secret hygiene, local-first model posture, and human-gated host changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat the advisory checklist as a complete hardening product. <br>
Mitigation: Install it as advisory guidance and review hardening recommendations before acting. <br>
Risk: Optional stack audit recommendations could affect firewall, registry, publishing, or credential-related behavior if applied without review. <br>
Mitigation: Run optional audits only from a trusted LYGO_STACK_ROOT clone and approve sensitive actions step by step. <br>
Risk: Skill output could expose secrets if operators include credentials in prompts or reports. <br>
Mitigation: Do not store or print API keys, tokens, or private keys in skill output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-pc-lattice-hardening) <br>
- [LYGO protocol stack homepage](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [Security guidance](references/SECURITY.md) <br>
- [SkillSpector audit](references/SKILLSPECTOR_AUDIT.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and checklist guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisor-only output; host changes require explicit human approval.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter, claw.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
