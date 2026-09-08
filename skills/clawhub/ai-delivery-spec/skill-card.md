## Description:

Use for creating, changing, reviewing, reverse-engineering, or accepting requirements, PRDs, prototypes, competitor material, or existing systems, including small UI, field, column, tab, dropdown, or legacy HTML changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[franklinxkk](https://clawhub.ai/user/franklinxkk)

### License/Terms of Use:

Apache 2.0

## Use Case:

Product managers, business stakeholders, designers, engineers, QA teams, and coding agents use this skill to turn ideas, existing systems, or change requests into reviewable requirements, PRDs, prototypes, structured handoff artifacts, and acceptance evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can influence broad requirements, PRD, prototype, and acceptance decisions across sensitive projects.

Mitigation: Invoke it intentionally for the current work stage, provide only the necessary files, and have project owners review outputs before using them as requirements.

Risk: Inputs may contain secrets, customer data, or other sensitive project information.

Mitigation: Do not provide raw secrets; pass scoped, sanitized materials and replace sensitive values with controlled references.

Risk: Domain and legal reference packs may be mistaken for final jurisdiction-specific requirements.

Mitigation: Treat those references as prompts for stakeholder and jurisdiction review before accepting them into a baseline.

Risk: Static validation gates do not prove business correctness, browser behavior, real integrations, customer acceptance, or production stability.

Mitigation: Use gate results as static contract evidence only and require separate business, implementation, browser, integration, security, and customer acceptance checks where applicable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/franklinxkk/skills/ai-delivery-spec)
- [README](README.md)
- [Lifecycle Reference](references/lifecycle.md)
- [Discovery Reference](references/discover.md)
- [Specification Reference](references/specify.md)
- [Prototype Reference](references/prototype.md)
- [Review Workspace Reference](references/review-workspace.md)
- [Change and Acceptance Reference](references/change-acceptance.md)
- [Context Management Reference](references/context.md)
- [Tool Adapters Reference](references/tool-adapters.md)
- [Troubleshooting Reference](references/troubleshooting.md)
- [Domain Coverage Reference](references/domain-coverage.yaml)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, YAML or JSON snippets, structured requirement artifacts, shell commands, and HTML prototypes when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local files, validation commands, and gate results when the target stage requires durable artifacts.]

## Skill Version(s):

5.4.9 (source: release evidence and changelog, released 2026-09-01)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
