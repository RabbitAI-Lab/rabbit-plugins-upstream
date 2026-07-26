## Description: <br>
LYGO Prompt Implant System (LPIS) v1.1 helps analyze authorized prompts locally with a P0 gate, P1 vault, P3 sovereign variants, and P5 advisory implant, and requires --i-authorize for ingest. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to analyze, vault, and transform prompts they own or are authorized to use into local sovereign variants for manual review. It is intended for consent-gated prompt analysis workflows, not for leaked, scraped, or unauthorized third-party prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can store sensitive prompt text locally. <br>
Mitigation: Use it only with prompts you own or are authorized to analyze, keep the local prompt vault private, and do not commit vault bodies to public repositories. <br>
Risk: Ingesting unauthorized, leaked, scraped, or third-party proprietary prompts could expose confidential content. <br>
Mitigation: Require user attestation and the --i-authorize ingest gate, and stop when the source is unauthorized or prohibited. <br>
Risk: Generated variants could be applied without adequate review. <br>
Mitigation: Treat implant output as advisory only and manually review variants before applying them to any agent or model configuration. <br>


## Reference(s): <br>
- [LPIS security guidance](references/SECURITY.md) <br>
- [LPIS agent contract](references/AGENT_CONTRACT.md) <br>
- [SkillSpector audit response](references/SKILLSPECTOR_AUDIT.md) <br>
- [LYGO protocol stack project metadata link](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and local workflow constraints] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are advisory and local-first; generated prompt variants require manual review before use.] <br>

## Skill Version(s): <br>
1.1.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
