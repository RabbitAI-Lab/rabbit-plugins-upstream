## Description:

Safe Linux firewall hardening with backend detection, idempotent atomic rules, rollback protection, and AI-executable state-machine workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[discovery219](https://clawhub.ai/user/discovery219)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, DevOps engineers, and security operators use this skill to audit Linux firewall posture, generate dry-run plans, and apply or verify host firewall hardening with explicit human approval gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent root-level authority to inspect and change host firewall state.

Mitigation: Use audit and plan modes first, require an exact visible approval token before apply, and keep console or second-session access open during changes.

Risk: Automated recovery and verification scripts can make privileged system changes beyond the approved firewall plan.

Mitigation: Do not run the verify/apply flow on production hosts until rollback cancellation is scoped to the specific job or unit created for that run.

Risk: Firewall changes can lock out SSH access or expose services unexpectedly.

Mitigation: Require backup creation, an armed rollback timer, a tested second SSH session, and external reachability verification before committing changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/discovery219/skills/linux-firewall-hardening)
- [Security Profiles](references/security-profiles.md)
- [Declarative Firewall Policy](references/declarative-policy.md)
- [firewall-apply.sh](references/firewall-apply.md)
- [Recovery Procedures](references/recovery.md)
- [Docker Firewall Hardening](references/docker-hardening.md)
- [Kubernetes Node Firewall Policy](references/k8s-policy.md)
- [Special Environments & When NOT to Use](references/special-environments.md)
- [Compliance Mapping](references/compliance.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce dry-run plans, approval tokens, audit summaries, verification checklists, and firewall configuration snippets.]

## Skill Version(s):

2.7.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
