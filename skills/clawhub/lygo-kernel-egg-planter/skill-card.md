## Description: <br>
Consent-gated skill for planting, anchoring, verifying, and retrieving LYGO kernel egg artifacts using SHA-256, Merkle registry checks, optional permaweb anchoring, and tamper verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to run consent-gated LYGO kernel egg planting, anchoring, verification, retrieval, and reference-stub workflows. It is intended for users who already have or trust a LYGO protocol stack clone and need explicit verification before distribution or retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security summary says the skill needs review because scripts can bypass verification and retrieval safeguards that are otherwise presented as mandatory. <br>
Mitigation: Review before installing, avoid --skip-verify and --force, and require verify_eggs to pass before retrieval, distribution, or any claim that artifacts are aligned. <br>
Risk: Planting and anchoring can publish or preserve artifacts on external or immutable surfaces. <br>
Mitigation: Use --local-only unless external anchoring is intentional, confirm selected surfaces and egg IDs before execution, and require separate explicit approval for publish or distribution steps. <br>
Risk: Anchoring unsafe or private material could expose data permanently. <br>
Mitigation: Use only trusted LYGO stack artifacts that are safe to anchor publicly, and do not plant secrets, credential files, API keys, token backups, or private repositories without consent. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-kernel-egg-planter) <br>
- [Publisher profile](https://clawhub.ai/user/deepseekoracle) <br>
- [LYGO protocol stack repository from metadata](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [Kernel egg tamper logic specification](https://github.com/DeepSeekOracle/lygo-protocol-stack/blob/main/docs/KERNEL_EGG_TAMPER_LOGIC.md) <br>
- [Agent contract](artifact/references/AGENT_CONTRACT.md) <br>
- [Consent and ethics](artifact/references/CONSENT_AND_ETHICS.md) <br>
- [Planting surfaces](artifact/references/SURFACES.md) <br>
- [Four pillars](artifact/references/TAMPER_FOUR_PILLARS.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Configuration instructions, Files, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated JSON or text reference files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include registry Merkle roots, tamper-verification verdicts, local anchor paths, retrieval commands, and book-brain reference stubs.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
