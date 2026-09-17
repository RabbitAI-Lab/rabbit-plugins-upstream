## Description:

Pi EvoX Loop helps coding agents recall validated repair patterns, record useful hits, and deposit new fixes after non-obvious failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to give coding agents a persistent repair-memory loop for recurring implementation, environment, and debugging failures. The optional experiment workflow helps measure whether inherited fixes reduce repeated errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist learned repair text and inject it into future agent system prompts.

Mitigation: Use the skill only when persistent agent memory is intended, review stored fixes before approval, and keep the default manual approval gate enabled.

Risk: Optional refinement can send session transcript content to a configured external endpoint.

Mitigation: Leave refinement disabled unless a trusted HTTPS endpoint is configured, and use a separate credential for that workflow.

Risk: Session diagnostics can read local agent-session archives that may contain sensitive task context.

Mitigation: Run diagnostics only in environments where reading those archives is acceptable, and avoid scheduled diagnostics when session sensitivity is unclear.

Risk: Combining automatic approval with LLM refinement can introduce unreviewed rewritten repair guidance.

Mitigation: Avoid using --auto-approve with --llm-refine for normal operation; require human review before refined fixes become reusable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project Homepage](https://github.com/stwhwing/pi-evox-lab)
- [Security and License Notes](docs/security-and-license.md)
- [Provider Configuration](docs/providers.md)
- [Other Agent Integration Guide](docs/other-agents.md)
- [Experiment Report](docs/experiment-report.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read and update a persistent repair-memory store when the user follows the recall, hit-registration, or deposit workflows.]

## Skill Version(s):

0.14.2 (source: frontmatter, package.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
