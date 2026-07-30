## Description: <br>
Consent-gated Kernel Egg Planter that creates local LYGO kernel egg registry artifacts, runs mandatory tamper verification, supports optional Turbo anchoring, and blocks retrieval without consent and an ALIGNED verify result. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT No Attribution (MIT-0) <br>


## Use Case: <br>
Developers and operators use this skill to plant, verify, and retrieve LYGO kernel eggs against a trusted local LYGO stack while preserving consent gates, tamper checks, and local-first publishing boundaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill intentionally runs allowlisted tools from the LYGO stack directory supplied by the user. <br>
Mitigation: Use only a LYGO_STACK_ROOT or --stack-root path you understand and control, run preflight first, and treat --i-trust-stack as executable trust in that local clone. <br>
Risk: Optional Turbo or permaweb anchoring can make published payloads difficult or impossible to revoke. <br>
Mitigation: Prefer --local-only unless external anchoring is intentional, and do not place secrets, private repositories, credentials, or token paths into egg payloads. <br>
Risk: Tampered or unverified eggs can lead agents to rely on invalid kernel artifacts. <br>
Mitigation: Run mandatory verify_eggs checks after planting and before retrieval, require an ALIGNED result, and do not bypass consent or verification gates. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-kernel-egg-planter) <br>
- [LYGO protocol stack](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [Kernel egg tamper logic](https://github.com/DeepSeekOracle/lygo-protocol-stack/blob/main/docs/KERNEL_EGG_TAMPER_LOGIC.md) <br>
- [Kernel egg retrieval page](https://deepseekoracle.github.io/lygo-protocol-stack/KernelEggRetrieval.html) <br>
- [Agent contract](references/AGENT_CONTRACT.md) <br>
- [Consent and ethics](references/CONSENT_AND_ETHICS.md) <br>
- [SkillSpector audit response](references/SKILLSPECTOR_AUDIT.md) <br>
- [Legal, honest planting surfaces](references/SURFACES.md) <br>
- [Four pillars](references/TAMPER_FOUR_PILLARS.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands; scripts produce local JSON registry and anchor artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Consent-gated execution, mandatory verification, optional Turbo anchoring, and no automatic GitHub, Hugging Face, ClawHub, or social publishing.] <br>

## Skill Version(s): <br>
1.3.1 (source: server release, claw.json, SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
