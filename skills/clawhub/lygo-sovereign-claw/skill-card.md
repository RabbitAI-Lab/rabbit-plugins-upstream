## Description: <br>
LYGO Sovereign Claw Router helps agents route consent-gated LYGO stack commands for P0 validation, local mycelium and ledger storage, optional consensus, and lattice, sentinel, and kernel egg workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and LYGO stack operators use this skill to install and run a gated command router for LYGO-OpenClaw tasks without loading the full hybrid OS. It provides setup guidance, command examples, and self-check behavior for stack-native and optional hybrid workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on external LYGO runtime code that is not fully contained in the artifact. <br>
Mitigation: Review the external LYGO repository and installer before running setup or enabling related runtime operations. <br>
Risk: Commands may create local memory and ledger files under the LYGO stack. <br>
Mitigation: Set LYGO_STACK_ROOT intentionally, review generated files, and only run commands you intend to authorize. <br>
Risk: Hybrid browser, social, token, or kernel egg workflows can have higher operational impact. <br>
Mitigation: Install optional hybrid components only when needed, provide credentials at runtime only, and require explicit consent for planter actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-sovereign-claw) <br>
- [LYGO protocol stack](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [Agent contract](references/AGENT_CONTRACT.md) <br>
- [Security notes](references/SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and command tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands depend on external LYGO runtime code and may create local memory and ledger files under the configured LYGO stack root.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence, skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
