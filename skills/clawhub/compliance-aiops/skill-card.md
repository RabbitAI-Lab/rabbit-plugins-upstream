## Description: <br>
Compliance AIops helps agents turn local AIops audit trails into framework-mapped evidence, gap analyses, exception reports, and tamper-evident evidence bundles for HIPAA, PCI-DSS, SOC 2, GDPR, ISO 27001, and DJCP L3 workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, platform engineers, and compliance operators use this skill to collect evidence from existing governed AIops audit logs, map activity to common control frameworks, investigate gaps and exceptions, and produce local evidence bundles for review. It supports evidence collection and reporting, not compliance certification or infrastructure operation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A user may treat audit-derived evidence as a compliance certification or final compliance verdict. <br>
Mitigation: Present outputs as evidence about recorded operations only, preserve control caveats, and require qualified review before making compliance claims. <br>
Risk: The skill can create local evidence bundles for any account that has filesystem permission to run it. <br>
Mitigation: Install it only for accounts authorized to read local AIops audit databases and create evidence bundles; use OS permissions or agent policy for query-only sessions. <br>
Risk: Optional bundle signing introduces signing-key handling requirements. <br>
Mitigation: Configure the optional signing key only when signatures are required, keep it encrypted in the tool's secret store, and provide the master password only in approved non-interactive environments. <br>
Risk: A tamper-evident bundle can detect later changes but cannot prove the source audit database was never altered before sealing. <br>
Mitigation: Record the bundle chain head out-of-band, run source-chain verification, and treat source audit databases as the system of record. <br>


## Reference(s): <br>
- [Compliance-AIops homepage](https://github.com/AIops-tools/Compliance-AIops) <br>
- [capabilities.md](references/capabilities.md) <br>
- [cli-reference.md](references/cli-reference.md) <br>
- [setup-guide.md](references/setup-guide.md) <br>
- [agent-guardrails.md](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands; generated evidence artifacts may be JSON, Markdown, or CSV.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local evidence bundle files under ~/.compliance-aiops/bundles/ when bundle-generation tools are used.] <br>

## Skill Version(s): <br>
0.8.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
