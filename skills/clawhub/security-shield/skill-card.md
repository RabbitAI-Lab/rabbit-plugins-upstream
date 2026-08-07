## Description:

Security-Shield helps agents verify external content, downloads, and new resources before trusting or acting on them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-hussein](https://clawhub.ai/user/z-hussein)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security reviewers, and agent operators use this skill to make agents treat internet content, downloads, attachments, and new resources as untrusted until source, integrity, scan, and sandbox evidence supports trust. It also supports scoped security audit summaries when a user explicitly approves a bounded scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Full-system audit guidance can touch local configuration, files, services, logs, or network state if applied too broadly.

Mitigation: Require an explicit bounded scope and user consent before host-wide enumeration, run with least privilege, and exclude sensitive paths and secrets by default.

Risk: Audit summaries could expose raw secrets or sensitive logs if findings are reported without filtering.

Mitigation: Summarize findings without raw credentials, tokens, private keys, or sensitive configuration values.

Risk: The skill may make agents more cautious with downloads and external content, which can slow normal workflows.

Mitigation: Set user expectations before installation and apply verification steps proportionally to the source, integrity, scan, and sandbox evidence available.

Risk: Server-resolved GitHub import provenance is unavailable for this version.

Mitigation: Do not infer repository provenance from artifact text; rely on server-resolved publisher, release version, and package hashes for this card.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/z-hussein/skills/security-shield)
- [Usage Guide](USAGE-GUIDE.md)
- [Attack Patterns Reference](references/attack.patterns.md)
- [Security Audit Checklist](references/audit-checklist.md)
- [Cryptography & Security Examples](references/crypto-examples.md)
- [Security Best Practices Reference](references/security-best-practices.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable payload; full-system audit guidance requires explicit user-approved scope.]

## Skill Version(s):

2.0.1 (source: server release evidence, artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
