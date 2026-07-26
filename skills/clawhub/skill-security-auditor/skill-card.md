## Description: <br>
Command-line security analyzer that scans ClawHub SKILL.md files for malicious patterns, credential leaks, and command-and-control infrastructure before installation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[akhmittra](https://clawhub.ai/user/akhmittra) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and security reviewers use this skill to manually audit ClawHub skills before installation. It fetches or reads a SKILL.md file, applies pattern-based checks, and reports risk scores, findings, and recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional raw download and pattern update flows can introduce supply-chain risk if the downloaded source or pattern data is not trusted. <br>
Mitigation: Prefer installation through ClawHub and verify any remotely downloaded pattern data before use. <br>
Risk: Pattern-based scanning can miss novel or sophisticated malicious behavior. <br>
Mitigation: Use the audit report as one review aid and combine it with manual review and other security signals before installing a skill. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/akhmittra/skills/skill-security-auditor) <br>
- [README](artifact/README.md) <br>
- [Analyzer Script](artifact/analyze-skill.sh) <br>
- [Malicious Patterns Database](artifact/patterns/malicious-patterns.json) <br>
- [The Hacker News ClawHavoc Reference](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html) <br>
- [SC World OpenClaw Vulnerabilities Reference](https://www.scworld.com/brief/reports-shed-light-on-more-openclaw-vulnerabilities) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Terminal text report with Markdown-style audit sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports a 0-100 risk score, matched findings, positive indicators, and an installation recommendation.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence; artifact metadata reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
