## Description:

Security checks for external content - downloads, fetched documents, attachments, and newly imported resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-hussein](https://clawhub.ai/user/z-hussein)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to verify external content before trusting it, including downloads, fetched documents, attachments, and newly imported resources. It helps agents treat external content as data until source, integrity, provenance, scan, and sandbox evidence are clear.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may block or delay actions involving untrusted external content when evidence or scope is incomplete.

Mitigation: Provide clear scope, source, integrity, provenance, scan, and sandbox evidence before asking the agent to trust or use external content.

Risk: Full-system security checks can read local configuration, files, services, logs, and network state within the agreed scope.

Mitigation: Require explicit user-defined scope and consent before host-wide enumeration, run with least privilege, and exclude sensitive paths and secrets by default.

Risk: Reference examples include shell commands and template code that may be inappropriate if copied directly into a production environment.

Mitigation: Review commands and examples before use, replace placeholder values through a secrets manager, and test only in a contained environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/z-hussein/skills/security-shield)
- [Attack Patterns Reference](references/attack.patterns.md)
- [Security Audit Checklist](references/audit-checklist.md)
- [Cryptography & Security Examples](references/crypto-examples.md)
- [Security Best Practices Reference](references/security-best-practices.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with checklists, inline command examples, and configuration recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask for more confirmation, use temporary sandboxes, log security-event summaries, or refuse unsafe untrusted-content actions unless scope and evidence are clear.]

## Skill Version(s):

2.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
