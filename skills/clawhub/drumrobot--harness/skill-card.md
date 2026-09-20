## Description:

Harness guides agents through stable LLM workflows by combining a clarify-ground-plan-generate-verify pipeline, pre-execution guardrails, and bounded recovery after verification failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use Harness to wrap autonomous or headless LLM workflows with clarification, grounding, scope checks, verification, and bounded retry or fallback behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Accidental invocation could slow or redirect normal agent work by adding clarification, grounding, planning, verification, and recovery gates.

Mitigation: Use narrow activation phrases or topic specifiers, and enable the harness for workflows that need stronger stability or autonomous-execution controls.

Risk: Destructive-operation blocking depends on clear scope and exact user authorization.

Mitigation: Require explicit operation and path authorization before retrying blocked actions, and treat broad approval language as insufficient.

Risk: The pipeline delegates planning and generation to a receiver such as code-workflow.

Mitigation: Confirm the receiver skill is installed or configure an alternate pipeline receiver before relying on the full pipeline flow.

## Reference(s):

- [Harness ClawHub page](https://clawhub.ai/drumrobot/skills/harness)
- [Pipeline guide](pipeline.md)
- [Guardrails guide](guardrails.md)
- [Recovery guide](recovery.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with checklists, tables, and inline command or configuration references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No hidden code, persistence, or data exfiltration found by Clawscan; may make agents ask clarifying questions, read grounding material, block destructive commands, and retry within a bounded recovery budget.]

## Skill Version(s):

0.1.3 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
