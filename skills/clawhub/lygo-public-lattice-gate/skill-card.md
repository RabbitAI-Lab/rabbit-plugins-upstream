## Description: <br>
Public lattice join and verify gate for foreign LYGO-aligned agents, with HTTPS verification of dual ledgers and hubs, an alignment score, dry-run Star Chart proposals, and restore-card output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT No Attribution (MIT-0) <br>


## Use Case: <br>
External agents, developers, and human operators use this skill to verify public LYGO lattice mirrors, assess readiness for public presence, draft a dry-run Star Chart proposal for review, and print a restore card with public links and digests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: License text is inconsistent across the release materials. <br>
Mitigation: Confirm the intended license with the publisher before redistribution or relying on reuse rights. <br>
Risk: Verification and restore commands contact fixed public HTTPS domains. <br>
Mitigation: Review the listed public domains before running networked commands in a restricted environment. <br>
Risk: Optional write flags can create local report or proposal files. <br>
Mitigation: Use write flags only with paths the operator intends to create or overwrite. <br>
Risk: Dry-run proposals may be mistaken for live Star Chart publication. <br>
Mitigation: Treat proposal output as a draft until separately reviewed and submitted through the live Star Chart workflow with explicit human approval. <br>


## Reference(s): <br>
- [Agent Contract](references/AGENT_CONTRACT.md) <br>
- [Security Notes](references/SECURITY.md) <br>
- [SkillSpector Audit Response](references/SKILLSPECTOR_AUDIT.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/deepseekoracle/skills/lygo-public-lattice-gate) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/deepseekoracle) <br>
- [Skill Homepage](https://github.com/DeepSeekOracle/lygo-protocol-stack/tree/main/docs/skills/lygo-public-lattice-gate) <br>
- [Source Repository Link from Skill Metadata](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [LYGO Claw Public USB Kit](https://deepseekoracle.github.io/lygo-protocol-stack/LYGO_CLAW_USB_PUBLIC.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Plain text and JSON emitted by CLI commands, with optional local JSON report files when write flags are supplied.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default zero disk writes; optional writes are limited to explicit report or proposal paths.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence, SKILL.md frontmatter, and claw.json; CLI script constants report 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
