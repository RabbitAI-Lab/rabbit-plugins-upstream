## Description:

Experience-inheritance runtime for coding agents: recall validated fixes at task start, register hits when fixes are used, deposit new fixes after repairing failures, and optionally run controlled closed-loop experiments to measure inheritance gains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers and coding-agent operators use this skill to give agents a persistent, reviewed store of past fixes that can be recalled for similar future tasks. It also supports optional controlled experiments for measuring whether inherited fixes reduce repeated failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent fixes can influence future agent runs, including future prompt context.

Mitigation: Install only when persistent experience reuse is intended, keep manual approval enabled, and periodically review or quarantine ledger entries before enabling injection.

Risk: Automatically approved or unreviewed refined entries may preserve instructions derived from external or untrusted session content.

Mitigation: Avoid --auto-approve-lowrisk and --allow-unreviewed-refine for sessions that may contain external or untrusted content.

Risk: Optional LLM refinement can send session content to a configured external endpoint.

Mitigation: Use LLM refinement only with an approved endpoint and after confirming the session content is suitable for that destination.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project homepage](https://github.com/stwhwing/pi-evox-lab)
- [Security and license notes](docs/security-and-license.md)
- [Provider configuration](docs/providers.md)
- [Other agent hosts](docs/other-agents.md)
- [Experiment report](docs/experiment-report.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and code or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update local experience-store entries and review ledger state when the user runs the provided commands.]

## Skill Version(s):

0.14.4 (source: frontmatter and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
