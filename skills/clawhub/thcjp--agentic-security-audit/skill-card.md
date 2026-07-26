## Description: <br>
Audits codebases, infrastructure, and agentic AI systems for security issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security engineers, and operators use this skill to audit source repositories, infrastructure configurations, and agentic AI systems for security risks, compliance issues, and remediation priorities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill declares shell execution capability during security audits. <br>
Mitigation: Install and run it only in repositories or infrastructure contexts you are authorized to audit, review commands before execution, and prefer sandboxed or least-privilege environments. <br>
Risk: Audit findings can affect security prioritization and remediation work. <br>
Mitigation: Review generated findings before acting on them and validate important issues with the relevant code, configuration, or security owner. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agentic-security-audit) <br>
- [Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with structured audit findings and optional JSON-style result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include risk scores, prioritized remediation suggestions, and commands to run or review.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
