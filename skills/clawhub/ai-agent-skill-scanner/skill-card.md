## Description: <br>
Security scanner for AI agent skills that detects hardcoded secrets, unsafe code execution, prompt injection, and malware patterns before installation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[certainlogicai](https://clawhub.ai/user/certainlogicai) <br>

### License/Terms of Use: <br>
Business Source License 1.1 <br>


## Use Case: <br>
Developers and security reviewers use this skill to scan ClawHub or OpenClaw skill directories before installation and receive first-pass findings on secrets, unsafe execution patterns, prompt injection language, and related risk signatures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security verdict is suspicious because the package includes an undocumented helper that can read external local company-brain context and inject it into vetting prompts. <br>
Mitigation: Review or remove brain_enhance.py before use in sensitive environments, and document any intended local context integration. <br>
Risk: Pattern matching can miss obfuscated or novel malicious behavior, and some directories such as .env, .git, virtual environments, and build output are skipped. <br>
Mitigation: Treat results as first-pass screening, manually review high-risk skills, and complement this scanner with deeper analysis before deployment. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/certainlogicai/skills/ai-agent-skill-scanner) <br>
- [Usage guide](docs/USAGE.md) <br>
- [CertainLogic Skill Vetter Plus documentation](https://certainlogic.ai/docs/skill-vetter-plus) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, analysis, guidance] <br>
**Output Format:** [Plain text or JSON scan report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Findings can include severity, rule identifier, file path, line number, message, and matched fragment when JSON output is requested.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
