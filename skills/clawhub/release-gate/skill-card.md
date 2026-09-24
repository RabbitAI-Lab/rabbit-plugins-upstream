## Description:

Enforces structured reviewer sign-off and audit logging before clearly irreversible actions such as deployments, migrations, public launches, pricing changes, or emails to real users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ferrentinomj-dev](https://clawhub.ai/user/ferrentinomj-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent teams use this skill to require explicit role-based pass/fail checks before high-stakes or hard-to-reverse changes. It provides checklist patterns and a Python helper for recording approved and blocked release decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release gate is a checklist and audit-log convention, not a technical lock that prevents deployment.

Mitigation: Treat unchecked or missing approvals as blockers, verify the checklist is complete before acting, and do not rely on the helper to stop bypasses.

Risk: A failed or skipped log write can leave an irreversible action without an audit trail.

Mitigation: Use an appropriate project log path, verify the log entry was written before proceeding, and serialize gate runs for multi-agent teams.

## Reference(s):

- [OWASP Secure Coding Practices Quick Reference Guide](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
- [The Twelve-Factor App](https://12factor.net/)
- [ClawHub Skill Page](https://clawhub.ai/ferrentinomj-dev/skills/release-gate)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown checklists with optional Python helper calls and deployment-command context]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces human-facing gate decisions and optional append-only deployment log entries.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
