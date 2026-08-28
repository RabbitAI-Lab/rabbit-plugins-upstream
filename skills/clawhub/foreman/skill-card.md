## Description:

foreman helps developers dispatch implementation work to background agents via the handoff CLI, take delivery against path whitelists, and gate merges with acceptance checks that prevent builders from modifying the tests, assertions, or CI config used to judge their work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering leads use this skill to dispatch implementation tasks to background agents, inspect bounded deliveries, and run acceptance checks before merge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository content and task prompts can be sent to external or configured model backends during dispatch.

Mitigation: Review backend configuration before use and choose hosted or local backends for sensitive repositories.

Risk: The optional caged worker passes DEEPSEEK_API_KEY into a worker container.

Mitigation: Use the caged worker only when that credential exposure is acceptable, and provide the key from the environment without storing it in the skill.

Risk: Verification commands in work orders can perform side effects if the user writes them that way.

Mitigation: Review work orders before dispatch and use side-effect-free preflight commands for worker and intake checks.

Risk: Copied CI workflow templates require repository-specific configuration before they provide meaningful protection.

Mitigation: Replace placeholders with persistent verification commands and configure dynamic acceptance only when the CI environment supports it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiaoba-dev/skills/foreman)
- [SKILL.md](artifact/SKILL.md)
- [Dispatch workflow](artifact/dispatch.md)
- [Acceptance workflow](artifact/verify.md)
- [Work order template](artifact/work-order.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with inline shell commands, JSON state examples, and workflow configuration templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce work orders, dispatch commands, acceptance decisions, and CI gate configuration guidance.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
