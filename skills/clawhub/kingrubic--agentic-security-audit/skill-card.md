## Description:

Audit codebases, infrastructure, and agentic AI systems for security issues, including dependency vulnerabilities, secrets, OWASP web risks, SSL/TLS configuration, file permissions, prompt injection, identity spoofing, memory poisoning, multi-agent communication, and agent permissions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kingrubic](https://clawhub.ai/user/kingrubic)

### License/Terms of Use:


## Use Case:

Developers, security engineers, and agent operators use this skill to run security review workflows across source code, infrastructure settings, and agentic AI workspaces. It helps identify vulnerable dependencies, hardcoded secrets, risky permissions, prompt-injection vectors, identity weaknesses, memory poisoning indicators, and multi-agent communication risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit commands may scan beyond the intended project or inspect host-level paths.

Mitigation: Run the skill first in a project-scoped workspace and approve host-level checks explicitly before use.

Risk: Audit findings may expose credentials, agent memory, or personal data in logs or chat output.

Mitigation: Redact secret and PII matches before sharing output, and avoid printing raw matched lines when reviewing sensitive repositories.

Risk: The workflow may install or invoke external audit tools.

Mitigation: Pin and review audit-tool versions before installation or execution.

## Reference(s):

- [Agentic Security Audit on ClawHub](https://clawhub.ai/kingrubic/skills/agentic-security-audit)
- [Agents of Chaos](https://arxiv.org/abs/2602.20021)
- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [NIST AI Agent Standards Initiative](https://www.nist.gov/caisi/ai-agent-standards-initiative)
- [Trivy Documentation](https://aquasecurity.github.io/trivy)
- [OpenClaw Security Crisis](https://conscia.com/blog/the-openclaw-security-crisis/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and bash scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include audit findings, command output summaries, remediation guidance, and generated shell scripts for project or agent-workspace scanning.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
