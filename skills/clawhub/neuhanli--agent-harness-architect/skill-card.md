## Description:

Agent Harness Architect helps developers clarify requirements, turn rough agent ideas into professional Agent Harness architecture designs, produce directly codeable design documents, and maintain a self-evolving knowledge base of harness frameworks and cross-domain design patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to turn rough ideas, requirements analyses, or existing agent architectures into directly codeable Agent Harness designs. It guides clarification, six-layer H=(E,T,C,S,L,V)+P architecture analysis, tradeoff review, adversarial design checks, and production readiness checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network research or knowledge-base updates can introduce unsuitable sources that influence future architecture recommendations.

Mitigation: Review proposed sources and diffs before allowing the skill to update its reference knowledge base.

Risk: Architecture guidance may be incorrect or over-applied if the user's requirements, constraints, or success criteria are incomplete.

Mitigation: Use the clarification workflow, require user confirmation for key decisions, and run the production checklist before treating a design as implementation-ready.

## Reference(s):

- [H Framework](references/h-framework.md)
- [Capability Boundary](references/capability-boundary.md)
- [Knowledge Index](references/knowledge-index.md)
- [Production Checklist](references/production-checklist.md)
- [Codex Harness](https://github.com/openai/codex)
- [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)
- [Hermes Agent](https://github.com/NousResearch/hermes-agent)
- [Letta](https://github.com/letta-ai/letta)
- [mini-SWE-agent](https://github.com/SWE-agent/mini-swe-agent)
- [OpenClaw Documentation](https://docs.openclaw.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown design documents, questionnaires, structured architecture specifications, code-oriented interface sketches, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose knowledge-base updates only after source review and user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
