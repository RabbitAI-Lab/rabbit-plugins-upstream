## Description: <br>
Excavationpro sovereign music portal on the LYGO lattice: free listen hub, CAS vault Merkle, ISRC ledger, HF streams, Kick/Rumble/Twitch live portals, and PayPal support, with agent routing, verification, and human-gated operation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to route people to the Excavationpro music portal, catalog, hash vault, live portals, and donation link, and to verify or operate related LYGO music workflows with explicit human approval for publishing actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Operator workflows can run local LYGO stack commands against a user-selected stack root. <br>
Mitigation: Set LYGO_STACK_ROOT only to a trusted local clone, review stack_cli commands before execution, and approve publishing actions only when intended. <br>
Risk: Portal health checks can make outbound requests to public music and dataset URLs. <br>
Mitigation: Limit checks to canonical MUSIC_PORTAL.json links and treat the results as read-only availability signals. <br>
Risk: HF upload, git publishing, kernel egg planting, and donation routing can affect external accounts or public surfaces. <br>
Mitigation: Require explicit human approval, keep tokens in the user-controlled environment, and use only the documented PayPal link. <br>


## Reference(s): <br>
- [Agent contract](references/AGENT_CONTRACT.md) <br>
- [Lattice map](references/LATTICE_MAP.md) <br>
- [Music portal manifest](references/MUSIC_PORTAL.json) <br>
- [Security guidance](references/SECURITY.md) <br>
- [SkillSpector audit response](references/SKILLSPECTOR_AUDIT.md) <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-excavationpro-music-lattice) <br>
- [LYGO protocol stack repository](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [Excavationpro listen portal](https://deepseekoracle.github.io/Excavationpro/excavationpro-listen.html) <br>
- [Excavationpro catalog ledger](https://deepseekoracle.github.io/Excavationpro/excavationpro-music-catalog.html) <br>
- [Excavationpro sovereign music hub](https://deepseekoracle.github.io/Excavationpro/excavationpro-sovereign-music-hub.html) <br>
- [HF stream dataset](https://huggingface.co/datasets/DeepSeekOracle/excavationpro-music-stream) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON-backed URLs and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Status and smoke-check scripts may emit JSON; publish and donation-related actions remain human-gated.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
