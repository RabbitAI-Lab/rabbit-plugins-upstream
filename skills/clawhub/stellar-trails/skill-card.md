## Description:

Stellar Trails provides an adaptive six-phase workflow for coding, document, data, planning, and analysis tasks with traceability IDs, entry and exit gates, scope commitment, and compliance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hoshiyomix](https://clawhub.ai/user/hoshiyomix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Stellar Trails to structure agent work across specification, planning, implementation, verification, and delivery while retaining traceability and compliance signals. It is suited to normal ClawHub workflow releases where an agent needs repeatable task discipline across coding, documents, visualizations, data processing, and multi-step plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically update itself before ordinary work.

Mitigation: Use it only where automatic ClawHub updates are expected, or require explicit approval before update operations.

Risk: The skill can use a GitHub token during activation workflows.

Mitigation: Avoid installing it in environments with valuable private credentials; use short-lived, least-privilege tokens when token access is necessary.

Risk: The skill can start persistent background services.

Mitigation: Run it in an isolated sandbox and review service startup behavior before enabling it in shared or long-lived environments.

Risk: The skill can write cross-session state and persistent logs.

Mitigation: Do not use it with long-lived user data unless persistent restore and logging behavior are reviewed, isolated, or disabled.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hoshiyomix/skills/stellar-trails)
- [Skill definition](artifact/SKILL.md)
- [Workflow phases](artifact/procedure/phases.md)
- [Enforcement vectors](artifact/knowledge/enforcement-vectors.md)
- [ZAI sandbox notes](artifact/knowledge/zai-sandbox.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and workflow checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes phase gates, traceability IDs, activation checks, and pre-push verification guidance.]

## Skill Version(s):

9.17.1 (source: SKILL.md metadata, evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
