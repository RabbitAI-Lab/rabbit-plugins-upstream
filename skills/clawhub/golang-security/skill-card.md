## Description:

Security best practices and vulnerability prevention for Golang. Covers injection (SQL, command, XSS), cryptography, filesystem safety, network security, cookies, secrets management, memory safety, and logging. Apply when writing, reviewing, or auditing Go code for security, or when working on any risky code involving crypto, I/O, secrets management, user input handling, or authentication. Includes configuration of security tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review, audit, and write Go code with security guidance for injection risks, cryptography, filesystem access, network behavior, cookies, secrets, memory safety, logging, and dependency vulnerability checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security review notes that a couple of security examples are imperfect if copied without review.

Mitigation: Treat examples as guidance, review generated code before use, and prefer vetted Go standard-library or established tool behavior for security-sensitive changes.

Risk: Audit and fix modes can inspect or modify Go source files.

Mitigation: Approve those modes only when project code review or remediation is intended, and review proposed changes before merging.

Risk: The skill can suggest shell commands for security tooling.

Mitigation: Run commands in an appropriate project environment and confirm tool installation steps such as govulncheck before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/samber/skills/golang-security)
- [Publisher Profile](https://clawhub.ai/user/samber)
- [Homepage](https://github.com/samber/cc-skills-golang)
- [Go Security Best Practices](https://go.dev/doc/security/best-practices)
- [govulncheck](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck)
- [gosec Security Linter](https://github.com/securego/gosec)
- [OWASP Go Secure Coding Practices](https://owasp.org/www-project-go-secure-coding-practices-guide/)
- [Security Architecture Patterns](references/architecture.md)
- [Security Review Checklist](references/checklist.md)
- [Cookie Security Rules](references/cookies.md)
- [Cryptography Security Rules](references/cryptography.md)
- [Filesystem Security Rules](references/filesystem.md)
- [Injection Security Rules](references/injection.md)
- [Logging Security Rules](references/logging.md)
- [Memory Safety Security Rules](references/memory-safety.md)
- [Network/Web Security Rules](references/network.md)
- [Secrets Management Security Rules](references/secrets.md)
- [Third-Party Data Leak Rules](references/third-party.md)
- [Threat Modeling Guide](references/threat-modeling.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with findings, recommendations, code examples, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose edits to Go source files and commands such as go test, gosec, and govulncheck when the host agent is authorized to inspect or modify a project.]

## Skill Version(s):

1.2.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
