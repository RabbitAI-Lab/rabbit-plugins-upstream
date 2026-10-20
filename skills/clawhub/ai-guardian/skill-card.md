## Description:

Helps agents inventory and govern local LLMs, scan prompts for sensitive content, review model policy and provenance, and audit observed usage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect local LLM models and resource use, identify unsanctioned models or digest changes, screen prompts, and review usage on single-endpoint runtimes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent access to write tools can change policy, pull models, or delete local model weights without an enforced approval gate.

Mitigation: For observation-only use, expose only scan and read tools or use a runtime account that cannot administer the model store; require human review before destructive actions.

Risk: Audit, usage, undo, and optional encrypted secret material are stored in local state.

Mitigation: Restrict access to ~/.ai-guardian and protect the master password used for optional secrets.

Risk: Prompt governance covers only requests routed through the guard; direct model calls can bypass it.

Mitigation: Route intended traffic through guarded tools and do not treat an empty observed-usage log as proof of no model activity.

## Reference(s):

- [AI Guardian on ClawHub](https://clawhub.ai/zw008/skills/ai-guardian)
- [AI Guardian project homepage](https://github.com/AIops-tools/AI-Guardian)
- [Capabilities](references/capabilities.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)
- [CLI reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports model inventory, policy verdicts, redacted prompt-scan findings, usage summaries, and recommended actions.]

## Skill Version(s):

0.13.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
