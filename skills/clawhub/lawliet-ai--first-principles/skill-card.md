## Description: <br>
Analyzes products by stripping marketing jargon to identify their fundamental physical, logical, and economic constraints from first principles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[Lawliet-ai](https://clawhub.ai/user/Lawliet-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, product evaluators, and technical due diligence reviewers use this skill to audit products or technologies by mapping physical, logical, and economic constraints, comparing implementation efficiency, and producing a structured verdict. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prior agent output in ~/.openclaw/swarm_tmp/expert_output.json could influence a new audit. <br>
Mitigation: Clear the handoff file before starting a new audit when prior task content should not be reused. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/Lawliet-ai/first-principles) <br>
- [audit_schema.json](artifact/audit_schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Analysis, Files, Guidance] <br>
**Output Format:** [Structured JSON following the bundled audit schema] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read prior expert output from ~/.openclaw/swarm_tmp/expert_output.json when available and may save the audit report to ~/.openclaw/swarm_tmp/audit_report.json.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
