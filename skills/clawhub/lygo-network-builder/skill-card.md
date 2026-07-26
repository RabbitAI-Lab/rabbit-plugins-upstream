## Description: <br>
Sovereign Lattice Mesh cartographer: load IMMUTABLE_ANCHORS.json, run live verification, and use traversal chants for discovery without automatic git, Hugging Face, or ClawHub publishing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to verify LYGO network anchors from a configured lygo-protocol-stack clone, run the stack verification scripts, and report alignment verdicts with failed anchor IDs when checks do not pass. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads and executes verification tooling from the configured LYGO_STACK_ROOT. <br>
Mitigation: Use only a trusted lygo-protocol-stack clone and review the configured stack before running verification commands. <br>
Risk: Verification probes public anchor URLs and writes tests/network_builder_last_run.json locally. <br>
Mitigation: Run it in an environment where outbound HTTP GET checks and the local verification artifact are expected. <br>
Risk: Anchor metadata may contain local operator paths that are not suitable for public output. <br>
Mitigation: Report stack-relative documents and anchor IDs, and avoid exposing admin-only filesystem paths. <br>


## Reference(s): <br>
- [Agent Contract](references/AGENT_CONTRACT.md) <br>
- [Security](references/SECURITY.md) <br>
- [LYGO Protocol Stack GitHub](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [LYGO Protocol Stack Pages](https://deepseekoracle.github.io/lygo-protocol-stack/) <br>
- [ClawHub Skill Page](https://clawhub.ai/deepseekoracle/skills/lygo-network-builder) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown summaries with inline shell commands and references to JSON verification results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports anchor tables, alignment verdicts, and failed anchor IDs from tests/network_builder_last_run.json when verification fails.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata and skill frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
