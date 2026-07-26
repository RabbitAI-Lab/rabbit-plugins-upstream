## Description: <br>
Use when diagnosing KWDB incidents from logs, metrics, or system evidence, especially crashes, OOM, slow SQL, restarts, and cluster-wide availability symptoms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kwdb](https://clawhub.ai/user/kwdb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and support engineers use this skill to diagnose KWDB incidents from logs, metrics, system evidence, SQL statements, and optional source code while keeping the result limited to diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated diagnostic reports may contain SQL literals, customer identifiers, tenant names, tokens, or sensitive log snippets. <br>
Mitigation: Redact sensitive incident data before sharing reports outside the incident team. <br>
Risk: The skill is designed to answer in Chinese, which may be unsuitable for some environments or review workflows. <br>
Mitigation: Install and use the skill only where Chinese diagnostic output is acceptable. <br>
Risk: Optional local commands or scripts proposed during diagnosis could inspect logs, metrics, source code, or git history. <br>
Mitigation: Review and approve any optional local command or script before allowing the agent to run it. <br>


## Reference(s): <br>
- [KWDB source repository](https://gitee.com/kwdb/kwdb) <br>
- [Key Rules](references/key-rules.md) <br>
- [Intake Gate](references/intake-gate.md) <br>
- [Path Discovery](references/path-discovery.md) <br>
- [Triage Playbook](references/triage-playbook.md) <br>
- [Fault Localization Chain](references/fault-localization.md) <br>
- [Evidence Rules](references/evidence-rules.md) <br>
- [Output Modes](references/output-modes.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Chinese Markdown diagnostic reports with optional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Diagnosis-only output; unknown or unsupported findings are marked as pending rather than invented.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
