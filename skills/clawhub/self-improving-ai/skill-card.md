## Description:

Captures learnings about GenAI/LLM configuration, model selection, inference optimization, fine-tuning, RAG pipelines, prompt engineering, multimodal processing, and cost management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI engineers use this skill to capture model behavior, prompt, RAG, inference, fine-tuning, multimodal, evaluation, and guardrail learnings as local markdown records. It also provides optional project-scoped reminders for reviewing and promoting recurring AI/LLM patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Learning logs may accidentally include API keys, model access tokens, customer data, PII, or sensitive model outputs.

Mitigation: Redact sensitive content before logging, avoid raw transcripts, and review tracked .learnings files before sharing or committing them.

Risk: Optional hooks can add recurring reminders across sessions if installed too broadly.

Mitigation: Enable hooks deliberately, keep them project-scoped, avoid empty matchers, and prefer the minimal UserPromptSubmit reminder unless error detection is needed.

Risk: Promoted learnings or generated skills can encode incorrect model guidance if adopted without review.

Mitigation: Review generated diffs, scan new skills before use, and require explicit approval before applying model configuration, prompt, policy, or skill changes.

Risk: Live production model testing or cross-skill reading can raise privacy and operational concerns.

Mitigation: Treat those actions as requiring explicit approval and privacy review before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jose-compu/skills/self-improving-ai)
- [Hook Setup Guide](references/hooks-setup.md)
- [OpenClaw Integration](references/openclaw-integration.md)
- [Entry Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local learning, model issue, and feature request entries; optional hooks emit reminder text when deliberately enabled.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
