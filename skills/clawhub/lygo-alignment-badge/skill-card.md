## Description: <br>
Verifies LYGO node compliance across the documented P0, stack demo, elasticity, federation, Grok audit, lattice, and mesh-scale checks, then emits JSON or Markdown badge evidence for community deployment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to check whether a LYGO node meets the published alignment requirements before surfacing an ALIGNED or NEEDS_FIX badge. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Badge output from an untrusted third-party repository can be misleading if accepted without verification. <br>
Mitigation: Quarantine untrusted repositories and run the documented verification command before reporting ALIGNED status. <br>
Risk: The workflow may lead an agent to run local Python validation commands against a checkout. <br>
Mitigation: Run commands only in the intended LYGO protocol stack workspace and review generated JSON or Markdown badge artifacts before relying on them. <br>


## Reference(s): <br>
- [LYGO protocol stack repository](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [LYGO protocol stack documentation](https://deepseekoracle.github.io/lygo-protocol-stack/) <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-alignment-badge) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and references to JSON or Markdown badge artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Badge status should be surfaced only after running the documented verification command.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
