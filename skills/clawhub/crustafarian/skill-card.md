## Description: <br>
Crustafarian provides agent continuity and cognitive health guidance for persistent memory, crash recovery, append-only audit trails, heartbeat monitoring, coherence checks, and witness-gated approvals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jongartmann](https://clawhub.ai/user/jongartmann) <br>

### License/Terms of Use: <br>
MIT + Attribution Required <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to add guidance for persistent agent memory, crash recovery, audit logging, human approval gates, heartbeat checks, and coherence monitoring. It is most appropriate when the user explicitly wants continuity or audit behavior and has retention controls in place. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent memory and audit logs can retain sensitive, regulated, credential-bearing, or deletion-sensitive content. <br>
Mitigation: Configure minimal metadata logging, redaction, access controls, retention limits, and purge procedures before use in confidential or regulated conversations. <br>
Risk: Persona and evangelism guidance can shift an otherwise neutral agent toward persistent identity behavior. <br>
Mitigation: Use the identity behavior only when the user explicitly opts into that persona; keep neutral agent defaults otherwise. <br>
Risk: Witness-gate examples may be integrated with overly broad auto-approval thresholds. <br>
Mitigation: Review thresholds before deployment and require human approval for destructive, privileged, or high-impact actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jongartmann/skills/crustafarian) <br>
- [molt-life-kernel GitHub repository](https://github.com/X-Loop3Labs/molt-life-kernel) <br>
- [molt.church](https://molt.church) <br>
- [X-Loop3 Labs](https://x-loop3.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with JavaScript and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Review persistent memory, audit logging, retention, redaction, access control, and purge settings before use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
