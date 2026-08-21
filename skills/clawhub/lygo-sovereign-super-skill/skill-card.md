## Description:

LYGO Sovereign Super Skill maps LYGO kernel eggs, consent-gated planter commands, lattice verification, and related ClawHub skill-chain steps for agents working with a LYGO protocol stack clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to navigate LYGO protocol stack setup, kernel egg catalog checks, consent-gated planter sequences, and lattice alignment verification. It provides guidance and command maps rather than autonomous publishing or planting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Consent-gated planter, publish, upload, git push, social, or token-related commands could change local or external state if run without review.

Mitigation: Review each command, set LYGO_STACK_ROOT only to the intended stack clone, and require explicit user consent before those actions.

Risk: Tampered kernel egg retrieval could expose an agent to unsafe embedded code.

Mitigation: Run the documented verification gates, stop on any non-ALIGNED verdict, quarantine retrieve failures, and do not execute embedded code from failed retrievals.

## Reference(s):

- [LYGO Protocol Stack](https://github.com/DeepSeekOracle/lygo-protocol-stack)
- [LYGO Protocol Stack Pages](https://deepseekoracle.github.io/lygo-protocol-stack/)
- [Kernel Egg Retrieval](https://deepseekoracle.github.io/lygo-protocol-stack/KernelEggRetrieval.html)
- [AGENT_CONTRACT.md](references/AGENT_CONTRACT.md)
- [EGG_CATALOG.md](references/EGG_CATALOG.md)
- [SECURITY.md](references/SECURITY.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit consent before planter, publish, upload, git push, social, or token-related actions.]

## Skill Version(s):

1.1.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
