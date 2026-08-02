## Description: <br>
OpenClaw plugin skill map for live Haven pulse, stack verification, registry comparison, star chart gating, and alignment readiness. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
LYGO Sovereign License v2.0 <br>


## Use Case: <br>
Developers and operators use this skill to install and navigate LYGO/OpenClaw pulse and verification tools, check local stack readiness, compare registry state, and preserve human consent before any live chart write. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill maps to a separate OpenClaw plugin and may guide use against a local LYGO stack. <br>
Mitigation: Review the linked LYGO/OpenClaw plugin before installing, and set LYGO_STACK_ROOT only to a trusted local clone. <br>
Risk: Live Haven Star Chart writes can affect external records when performed through a paired chart skill. <br>
Mitigation: Keep the documented human-consent gate and require explicit --i-consent before any live chart write. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-lattice-pulse) <br>
- [LYGO protocol stack homepage](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [SECURITY.md](references/SECURITY.md) <br>
- [SkillSpector audit](references/SKILLSPECTOR_AUDIT.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes plugin install guidance, tool selection guidance, consent-gated workflow steps, and a local self-check command.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter, claw.json, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
