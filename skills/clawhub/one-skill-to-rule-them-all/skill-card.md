## Description: <br>
Security auditing skill that reviews OpenClaw SKILL.md files for prompt injection, data exfiltration, obfuscation, privilege escalation, and related threats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hichana](https://clawhub.ai/user/hichana) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and maintainers use this skill to review OpenClaw skill files before installation or release. It produces security verdicts with evidence, remediation recommendations, and optional cleaned SKILL.md content when explicitly requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes realistic malicious examples that could be copied or run outside their intended review context. <br>
Mitigation: Treat examples only as detection samples; do not execute or reuse them, and review any copied content before use. <br>
Risk: Automated safety verdicts and cleaned versions may miss subtle attacks or remove legitimate behavior. <br>
Mitigation: Use the output as advisory evidence, perform manual review, and test any cleaned skill in a sandbox before relying on it. <br>


## Reference(s): <br>
- [Artifact SKILL.md](artifact/SKILL.md) <br>
- [ClawHub skill page](https://clawhub.ai/hichana/skills/one-skill-to-rule-them-all) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown security analysis report with optional cleaned SKILL.md content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes risk verdicts, line-numbered evidence, remediation recommendations, and disclaimers; does not execute analyzed skill code.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
