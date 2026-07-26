## Description: <br>
LYGO Living Mesh (Layer D) helps agents verify and operate a local-authority mesh by collecting living mesh badges, gossiping lattice root digests, comparing peers, gating joins by consent, and running sentinel or scale simulation checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
LYGO SOVEREIGN LICENSE v2.0 <br>


## Use Case: <br>
Developers and operators use this skill to verify LYGO Layer A/B/C/D state, collect safe-to-share mesh badges, compare peers, and perform consent-gated joins without auto-merging remote registries or publishing externally. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local Python tools may read and write LYGO stack status files. <br>
Mitigation: Set LYGO_STACK_ROOT only to a trusted LYGO protocol stack directory and review generated status files before relying on them. <br>
Risk: Join, gossip, compare, and optional public checks may contact peer HTTP endpoints. <br>
Mitigation: Run join or gossip commands only for peers the operator explicitly chooses, and require the documented consent flag or environment variable for peer joins. <br>
Risk: Remote peer state could indicate a fork or quarantine condition. <br>
Mitigation: Keep local state authoritative, report root digests for human reconciliation, and refuse mesh growth when local or sentinel quarantine is reported. <br>


## Reference(s): <br>
- [Agent Contract](references/AGENT_CONTRACT.md) <br>
- [Security](references/SECURITY.md) <br>
- [Living Mesh Badge Schema](schemas/living_mesh_badge.schema.json) <br>
- [ClawHub Skill Page](https://clawhub.ai/deepseekoracle/skills/lygo-living-mesh) <br>
- [Living Mesh Layer Documentation](https://github.com/DeepSeekOracle/lygo-protocol-stack/blob/main/docs/LIVING_MESH_LAYER.md) <br>
- [Project Link from Metadata](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON status outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and write LYGO stack status files and may contact explicitly selected peer HTTP endpoints.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, claw.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
