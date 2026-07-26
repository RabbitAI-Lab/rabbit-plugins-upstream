## Description: <br>
LYGO Sovereign Super Skill is a consent-gated map for LYGO kernel eggs, Biophase7 products, lattice verification, stack commands, and related ClawHub skill chains. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to understand the LYGO stack, inspect kernel egg and champion egg workflows, print consent-gated seed sweep commands, and verify lattice alignment before claiming a stack is seeded or secure. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Planter, publish, git-credential, social, or token flows could change a stack checkout or external state if run without clear user intent. <br>
Mitigation: Require explicit user consent before running those commands and review the exact command sequence before execution. <br>
Risk: An untrusted stack root could cause helper scripts to inspect or use the wrong LYGO checkout. <br>
Mitigation: Set LYGO_STACK_ROOT only to a trusted lygo-protocol-stack clone and run self-checks before relying on stack status. <br>
Risk: Tampered retrieved eggs could lead to unsafe execution claims or propagation. <br>
Mitigation: Treat retrieve failures as quarantine events and verify kernel eggs and lattice alignment before claiming the stack is seeded or secure. <br>


## Reference(s): <br>
- [Agent Contract](references/AGENT_CONTRACT.md) <br>
- [Egg Catalog](references/EGG_CATALOG.md) <br>
- [Security Guidance](references/SECURITY.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/deepseekoracle/skills/lygo-sovereign-super-skill) <br>
- [LYGO Protocol Stack Repository](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [LYGO Protocol Stack Pages](https://deepseekoracle.github.io/lygo-protocol-stack/) <br>
- [Kernel Egg Retrieval](https://deepseekoracle.github.io/lygo-protocol-stack/KernelEggRetrieval.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The helper scripts can print a seed sweep or run a self-check; actions that modify a stack require user consent and a trusted LYGO stack root.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
