## Description:

Packages an approved POC scenario, PRD, and deployment constraints into a reusable, evaluable Agent Skill, and can build guarded mock POC scaffolds when explicitly requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xukun0821](https://clawhub.ai/user/xukun0821)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and field delivery teams use this skill to convert approved requirements and deployment constraints into reviewable Agent Skill design packages, installable skill structures, evaluation criteria, and mock-first POC scaffolds. It is intended for pre-production packaging and validation handoff, not for replacing representative real-run validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated skill packages or POC files could be installed before adequate review.

Mitigation: Review generated files before installation and run the included package validator and smoke evaluations before handoff.

Risk: A mock POC scaffold could be mistaken for production-ready integration.

Mitigation: Keep production credentials and real integrations out of the scaffold, preserve mock-only boundaries, and require explicit authorization before adding external write actions.

Risk: Incomplete or unapproved requirements could lead to misleading skill behavior or evaluation criteria.

Mitigation: Use the skill only with already-approved requirements and deployment constraints; pause or return upstream when required inputs are missing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xukun0821/skills/fde-agent-skill-designer)
- [Agent skill design package template](references/agent-skill-pack.md)
- [Agent skill assessment design](references/evaluation-design.md)
- [General Agent Skills platform adaptation](references/platform-adapters.md)
- [Minimum runnable POC build mode](references/poc-build-mode.md)
- [Public method sources](references/public-sources.md)
- [OpenAI: Build skills](https://developers.openai.com/codex/skills/)
- [Anthropic: Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Microsoft Agent Skills documentation](https://learn.microsoft.com/en-us/agent-framework/agents/skills)
- [OWASP Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, code files, JSON manifests, YAML configuration, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated POC scaffolds are mock-first, require human review, and are not production-approved by default.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
