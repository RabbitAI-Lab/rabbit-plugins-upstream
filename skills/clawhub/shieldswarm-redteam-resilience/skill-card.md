## Description:

A defensive SRE/SecOps resilience skill that provides authorization-gated guidance and templates for red-team and purple-team planning, incident response, rollback, postmortems, and model-resilience reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Security, SRE, SecOps, and platform operators use this skill to structure authorized defensive resilience work, including rules of engagement, approval records, rollback planning, evidence redaction, stakeholder updates, and postmortems. It is best treated as a documentation and template package unless missing executable controls are added and reviewed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package claims approval gates, validators, timeout wrappers, and self-heal integrations that are not fully bundled or permission-scoped.

Mitigation: Treat the release as templates and guidance only until the missing executable controls are added, reviewed, and tested in the target environment.

Risk: Operational resilience exercises can affect production or staging systems if scope, approvers, rollback owners, and abort conditions are not concrete.

Mitigation: Require written rules of engagement, named approvers, rollback plans, and bounded validation metrics before any exercise or configuration change.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/shieldswarm-redteam-resilience)
- [README](artifact/README.md)
- [Skill Definition](artifact/SKILL.md)
- [Agent Discovery](artifact/AGENT_DISCOVERY.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration, shell commands]

**Output Format:** [Markdown templates, YAML configuration templates, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs require human authorization, review, and environment-specific scoping before operational use.]

## Skill Version(s):

1.0.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
