## Description:

Harness coordinates stable agent workflows by enforcing clarify-ground-plan-generate-verify pipelines, guardrails for scope and destructive actions, and bounded recovery from verification failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to wrap autonomous or repeated agent workflows with clarification, grounding, scoped execution, verification, and recovery behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger phrases may activate the harness for general workflow-stability requests.

Mitigation: Use explicit topic names such as pipeline, guardrails, or recovery when invoking the skill.

Risk: Delegated planning or generation steps can propose or execute actions outside the user's intended scope.

Mitigation: Apply the built-in scope check before dispatched stages and verify the final diff against the stated request and plan.

Risk: Destructive commands or state-changing operations could be requested during an autonomous workflow.

Mitigation: Require explicit, single-use authorization that names the exact operation and target before allowing denylisted actions.

## Reference(s):

- [Harness Skill Page](https://clawhub.ai/drumrobot/skills/harness)
- [Harness Overview](artifact/SKILL.md)
- [Pipeline Guide](artifact/pipeline.md)
- [Guardrails Guide](artifact/guardrails.md)
- [Recovery Guide](artifact/recovery.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with checklists, reports, clarifying questions, command examples, and configuration options.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce guardrail block reports, scope drift reports, verification reports, retry traces, and fallback summaries.]

## Skill Version(s):

0.1.1 (source: frontmatter, release evidence, changelog released 2026-08-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
