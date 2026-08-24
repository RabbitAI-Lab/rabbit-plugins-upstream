## Description:

Converts exported Dify workflow or chatflow YAML into deployable standalone code projects while asking for missing credentials, resources, and deployment choices instead of fabricating them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[somkh](https://clawhub.ai/user/somkh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to migrate Dify workflow or chatflow exports into runnable Python FastAPI or Node.js Express services, including analysis, scaffolding, code generation, verification, and delivery notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated projects can read named environment variables and secrets.

Mitigation: Review every env and secret reference before running, keep credentials in environment files, and avoid hardcoding sensitive values.

Risk: Generated or DSL-derived code may execute in the produced service.

Mitigation: Generate and verify projects in an isolated folder or container with minimal environment variables, then review generated handlers before deployment.

Risk: Generated services may call outbound HTTP, tool, model, or LLM endpoints described by the DSL.

Mitigation: Review each outbound endpoint and authorization setting before running or deploying the generated service.

Risk: Template dependencies may be outdated by deployment time.

Mitigation: Pin, scan, or update generated project dependencies before deploying generated services.

## Reference(s):

- [Dify DSL to Code on ClawHub](https://clawhub.ai/somkh/skills/dify-dsl-to-code)
- [Code Generation Patterns](references/codegen-patterns.md)
- [Dify DSL Components](references/dsl-components.md)
- [Dify DSL Node Types](references/dsl-node-types.md)
- [Interaction Playbook](references/interaction-playbook.md)
- [Example Chatflow QA DSL](assets/examples/example-chatflow-qa.yml)
- [Example Workflow Review DSL](assets/examples/example-workflow-review.yml)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands plus generated project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated projects may target Python FastAPI or Node.js Express and include environment placeholders, templates, verification commands, and delivery notes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
