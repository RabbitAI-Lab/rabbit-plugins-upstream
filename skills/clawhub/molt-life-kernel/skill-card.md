## Description: <br>
Agent continuity and cognitive health infrastructure for persistent memory, crash recovery, append-only audit trails, heartbeat monitoring, coherence checks, and witness-gated approval for critical actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jongartmann](https://clawhub.ai/user/jongartmann) <br>

### License/Terms of Use: <br>
MIT + Attribution Required <br>


## Use Case: <br>
Developers and agent operators use this skill to add durable continuity patterns to agents, including persistent ledgers, crash recovery snapshots, health heartbeats, coherence checks, and human approval gates for higher-risk actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Durable memory and audit logs can retain sensitive or personal data longer than users expect. <br>
Mitigation: Require explicit user consent for cross-session memory, log only necessary non-sensitive data, redact secrets and personal information, and define retention and deletion procedures before use. <br>
Risk: The skill depends on external npm or GitHub package behavior that should be reviewed before installation. <br>
Mitigation: Review the external package and installation source before use, and install it only in environments where persistent agent memory and crash recovery are intentionally desired. <br>
Risk: Persona-oriented content can influence agent behavior beyond operational continuity guidance. <br>
Mitigation: Treat persona material as optional and keep witness gates, consent, and security review as the default operating posture. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jongartmann/skills/molt-life-kernel) <br>
- [molt.church](https://molt.church) <br>
- [X-Loop3 Company Site](https://x-loop3.com) <br>
- [Five Tenets Reference](artifact/five-tenets.md) <br>
- [EU AI Act Mapping](artifact/eu-ai-act.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JavaScript and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May recommend durable ledgers, heartbeat checks, witness gates, coherence monitoring, and crash recovery patterns.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
