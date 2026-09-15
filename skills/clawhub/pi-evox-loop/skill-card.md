## Description:

Give coding agents an experience-inheritance runtime that recalls reviewed fixes at task start, records used fixes, deposits newly learned repairs, and can run controlled closed-loop experiments to measure inheritance gains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to give coding agents a reviewed local memory loop for recurring repair patterns, environment-specific fixes, and post-task learning. It is also useful for measuring whether inherited fixes reduce repeat failures in controlled agent experiments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reviewed fixes from a shared local experience store can influence future agent prompts across tasks or projects.

Mitigation: Use project-scoped installation when possible, review the stored fixes regularly, and avoid global extension setup unless cross-project recall is intentional.

Risk: Unreviewed or low-quality distilled fixes can add misleading guidance to later agent runs.

Mitigation: Keep the manual review gate enabled for normal use and avoid --auto-approve with untrusted or noisy sessions.

Risk: Optional LLM refinement can send session content and API credentials to the configured endpoint.

Mitigation: Enable --llm-refine only with an approved endpoint, understand what transcript content may be sent, and prefer local or controlled endpoints for sensitive work.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project Homepage](https://github.com/stwhwing/pi-evox-lab)
- [README](README.md)
- [Security and License](docs/security-and-license.md)
- [Other Agent Integration](docs/other-agents.md)
- [Experiment Report](docs/experiment-report.md)
- [Provider Configuration](docs/providers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, and generated local experience records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include recalled fix lists, hit registrations, distilled repair strategies, local metrics, and experiment summaries.]

## Skill Version(s):

0.14.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
