## Description: <br>
LYGO OpenClaw is a third-party ClawHub router alias for the LYGO sovereign command framework, mapping operators to P0-P5 gated stack commands and consent-gated OpenClaw workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
LYGO Sovereign License v2.0 <br>


## Use Case: <br>
External developers and stack operators use this skill to install and operate the lygo-open-claw alias, route commands through documented P0-P5 gates, and invoke related LYGO stack tools only from a trusted local clone. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: External stack commands depend on a separate LYGO clone outside this package. <br>
Mitigation: Set LYGO_STACK_ROOT only to a clone the operator trusts and treat the external stack and paired skills as separate trust decisions. <br>
Risk: Planter, hybrid runtime, social, or live chart operations can have unintended effects if run without clear operator intent. <br>
Mitigation: Run those operations only with explicit human consent; the artifact states no automatic push, ClawHub publish, or social posting from this skill. <br>
Risk: Secrets could be exposed if stored inside the skill package. <br>
Mitigation: Keep API keys, Discord tokens, and private wallets outside the skill tree and load credentials only at runtime from operator-local secrets. <br>
Risk: The public slug is an alias, which can confuse operators about the canonical package. <br>
Mitigation: Document lygo-open-claw as an alias of lygo-sovereign-claw and verify the intended slug before installation or execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-open-claw) <br>
- [LYGO protocol stack homepage](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [SECURITY](references/SECURITY.md) <br>
- [AGENT_CONTRACT](references/AGENT_CONTRACT.md) <br>
- [SKILLSPECTOR_AUDIT](references/SKILLSPECTOR_AUDIT.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are operator-facing command maps and safety notes; shell commands that invoke external stack tools require a trusted LYGO_STACK_ROOT.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter, claw.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
