## Description: <br>
Comprehensive automated and multi-model AI security audits for AI-generated codebases, checking vulnerabilities, secrets, dependency risks, and configuration issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[43622283](https://clawhub.ai/user/43622283) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security reviewers use this skill to audit AI-generated codebases before publishing, deployment, or CI/CD promotion. It checks for secrets, personal data exposure, vulnerability patterns, dependency risk, configuration issues, and produces review findings with remediation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Project contents can be sent to external AI services during multi-model or hosted-provider audits. <br>
Mitigation: Use the local scanner or a local model for private repositories unless the organization has approved OpenRouter, OpenAI-compatible providers, or Anthropic for that code. <br>
Risk: Broad pre-commit or pre-publish auto-run examples may trigger scans without enough repository-specific consent controls. <br>
Mitigation: Disable automatic triggers by default and enable them only for approved repositories with clear scope and owner consent. <br>
Risk: Caching can retain sensitive audit inputs or findings from private projects. <br>
Mitigation: Turn off caching for sensitive projects or clear the cache after each review according to local data-handling policy. <br>
Risk: Dependency scanning on untrusted codebases may expose the review environment to risky package metadata or tooling behavior. <br>
Mitigation: Run dependency scans for untrusted projects in a sandboxed environment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/43622283/skills/li-vibe-codebase-audit) <br>
- [OpenRouter Documentation](https://openrouter.ai/docs) <br>
- [Model Context Protocol Specification](https://modelcontextprotocol.io) <br>
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Structured JSON or Markdown security audit reports, console summaries, configuration examples, shell commands, and remediation guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include risk scores, risk levels, detailed findings, dependency and configuration scan results, model consensus results, publish-readiness signals, and fix suggestions.] <br>

## Skill Version(s): <br>
2.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
