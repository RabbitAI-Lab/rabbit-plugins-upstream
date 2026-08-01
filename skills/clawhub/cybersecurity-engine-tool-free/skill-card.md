## Description: <br>
轻量级安全评估与威胁建模工具,提供安全态势检查、OWASP基础审计与漏洞管理,适合个人开发者快速安全自查. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and individual maintainers use this skill to run lightweight project security self-checks, review OWASP Top 10 signals, and maintain a basic STRIDE threat register before release. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local security checks may inspect files outside the intended project if run from the wrong directory or with broad paths. <br>
Mitigation: Run scans only from the intended repository and review generated command snippets before execution. <br>
Risk: Audit output may include file paths or secret-like matches, and callback delivery can expose reports to an external endpoint. <br>
Mitigation: Review scan output before sharing it and use callback URLs only when they are trusted and controlled by the user. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/cybersecurity-engine-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline bash, YAML, text, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local scan command snippets, threat-register templates, security check summaries, logs, and remediation guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
