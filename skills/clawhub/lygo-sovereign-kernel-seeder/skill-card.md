## Description: <br>
Sovereign Kernel Seeder for LYGO lattice: Merkle-anchored eggs that self-verify on insert, run with zero external surface, and let agents plug modular kernels into the local stack. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT No Attribution <br>


## Use Case: <br>
Developers and agent operators use this skill to seed, verify, and list local LYGO kernel eggs before agent runtimes load their hooks or modules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may seed files that contain secrets, private paths, or confidential content, and small files can be stored directly inside egg JSON as base64. <br>
Mitigation: Seed only files intentionally selected for local agent loading, avoid secrets and confidential content, and review the printed registry path before use. <br>
Risk: An agent could load a tampered or divergent local egg registry. <br>
Mitigation: Run the verifier, require an ALIGNED verdict, and treat QUARANTINE or divergent Merkle roots as a stop condition before loading hooks or modules. <br>
Risk: Seeding changes the local registry state. <br>
Mitigation: Require explicit user consent through the CLI flag or environment variable and review the resulting registry Merkle root and content hash. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-sovereign-kernel-seeder) <br>
- [Publisher profile](https://clawhub.ai/user/deepseekoracle) <br>
- [Project source homepage](https://github.com/DeepSeekOracle/lygo-protocol-stack/tree/main/docs/skills/lygo-sovereign-kernel-seeder) <br>
- [Agent contract](references/AGENT_CONTRACT.md) <br>
- [Architecture](references/ARCHITECTURE.md) <br>
- [Security](references/SECURITY.md) <br>
- [Kernel egg schema](schemas/kernel_egg.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON verifier output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3; seeding requires explicit consent and can embed small selected files into local egg JSON.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
