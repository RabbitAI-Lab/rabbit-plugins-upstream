## Description:

Experience-inheritance runtime for coding agents: recall validated fixes at task start, register hits when used, deposit fixes after repairing failures, and optionally run controlled experiments to measure inheritance gains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the skill to help coding agents reuse validated fixes across tasks, record newly learned solutions, and optionally measure the effect with controlled experiments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote pool imports can approve unauthenticated prompt content that may influence future agent sessions.

Mitigation: Avoid `--tier official` for remote pools unless you control and trust the source; prefer community or quarantine review for imports.

Risk: LLM refinement can send session content to a configured external endpoint.

Mitigation: Leave `--llm-refine` disabled unless you explicitly trust the configured endpoint.

Risk: Hooks or agent instruction snippets can affect agent behavior when enabled.

Mitigation: Review hooks and AGENTS/CLAUDE snippets before enabling them with `--yes`.

## Reference(s):

- [Pi EvoX Loop project](https://github.com/stwhwing/pi-evox-lab)
- [Pi EvoX Loop on ClawHub](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Pi coding agent](https://github.com/earendil-works/pi)
- [EvoMap Evolver](https://github.com/EvoMap/evolver)
- [Numbat agent behavior auditor](https://github.com/perplexityai/numbat)
- [FlyLoRA paper](https://arxiv.org/abs/2510.08396)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Markdown, JSON]

**Output Format:** [Markdown guidance, runnable shell commands, and optional JSON or text experiment reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local experience-memory and experiment artifacts.]

## Skill Version(s):

0.26.0 (source: ClawHub release metadata, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
