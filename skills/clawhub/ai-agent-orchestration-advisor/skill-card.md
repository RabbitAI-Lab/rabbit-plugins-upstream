## Description:

Helps developers compare multi-agent frameworks and design architectures, starter code, evaluations, and guardrails without installing, running, or deploying frameworks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI engineers use this skill to select multi-agent frameworks and plan agent topology, starter code, evaluation, guardrails, and costs. Product and data teams can use its trade-off analysis to scope production workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Example integrations may send business data to external search or third-party services.

Mitigation: Review each proposed tool and use approved internal services where data must remain private.

Risk: Adapting starter code without safeguards may expose secrets or sensitive content in logs.

Mitigation: Keep secrets in environment variables, minimize input data, and redact logs before use.

Risk: Framework recommendations and generated code may be unsuitable for a particular production environment.

Mitigation: Human-review recommendations and examples, then test them against the team's security, evaluation, and deployment requirements.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/gechengling/skills/ai-agent-orchestration-advisor)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Markdown with comparison tables, architecture diagrams, and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory output only; example code requires review and adaptation before execution.]

## Skill Version(s):

3.0.2 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
