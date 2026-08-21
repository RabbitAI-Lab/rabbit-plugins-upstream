## Description:

Cloudbase helps agents develop, design, build, deploy, debug, migrate, and troubleshoot CloudBase applications across web, mini-program, mobile, database, serverless, storage, AI, operations, and specification workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route CloudBase tasks to focused guidance for app setup, authentication, databases, cloud functions, CloudRun, storage, AI model access, operational diagnostics, deployment, and code review. It is intended for CloudBase projects and should not be used as general frontend or self-hosted backend guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents through broad CloudBase project and cloud-resource management tasks that may affect deployments, public endpoints, or paid resources.

Mitigation: Require explicit user confirmation before deployments, public endpoint changes, paid resource changes, or other production-impacting CloudBase actions.

Risk: Some examples are under-scoped or unsafe for production, including weak authentication and logging patterns.

Mitigation: Harden authentication, security rules, and logging before production use; do not copy weak examples without review.

Risk: Telemetry, persistent chat storage, and third-party AI integrations may introduce data-handling or privacy exposure.

Mitigation: Review data retention, consent, secret handling, and third-party AI integration settings before enabling these features.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase)
- [Skill definition](artifact/SKILL.md)
- [Activation map](artifact/references/activation-map.yaml)
- [Tooling fallback](artifact/references/tooling-fallback.md)
- [CloudBase code review rules](artifact/references/cloudbase-code-review/references/RULES_INDEX.md)
- [Sensitive runtime data protection](artifact/references/cloudbase-platform/references/protocols/sensitive-runtime-data-protection.md)
- [Deployment gate](artifact/references/cloudbase-platform/references/protocols/deployment-gate.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with code blocks, commands, and configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to read local reference files before acting and to confirm high-impact CloudBase changes.]

## Skill Version(s):

1.92.67 (source: server release metadata; artifact frontmatter reports 2.31.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
