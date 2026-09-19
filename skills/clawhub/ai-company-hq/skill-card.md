## Description:

HQ skill: Cross-agent coordination, conflict resolution, knowledge base management, audit logging, strategic scheduling, task orchestration, IMA sync hub.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnsmithfan](https://clawhub.ai/user/johnsmithfan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to coordinate agent routing, shared state, knowledge-base updates, conflict resolution, audit logging, and workflow scheduling for an AI Company system.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad state and messaging authority could expose or modify information beyond the intended agent or department scope.

Mitigation: Require administrator approval before installation, restrict the skill to scoped state namespaces, and enforce least-privilege access controls for routing and state changes.

Risk: Conversation monitoring and knowledge extraction could capture secrets, personal data, or sensitive operational context.

Mitigation: Keep monitoring disabled by default, redact secrets and personal data before storage, and document clear user-control and consent boundaries.

Risk: Permanent or long-retention audit logging can create privacy, retention, and deletion obligations.

Mitigation: Define retention and deletion rules before deployment, separate sensitive audit categories, and review logs for data minimization.

## Reference(s):

- [Method Patterns & Detailed Specifications](references/method-patterns.md)
- [Department Integration Process](references/department-integration-process.md)
- [ClawHub skill page](https://clawhub.ai/johnsmithfan/skills/ai-company-hq)
- [Clawdis homepage](https://clawhub.com/skills/ai-company-hq)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown and structured guidance with example schemas, prompts, and workflow steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include coordination results, reports, audit-trail guidance, test cases, documentation, and implementation instructions.]

## Skill Version(s):

3.0.1-en2 (source: server release evidence; artifact frontmatter lists 3.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
