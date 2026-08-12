## Description:

Local Ollama multi-role army and assistant hub for queue-driven local automation, command-center monitoring, and optional consent-gated supervisor workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run local Ollama worker roles, propose or review queue tasks, check health and sentinel status, and manage optional local automation surfaces. It is intended for controlled local machines where the user can review configuration, queue files, and consent-gated launchers before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act as a powerful local automation hub with runtime and desktop-launcher paths that may be broader than a minimal skill surface.

Mitigation: Install only on a controlled local machine, read the security references first, and review queue files, config flags, and desktop launchers before running them.

Risk: Queue tasks may execute when a daemon or worker role is running.

Mitigation: Review task JSON before placing it in an execution queue, and avoid automatic queue writes by agents.

Risk: Self-tune can rewrite configuration and prune queue files when enabled.

Mitigation: Keep self_tune disabled by default and enable it only after explicitly accepting configuration mutation.

Risk: Full-capacity PowerShell launchers intentionally spawn multiple Python processes when all gates are set.

Mitigation: Use the in-process Python launcher for normal operation and run the full-capacity PowerShell path only with explicit operator consent.

Risk: Optional public probes, browser opening, planting, social pulse, and external memory writes can have effects outside the default local-only path.

Mitigation: Leave those flags disabled unless the user intends the specific effect and has confirmed the relevant local stack path and consent settings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-ollama-army)
- [LYGO protocol stack homepage](https://github.com/DeepSeekOracle/lygo-protocol-stack)
- [LYGO resonance companion](https://deepseekoracle.github.io/Excavationpro/LYGORESONANCE.html)
- [Security guidance](artifact/references/SECURITY.md)
- [Security audit notes](artifact/references/SECURITY_AUDIT.md)
- [SkillSpector audit response](artifact/references/SKILLSPECTOR_AUDIT.md)
- [Agent contract](artifact/references/AGENT_CONTRACT.md)
- [ClawHub security audit](https://clawhub.ai/deepseekoracle/skills/lygo-ollama-army/security-audit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON task proposals, configuration notes, code snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal output should keep queue writes, self-tune, planting, autonomous supervisor, full-capacity launchers, browser open, and public probes behind explicit user review or consent.]

## Skill Version(s):

0.8.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
