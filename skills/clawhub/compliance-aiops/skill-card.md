## Description: <br>
This skill helps agents read local AIops audit trails and produce framework-mapped compliance evidence, change-approval reports, gap analyses, exception reports, and hash-chain-sealed evidence bundles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and compliance reviewers use this skill to turn existing governed AIops audit trails into evidence for HIPAA, PCI-DSS, SOC 2, GDPR, ISO 27001, and DJCP L3 controls. It is intended for evidence collection, control coverage review, gap analysis, exception reporting, and bundle integrity checks, not for certifying compliance or operating infrastructure. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read referenced AIops audit databases and create or sign local evidence bundles. <br>
Mitigation: Install and run it only from an account that is allowed to access those audit trails and write evidence bundles; for query-only sessions, restrict the agent prompt or operating-system permissions. <br>
Risk: A model could overstate evidence as a compliance certification or ignore missing, truncated, or weak audit data. <br>
Mitigation: Require tool-backed answers, report control strengths and caveats, and state that the output is evidence rather than certification. <br>
Risk: Hash-chain-sealed bundles are tamper-evident, not tamper-proof. <br>
Mitigation: Record chain heads out of band and treat the source audit databases as the system of record when verifying or investigating mismatches. <br>


## Reference(s): <br>
- [Compliance AIops homepage](https://github.com/AIops-tools/Compliance-AIops) <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/compliance-aiops) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>
- [Capabilities](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with CLI commands and references to local JSON, Markdown, or CSV evidence bundle outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to create local evidence bundles under ~/.compliance-aiops/bundles/ when the user asks for bundle generation or export.] <br>

## Skill Version(s): <br>
0.6.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
